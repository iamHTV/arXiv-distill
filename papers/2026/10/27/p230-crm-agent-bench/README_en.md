# 2610.32004 — CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments

## Core Value (1 sentence)

CRM-Agent-Bench is an execution-grounded benchmark for tool-using agents in stateful enterprise environments, comprising 555 stateful, multi-turn tasks across 9 business domains and 36 capability tags — strict success across 16 systems ranges from 64.32% to 83.60%, showing current agents still struggle to execute multi-step business processes accurately and comply with policies.

## Problem

Deploying language agents in real applications demands more than the right answer: an agent must execute a multi-step business process correctly, follow domain-specific rules, and interact with a user across a dialogue, where the gap between saying and doing is the gap between a satisfied customer and a real loss. Existing benchmarks often only evaluate the final answer without checking whether the agent executed the correct tools, arguments, order, and target state.

## Contribution

1. **CRM-Agent-Bench**: An execution-grounded benchmark of 555 stateful, multi-turn tasks across 9 business domains and 36 capability tags.
2. **Executable contract**: Each task supplies a task-specific executable contract drawn from checks over actions, arguments, order, response, target state, and protected state; success is the strict conjunction of the checks declared for that task.
3. **Full agent system evaluation**: Evaluates the complete agent system through these contracts and reports scored coverage, latency, and cost.
4. **Results**: Across 16 systems evaluated on the audited final release, strict success spans 64.32% to 83.60%; leading systems diverge sharply in cost and per-domain reliability.

## Method

CRM-Agent-Bench builds each task as an executable contract including:

1. **Action checks**: Did the agent call the right tool?
2. **Argument checks**: Did the agent pass the right arguments?
3. **Order checks**: Did the agent execute actions in the right order?
4. **Response checks**: Did the agent respond with the right content?
5. **Target state checks**: Is the system state after execution correct?
6. **Protected state checks**: Did the agent perform forbidden actions on protected state?

Success is the strict conjunction of all declared checks for that task. The benchmark reports scored coverage, latency, and cost.

## KNOWLEDGE — Data & Concepts

- 555 stateful, multi-turn tasks across 9 business domains.
- 36 capability tags.
- 16 agent systems evaluated.
- Strict success: 64.32% to 83.60%.
- Leading systems diverge sharply in cost and per-domain reliability.
- Project: https://github.com/salesforce-misc/crm-agent-bench
- Project page: https://crm-agent-bench.github.io/

## INSIGHT — Mechanism & Why

[Low strict success (64.32%–83.60%)] occurs BECAUSE [current agents still struggle to execute multi-step business processes accurately — calling wrong tools, passing wrong arguments, executing in wrong order, or violating protected state]. This means [evaluating only by final answer hides execution flaws in the workflow].

[Leading systems diverge sharply in cost and per-domain reliability] occurs BECAUSE [no system optimizes everything — some systems achieve high accuracy but are expensive, some are cheap but unreliable in certain domains]. This means [there is a trade-off between quality, cost, and per-domain reliability when choosing agents for enterprise].

## IDEA — Actionable Applications

1. Build executable contracts for internal agents: Before deploying agents for business processes, define clear checks on actions, arguments, order, response, target state, and protected state. First step: list required steps in the process and write automated checks for each step.

2. Evaluate agents on scored coverage, latency, and cost: Don't just measure final accuracy; measure the fraction of checks passed, execution latency, and cost per task. First step: set up metrics across these three dimensions for each candidate agent.

3. Check protected state: Identify system states the agent must not modify (e.g., account balance, maximum discount) and build checks to block the agent from performing forbidden actions. First step: list protected states in your system and write blocking rules.

## WISDOM — General Principle

- Principle: In enterprise agent systems, the ability to execute processes correctly is as important as answering correctly — an agent must not just "say" it did something, but must actually "do" every step correctly.
- When to use: When building agents for stateful business processes (CRM, accounting, supply chain, etc.).
- When NOT to use: Agents that only answer questions without taking actions on systems.
- Example outside original domain: In banking, a loan approval agent must not just say "approve" but must correctly execute every step — income check, credit history, collateral — and must not modify protected states like regulatory capital requirements.

## Assumptions & Limitations

- Conditions that must hold: stateful tasks with executable checks; enterprise environment with clear rules.
- Paper's acknowledged limitations: benchmark focuses on CRM environment; 16 systems evaluated may not represent all agents in the market.
- Limitations paper does NOT state: effectiveness on non-CRM domains; cost of maintaining executable contracts at scale; generalizability across different agent frameworks.

## Metadata

- Year: 2026
- Authors: Monojit Banerjee, Zhujun Lan, Defu Cao
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.32004
- Citation count: not yet (new paper, Oct 2026)