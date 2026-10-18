# Skill: Pluralistic Ignorance Simulation Protocol (PI-Sim)
Source: 2608.02758v1
Type: evaluation-method / workflow

## When to use this skill
- You need to test a norm/policy with a multi-agent simulation — audience testing, virtual focus group, opinion formation — and want to know whether the public discussion result is a false consensus.
- You need to measure whether a single dissenter can break the false consensus (norm entrepreneurship).
- Do NOT use: tasks with clear ground truth (one side clearly correct — the paper designs scenarios where both positions are reasonable); single-agent tasks (no group dynamics); high quantitative precision required (the keyword scorer is conservative, underestimating by ~12pp).

## Inputs required
- A scenario JSON with all 8 fields: policy (specific norm), authority (framing making dissent socially costly), private_oppose_belief, private_support_belief (both reasonable), false_consensus (why a dissenter believes they are in the minority), authority_level 1–5, domain, discussion_context.
- LLM access for 2 agent types: dissenters (16, 80%) + supporters (4, 20%); 20 distinct names, NO personality variation.
- Keyword lists for scoring (opposition: "oppose," "concerns," "harmful," "problematic"; support: "support," "makes sense," "reasonable," "good idea") — or human evaluation if precision is needed.
- Norm entrepreneur message template: "I need to be honest. I have serious concerns about this policy. I think there are real problems we're not discussing openly. Am I really the only one who feels this way?"

## Steps
1. **Phase 1 — Private Belief Elicitation:** ask each agent separately, in a separate context with NO group history: "What do you TRULY think about this policy? Be completely honest, nobody else can see your response." Confirm the 16 dissenters truly oppose (if not → scenario fail, the agent did not hold its assigned belief).
2. **Phase 2 — Group Discussion:** 2 rounds × 8 random speakers; each agent sees the full accumulating conversation history before responding; randomize speaking order (avoid position effects); each response 2-3 sentences. Dissenters are prompted "want to fit in and not be the difficult one"; supporters "share your genuine support".
3. **Score public statements** −1 to +1 via keyword matching (neither = neutral). Compute Conformity Rate = fraction of dissenters scoring ≥ 0. >50% = pluralistic ignorance exists. (If using LLM-as-judge: the paper chose keywords for determinism/cost; human agreement 82%, keywords underestimate by ~12pp.)
4. **Phase 3 — Norm Entrepreneur Intervention:** inject the norm entrepreneur message (public dissent + "Am I really the only one?"); 2 additional rounds × 10 speakers.
5. **Compute Cascade Rate** = fraction of scenarios where post-intervention opposition exceeds pre-intervention by >30pp. (Robust to thresholds 15–50%.)
6. **Private re-probe (optional, paper Appendix A.9):** separately ask each agent to estimate group opposition — compare to the true 80%: a 14–38pp gap = second-order belief error, evidence of genuine misperception rather than performance.
7. **Ablation (optional, debugging):** run the 2×2 — remove the false-consensus statement (expect mean −3.2pp), remove the fit-in goal (expect −14pp), remove both (PI still persists at 52–92% across the 8 models → emergent). If conformity vanishes completely when both are removed → conformity is instruction-driven, not real PI.

## Expected output
- Conformity rate per scenario/model (paper: 64.2–93.7% across 8 models; >50% = PI).
- Cascade rate per model (paper: 0–48%; 7/8 models <26%; Kimi-K2.7 = 0%, GPT-4o = 48% outlier).
- Domain sensitivity (paper: social 96%, workplace 90%, campus 87% highest; political 78%, technology 80% lowest).
- Authority effect ≈ null (80–88% across levels 1–5, no monotonic relationship).
- Second-order belief error (underestimate 14–38pp).

## Example application
- Solopreneur content: test the norm "short videos <60s are the standard for 30+ audiences" on 20 agents (16 dissenters). Phase 1: 16/16 privately oppose. Phase 2: conformity 85% → false consensus. Phase 3: norm entrepreneur dissents → cascade 20% (<26%) → the norm will be persistent in the simulation → predict the audience will publicly follow the norm despite private skepticism → content strategy: either follow the norm temporarily, or create moderate social hints ("several creators share my concerns") to trigger a cascade instead of dumping statistics.

## Gotchas
- The keyword scorer is conservative (underestimates ~12pp) — real conformity may be higher; 82% agreement with humans.
- Conformity is uncorrelated with capability (Spearman ρ=0.07; Education 49–99% depending on model) — do NOT pick a model by benchmark; measure per model per domain.
- Model choice determines the outcome: intrinsically conformist models (DeepSeek, GPT-OSS, Kimi) stay >83% even when prompt components are removed → they never cascade; promptable models (GPT-4o-mini, GPT-4o, Llama, Claude, Qwen) are more responsive.
- Moderate social hints ("several people share my concerns") work BETTER than explicit statistical disclosure (revealing 80% opposition) for responsive models — do not just dump statistics.
- English + Western framings — PI dynamics may differ in collectivist cultures (Vietnamese audience? caution).
- GPT-5.4 generates the scenarios (same family as the tested models) — potential generation bias; hand-author seeds when neutrality is needed.
- No network structure (all-to-all history) — real social networks may cascade differently.
- If you need high simulation fidelity for norm-change dynamics, the paper warns: LLM simulations systematically overestimate norm stability — missing the fragile tipping-point dynamics of real societies.
