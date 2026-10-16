# Skill: heart-tool-use-planner-router-verifier
Source: 2609.01736v1
Type: framework

## When to use this skill
- An agent needs to call tools (search, calculation, data extraction) multiple times in one task.
- Want to reduce API cost when calling tools (up to 85%).
- Want to improve tool-use accuracy on real-world tasks.

## When NOT to use
- Agent calls no tools, answers only from internal knowledge.
- Only calls one simple tool, no need to manage complex tool-calling flow.

## Required input
- A library of tool primitives (reusable tool functions) already available or to be built.
- A large LLM (planner) and a small model (router/executor).
- Tasks requiring multi-step tool use.

## Steps
1. Build tool primitives: a library of reusable functions for common tasks (search, calculation, data extraction, etc.).
2. Set up Planner: large model plans the tool-calling steps for the task.
3. Set up Router: route each step to the appropriate tool primitive.
4. Set up Verifier: verify tool results before answering the user (prevents hallucination/errors).
5. Combine large and small models: large for planning, small for executing simple tool calls (reduce cost up to 85%).

## Expected output
- 84% task completion on 50 real-world tasks (3.8× frontier commercial models).
- Reduce API cost up to 85% vs using large model for every step.
- 0.0% attack success rate under prompt injection attacks.

## Example application
Solopreneur building a market research article agent: Planner plans steps (search competitors, get prices, synthesize), Router routes each step to search or calculation tool, Verifier checks data before writing article. Use large model for planning, small model for search/calculation → reduce API cost by over 75%.

## Gotchas
- SFT-based models almost entirely fail on dynamic agentic tool scenarios — don't use plain SFT for complex tool use.
- Need a curated library of tool primitives; if not available, must build from scratch.
- 85% cost reduction is for the large+small model combination case, not all cases.
