# Skill: Kế toán energy agentic workflow (agentic-eCAL accounting)
Source: 2609.18283
Type: evaluation-method (energy/memory accounting framework)

## Khi nào dùng skill này
- Bạn triển khai multi-agent system (đội agent nhiều người) và muốn biết/khống chế cost energy + GPU per workflow — đặc biệt khi chọn host edge/cloud, chọn model, chọn topology team.
- Bạn đang cân nhắc thêm agent vào team hoặc thêm reasoning depth (độ sâu bước) — cần estimate marginal energy trước khi commit.
- Bạn cần chứng minh/justify multi-agent design (design đội nhiều agent) có thật sự worth cost hay đơn agent đủ.

## Khi NÊNG DÙNG
- Workflow có nhiều LLM call vòng lặp tích lũy history (history-carrying loops), tool call, retrieval — energy không tuyến tính, cần accounting.
- Bạn serve batch production (b ≥ 64) — regime prefill-dominated bùng nổ quadratic.

## Khi KHÔNG nên dùng
- Single one-shot call, không loop/history, low-QPS → dùng simple per-token estimate đủ (c_pre·p_in + c_dec·p_out với coefficients datasheet).
- Không access NVML (NVIDIA management library — thư viện đo power GPU) hoặc serverless opaque billing → calibrate không được, chỉ ước lượng rough.

## Input cần có
- Workflow DAG: agents, edges (hand-off), steps K; token counts per step (p_in, p_out).
- Model specs: N_params (hoặc N_act cho MoE — mixture-of-experts), γ KV bytes/token (36–512 kB/token tùy model), weight GB.
- Host specs: M_u VRAM [GB], serving batch b.
- GPU measured coefficients lý tưởng (NVML); fallback datasheet: BHBM bandwidth, TDP P, prefill η≈0.74–0.85.
- Hand-off protocol choice: transcript / increment / summary / KV-cache.

## Các bước thực hiện
1. **Classify + map workflow**: W = (A, E), K steps; classify mỗi agent: Generate (charged p_out), Transform (refine 1 work line), Ground (retrieval/tool — import external tokens vào p_in), Aggregate (read all candidate set — p_in grows with set size). Đếm edges E — topology cost = N·p_0 + E·τ (shape graph không matter, edge count matter).
2. **Memory feasibility gate** per site: β·N_params + γ·Σ_(a hosted)c_a ≤ M_u (β=2 bytes/param FP16; 4-bit 70B ~32–64 GB class). Đồng thời tính concurrent sessions: capacity = (M_u − βN_params)/(γ · Σ context per session) — tại N=10 agent team: Orin 8GB 1–2 sessions, A100 59; pick model narrow-KV (GPT-OSS-20B 48 kB/token host 112 sessions vs OLMo-2-7B 512 kB only 7).
3. **Two-rate call energy**: E_call = c_pre·p_in + (a_dec/b + c_0)·p_out. Hệ số 7–8B class dưới đây mang tính tham khảo — tốt nhất là tự calibrate trên GPU của bạn: Qwen2.5-7B c_pre 0.023, a_dec 3.2, c_0 0.02; Llama-3.1-8B c_pre ≈ 0.02–0.03 (paper không cho riêng), a_dec 3.3, c_0 0.06 J/token. Datasheet fallback: c_pre ≈ N_params·β·P/(η_pre·Π); c_dec datasheet là lower bound (~70% peak bandwidth serving) → expect ~1/3 magnitude error.
4. **Workflow energy**: E_W = (1+γ_v)[ΣE_call + ΣE_tool + ΣE_ret + E_tx], γ_v ≈ 0,10 orchestration overhead. E_ret = embedding FLOPs + α_idx·d_emb·log(M_vec); nhớ retrieval inject tokens vào p_in bước sau (context 2K→10K ~3× energy/token 70B). E_tx = Σ B_payload·ε_uv (ε: 5G 10⁻⁶, metro 10⁻⁷, optical 10⁻⁸ J/b) — text hand-off dự kiến <0.25% E_W; nếu E_tx lớn hơn nhiều → bạn đang migrate KV cache (18.9 Gbit vs 0.33 Mbit transcript) → STOP, keep cache local.
5. **Scaling diagnosis**: history-carrying → Σp_in quadratic K²/2 → energy exponent a ∈ [1,2]: small batch decode-bound a≈1; production batch prefill-bound a≈2 (Qwen measured 1.10→1.42 với b 2→256). Estimate total energy at target K, N, b trước khi deploy; batching savings: −38.1% N=2 nhưng −15.4% N=30 — đừng giả định batch cứu large team.
6. **Hand-off protocol select**: increment (0.051 Mbit/3-round session) hoặc bounded summary (0.079) — KHÔNG full transcript (0.33 Mbit, quadratic growth 30× K=1→6), KHÔNG KV-cache migration (18.9 Gbit, 5 orders magnitude, non-transportable cellular). Protocol choice dynamic range 3.7×10⁵ — impact lớn nhất (vs architecture 4.8×, bearer 10³).
7. **agentic-eCAL metric**: (E_W + γe·E_emb)/B_useful [J/b], B_useful = f·T_out, γe = 1/G embodied amortization (parity crossover 8B class ≈ 1.2×10¹⁰ invocations; operational-dominated beyond). So sánh candidate designs theo kJ/solved task (kJ trên task giải được) chứ không kJ/run — energy wasted on failed runs vẫn tính.
8. **Multi-agent justification test**: benchmark single ReAct baseline before multi topology — ZSM benchmark evidence: multi-agent cost 4.0×–23.9× energy mà success không nhất quán better (9B: Single 61.7% vs best-multi 64.6% at 2.9× energy; 7B: Single 9.2% BETTER multi 0.4–4.6%). Adopt multi chỉ khi kJ/solved-task beat single.
9. **Efficiency levers order** (impact giảm dần): (1) hand-off payload (increment/summary); (2) team size/coupling (sparse/chain, cap N); (3) KV-width model selection + batch (but verify a-regime); (4) prefix caching reuse (TTFT −4×); (5) bearer/placement — near-zero impact cho text.

