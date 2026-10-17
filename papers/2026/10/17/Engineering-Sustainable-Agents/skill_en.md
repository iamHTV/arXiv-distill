# Skill: sustainable-agent-design
Source: 2610.03010v1
Type: framework

## When to use this skill
- Building developer agent systems and wanting to reduce energy consumption and inference time.
- Need to select model and prompt per task rather than using one configuration for all tasks.
- Balance accuracy, energy, and time trade-offs.

## When NOT to use this skill
- Single-step tasks that don't need an agent.
- Don't need to optimize energy consumption and time.
- No multiple models and prompts to choose from.

## Input needed
- Software engineering tasks: code generation, technical debt identification, code vulnerability detection, log parsing, log analysis.
- LLM models (open-weight models).
- Agent harnesses.
- Skill specifications (skill spec) and test cases.

## Steps to execute
1. Identify software engineering tasks to perform.
2. Select LLM model suitable for each task.
3. Select prompt strategy suitable for each task.
4. Select agent configuration (non-agentic, single-agent, multi-agent).
5. Select hardware platform (CPU, GPU, etc.).
6. Evaluate each configuration in terms of accuracy, inference latency, and energy consumption.
7. Select Pareto-optimal configuration (saving energy and time without reducing accuracy too much).

## Expected output
- Reduce energy consumption and inference time for agent dev.
- Maintain accuracy for software engineering tasks.
- Select Pareto-optimal configuration for each task.

## Application example
- Build a dev agent to write code, fix bugs, and write tests. Use sustainable agent design to select model and prompt per task, reducing energy consumption and time without reducing accuracy too much.

## Gotchas
- Evaluated on code-repair benchmarks from GitHub issues; results may not transfer to agent benchmarks in other domains.
- Evaluated on 4 backbone models.
- No detailed information about training time and computational cost.
- Do not default to multi-agent — lightweight configurations are often Pareto-optimal.
