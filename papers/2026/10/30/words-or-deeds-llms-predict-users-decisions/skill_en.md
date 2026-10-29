# Skill: dialogue-user-decision-evaluation (evaluate dialogue-based user decision prediction)

Source: 2610.36813v1
Type: evaluation-method / workflow

## When to use this skill

- You are building an agent/LLM that predicts user actions from dialogue content (e.g. a sales agent guessing whether a user will accept an offer).
- You want to evaluate whether the predictor over-estimates users' promises, and whether it captures how behavior varies by agent persona.
- You need to report prediction quality per statement type (kept/broken) and per agent, not just aggregate accuracy.

Do NOT use this skill when:
- You only need a general cooperation trend without per-user detail.
- The agent does not call external tools; there are no promises or commitments in the dialogue.

## Input needed

- Interaction data: for each round, the user's stated decision, the actual decision (cooperate/defect), the agent the user faced, and the prior decision history of both sides.
- At least two agent personas with different behavior, to compare against.
- One or more LLM predictors to run predictions.
- Tools to compute AUC, accuracy, and prediction bias (predicted minus actual).

## Steps to execute

1. Collect linked data: for each interaction, record what the user said about their decision, the actual decision afterwards, the agent they faced, and the prior decision history of both user and agent.
2. Split data into groups: statements kept, statements broken, statements inconsistent with prior decisions, and per agent/persona.
3. Run the predictor on each information combination (decision record R and dialogue D across 19 combinations), computing AUC and accuracy per group.
4. Insert a statement sentence into rounds without a stated decision, measuring how much the prediction changes versus swapping the user's prior decision.
5. Add Big Five (BFI) scores or compatibility score to the prompt, measuring how much prediction bias is reduced.
6. Report results separately for kept and broken statements, and per agent — not just aggregate accuracy.

## Expected output

- AUC and accuracy of the predictor per statement type (kept/broken) and per agent.
- The extent to which the predictor over-estimates word-keeping rate (predicted keep rate vs actual keep rate).
- Prediction bias difference between agents (e.g. +8.6 points with one agent type, −6.0 points with another).
- Whether adding dialogue meaningfully changes prediction.

## Example application

A sales agent needs to decide whether to adjust price based on a customer's promise ("I will buy if you give 10% off"). Apply the skill: (1) store each promise and whether the customer actually bought afterwards; (2) split into kept and broken promises; (3) run the prediction model on prior purchase history plus dialogue content; (4) compute AUC separately for kept and broken promises; (5) if the model predicts keep rate .70 but actual is .40, reduce the weight of new promises in the concession decision. Result: the agent does not over-concede based on unreliable promises.

## Gotchas

- A promise in dialogue should not be weighted equal to actual behavior; track each user's word-keeping rate.
- Adding dialogue content to model input does not consistently increase AUC (.80 → .79, no detectable gain) — do not drop actual decision history in favor of more dialogue.
- Aggregate accuracy near zero bias can hide large per-agent errors (differences up to 14.6 points between agents).
- Adding personality scores to the prompt only reduces bias by about a quarter — most of the bias remains.
- The study used only 42 Chinese university students, short low-stakes games, all counterparts were GPT-4o — results may differ on real-world data.
