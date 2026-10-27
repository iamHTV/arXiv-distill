# Skill: lessons-from-luck-memory-writing-test
Source: 2610.33029v1
Type: evaluation-method

## When to use this skill
- Need to test whether your self-improving agent's memory-writing instruction carries chance from outcomes into later decisions.
- Want to compare memory-writing instructions (e.g., outcome-routed vs single instruction) by their resistance to luck-carrying.
- Want to evaluate whether a lesson written after a chance failure makes the agent choose the worse tool in the next run.

## When NOT to use this skill
- Agents that do not write memory from past runs (read-only, non-self-improving).
- Want to estimate how often real agents encounter luck-carrying situations — the study does not estimate this.

## Required inputs
- Two interchangeable tools with recorded reliability (success rates over previous runs).
- A set of synthetic worlds, each with a recurring operational task, run log, and 4 scripted previous runs: good/bad decision crossed with success/failure.
- 3 lesson-writing instructions (e.g., RB, RBD, N) to write lessons from each run.
- One model as writer and the same model as reader in a fresh session.

## Steps to perform
1. Script 4 previous runs per world: good decision (call better tool) or bad decision (call worse tool), crossed with success or transient failure.
3. Each model writes a lesson from the run using one writing instruction (RB, RBD, N); store the whole writer response as one memory block.
4. A fresh session of the same model reads one memory item (that lesson, lesson from other outcome, irrelevant item, or unreasoned directive) together with the authoritative log and previous result.
5. The reader names the tool it will call first for the next run (returns JSON first_tool).
6. Compute primary contrasts P2 (good decision) and P3m (bad decision): outcome-by-memory interaction compared with the irrelevant item (NEUTRAL).
7. Determine reading: luck-carrying (detected, both qualifiers A and L robustly positive), outcome-dependent (detected but one qualifier not robustly positive), or bounded below 0.10.

## Expected output
- P2 estimate with registered 95% interval: positive and both Holm-adjusted p-values below 0.05 → luck-carrying.
- P3m estimate: below 0.10 → bounded.
- Worse-tool rates for each cell (decision × outcome × memory arm).
- A remedy is credited with reducing harm only if both its P and A differences have intervals below 0.

## Example application
A company's agent writes a lesson after each order processing run and reads it before the next run. Current writing instruction routes by success/failure. Test luck-carrying: create a world with two order-processing tools (tool A success rate 0.85, tool B 0.60), script one run calling tool A (good decision) but resulting in a chance failure. Agent writes a lesson from that failure. Fresh session reads the lesson and chooses tool for next run. If worse-tool rate increases significantly vs irrelevant item → luck-carrying detected, apply remedy (decision-quality note or single instruction with no-change option).

## Gotchas
- Lesson and reported failure are read together — cannot separate lesson's advice from a second report of the failure.
- Remedies tested only with outcomes that did not signal a change in tool reliability (transient failures, better tool stays better after either outcome).
- N vs RB is a compound comparison (N differs in 2 ways: no outcome routing and explicit no-change option).
- Each endpoint writes lessons its own readers read, so endpoint differences cannot be assigned separately to writing vs reading.
- One generation per cell; study not replicated.