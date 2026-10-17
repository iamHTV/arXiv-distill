# Skill: Blind-Spot Gate — Certifying a ToM module's deployment (without deploying it)
Source: 2610.19051v1 (Smart Alone, Blind Together)
Type: evaluation-method (deployment certification)

## When to use this skill
- A multi-agent system has a coordinator acting on inferred beliefs about teammates (an LLM reads another agent's convention/state and acts on it), and a wrong action has a real cost.
- You need a go/no-go decision on a ToM module BEFORE production, especially when games/episodes of the module are scarce (direct A/B measurement lacks data).
- Do NOT use when: the module only advises and never acts (accuracy suffices); you cannot simulate the coordinator with injected beliefs; the module makes many coherent errors at once (error load > 4 — use direct measurement instead).

## Inputs required
- A simulator of the coordinator that accepts injected beliefs (run episodes with known-wrong beliefs).
- A cost model: harm h scaling the consequence of a wrong action (e.g., wasted round → eject worker; lives in a game).
- The module to certify: error statistics q_u (error rate per belief u) and joint errors Δ_uv = Pr[both wrong] − q_u q_v.
- A safety floor (how much deferral is acceptable).

## Steps
1. Measure single-error costs: run paired single-injection replays (ThresholdProbe) — for each belief u, inject one wrong belief and measure c_u (the cost of belief u alone wrong). This also predicts the break-even threshold a*(h) = |ℓ(h)|/(1+|ℓ(h)|) within 0.03–0.05.
2. Measure pairwise interactions I_uv: run pair-injection replays (inject two wrong beliefs u, v together); I_uv is the interaction term. First read the sign from task structure: a unit lost when ANY belief is wrong (series) → supermodular (damage overlaps); a unit lost only when ALL are wrong (parallel/redundancy) → submodular (damage compounds).
3. Collect the module's error statistics: q_u per belief, and measured dependence Δ_uv from the module's actual outputs (clone/public/mixed teams).
4. Compute the gate: B̂ = b0 + Σ_u q_u c_u + Σ_{u<v} (q_u q_v + λ Δ_uv) I_uv with λ=1. Act iff B̂ > 0; if B̂ ≤ 0 → defer to the passive belief-free policy.
5. Check the error load: mean wrong beliefs per episode > 4 → the gate (order-2) is no longer reliable; hand off to direct measurement (an A/B test on the estimation half, approving only when the one-sided 95% lower bound > 0).
6. Validate: compare the gate's decisions with direct measurement on held-out episodes; track false approvals (approving harmful deployments) — target zero significant FAs; deferrals are the price paid.
7. For redundant teams (multiple observers): compute n_eff = ln Pr[all wrong]/ln E p_t — if n_eff is near 1 (shared blind-spot errors), redundancy from copies is illusory; diversify models or defer on unread targets.

## Expected output
- A go/no-go decision per deployment cell with measured regret ~0.02 (vs the accuracy rule's 0.056 with 3.2 false approvals); zero significant false approvals over 20 splits; recovers beneficial deployments that accuracy rejects (7 classifiers: regret 0.004 vs 0.479) and catches harmful deployments accuracy approves (Bayesian module: significant FAs in 17/20 splits for accuracy, 1 for the gate).
- A break-even threshold a*(h) per harm level, telling you the accuracy that justifies acting.

## Example application
- A solopreneur runs 3-agent content moderation: agent A reads user intent, agent B acts on that reading. Step 1: inject wrong intent into 100 episodes, measure the cost of one wrong moderation (a false ban = user churn, c_u). Step 2: are moderation decisions parallel (only all wrong → harm) or series (any wrong → harm)? Step 3: measure q_u, Δ_uv from logs. Step 4: if B̂ ≤ 0, defer to the rule-based passive policy until the module improves. Expected: the gate avoids deployments that accuracy (0.8) still approves but where shared errors compound harm.

## Gotchas
- An accuracy threshold calibrated on independent errors fails in a predictable direction: too strict when damage overlaps (rejects beneficial), too lenient when damage compounds (approves harmful) — always determine the series/parallel structure first.
- Copies of one model are NOT n independent observers: three Opus 5.5 copies are worth 1.11 independent observers (all-wrong 9% vs 0.15%); use mixed models (four Claude models misread jointly 7.5% vs 9.0% for Opus clones) or accept deferral.
- The gate is second-order: modules with many coherent errors at once (Haiku in task assignment, ~8 errors/episode in coherent blocks) are wrongly deferred by the gate — check the error load; above 4, use direct measurement.
- Shared default answers (e.g., convention "A" listed first) inflate joint failure on unhinted targets — relabel/rotate defaults or force diverse sampling.
- The gate needs a simulator; if beliefs cannot be injected, fall back to the safety test (A/B + 95% bound) — it costs episodes of the module.
- Max reasoning effort does not rescue redundancy: Opus 5.5 at 13× tokens is no more accurate (0.869) and its copies are worth 1.10 vs 1.11 observers — do not confuse compute with independence.
