# [2610.01833v1] Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills

## Problem
- Enterprise AI agent skills are not static artifacts — they are continually revised as tool APIs change, LLM versions update, or skill specifications are refined from operational feedback. Prior work does not address process-level behavioral drift during evolution — because it only checks final-output accuracy, missing procedural deviations like calling APIs with wrong scope, skipping required database readback, or writing intermediate results to the wrong table.

## Contribution
- Continuous evaluation framework combining outcome-level and process-level quality checks for enterprise agentic skills.
- Five-stage pipeline independent of the agent session under evaluation: (1) capture input + parse tool-call trace, (2) compute ground truth via independent API calls, (3) materialize template test cases, (4) evaluate (outcome + process checks), (5) report root failures with cascade attribution.
- Template test cases with runtime-resolved placeholders instead of hardcoded values, providing reusable regression coverage.

## Method (core summary)
- Stage 1: Agent records input parameters to structured log; captures full tool-call trace (tool name, arguments, return value, conversation turn index) from harness execution log.
- Stage 2: Standalone Python script calls the same real APIs via an independent execution path, computing expected per-application apportionment values.
- Stage 3: Template test cases describe intended skill behavior using runtime-resolved placeholders (e.g., $k8s_host_date_calls); dependency links (depends_on) define root failures and cascaded effects.
- Stage 4: Three evaluation layers — Level 1: pre-specified final numerical outcomes; Level 2: seven final-state checks per skill; Level 3: trajectory checks across four dimensions: tool selection, tool arguments, tool ordering, argument scope. LLM judge used only for brittle checks where exact matching is unstable.
- Stage 5: When a check fails, framework traverses the dependency graph to distinguish root failures from cascaded failures.

## Key Findings
- 240 automatic trials, 2 skills (Revenue: 104 test cases; Productivity: 80 test cases), 2 spec variants (SKILL.md, Skill.txt), 2 harnesses (Claude Code, Codex), 3 models (GPT-5.6-Sol, Claude Opus 4.8, Claude Sonnet 4.6).
- 175/240 passed all applicable final numerical checks; among them, 162 (92.6%; Wilson 95% CI: 87.7–95.6%) had at least one additional evaluator-detected deviation → final-value checks alone miss deviations in 67.5% of all trials.
- 164/240 passed all seven final-state checks; among them, 151 (92.1%; Wilson 95% CI: 86.9–95.3%) still violated at least one trajectory check.
- Dependency attribution compresses mean 6.34 failed checks per run to 2.65 roots (−58%).
- No configuration reached 100% mean suite score; Revenue deviations at most one cent.

## Actionable Insights
1. Combine outcome and process checks in the evaluation pipeline to detect behavioral drift even when final output is correct. Application: add a process check layer to the agent enterprise evaluation pipeline — check tool selection, arguments, ordering, scope alongside final value check.
2. Use template test cases with runtime-resolved placeholders instead of hardcoded values to reuse regression suites when specs change. Application: write template test cases with placeholders like $k8s_host_date_calls, resolved at runtime from ground truth, with dependency graphs to compress failed checks to root causes.

## Assumptions & Limitations
- Evaluates one enterprise system and two related skills; generalization to other skill types, tool suites, or non-quantitative outputs remains open.
- 10 trials per cell limits statistical power for small effect sizes.
- Root labels not independently validated as causal explanations.
- Longitudinal validation under real API evolution remains future work.

## Metadata
- Year: 2026, authors: Ngoc Phuoc An Vo (IBM), Aarya Doshi (Georgia Tech), Vadim Sheinin (IBM), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2610.01833v1
