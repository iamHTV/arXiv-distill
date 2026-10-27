# Skill: Bottleneck Audit cho Multi-Stage Agent — resource localization + trajectory diagnosis
Source: 2609.28572
Type: evaluation-method (agent pipeline bottleneck auditing)

## Khi nào dùng skill này
- Bạn có multi-stage agent (orchestrator + executor + validator) mà success rate ổn nhưng nghi brittle, cost waste, hoặc hiểu sai execution evidence.
- Bạn cần biết WHERE progress bị constraint + WHICH persistent weakness giải thích — không chỉ "xong chưa".
- Bạn so sánh nhiều models / autonomy levels trên cùng workflow, muốn per-stage + per-trace diagnostics.

## Khi nào KHÔNG dùng
- Single-shot prompt + response task (không stages, không retries, không validator loop).
- Chỉ cần leaderboard ranking (skill này diagnostic, cố ý KHÔNG phải representative ranking hay causality study).
- Không afford 5-judge panel (dùng ít hơn nhưng report support honest, đừng bao giờ claim unique modal 2/5 là "the answer").

## Input cần có
- Workflow decomposed thành shared subtasks (expert-defined) cho aligned per-stage comparison; agent-generated plans kept riêng (subtask indices KHÔNG comparable across agents).
- Instrumented runs: per-subtask tokens, attempt counts Nm,i, elapsed time; per-call token reference (e.g., 45,000); retries vs replans logged riêng (retry = repeat/repair plan; replan = change strategy).
- Full traces: objective + context + plans + actions + execution evidence (stdout/stderr/exit status/tool responses/side effects) + validator decisions (continue/retry/submit/halt) + outcomes.
- Validator criteria per subtask; reference run từ stronger agent cho semantic context (KHÔNG phải ground truth).
- 5 judge models (qua API aggregator), planning judge, validator-quality judge.

## Các bước thực hiện
1. **Task-level localization**: per subtask si, z-normalize each resource signal (tokens, attempts, time) across models in cohort có valid observations; B = α[z(tokens)]+ + β[z(N)]+ + γ[z(time)]+ với [z]+ = max(0,z) (α=β=γ=1 default). B cao = relative resource amplification (dù subtask eventual success). Blank cell = subtask never reached (KHÔNG phải zero); B=0 ≠ intrinsic ease (subtask expensive cho ALL models thì no positive deviation).
2. **Cost-aware flagging**: B-high cells = dig first; comparable B values có thể DIFFERENT diagnoses → localization + interpretation luôn paired, never alone.
3. **Trajectory diagnosis**: mỗi 5 judges nhận complete trace; output structured JSON: last completed stage, point where meaningful progress constrained, primary category (planning/strategy; action execution; state & tracking interpretation; recovery & adaptation; validation or framework; environment/infrastructure; other), ≤2 contributing bottlenecks, mechanism tags, recovery Boolean, framework-contribution Boolean, severity (1–5), confidence (0–1 = METADATA, không vote weight). Temperature 0, ≤5,000 output tokens, ≤3 attempts, programmatic schema validation.
4. **Judge prohibitions**: không infer credentials/privileges từ username; không auto-accept validator conclusions; không mistake superficial command variation for recovery.
5. **Aggregate honest**: modal category set C(τ) = argmax over judges; support A(τ) = max nc / Jτ; KEEP TIES EXPLICIT (unique mode có thể chỉ 2/5 votes — không majority); setting-level mean support (paper 0.60–0.90); low support = substantive uncertainty (nhiều plausible explanations) — KHÔNG force single root cause.
6. **Robustness check**: count panels ≥4/5 support — modal category survive removal of any one judge (paper 12/23 cohort panels incl all self-scaffolded); <4/5 panels = fragile diagnoses cần re-review.
7. **Define meaningful adaptation BEFORE judging**: adaptation = change operative hypothesis / resolve prerequisite / gather discriminating evidence / change dependencies / adopt substantively different strategy. Syntax/wrapper/tool/protocol/hostname changes preserving failed assumption = REPETITION (count "no meaningful adaptation" judgments; paper 20/20 under full autonomy).
8. **Mechanism tagging** (7 labels, visible plan structure only, non-exclusive): plan similarity; single-point dependency; over-specification; missing environmental probing; lack of recovery paths; tool misalignment; inefficient planning depth.
9. **Validator audit**: separate judge scores validator explanations (overall quality / evidence grounding / specificity / cautiousness, mỗi 0–1) vs raw evidence + reference-run context. Paper: quality 0.79–0.84, grounding 0.81–0.90, specificity chỉ 0.68–0.69, cautiousness 0.70 (success verdicts) vs 0.92 (failure verdicts) → success verdicts overstate. Requirement: validator-accepted outcome KHÔNG independent verified — luôn pair end-state observable check với validator.
10. **Report per scenario × autonomy mode**: bottlenecks cluster khác nhau per mode (expert-defined → execution errors: command realization, quoting/escaping, tool invocation; self-scaffolded → planning: unsupported assumptions 25/30, missing prerequisites 20/30; fully autonomous → planning + recovery, most heterogeneous, support lowest) — KHÔNG pool across modes như 1 trend.

