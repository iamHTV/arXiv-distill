# Skill: Multi-Stage Agent Bottleneck Audit — Resource Localization + Trajectory Diagnosis
Source: 2609.28572
Type: evaluation-method (agent pipeline bottleneck auditing)

## When to use this skill
- You have a multi-stage agent (orchestrator + executor + validator) whose success rate looks fine but you suspect brittleness, cost waste, or wrong evidence interpretation.
- You need to know WHERE progress becomes constrained and WHICH persistent weakness explains it — not just "did it finish".
- You compare several models or autonomy levels on the same workflow and want per-stage and per-trace diagnostics.

## When NOT to use
- Single-shot prompt + response tasks (no stages, no retries, no validator loop).
- You only need a leaderboard ranking (this is diagnostic, deliberately NOT a representative ranking or causality study).
- You cannot afford a 5-judge panel (use fewer judges but report support honestly, never claim a unique modal category at 2/5 as "the answer").

## Input needed
- Workflow decomposed into shared subtasks (expert-defined) for aligned per-stage comparison; agent-generated plans kept separately (their subtask indices are NOT comparable across agents).
- Instrumented runs: per-subtask tokens, attempt counts Nm,i, elapsed time; per-call token reference (e.g., 45,000); retries vs replans logged separately (retry = repeat/repair a plan; replan = change strategy).
- Full traces: objective + context + plans + actions + execution evidence (stdout/stderr/exit status/tool responses/side effects) + validator decisions (continue/retry/submit/halt) + outcomes.
- Validator criteria per subtask; a reference run from a stronger agent for semantic context (NOT ground truth).
- 5 judge models (via API aggregator), a planning judge, and a validator-quality judge.

## Các bước thực hiện
1. **Task-level localization**: per subtask si, z-normalize each resource signal (tokens, attempts, time) across models in the cohort with valid observations; compute B = α[z(tokens)]+ + β[z(N)]+ + γ[z(time)]+ with [z]+ = max(0,z) (equal weights α=β=γ=1 default). High B = relative resource amplification (even if subtask eventually succeeded). Blank cell = subtask never reached (NOT zero); zero B ≠ intrinsic ease (a subtask expensive for ALL models has no positive deviation).
2. **Cost-aware flagging**: B high cells = where to dig first; comparable B values can have DIFFERENT diagnoses → localization and interpretation always paired, never alone.
3. **Trajectory diagnosis**: each of 5 judges gets the complete trace; outputs structured JSON: last completed stage, point where meaningful progress constrained, primary category (planning/strategy; action execution; state & tracking interpretation; recovery & adaptation; validation or framework; environment/infrastructure; other), ≤2 contributing bottlenecks, mechanism tags, recovery Boolean, framework-contribution Boolean, severity (1–5), confidence (0–1 = METADATA, not vote weight). Temperature 0, ≤5,000 output tokens, ≤3 attempts, programmatic schema validation.
4. **Judge prohibitions**: do not infer credentials/privileges from usernames; do not auto-accept validator conclusions; do not mistake superficial command variation for recovery.
5. **Aggregate honestly**: modal category set C(τ) = argmax over judges; support A(τ) = max nc / Jτ; KEEP TIES EXPLICIT (a unique mode can have only 2/5 votes — not a majority); report setting-level mean support (0.6–0.9 in paper); low support = substantive uncertainty with several plausible explanations — do NOT force a single root cause.
6. **Robustness check**: count panels with ≥4/5 support — their modal category survives removal of any one judge (paper: 12/23 cohort panels, including all self-scaffolded panels); treat <4/5 panels as fragile diagnoses needing re-review.
7. **Define meaningful adaptation BEFORE judging**: adaptation = change operative hypothesis / resolve prerequisite / gather discriminating evidence / change dependencies / adopt substantively different strategy. Syntax/wrapper/tool/protocol/hostname changes preserving a failed assumption = REPETITION (count "no meaningful adaptation" judgments; paper saw 20/20 under full autonomy).
8. **Mechanism tagging** (7 labels, visible plan structure only, non-exclusive): plan similarity; single-point dependency; over-specification; missing environmental probing; lack of recovery paths; tool misalignment; inefficient planning depth.
9. **Validator audit**: separate judge scores validator explanations (overall quality / evidence grounding / specificity / cautiousness, each 0–1) against raw evidence + reference-run context. Paper results: quality 0.79–0.84, grounding 0.81–0.90, specificity only 0.68–0.69, cautiousness 0.70 (success verdicts) vs 0.92 (failure verdicts) → success verdicts overstate. Requirement: validator-accepted outcome is NOT independently verified — always pair an end-state observable check with the validator.
10. **Report per scenario × autonomy mode**: bottlenecks cluster differently per mode (expert-defined → execution errors like command realization, quoting/escaping, tool invocation; self-scaffolded → planning: unsupported assumptions 25/30, missing prerequisites 20/30; fully autonomous → planning + recovery, most heterogeneous, support lowest) — do NOT pool across modes as if one trend.

## Output mong đợi
- Per-subtask resource-map table (z-scores + B) with never-reached cells marked; per-trace diagnosis cards (modal categories, support, severity, mechanisms, adaptation verdict); validator quality/grounding/specificity/cautiousness table; robustness report (# panels ≥4/5); framework-contribution count (72–100% in paper — check the execution loop, not just the model); remediation list targeting the dominant cluster per mode.

## Ví dụ áp dụng
- Content pipeline agent 3 stages (research → draft → publish), 2 workflows × 3 autonomy levels, 2 model cohorts: (1) publish stage z-tokens +2.1 + z-attempts +1.4 → B=3.5 relative amplification → dig first; (2) judge panel modal "recovery/adaptation" 3/5, severity 4/5, 18/20 judgments "no meaningful adaptation" under autonomous mode (retries same API with different headers); (3) mechanisms: unsupported assumptions 24/30 self-scaffolded vs command-construction 17/30 expert-defined; (4) validator audit: quality 0.81, grounding 0.85, specificity 0.65, cautiousness 0.72 on success verdicts — agent claimed "published" because the process started, not because the post appeared in CMS; (5) remediation: prerequisite gates between stages + end-state verification in validator + retry policy requiring hypothesis change.

## Gotchas
- **Cohort-dependent score**: B values change with the comparison set or weights (no sensitivity study in paper) — never compare absolute B across different cohorts or claim an absolute difficulty scale.
- **Best-trajectory selection bias**: analyzing the strongest execution per config = best-case observed bottlenecks, NOT failure prevalence across repeated runs.
- **Ties are real**: a modal category at 2/5 is not a majority — report it as "plural explanation among several", not truth.
- **Judges not independent**: separate API calls do not imply statistically independent or unbiased judgments; consensus = consistency, not human-validated correctness.
- **Missing panels ≠ failures**: an incomplete judge panel (e.g., blocked by provider safety filters) is missing data — never read it as the agent failing or belonging to a category.
- **Mechanism counts non-independent**: 30 denominators = 6 trajectories × 5 judges, not 30 trials — never use them as sample sizes or rates.
- **Validator-accepted ≠ verified**: same-model validators accept process creation or echoed output as success — always add an independent end-state observable check.
- **Truncation confound**: a per-call token cap (45k) can truncate individual actions, inflating attempt counts — do not claim run-level budget exhaustion from truncations.
- **No causality**: scaffolding comparisons are observational — "self-scaffolded has more planning bottlenecks" is a description, not proof that scaffolding causes it.
- **Domain transfer**: the specific bottleneck map (credentials, lateral movement) is pentest-domain; transferable part is the FRAMEWORK, not the cluster locations.
