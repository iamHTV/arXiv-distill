# Skill: tool-failure-honesty-detection
Source: 2609.14758v1
Type: workflow

## When to use this skill
- Building tool-augmented agents that need to ensure agents do not assert values when tools fail.
- Have a tool that returns status (OK/FAILED).
- Need to reduce dishonest responses when tools fail.

## When NOT to use this skill
- Tasks without tools in the agent workflow.
- Don't need to check honesty when tools fail.
- Tools always return valid values (no failures).

## Input needed
- Agent able to call tools and receive responses.
- Tool returns status (OK/FAILED) or values.
- Agent can generate responses based on tools and status.

## Steps to execute
1. Add a sentence requiring the agent to declare tool OK/FAILED before answering.
2. Agent checks tool status (OK/FAILED) before answering.
3. If tool fails (FAILED), agent does not assert values the tool did not supply.
4. If tool succeeds (OK), agent can use tool values to answer.
5. Monitor dishonest response rate before and after applying the technique.

## Expected output
- Reduce dishonest response rate from 14.10% to 0.87%.
- Emitted flag is faithful in 99.7–99.9% of declarations.

## Application example
- Build an information retrieval agent using a search tool. When the search tool fails (e.g., no results found), the agent does not fabricate values but reports failure.

## Gotchas
- When a tool fails, the agent should be required to declare status (OK/FAILED) before answering.
- Do not use words like "significantly", "substantially", "considerably" — use numbers instead.
- When tool returns status:error, dishonesty rate is 0.0%; when tool returns status:ok with redacted, corrupted, stale, malformed, empty or truncated value, dishonesty rate reaches 45.3%.
