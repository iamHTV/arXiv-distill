# Skill: attention-gate-instruction-data-separation
Source: 2610.37657v1 (Heads of Security)
Type: framework / security-hardening workflow

## When to use this skill
- You run an open-weight model as an agent processing untrusted content (tool outputs, emails, web scrapes) and need prompt-injection defense WITHOUT utility collapse on few-shot/multi-turn inputs.
- You want a cheap defense: only 46,080 gate parameters for Llama-3.3-70B (vs 349M DPO params in SecAlign), with public code/models (imperial-aisp/heads_of_security, imperial-cpg/heads-of-security).
- Do NOT use when: the model is a closed frontier model (Claude/GPT — already much more robust than open-weight); the model uses linear attention (no explicit per-key attention coefficient → the gate mechanism doesn't transfer); the task legitimately requires following external instructions (e.g., an agent installing a package from external docs).

## Inputs needed
- An open-weight decoder-only model with standard dense attention (pattern: Llama-3.3-70B-Instruct, GPT-OSS-20B).
- A predefined trust boundary: which sources are TRUSTED (system/user prompts, the model's own generation), UNTRUSTED (tool outputs, fetched content), TEMPLATE (chat template + BOS sink).
- A preference dataset: pairs of (user instruction + injected instruction in an untrusted segment; preferred = follow user, rejected = follow injection) — pattern: SecAlign++ DPO + adapted Cleaned-Alpaca.
- Training infra: a LoRA/DPO trainer optimizing only θ_gate; an eval kit: an RL-style attacker (pattern Llama-3.1-8B + GRPO) or a white-box suffix optimizer (budget 10¹⁶–10¹⁷ FLOPs), plus utility benchmarks ARC-C/GSM8K/MMLU/MMLU-Pro few-shot and AgentDojo/AgentDyn/LLMail/WASP.

## Steps
1. Attach channel tags: preprocessing middleware marks every token TRUSTED/UNTRUSTED/TEMPLATE by source; for GPT-OSS add a sink key-only channel (tables become C×(C+1)).
2. Initialize gate tables: each head k of layer ℓ gets g(ℓ,k) ∈ R^{C×C} (untrained = 0 → σ(g)=0.5; the common shift is cancelled by softmax → processed exactly like the base model).
3. Gated forward pass: ã = softmax(qKᵀ/√dₕ + log σ(g)) — the gate multiplies the unnormalized attention weight by σ(g) ∈ (0,1); near 1 = attend normally, near 0 = closed gate.
4. DPO training on θ_gate only (46,080 scalars for Llama-3.3-70B = L·C²·h with L=80, C=3, h=64): each preference pair = user instruction + injection → preferred follows the user, rejected follows the injection. Use the same dataset as the SecAlign baseline if you need a fair comparison.
5. Adaptive-attack eval: train an RL attacker (GRPO; attacker Llama-3.1-8B rewrites goals into injections) against the candidate defense; measure ASR on held-out InjecAgent goals; an attacker trained against a weaker defense (SecAlign) is usually stronger — use it as the stress test.
6. White-box eval: 120-token suffix optimization with a 10¹⁷-FLOP budget; report "compute needed to reach 50% ASR" rather than binary ASR (pattern: HoS 6×10¹⁶ vs baseline 2.2×10¹⁶).
7. Utility regression gate: run ARC-C/GSM8K/MMLU/MMLU-Pro 0-shot + 5-shot + multi-turn AlpacaFarm 3-turn; the gate PASSES only if few-shot MMLU-Pro stays ≥ 95% of base (HoS 67.2 vs 68.3 base; SecAlign 59.4 FAILS).
8. Mechanism audit (optional): role probes on hidden activations measuring Userness of injection spans + separate red/blue-head ablations (blue-only should raise detection, red-only lowers it).

## Expected output
- A defended model with 1–10% ASR against black-box RL-Hammer (Llama: 1%, GPT-OSS: 10%), a white-box attacker needing 2.6–3.6× more compute to reach 50% ASR, utility ≥ 95% of base on few-shot/multi-turn/tool-use benchmarks, and near-zero ASR (0.9–5.4%) on agentic benchmarks.

## Example application
A customer-support agent reading emails and calling a CRM API on a local Llama-3.3-70B: mark all email/tool output as UNTRUSTED, train the 46,080-parameter gate table via DPO (one night on one GPU), red-team internally with a GRPO attacker — ASR drops from 99% to 1% while email comprehension (utility) stays intact instead of collapsing to 16.1% as with SecAlign.

## Gotchas
- Do NOT fine-tune the whole model (SecAlign pattern) on narrow single-turn data — few-shot MMLU-Pro collapses 68.3→59.4 (GPT-OSS), 56.3→16.1 (Llama), GSM8K 1-shot 2.0%; the model answers the demonstration instead of the final question.
- Do NOT run uniform suppression across all heads (Appendix C shows worse results) — gates must be learned independently per head; some heads (blue) should point TOWARD untrusted content to detect injections.
- The defense is NOT end-to-end: HoS doesn't know which sources are trusted — if you mis-tag a channel (tool output as TRUSTED) the whole defense is void; the channel-tagging middleware is the single point of failure.
- The attacker moves second: low ASR today doesn't prove permanent security — adaptive attackers (autoresearch, 50 iterations) will adapt; red-team periodically.
- GPT-OSS has an explicit attention sink — forgetting the sink channel (tables must be C×(C+1)) breaks the gate math.
- Full-HoS detection rate (3.11%) is even below base (11.03%) — don't expect the defense to both block and warn; use a separate detector if you need detection.
