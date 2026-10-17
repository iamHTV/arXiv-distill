# Skill: continuous-process-level-evaluation
Source: 2610.01833v1
Type: framework

## When to use this skill
- Enterprise AI agent skill is continually revised (tool APIs change, LLM versions update, specs refined from operational feedback).
- Need to detect process-level behavioral drift even when final output is correct.
- Can call real APIs via an independent path to compute ground truth.

## When NOT to use this skill
- Skill has non-quantitative outputs that cannot be checked numerically.
- No independent API path available to compute ground truth.
- No need for continuous evaluation across multiple spec revisions.

## Input needed
- Enterprise agent skill with clear specification (SKILL.md or Skill.txt).
- Template test cases describing intended skill behavior.
- Standalone script calling real APIs via independent execution path.
- Agent harness providing tool-call trace: tool name, arguments, return value, turn index.
- Verifier or human review process for root causes.

## Steps to execute
1. Add a line to the first step of the skill spec directing the agent to record all parsed input parameters to a structured log.
2. Capture the full tool-call trace from the harness execution log: tool name, arguments, return value, conversation turn index.
3. Run a standalone Python script calling the same real APIs via an independent execution path, computing expected per-application values (ground truth).
4. Write template test cases using runtime-resolved placeholders (e.g., $k8s_host_date_calls) instead of hardcoded values; expand templates into presence, argument, scope, execution, redundancy, and call-count checks.
5. Define dependency links (depends_on) between test cases to distinguish root failures from cascaded effects.
6. Evaluate across three layers: Level 1 pre-specified final numerical outcomes; Level 2 seven final-state checks per skill; Level 3 trajectory checks across four dimensions: tool selection, tool arguments, tool ordering, argument scope.
7. Use LLM judge only for brittle checks where exact matching is unstable; execute numeric comparisons through a calculator tool.
8. When a check fails, traverse the dependency graph to distinguish root failures from cascaded failures; report roots with cascaded descendants to reduce the initial review set.

## Expected output
- Continuous evaluation pipeline detecting process-level drift even when final output is correct.
- Reduced number of failed checks needing initial diagnosis (mean 6.34 → 2.65 roots, −58%).
- Reusable template test cases across specs, models, and harnesses.

## Application example
- Revenue Apportionment skill: when spec is condensed or tool API changes, the model shifts behavior at ambiguous steps but the final number remains correct. Add process checks: enforce required phase sequence (fetch → stage → readback → allocate → write), check date ranges and filters with typed constraints, check per-cluster and per-host tool call scope.

## Gotchas
- Framework evaluates one enterprise system and two related skills; generalization to other skill types is unclear.
- 10 trials per cell limits statistical power for small effect sizes.
- Root labels are descriptive, not validated causal explanations.
- LLM judge supplements rather than replaces programmatic checks and does not discover candidate calls.
