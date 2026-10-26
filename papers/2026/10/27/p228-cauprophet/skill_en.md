# Skill: cauprophet-causal-cognition-agent

Source: 2610.32477
Type: framework

## When to use this skill

- Building agents that need to develop causal understanding from experience and apply it to new decisions.
- Long-horizon tasks requiring agents to remember and reuse causal knowledge across sessions.
- Financial analysis, scientific research, or decision processes requiring causal understanding, not just correlation.

## When NOT to use this skill

- Simple tasks that only need information retrieval, without causal understanding.
- No sufficient evidence to test causal relationships.

## Input needed

- Historical data about tasks and executed results.
- Environment that can provide evidence and new observations continuously.
- Causal inference toolbox.

## Steps to execute

1. Build Causal Cognition: organize knowledge around explanations of how factors influence one another, with conditions, time scales, evidence, and unresolved questions.
2. Build Causal Belief: combine knowledge from Causal Cognition with current evidence to create structured belief capturing causal factors and effects of possible actions.
3. Use Causal Scout: compare alternative explanations and suggest observations that can distinguish them.
4. Make decisions based on Causal Belief: select actions based on causal understanding, not just correlation.
5. Continuous update: as new observations emerge, revise Causal Belief and update Causal Cognition.
6. Apply stored knowledge to new tasks: retrieve relevant Causal Cognition and combine with current evidence.

## Expected output

- Causal Cognition containing causal relationships and conditions of application.
- Causal Belief for each task, guiding decisions.
- Continuously updated causal knowledge persisting beyond individual experiences.

## Example application

A stock analysis team using CauProphet: agent builds Causal Cognition about factors influencing stock returns (price, volume, volatility, market news). In a new analysis period, agent combines stored knowledge with current evidence to build Causal Belief, selects stock ranking formula, and achieves 25.4% improvement over non-causal agent.

## Gotchas

- When evidence is insufficient, agent relies more on base model's prior knowledge.
- Experiments cover a limited number of stages; longer studies needed.
- Not all tasks have clear causal structure.