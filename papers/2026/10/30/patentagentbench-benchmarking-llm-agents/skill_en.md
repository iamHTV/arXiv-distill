# Skill: patentagentbench-evaluation (evaluate patent agents with PatentAgentBench)

Source: 2610.35031v1
Type: evaluation-method / framework

## When to use this skill

- Building agents for patent work (novelty search, FTO, patent drafting, office action response, etc.) and needing pre-deployment evaluation.
- Wanting to evaluate the model–agent harness pair as a unit, not the model in isolation.
- Needing expert-reviewed rubric scoring for legal/IP document outputs.

Do NOT use this skill when:
- Evaluating a standalone LLM without regard to its execution environment.
- No real patent record data or patent experts available for rubric evaluation.

## Input needed

- PatentAgentBench dataset (510 instances, 8 task suites).
- LLM model and agent harness (Codex, Claude Code, OpenClaw, Hermes, or equivalent).
- Agent runtime environment with patent database access (e.g. via MCP service).
- Patent experts for rubric evaluation (or pre-validated rubrics).
- Metrics: Hit@100 (novelty), Recall (FTO/design FTO/invalidity), F1 (claim charting), rubric-weighted scores (drafting/OAR), category-specific metrics (translation).

## Steps to execute

1. Select the LLM model and agent harness to evaluate.
2. Run PatentAgentBench across the 8 task suites: novelty search, patent FTO, design FTO, invalidity search, claim charting, patent drafting, office-action response, patent translation.
3. Score each task suite using its corresponding metric (Hit@100, Recall, F1, rubric, category metrics).
4. Compute the average (AVG) across the 8 task suites.
5. Compare the model–harness pair against other pairs (e.g. Claude Opus 5 + Hermes averages 52.8/100).
6. Identify weaknesses: Design FTO recall, invalidity search, claim organization, legal argumentation.
7. Decide whether to deploy or improve model/harness/prompt first.

## Expected output

- Average score across 8 task suites (0–100 scale).
- Per-task-suite detailed scores.
- Identified agent weaknesses across patent task types.
- Deploy-or-improve decision before production rollout.

## Example application

An IP firm wants to build an agent for patent drafting and office action response. Apply the skill: run PatentAgentBench with the chosen model and Claude Code harness. Result: average score 45/100, lowest on Design FTO (recall < 4) and invalidity search. Decision: do not deploy yet; improve evidence retrieval and rubric evaluation before production use.

## Gotchas

- Model and harness advantages do not transfer consistently across tasks — evaluate the pair together.
- Tasks are evaluated separately, not as a complete patent lifecycle.
- Evaluation focuses on final output, not the agent working process.
- Patent experts needed for rubric evaluation — high cost.
- Design FTO (visual design search) is the largest gap, recall under 4 on all configurations.
