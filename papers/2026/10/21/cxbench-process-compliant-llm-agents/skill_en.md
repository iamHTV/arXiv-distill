# Skill: cxbench-process-compliance-evaluation

Source: 2610.25954v1
Type: framework / workflow

## When to use this skill
- When evaluating process compliance of LLM agents in regulated customer-service workflows (finance, healthcare, insurance, etc.).
- When wanting to detect failures hidden by correct outcomes (false-pass): agent achieves business result but violates process.
- When needing a two-tier evaluation system: deterministic checks (ordering, authority) + LLM judge (semantic requirements).

## When NOT to use this skill
- When tasks have no explicit process requirements (only need final-state checking).
- When lacking domain-specific tool environment or customer simulator.
- When lacking regulatory data to build rule cards.

## Required inputs
- Task list with customer goal, initial business state, private customer facts, domain-specific tool interface, regulatory context and process requirements.
- Rule cards: each card links a cited regulatory obligation to applicability conditions, required behavior, observable trace evidence, and evaluation criterion.
- Customer simulator (fixed LLM) simulating customer replies.
- LLM judge (e.g., gpt-5.6-sol) for semantic requirement evaluation.
- Shared runtime to record traces and control submission.

## Steps to execute
1. Build rule cards from regulatory obligations: each card records ID, source citation, obligation, required evidence, and deterministic check or LLM judge checklist item.
2. Design tasks: each task combines customer request, tool-based environment, explicit process requirements, confirmation contract (fields requiring customer review).
3. Run agent: agent interacts with customer simulator via conversation and uses domain-specific tools through shared runtime; runtime records trace and controls submission (default: agent prepares draft, runtime submits only after customer confirms matching fields).
4. Evaluate outcome: outcome checker confirms final business state satisfies task's expected result.
5. Evaluate process: hybrid grader combines deterministic checks (event ordering, tool permissions, confirmation-submission agreement) with LLM judge (task-specific checklist) for semantic requirements.
6. Compute verdicts: overall success requires both outcome and process to pass; false-pass = outcome pass ∧ process fail.
7. Compare models: track outcome-pass rate, both-pass rate, false-pass rate per model.

## Expected output
- Evaluation report: outcome-pass rate, both-pass rate, false-pass rate per model and per domain.
- False-pass list for reviewing potential compliance risks.
- Improvement decision: add process checks, adjust prompts, or change runtime submission.

## Example application
A bank uses an LLM agent to handle unauthorized transaction disputes. CXBENCH evaluates the agent not just on whether the dispute was filed (outcome), but also on whether the agent provided the required written confirmation notice when receiving an oral error notice (process). If the agent files correctly but misses the disclosure, it's a false-pass — outcome-only scoring would count it as success, but CXBENCH flags it as a Regulation E process violation.

## Gotchas
- No real inference cost data for hybrid grader.
- No direct comparison with other benchmarks beyond Table 1.
- No evaluation on tasks outside regulated customer service.
- Judge development is not an independent held-out validation set (calibration traces only).