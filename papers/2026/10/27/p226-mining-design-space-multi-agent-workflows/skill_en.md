# Skill: mining-design-space-multi-agent-workflows

Source: 2610.31709
Type: framework

## When to use this skill

- Designing multi-agent LLM workflows for complex reasoning tasks requiring coordination between agents.
- Wanting to choose communication topology and prompt templates that can improve accuracy without extensive trial and error.
- Can collect execution traces from prior workflow searches.

## When NOT to use this skill

- Simple tasks that don't require multiple agent coordination (single-agent suffices).
- No prior workflow search data available (no MCTS traces or evaluated workflows).

## Input needed

- Collection of evaluated workflows with graph.py source code and prompt.py templates.
- Task bundle with deterministically verified scores.
- Tool to run workflows and collect execution traces.

## Steps to execute

1. Run workflow search via MCTS (e.g., AFlow) over N rounds per task, retaining ALL intermediate rounds (not just the best workflow).
2. Build a corpus of (workflow, task, score) triplets from all search rounds, including failed rounds.
3. Analyze workflow code (graph.py) and prompt templates (prompt.py) to extract features: entry operator, chain length, placeholder count, prompt template length, etc.
4. Fit a regression model from workflow features and task descriptors to score, using L0-penalized objective (R² − λ||φ||₀) to select fewest features with highest explanatory power.
5. Verify extracted principles on held-out searches not used during training.
6. Apply verified principles: avoid starting with Star fan-out, use SharedMemory instead of Debate, write specific prompts with named placeholders.

## Expected output

- List of workflow design principles verified on held-out data.
- Scoring formula and L0-penalized objective for evaluating new workflow designs.
- Specific recommendations on communication topology and prompt templates for target task.

## Example application

A team building a multi-agent customer support agent: instead of having 5 agents independently handle different aspects of an order then aggregating (Star-first), start with a sequential coordinator (Sequential) and use a persistent shared document (SharedMemory) for agents to update order information. Write detailed prompt templates with placeholders like {order_details}, {customer_history} to route context.

## Gotchas

- Star-first hurts accuracy (median Δ = −0.045) — do not start with independent fan-out.
- SharedMemory outperforms Debate (Δ = +0.135) — persistent document better than multi-round conversation.
- Prompt specificity has gains comparable to communication-structure selection (Δ = +0.118) — do not underestimate prompt template design.
- R² from graph.py only = 0.521, with prompt.py = 0.638 — sub-topological structure in prompt matters as much as macro-topology.