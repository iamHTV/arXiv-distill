# Skill: RAAC — Retrieval-Aware Agent Controller (anti-stagnation for DRAs)
Source: 2608.15191
Type: evaluation-method / control-loop framework

## When to use this skill
- A deep research / RAG agent issues many search iterations while recall has already saturated — suspected "reasoning stagnation" (the agent loops and doesn't know when to stop)
- You want to cut search calls/cost without hurting (or while improving) recall/accuracy
- The agent is a black box or any architecture (RAAC is agent-agnostic, works outside the agent's policy)

Do NOT use: short trajectories (1–3 searches) — the controller overhead (~10% latency) isn't worth it; simple factoid queries needing no multi-hop; no criteria (human or LLM-generated) available to compute coverage.

## Input required
- Agent trajectory: history H_t = (thought, action/query, observation/docs) per turn; top-k docs per search (paper uses k=5)
- An encoder for embeddings (paper uses Qwen3-Embedding-4B)
- A criteria list C for the query (human-provided like BROWSECOMP-PLUS, or LLM-generated — but use the Cov signal ONLY with human criteria)
- One LLM for the critical re-thinker and the controller (paper uses Claude Sonnet 4.5)

## Steps
1. At the end of each iteration t, compute 4 signals: Nov_t = |D_t \ D_{1:t-1}|/|D_t| (fraction of never-before-seen docs); Cov_t = (1/|C|)ΣW(c,t) with W = 1.0 fully covered / 0.5 partial / 0 uncovered; Div_t = 1 − cos(e_t, e_{t-1}) (how different consecutive queries are); Sim_t = cos(e_t, e_x) (is the query still near the original topic — guardrail).
2. The controller (prompt-based) maps signals → action ∈ {continue, intervene, stop}. Rules of thumb from the paper: Nov ≈ 0 for several consecutive iterations + high Cov → stop; Nov ≈ 0 but low Cov + low Div (repeating queries) → intervene; Sim dropping sharply → intervene (drifting).
3. Intervene: call the critical re-thinker with H_t → output (critical reasoning thought τ' + a substantially different, creative query q'); retrieve docs D'; append the triplet (τ', q', D') to the history — do NOT restart the trajectory.
4. Stop: generate the intermediate/final answer from H_t (same spawn-answer pattern: τ'_T, r_T ~ π(·|f(H_t))).
5. Track win/tie/loss against gold docs: win = RAAC retrieves more gold documents; target win ≈ 2× loss (paper: 33–41% win vs 15–18% loss). If loss > win, re-check signal thresholds.
6. (Optional) Ablation check: without human criteria, run WITHOUT Cov (paper: Cov hurt on NEuCLIR/LEGALSEARCH when criteria were LLM-generated).

## Expected output
- Search calls reduced ~14 on average (paper: up to 44, −33% to −58% depending on agent/dataset) with recall/accuracy improved or held (accuracy +up to 10%, +3% avg); controller overhead ~10% of agent latency.

## Example application
- A BrowseComp-Plus query: the base agent answers at iteration 23 although the answer was available at iteration 8. With RAAC: intervene early → relevant document at iteration 4 → stop at iteration 8. Tongyi-DR: 77.8→33.6 search calls (−44) with recall 48.4→59.0.

## Gotchas
- Nov is the most important primary signal (AUROC 0.81 vs New-item Recall) — don't drop it; Div has the lowest correlation (0.46–0.64), don't rely on Div alone.
- Use Cov only with human criteria; LLM-generated criteria made Cov hurt performance on 2 of 3 datasets.
- The controller is prompt-based with fixed weights — not per-query adaptive; for a specific domain, tune thresholds or move to a learned controller (the paper's future work).
- Keep Sim as a guardrail: high novelty + low Sim = drifting off-topic; don't reward novelty alone.
- CPM-Report-style agents (terminate too early) need the opposite: RAAC will INCREASE search calls — don't mistake increased calls for a bug.
- The ~10% latency overhead assumes short controller outputs; if the critical re-thinker outputs long text, overhead grows.
