# Skill: Designing Scalable Multi-Agent Systems with 4 Principles

Source: 2607.27942v1
Type: framework

## When to use this skill
- You are building an LLM-based multi-agent system (MAS) and want to know how to scale without degrading performance.
- You have a base LLM that already achieves acceptable accuracy on single tasks and want to know when to add agents.
- You need to design inter-agent communication to avoid context overload as the system grows.

## When NOT to use this skill
- The base LLM does not yet achieve basic accuracy on the target task — architectural complexity cannot compensate for a weak model.
- You need a simple system where one agent is sufficient — no multi-agent needed.

## Input required
- A clearly defined target task (e.g., solving system engineering tasks, writing code, managing projects).
- A base LLM already evaluated on single tasks.
- A list of required agent roles (e.g., Planner, Solver, Tester, Approver).

## Steps to execute
1. Confirm base model capability: run the single model on the target task; proceed only if accuracy meets an acceptable threshold.
2. Design a primarily sequential workflow, inserting feedback loops only at stages that truly need refinement (e.g., Tester → Solver).
3. Apply summary-based communication: each agent, upon finishing, writes a 2–3 sentence natural-language summary into a shared channel; do not share full reasoning traces.
4. Limit each agent to at most 3 successors in the topology to control complexity.
5. Expand architecture incrementally (Singleton → MAS-S → MAS-M → MAS-L), tracking cost and accuracy at each level; stop when accuracy no longer improves.

## Expected output
- A multi-agent system with clear architecture, each agent knowing its role and successor.
- Each turn produces only a concise summary, not a full context dump.
- Inference cost scales linearly (not exploding); accuracy peaks at intermediate complexity.

## Example application
You build an autonomous code-writing agent. Instead of one large agent doing everything, split into: Planner (makes plan), Coder (writes code), Tester (runs tests), Reviewer (checks work). Each agent receives a summary from the previous agent, does its work, then writes a summary to the shared channel and decides who runs next. If tests fail, the Reviewer triggers a loop back to the Coder.

## Gotchas
- Do not add agents to compensate for a weak base LLM — MAS exploits existing capability, it does not create capability from nothing.
- Consistency is often below 50% at every scaling level — measure consistency alongside accuracy.
- Feedback loops only help if the responsible agent actually triggers them; if not, loops are skipped and add no value.