## Output mong đợi
- Bảng năng lượng per workflow [J] + per useful bit [J/b] + memory sessions hostable + verdict: (a) feasible chỗ nào host (memory gate), (b) regime a (decode- vs prefill-bound), (c) kJ/solved-task so single baseline → adopt/reject multi-agent + protocol recommendation.

## Ví dụ áp dụng
- Pipeline content 3 agent (writer→editor→publisher) Qwen2.5-7B, K=4 round, b=64, 24GB L4: writer 700→200, editor 2000→120 (Ground, prefill 2× output), publisher 1370→400. Σp_in quadratic ≈ 9.000 tokens → E_call ≈ 0.023·9000 + (3.2/64+0.02)·720 ≈ 207 + 61 ≈ 268 J/workflow (γ_v 10% → ~295 J). Hand-off full transcript 4 round ≈ 0.9 Mbit → E_tx 5G ≈ 0.9 mJ ≪ E_W (0.0003%) → placement decision theo VRAM: 24GB fits 7–8B + context ~2 sessions; editor redesign send summary 0.079 Mbit → E_tx không đổi negligible nhưng p_in bước publisher giảm ~1.200 tokens → E_W −~40 J. Kết luận: keep edge L4, bound editor context, skip multi-agent debate thêm (would push N→exponent 1.4).

## Gotchas
- **Magnitude error ~1/3 nếu dùng datasheet**: coefficients phải calibrate NVML trên stack serving thực (vLLM continuous batching); form model đúng, magnitude datasheet underestimates decode floor c_0 (PagedAttention fragmentation + idle draw).
- **KV width beats weight class** khi chọn model phục vụ density: Llama-3.1-8B tốn ~2× Qwen2.5-7B năng lượng (c_0 0.06 vs 0.02) dù cùng class — đừng assume "cùng 8B = cùng cost".
- **Batch không cứu team lớn**: savings 38.1% (N=2) → 15.4% (N=30); quadratic prefill thắng amortization → cap team hoặc chuyển sparse coupling.
- **Transport trap nghịch lý**: E_tx/E_prefill 1/496 khiến Distribution "free" — nhưng cost thật nằm ở EXTRA inference + context processing khi agent giao tiếp (re-prefill transcript) → optimizing bandwidth là wasted effort; optimize context retention.
- **KV cache non-transportable**: migrating cache 18.9 Gbit/session vượt compute energy trên mọi cellular bearer (parity 5.1×10⁻⁸ J/b) → context bound local accelerator; design stateless horizontal scale kém hiệu quả cho agent stateful.
- **MoE**: dùng N_act (active routed parameters) cho FLOPs, không N_params — unrouted experts chiếm memory nhưng không matmul.
- **Failure runs count**: năng lượng failed attempts vẫn tiêu thụ → metric kJ/solved-task (như paper Fig. 9b), không kJ/run — 7B multi topology "0.4–4.6% success" nghĩa kJ/solved lên 5222.3.
- **Entrance embodied**: cho open-weight model reused massively (G > crossover), embodied amortizes → near-zero; nhưng private small-scale deployment (G nhỏ) embodied chiếm dominant → dùng model nhỏ reuse cao.
