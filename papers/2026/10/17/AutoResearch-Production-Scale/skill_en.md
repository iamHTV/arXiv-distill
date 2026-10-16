# Skill: AutoResearch Production Scaffolding
Source: 2609.30541
Type: framework (multi-agent orchestration for long-horizon experiment loops)

## When to use this skill
- Running an autonomous optimization loop (ML training script, content pipeline, automation) where each iteration costs real compute/money
- Campaigns longer than a single context window, spanning multiple runs/jobs
- Do NOT use: one-shot tasks, cheap disposable iterations (auto-revert suffices), or trivial evaluation without an agent

## Inputs required
- Repeatable task: script/code or config the agent edits (train.py, config)
- Immutable evaluator: metric (scalar or multi-criteria) the agent must NOT modify
- program.md: research program + accumulated findings + constraints (known negative results)
- Compute budget + keep threshold (τkeep), stagnation threshold (τstag), window size

## Steps
1. Identify the smallest self-contained loop (hypothesis → run → evaluation) that still produces signal — over-broad loops waste budget, over-narrow loops cannot reach improvements.
2. Add a Code Fixer gate (pre-execution): an Opus-class agent reviews + rewrites the Researcher's script in a single pass before execution; catches DDP/multi-GPU misconfiguration, OOM precursors, recomputation, dataloader bugs, eval-loop errors. Do NOT use a two-step Reviewer→JSON→author loop (produces consecutive malformed JSON).
3. Persist cross-job: after each Keep, update program.md + iteration summary → durable storage (S3); encode constraints and known failures. Every new job inherits the full history.
4. Configure the Criticizer (stagnation-only): fires when the best metric has not improved >8% relative over a 5-iteration window; emits a 2–5 sentence directive pointing to a NEW region of the design space (not specific code); clears the directive on Keep. 3 iterations = noise, 8 iterations = too late.
5. Split models by role: Sonnet-class for high-volume code generation; Opus-class for gate/critic roles where a wrong call wastes hours of compute.
6. Scale to cost: expensive iterations (hours) → pre-execution gate; cheap iterations (minutes) → post-execution automatic revert. Multi-metric reporting + human QA between runs to mitigate metric fixation.

## Expected output
- An agent loop running hundreds of experiments without losing iterations to coordination failure; catches paradigm shifts via directives; negative results are not re-tested (reduced, not eliminated).

## Example application
- Content optimization pipeline: each iteration = agent tweaks recommendation strategy + measures CTR. Code Fixer validates the plan before launch; Criticizer triggers "the problem is not the content, it is the representation" when CTR flatlines for 5 cycles.

## Gotchas
- Two-step review (Reviewer returns JSON → another agent authors) fails with 14 consecutive malformed JSON calls — always single-pass rewrite.
- The 8%/5 thresholds were chosen empirically on recommendation — recalibrate for other domains.
- The agent still re-tests prohibited configs ~6 times despite explicit program.md prohibition — memory decay is reduced, not eliminated.
- Metric fixation is NOT solved: the agent never questions the metric — human QA between runs is mandatory.
