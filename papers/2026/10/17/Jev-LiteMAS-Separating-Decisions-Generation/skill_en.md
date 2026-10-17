# Skill: jev-litemas-decision-routing
Source: 2610.21411v1
Type: framework

## When to use this skill
- Building multi-agent systems that need to reduce token cost for orchestration decisions (routing and review).
- Have specialized expert agents and need to select the right expert for each task.
- Need to inspect intermediate artifacts before deciding the next step.

## When NOT to use this skill
- Tasks don't involve multiple specialized agents.
- Don't need to reduce token cost (only care about absolute quality).
- No predefined expert roles and legal actions available.

## Input needed
- List of expert roles and legal actions predefined.
- Task and prior expert outputs.
- Lightweight decision model (Jev).
- Generative LLM for task execution and artifact review.

## Steps to execute
1. Analyze task and select expert dynamically from task and prior expert outputs, using accumulated context to ground subsequent execution without pre-generated trajectory.
2. Expert executes task and generates intermediate artifact.
3. Jev screens intermediate artifacts based on task criteria: passing artifacts proceed directly, flagged ones undergo LLM re-review for acceptance (ACCEPT) or corrective feedback (REVISE).
4. Evaluate on benchmarks and two backbones (e.g., DeepSeek-V4-Flash, GPT-5).
5. Monitor generative-LLM token count and accuracy.

## Expected output
- Reduces generative-LLM tokens by 12.7–54.6% vs LAS.
- Maintains accuracy within 1.34 percentage points.
- Reduces latency in seven of eight settings.

## Application example
- Build multi-agent system for complex tasks: use Jev to dynamically select expert agents (e.g., code expert, test expert, doc expert), inspect intermediate artifacts before deciding next step, only call LLM review when artifact needs correction.

## Gotchas
- Feedback-driven routing operates over a predefined pool of expert roles and legal actions.
- Framework does not dynamically create new expert roles.
- Evaluated on 4 benchmarks and 2 backbones.
