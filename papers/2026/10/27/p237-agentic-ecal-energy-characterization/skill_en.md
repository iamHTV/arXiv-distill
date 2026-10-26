# Skill: Energy Accounting for Agentic Workflows (agentic-eCAL)
Source: 2609.18283
Type: evaluation-method (energy/memory accounting framework)

## When to use this skill
- You deploy a multi-agent system and want to know/control energy + GPU cost per workflow — especially when choosing edge/cloud hosting, models, or team topology.
- You consider adding agents to a team or adding reasoning depth (steps) — estimate marginal energy before committing.
- You need to justify a multi-agent design (many agents) as actually worth the cost vs a single agent.

## Prerequisites (must have)
- Workflow with multiple LLM calls in history-accumulating loops, tool calls, retrieval — energy is non-linear, needs accounting.
- You serve production batches (b ≥ 64) — the prefill-dominated regime where quadratic effects explode.

## When NOT to use
- Single one-shot call, no loop/history, low QPS → a simple per-token estimate suffices (c_pre·p_in + c_dec·p_out with datasheet coefficients).
- No NVML (NVIDIA management library for GPU power measurement) access or opaque serverless billing → cannot calibrate, only rough estimates.

## Inputs required
- Workflow DAG: agents, edges (hand-offs), steps K; token counts per step (p_in, p_out).
- Model specs: N_params (or N_act for MoE — mixture-of-experts), γ KV bytes/token (36–512 kB/token depending on model), weight GB.
- Host specs: M_u VRAM [GB], serving batch b.
- GPU-measured coefficients ideally (NVML); fallback datasheet: HBM bandwidth BHBM, TDP power P, prefill utilization η ≈ 0.74–0.85.
- Hand-off protocol choice: transcript / increment / summary / KV-cache.

