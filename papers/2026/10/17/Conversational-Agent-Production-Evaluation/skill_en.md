# Skill: Commissioned Agent Evaluation (behavior-specific production agent evaluation)
Source: 2609.32092
Type: evaluation-method / workflow

## When to use this skill
- A production LLM agent (conversational shopping assistant, support agent) needs a specific behavior improved
- Aggregate metrics (relevance, intent understanding, satisfaction) show poor quality but don't indicate which behavior to fix
- Logs can't be replayed (each modification changes subsequent turns) and the system varies run-to-run (LLM stochasticity + daily-changing data)

Do NOT use: the behavior can't be reproduced locally (the investigation must stop — don't optimize against an unstudiable behavior); real users can't be simulated closely enough to reproduce behaviors; you need business outcomes (that requires A/B tests, not this offline framework).

## Input required
- Production logs: customer messages + request context (page, shopping context) + items shown + pseudonymized customer identifiers
- A local instance of the production assistant (full components: guards, router, agents, retrieval, curation)
- An LLM judge + LLM compiler (assertion generation) + customer simulator (grounded user simulation)
- A short description of the behavior to investigate (from a report or automated quality assessment)

## Steps
1. Commission: identify the behavior; the harness produces (a) targeted assertions (pass/fail conditions at several strictness levels: any / first / ≥75% / all) into a versioned assertion library, (b) a fixed cohort of scenarios from the production pool (sampling: random / embedding-based farthest-point–nearest-neighbor–stratified–hybrid / intent-based). Human review of assertions before freezing. Freeze: cohort + assertions + evidence fields + decision thresholds + roles (target/guardrail/diagnostic).
2. Reproduce: run the unchanged local assistant on the cohort; reproduction succeeds when targeted assertions fail on enough of the cohort and the local failure rate ≈ the reported rate. If it fails → stop the investigation.
3. Baseline: ≥3 runs of the unchanged system → stored baseline (behavior + run-to-run variation).
4. Hypothesize: the Improvement Orchestrator reads the assertion profile + traces → diverse hypotheses (prefer diverse over variations of the same local change; propose along the COMPLETE interaction path, not just the component where the failure is visible). Each hypothesis = an isolated modification on a clean local version. Autonomy budget caps the number of versions.
5. Compare: run the modified version the same number of runs on the same scenarios; paired difference per scenario (modified mean − baseline mean); 2,000 percentile bootstrap resamples (fixed seed); verdict: signal+ (interval entirely >0), signal- (<0), noise (contains 0, half-width ≤ threshold 0.05 on the 0–1 scale / 0.25 on the 1–5 scale), borderline (contains 0, half-width > threshold). Borderline → extend to 5 runs.
6. Advance: target signal+ + no guardrail signal- → a second evaluation under the same conditions → both pass → human review → possible online A/B test. Stop at the first reproducible improvement (to avoid optimizing for the frozen cohort).
7. Post-investigation: a reflection step reviews the investigation and how it was conducted; if the evaluation itself was the cause → propose a harness revision (scenario selection, simulation, interpretation) → human approval → new version, applied to future investigations only, NEVER altering recorded decisions.

## Expected output
- A verdict per hypothesis with a paired bootstrap interval + an assertion profile (where the failure lives: any/first/≥75%/all); a modification passing both evaluations → human review + A/B test candidate; a human-gated harness revision list.
- Example: carousel category failure — the profile shows first product 0.833 vs all 0.640 → effect on prominent positions → fix the curation prompt (strict rule) → first product +0.060, all +0.007.

## Example application
- A shopping assistant returning out-of-category products: commission 4 assertions (any/first/≥75%/all category match), a 51-conversation production cohort, 3 baseline runs; hypothesis "the curation prompt's preference is insufficient" → strict rule prompt → 3 runs → paired bootstrap: first product +0.060, profile confirms the prominent-position mechanism → deploy. Gender case: h1 (tool description) borderline +0.067 [−0.022,+0.178] → reject; h2 (context as binding default in a different agent's system prompt) +0.267 [+0.067,+0.511] signal+ + reproduced in 3 runs + guardrail passes → confirmed offline.

## Gotchas
- DON'T pool all sessions: pooling counts scenario difficulty as uncertainty and loses small improvements that hold in every scenario. The scenario is the unit of analysis; repeated sessions are NOT independent observations.
- A higher guardrail score is NOT a reason to accept (task completion 4.27→4.96 in the gender case — only target signal+ matters; guardrails only need no signal-).
- Audit the judge as software: evidence sufficiency (an assertion lacking the evidence it needs), config propagation (temperature=0 configured but not passed to the model), statistics (between-scenario vs across-run variance). Plausible-looking output can still be wrong.
- The cohort is NOT a random sample — its failure rate describes the cohort, NOT the production frequency; don't report it as a production rate.
- Multiplicity: the hypothesis count is not fixed in advance (50 nulls @ 0.05 → P(≥1 false signal+) > 0.9); classical corrections (Bonferroni) don't fit (the same modification accepted early, rejected late) — use anytime-valid e-values (Ville's inequality) for long loops; small cohorts (9 scenarios) → bootstrap under-covers, so borderline triggers more runs, not acceptance.
- Cost scales with hypotheses: a 3-turn session ≈ 4k (simulator) + 13k (task-completion) + 6k per assertion tokens; a 300-session × 4-assertion investigation ≈ 10M tokens.
- A frozen evaluation goes stale: record the assistant build + judge models; rerun the baseline when either changes.
- The simulator does NOT replay the log — the first message is unchanged, subsequent turns are GENERATED conditioned on the recorded messages (style examples, not a script); validate it by reproducing reported failures + reading for plausibility.
- The loop stops at the first reproducible improvement BY DESIGN — exploring further requires new evidence or a fresh cohort (don't loop on the frozen cohort).
