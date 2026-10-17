# Skill: Agent Governance Layer

Source: 2609.22476v1
Type: framework

## When to use this skill
- You are building an LLM agent for a safety-critical system (finance, healthcare, energy, control room) and need to ensure the agent cannot perform dangerous actions without control.
- You need to prevent hallucinated numbers and uncontrolled tool use.
- You want a persistent audit trail for every agent action.

## When NOT to use this skill
- Non-critical applications where agents can freely use tools without approval.
- You don't have a deterministic backend to validate LLM-generated numbers.

## Input required
- List of allowed backend tools (whitelist) with argument schemas.
- List of side-effect actions requiring human approval.
- A deterministic backend for computing and rendering numbers.
- Maximum step budget per agent session.

## Steps to execute
1. Build a governance layer between LLM and all tools/backend — LLM only sends JSON action contracts through the layer, never calls tools directly.
2. Only allow whitelisted tools to execute; schema-validate arguments before running; reject unknown tools or malformed inputs.
3. Set an execution step budget (e.g., 5 steps); agent must terminate when the limit is reached.
4. Require explicit operator approval before every side-effect action (data modification, notifications, external processes). Log approval decisions in the persistent audit store.
5. Every number shown to users must be rendered from deterministic backend results, with unit, variable, and time — LLM cannot generate numbers.
6. Log every tool call, arguments, timestamp, execution status, and output in a persistent audit store.

## Expected output
- An agent with governance constraints: only permitted tools run, dangerous actions need approval, numbers are always accurate from backend.
- A persistent audit trail for all agent activity supporting post-incident review.
- Low governance overhead (12–16ms per request).

## Example application
You build a stock trading assistant agent. The agent can view stock prices (read-only) without approval, but every buy/sell order (side-effect) must be approved by the trader through the governance layer before execution. All numbers about price and volume in responses must come from the backend system, not estimated by the agent.

## Gotchas
- Removing the governance layer causes the model to execute all approval-requiring actions without authorization (45/45 runs in the experiment).
- Without a governance layer: only 39.2% of answers have backend-supported numbers (the rest are LLM-hallucinated).
- The governance layer must be bypass-proof — the LLM cannot modify or skip the governance rules.