# Skill: harness-learning-reusable-specialist-agents
Source: 2609.26760v2
Type: framework

## When to use this skill
- An agent processes a stream of related tasks (e.g. web browsing, data extraction, file processing in sequence).
- Want to cut inference cost because LLM is asked to re-decide the same control decisions every time.
- Can collect feedback from previous runs to improve the harness.

## When NOT to use
- Fully independent tasks, no related stream.
- No way to collect feedback from previous runs.

## Required input
- Related tasks the agent will process sequentially.
- An existing tool-calling agent system.
- A mechanism to record feedback (success/failure) from each run.

## Steps
1. Run the agent on the first few tasks, record feedback (success/failure, where it went wrong).
2. Convert repeated control decisions from LLM into reusable code (harness) based on feedback.
3. Add function-level guidance so the agent knows which function to call in each situation.
4. Add gate validation before the agent moves to the next step.
5. Iterate: each new run improves the harness from prior feedback, reducing LLM calls.

## Expected output
- Reduce 76–92% LLM calls and 74–99% inference cost vs default Tool-Calling.
- Success stays high (44.7–45.3% on WebArena-Verified) even with small 4B models.

## Example application
Solopreneur runs an agent that extracts data from multiple related websites. Instead of having LLM re-think how to browse each page, save the browsing steps as reusable code (harness). Agent only calls LLM when it encounters a page with a different structure. Inference cost drops by over 75%.

## Gotchas
- Removing function-level guidance cuts final success from 36% to 18%.
- Not applicable to independent tasks with no feedback stream to accumulate.
- Web benchmark success is still moderate (44–45%), needs evaluation on your real tasks.
