# Skill: unimaso-prompt-model-optimization

Source: 2610.31743
Type: framework

## When to use this skill

- Building multi-agent LLM systems with agents having different roles.
- Wanting to reduce inference cost without sacrificing task quality.
- Can measure inference cost of each model and task performance.

## When NOT to use this skill

- Systems with only one agent.
- All agents need the same reasoning capability level.

## Input needed

- List of agents and their roles in the multi-agent system.
- Available model pool with different capability levels.
- Task evaluation dataset and inference cost measurement tool.

## Steps to execute

1. Classify agents by role and reasoning requirements: identify which agents need deep reasoning and which only need formatting tasks.
2. Set up search space containing (prompt, model) pairs for each agent role.
3. Use cost-aware Pareto search to find useful quality–cost trade-offs.
4. Evaluate candidates via multi-level feedback: local, downstream, and global.
5. Coordinate updates via topology-aware co-evolution based on agent roles and dependencies.
6. Store successes and failures in cross-level trajectory memory to guide subsequent rounds.
7. Apply optimized model assignment and prompt for each agent role.

## Expected output

- Optimal model assignment for each agent role.
- Optimal prompt for each agent role.
- Identified quality–cost trade-offs.
- Reduced deployment cost compared to homogeneous strongest-model configuration.

## Example application

A team building a multi-agent customer support system: FAQ-handling agents use small cheap models, complex-complaint agents use large models. Use UniMASO to jointly optimize prompts and models for each role, reducing deployment cost by 85.2% compared to using strongest model for every agent while maintaining equivalent quality.

## Gotchas

- Not every agent needs the strongest model.
- Separate prompt optimization misses the interaction between prompts and models.
- Need to consider both quality and cost, not just quality.
- Cross-level trajectory memory helps avoid repeating failures during optimization.