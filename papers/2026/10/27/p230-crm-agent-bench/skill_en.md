# Skill: crm-agent-bench-contract-evaluation

Source: 2610.32004
Type: evaluation-method

## When to use this skill

- Evaluating tool-using agents in stateful enterprise environments.
- Building executable contracts to verify agents execute business processes correctly.
- Measuring scored coverage, latency, and cost of agents.

## When NOT to use this skill

- Agents that only answer questions without taking actions on systems.
- No clear business rules to write executable contracts.

## Input needed

- List of stateful, multi-turn business tasks.
- Checks on actions, arguments, order, response, target state, and protected state.
- Execution environment to run agents and collect traces.

## Steps to execute

1. Build executable contracts for each task: define checks on actions, arguments, order, response, target state, and protected state.
2. Run agents on each task, recording full execution traces.
3. Score strict success: success is the strict conjunction of all declared checks.
4. Report scored coverage (fraction of checks passed), latency, and cost.
5. Analyze per-domain reliability and cost of each agent system.

## Expected output

- Strict success score for each agent.
- Scored coverage, latency, and cost for each task.
- Per-domain reliability analysis and deployment cost analysis.

## Example application

A team building an internal CRM agent: before deploying an agent for customer care processes, write executable contracts for each task (e.g., "update contact info" must call the right tool, pass right arguments, not modify protected states like credit limits). Use CRM-Agent-Bench to evaluate the agent on strict success, scored coverage, latency, and cost.

## Gotchas

- Strict success requires ALL checks to pass, not just most.
- Leading systems diverge sharply in cost and per-domain reliability — no system optimizes everything.
- Protected state must not be modified by the agent.
- Evaluates the full agent system, not just the language model alone.