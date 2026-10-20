# Skill: Auditing LLM Call-Site Contracts in Agentic Systems
Source: 2610.24545
Type: evaluation-method

## When to use this skill
- Before deploying an agent whose LLM calls select tools, judge actions, or write code to run.
- When auditing security: "the agent has checks" yet still shows odd behavior.
- Do NOT use for one-off scripts without side effects.

## Inputs required
- Agent code plus a list of LLM call sites.
- For each call site: output type and consumer: control flow, execution, model context, human display, data.

## Steps
1. Trace every model output to its final consumer; mark outputs that reach control flow or execution (decision-relevant).
2. Write the expected contract per call site — pre-condition, prompt constraint, post-condition — BEFORE reading the implementation, to avoid bias.
3. Compare expected vs implemented; assign each gap to one of 10 patterns: unchecked call inputs, over-broad authority, underspecified prompt, faulty request assembly, partial format check, unchecked content, fail-open handling, unvalidated action, prompt-only check, path-dependent check.
4. Prioritize fixes: post-conditions (72% gap rate), fail-open handling, and unvalidated actions at decision-relevant sites.
5. Fix with a code change that enforces the constraint (capability-bound where possible), then retest the attack path.

## Expected output
- A per-call-site gap table by pattern plus the % of contract satisfied; target 100%, not "has checks".

## Example
- A customer-service agent picks tools: code checks that the reply parses (partial format check) but not that the tool name is in the candidate pool → unvalidated action. Fix: dispatch only runs tools from the offered set — JARVIS picked tools outside the pool in all 5 runs for lack of this check.

## Gotchas
- Exception handlers returning a default ALLOW = fail-open — switch to DENY/ask-user.
- Constraints stated only in the prompt that code could decide (syntactic) = prompt-only — move them into code.
- Checks that run only on the main path = path-dependent — test every branch.