## Steps
1. **Classify + map the workflow**: W = (A, E), K steps; classify each agent: Generate (charged for p_out), Transform (refines one work line), Ground (retrieval/tool — imports external tokens into p_in), Aggregate (reads the whole candidate set — p_in grows with set size). Count edges E — topology cost = N·p_0 + E·τ (graph shape doesn't matter, edge count does).
2. **Memory feasibility gate** per site: β·N_params + γ·Σ_(hosted agents)c_a ≤ M_u (β = 2 bytes/param at FP16; 4-bit 70B ≈ 32–64 GB class). Also compute concurrent sessions: capacity = (M_u − β·N_params) / (γ · Σ context per session) — for a 10-agent team: Orin 8GB hosts 1–2 sessions, A100 hosts 59; prefer narrow-KV models (GPT-OSS-20B 48 kB/token hosts 112 sessions vs OLMo-2-7B's 512 kB hosting only 7).
3. **Two-rate call energy**: E_call = c_pre·p_in + (a_dec/b + c_0)·p_out. 7–8B class reference coefficients (calibrate your own): Qwen2.5-7B c_pre 0.023, a_dec 3.2, c_0 0.02; Llama-3.1-8B c_pre ~0.02–0.03, a_dec 3.3, c_0 0.06 J/token. Datasheet fallback: c_pre ≈ N_params·β·P/(η_pre·Π); datasheet c_dec is a lower bound (serving sustains ~70% of peak bandwidth) → expect ~1/3 magnitude error.
4. **Workflow energy**: E_W = (1+γ_v)·[ΣE_call + ΣE_tool + ΣE_ret + E_tx], γ_v ≈ 0.10 orchestration overhead. E_ret = embedding FLOPs + α_idx·d_emb·log(M_vec); remember retrieval injects tokens into the next step's p_in (context 2K→10K ≈ 3× energy/token on 70B). E_tx = Σ B_payload·ε_uv (ε: 5G 10⁻⁶, metro 10⁻⁷, optical 10⁻⁸ J/b) — text hand-offs should be < 0.25% of E_W; if E_tx is much larger you are migrating the KV cache (18.9 Gbit vs 0.33 Mbit transcript) → STOP, keep the cache local.
5. **Scaling diagnosis**: history-carrying → Σp_in quadratic K²/2 → energy exponent a ∈ [1,2]: small batch decode-bound a≈1; production batch prefill-bound a≈2 (Qwen measured 1.10→1.42 as b goes 2→256). Estimate total energy at target K, N, b before deploying; batching savings: −38.1% at N=2 but only −15.4% at N=30 — don't assume batching rescues large teams.
6. **Hand-off protocol selection**: increment (0.051 Mbit per 3-round session) or bounded summary (0.079) — never full transcript (0.33 Mbit, quadratic 30× growth for K=1→6), never KV-cache migration (18.9 Gbit, five orders of magnitude, non-transportable on cellular). Protocol choice spans a 3.7×10⁵ dynamic range — the biggest impact lever (vs architecture 4.8×, bearer 10³).
7. **agentic-eCAL metric**: (E_W + γe·E_emb) / B_useful [J/b], B_useful = f·T_out, γe = 1/G embodied amortization (crossover for the 8B class ≈ 1.2×10¹⁰ invocations; operational-dominated beyond). Compare candidate designs by kJ per solved task — not kJ per run — energy wasted on failed runs still counts.
8. **Multi-agent justification test**: benchmark a single ReAct baseline before any multi-agent topology — ZSM benchmark evidence: multi-agent costs 4.0×–23.9× energy with inconsistent success (9B: Single 61.7% vs best-multi 64.6% at 2.9× energy; 7B: Single 9.2% was BETTER than multi's 0.4–4.6%). Adopt multi-agent only when kJ/solved-task beats single.
9. **Efficiency levers in impact order** (decreasing): (1) hand-off payload (increment/summary); (2) team size/coupling (sparse/chain, cap N); (3) KV-width model selection + batch (verify the a-regime first); (4) prefix-cache reuse (TTFT −4×); (5) bearer/placement — near-zero impact for text.

## Expected output
- Per-workflow energy table [J] + per useful bit [J/b] + hostable memory sessions + verdict: (a) where it can host (memory gate), (b) scaling regime a (decode- vs prefill-bound), (c) kJ/solved-task vs single baseline → adopt/reject multi-agent + protocol recommendation.

## Example application
- 3-agent content pipeline (writer→editor→publisher) on Qwen2.5-7B, K=4 rounds, b=64, 24GB L4: writer 700→200, editor 2000→120 (Ground agent, prefills 2× its output), publisher 1370→400. Σp_in quadratic ≈ 9,000 tokens → E_call ≈ 0.023·9000 + (3.2/64+0.02)·720 ≈ 207+61 ≈ 268 J/workflow (×1.10 overhead → ~295 J). Full-transcript hand-off for 4 rounds ≈ 0.9 Mbit → E_tx ≈ 0.9 mJ over 5G ≪ E_W (0.0003%) → decide placement by VRAM: 24GB fits the 7–8B class with context for ~2 sessions; redesign the editor to send a summary (0.079 Mbit) → E_tx unchanged (negligible) but the publisher's p_in drops ~1,200 tokens → E_W −~40 J. Conclusion: keep edge L4, bound the editor's context, skip extra multi-agent debate (would push the N-axis exponent toward 1.4).

## Gotchas
- **~1/3 magnitude error with datasheet coefficients**: calibrate with NVML on your actual serving stack (vLLM continuous batching); the model's form is right, but datasheet values underestimate the decode floor c_0 (PagedAttention fragmentation + idle draw).
- **KV width beats weight class** for serving density: Llama-3.1-8B uses ~2× Qwen2.5-7B energy (c_0 0.06 vs 0.02) despite the same class — don't assume "same 8B = same cost".
- **Batching doesn't rescue large teams**: savings 38.1% (N=2) → 15.4% (N=30); quadratic prefill wins over amortization → cap team size or switch to sparse coupling.
- **The transport paradox trap**: E_tx/E_prefill of 1/496 makes distribution look "free" — but the real cost is the EXTRA inference + context processing that agent communication induces (transcript re-prefill) → optimizing bandwidth is wasted effort; optimize context retention.
- **KV cache is non-transportable**: migrating it costs 18.9 Gbit/session, exceeding compute energy on every cellular bearer (parity 5.1×10⁻⁸ J/b) → context is bound to its local accelerator; stateless horizontal scaling is inefficient for stateful agents.
- **MoE**: use N_act (active routed parameters) for FLOPs, not N_params — unrouted experts occupy memory but no matmul.
- **Failure runs count**: failed attempts still consume energy → use kJ/solved-task (like Fig. 9b), not kJ/run — the 7B multi topologies' "0.4–4.6% success" means up to 5,222.3 kJ per solved task.
- **Embodied entry**: for massively reused open-weight models (G above crossover), embodied energy amortizes to near-zero; but private small-scale deployments (small G) are embodied-dominated → prefer small models with high reuse.
