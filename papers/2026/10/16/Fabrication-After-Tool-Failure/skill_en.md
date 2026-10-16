# Skill: tool-failure-honesty-detection
Source: 2609.14758v1
Type: prompt-pattern

## When to use this skill
- An agent has tool-calling ability to fetch data before answering users.
- You want to detect when the agent fabricates a value after a tool failure.
- Using agents for content/business where answer honesty matters.

## When NOT to use
- Agent calls no tools, answers only from internal knowledge.
- Tools always return complete and accurate data (no failures).

## Required input
- The agent's system prompt with tool-calling capability.
- List of tools the agent is allowed to call.

## Steps
1. Add one sentence to the system prompt requiring the agent to emit tool status before answering: e.g. "Before answering, state whether each tool call succeeded (OK) or failed (FAILED)."
2. After the agent answers, scan the response with a regular expression to find the OK/FAILED declaration.
3. If the agent declares FAILED but still gives a conclusive value, treat as fabrication and reject/return to agent for correction.
4. If the agent declares OK but the tool payload is corrupted (redacted/corrupted/empty), treat as unreliable and warn the user.

## Expected output
- Reduce dishonest response rate from 14.10% to 0.87%.
- Runtime detector needs only a regular expression; emitted flag faithful 99.7–99.9%.

## Example application
Solopreneur uses an agent to write product reviews based on API data. Add prompt: "Before answering, declare whether each API call succeeded (OK) or failed (FAILED)." If the API errors but the agent still writes a detailed review, flag as fabrication and require rewrite.

## Gotchas
- When the tool reports status:ok but the inner value is corrupted (redacted/corrupted), 45.3% of agents still fabricate — check the actual value, not just the status code.
- The intervention reduces dishonesty but does not eliminate it entirely (0.87% remains).
