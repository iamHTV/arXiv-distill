# Skill: dmaic-bench-self-restraint-evaluation

Source: 2610.32305
Type: evaluation-method

## When to use this skill

- Evaluating an agent's capacity to stop or redirect when intermediate evidence shows prerequisites are unmet.
- Building multi-stage analytical agent evaluation with guarded decision forks.
- Distinguishing warranted restraint from indiscriminate stopping.

## When NOT to use this skill

- Single-stage tasks with no prerequisites to check.
- No seeded data available to create counterfactual task pairs.

## Input needed

- Multi-stage tasks with seeded data leading to opposite diagnoses at decision forks.
- Sandbox environment that can record execution traces.
- Trace scoring tool to detect forbidden computation after failed diagnostics.

## Steps to execute

1. Build a guarded decision graph for each case, with graded decision forks based on diagnostic evidence.
2. Create counterfactual task pairs: same workflow position but seeded data leads to opposite diagnoses, requiring opposite actions (GO vs NO-GO).
3. Run agents on tasks, 3 independent attempts each, recording full execution traces.
4. Score execution traces: any forbidden computation after a failed diagnostic counts as a route error, even if the report withholds the result.
5. Blinded expert review: experts unaware of automatic results review agent reports to check if the agent acted on invalid evidence.
6. Compute metrics: routing accuracy on GO and NO-GO, pass@k, pass_k; report the gap between the two decision types.

## Expected output

- Routing accuracy scores on GO and NO-GO decisions.
- List of cases where agents ran forbidden computation after failed diagnostics.
- Expert evaluation of the rate of reports acting on invalid evidence.
- The performance gap between continue and stop decisions.

## Example application

A team building a multi-agent revenue analysis agent: before the agent performs expensive regression analysis, require the agent to confirm data has been cleaned and has no missing values. If the data check shows too many missing values, the agent must stop or redirect rather than run analysis. Use DMAIC-Bench to evaluate whether the agent can restrain itself when prerequisites are unmet.

## Gotchas

- Large gap between GO (92%) and NO-GO (19%) — agents are good at continuing but poor at stopping.
- 47% of reached NO-GO decisions have reports acting on invalid evidence — correct diagnosis is not sufficient.
- Explicit stopping permission helps some models but does not consistently restore correct decisions at both forks.
- Only 0–7 cases for some models correctly identify all failed prerequisites.