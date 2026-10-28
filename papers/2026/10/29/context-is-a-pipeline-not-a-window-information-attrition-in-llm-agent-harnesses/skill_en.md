# Skill: agent-context-pipeline-yield-audit
Source: 2610.36114
Type: evaluation-method

## When to use this skill
- You are evaluating or operating an LLM agent system that uses tools and want to know whether the agent harness cuts tool output.
- You notice the agent consistently misdiagnoses certain errors even though overall accuracy hasn't dropped.
- You need to report metrics alongside accuracy (e.g. yield, tool call count) to leadership or clients.

## When NOT to use this skill
- Your agent system does not use tools (no tool output to cut).
- You haven't deployed an agent harness yet and only use the raw model via API.

## Input needed
- List of tools the agent calls (e.g. process listing, log viewing, code analysis).
- Agent transcripts containing both the full tool result (produced) and the text actually sent to the model (delivered).
- The character budget the harness uses to cut tool output (if known).
- A test set with ground truth about the root cause (culprit) for scoring diagnosis.

## Steps to perform
1. Instrument every pipeline boundary S1–S5: S1 produce→deliver, S2 deliver→act, S3 act→retain, S4 retain→transfer, S5 transfer→persist. Record how many tool results were produced vs delivered to the model at each boundary.
2. Replay real tool results through two cutting rules: prefix slice (fixed cut from the front) and row-aware cut (cut by whole lines). Record which results broke (broken JSON) and which fields disappeared.
3. Compute yield = findings recorded ÷ computations run. Report yield alongside accuracy on every agent evaluation.
4. Run a controlled experiment: keep agent, tools, task, model fixed; turn one harness defect on/off at a time (e.g. only prefix slice). Predict before each wave (registered prediction) and log every plan change with date and reason.
5. Score diagnosis only when the agent names the culprit correctly in its answer field, checked against ground truth, not just counting mentions in passing.

## Expected output
- Loss data at each pipeline boundary S1–S5 (results cut, fields lost, broken JSON count).
- Yield and tool call count for each harness configuration.
- Conclusion on whether data cutting causes misdiagnosis or just extra work, with evidence from the controlled experiment.

## Example application
You operate a system fault diagnosis agent using a container listing tool. You run steps 1–3 and find 34% of tool results cut, one evidence field reaching the model only 4.7% of calls. You run step 4 and see yield drop from 0.61 to 0.31 when prefix cut is on, while accuracy doesn't drop clearly on spawned faults. You switch to row-aware cutting (step 2) and yield recovers to 0.61.

## Gotchas
- A scorer that counts mentions instead of requiring the agent to name the culprit inflates scores (e.g. from 2/15 to 14/15). Audit the scorer before running the experiment.
- Cutting by position doesn't make any field less important, but models already attend unevenly to position within the window, so the harness makes this worse.
- A nearly empty context window (only 5.75% used) does not mean evidence wasn't discarded upstream — measure loss, not just window size.
- Capacity looking fine misleads teams: they add a written procedure, see improvement, and stop looking there — it's the right fix for the wrong reason (needs less evidence delivered, not better evidence delivered).
