# Skill: Conditional-Insight Routing Loop for Agent Configurations
Source: 2610.35690 (EvoRouter)
Type: workflow / evaluation-method (training-free manual adaptation of the paper's expert loop)

## When to use this skill
- Your agent system uses a model pool or MAS (multi-agent system) configurations (collaboration modes, agent counts, interaction rounds, skills) and you don't yet know which configuration fits which task type.
- Inference cost grows fast as you scale agents while accuracy does not improve proportionally.
- Do NOT use: single-model/single-tool agents — no configuration space to optimize; 100% homogeneous tasks; cost per execution not logged.

## Inputs needed
- Execution log: each record with task type, difficulty, budget, config used (model, mode, agent count, rounds, skills), outcome (pass/fail from a verifier), cost (FLOPs, tokens, or money — pick ONE consistent unit).
- Config catalog: all available models/modes/agents/rounds/skills with descriptions.
- Per-task-type verifier: code sandbox tests, QA exact match, or NL rubric.
- Per-task-type reference budget = cost of the current best baseline configuration.

## Steps
1. Log quality–cost–config for at least 50–100 executions across task types before distilling anything (a single trajectory is insufficient evidence — the paper's core gap).
2. Periodically (weekly), run an expert LLM through the paper's 3-step distillation: (i) rule induction — compare intra-type trajectories across success/failure and cost spectra to extract conditional rules on capability alignment, scaling saturation, and configuration interaction; (ii) precondition refinement — when two rules conflict, tighten boundaries (add difficulty/domain dimensions); (iii) capacity pruning — merge duplicate rules, keep a ~20-rule ceiling to curb context inflation.
3. Every rule MUST be of the form "IF <task conditions> THEN <configuration>" with explicit applicability conditions — no unconditional rules (Insight 1: benefits reverse across task types).
4. Manual routing policy: new task → match rule conditions → use that configuration; no-match → cheapest default configuration + log for later distillation.
5. Architect a cost penalty per the paper: penalty = log2(1 + cost/budget); a configuration rule is valid only when its success rate exceeds its failure rate — prioritize "success at low price" over "success at any price".
6. After each batch of ~50 executions: re-verify each rule against new outcomes; stale rules get pruned; new patterns go back to step 2.

## Expected output
- A ruleset {conditions → configuration} with measured average accuracy and average cost per rule, plus a default configuration for no-match, plus logged saturation points for rounds/agents per task type.

## Example application
- Content agency workflow: log 120 posts (blog/social/email) × 3 configurations → rules "IF social AND length <300 words THEN 1 small agent + IO; IF blog AND needs data THEN 2 agents + Debate"; applying them keeps accuracy while cutting cost ~40%, analog of the paper's 50.95%.

## Gotchas
- Do NOT trust a single run's outcome: the paper shows one trajectory reflects only one configuration — need ≥5–10 runs per cell before inducing rules.
- Scaling is NOT proportional: rounds/agents have configuration-dependent saturation points (Insight 2) — set a default cap (e.g. 3 rounds), expand only on verifier failure.
- Model-composition rankings reverse across collaboration modes (Insight 3) — test combinations, not components in isolation.
- Old insights conflicting with new ones require precondition refinement, otherwise the policy gets pulled in two directions.
- Cost units must be consistent (never mix tokens with money in one log).