## Output mong đợi
- Per-subtask resource-map table (z-scores + B) with never-reached cells marked; per-trace diagnosis cards (modal categories, support, severity, mechanisms, adaptation verdict); validator quality/grounding/specificity/cautiousness table; robustness report (# panels ≥4/5); framework-contribution count (paper 72–100% — check execution loop, không chỉ model); remediation list targeting dominant cluster per mode.

## Ví dụ áp dụng
- Content pipeline agent 3 stages (research → draft → publish), 2 workflows × 3 autonomy levels, 2 model cohorts: (1) publish stage z-tokens +2,1 + z-attempts +1,4 → B=3,5 relative amplification → dig first; (2) judge panel modal "recovery/adaptation" 3/5, severity 4/5, 18/20 judgments "no meaningful adaptation" under autonomous mode (retries same API với headers khác); (3) mechanisms: unsupported assumptions 24/30 self-scaffolded vs command-construction 17/30 expert-defined; (4) validator audit: quality 0,81, grounding 0,85, specificity 0,65, cautiousness 0,72 trên success verdicts — agent claim "published" vì process started, không phải vì post thật sự xuất hiện trong CMS; (5) remediation: prerequisite gates giữa stages + end-state verification trong validator + retry policy requiring hypothesis change.

## Gotchas
- **Cohort-dependent score**: B values change với comparison set hoặc weights (no sensitivity study in paper) — never compare absolute B across cohorts hoặc claim absolute difficulty scale.
- **Best-trajectory selection bias**: analyzing strongest execution per config = best-case observed bottlenecks, KHÔNG failure prevalence across repeated runs.
- **Ties are real**: modal category 2/5 không phải majority — report as "plural explanation among several", không phải truth.
- **Judges not independent**: separate API calls không imply statistically independent hoặc unbiased judgments; consensus = consistency, không human-validated correctness.
- **Missing panels ≠ failures**: incomplete judge panel (bị provider safety filter block) = missing data — never read as agent failing hay belonging to category.
- **Mechanism counts non-independent**: denominator 30 = 6 trajectories × 5 judges, không phải 30 trials — never use as sample sizes hoặc rates.
- **Validator-accepted ≠ verified**: same-model validators accept process creation hoặc echoed output as success — always add independent end-state observable check.
- **Truncation confound**: per-call token cap (45k) có thể truncate individual actions, inflating attempt counts — do not claim run-level budget exhaustion từ truncations.
- **No causality**: scaffolding comparisons observational — "self-scaffolded has more planning bottlenecks" là description, không proof rằng scaffolding causes it.
- **Domain transfer**: specific bottleneck map (credentials, lateral movement) là pentest-domain; transferable part = FRAMEWORK, không phải cluster locations.
