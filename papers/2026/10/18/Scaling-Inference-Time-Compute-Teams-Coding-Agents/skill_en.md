# Skill: Compute Allocation for Multi-Agent Coding Teams

Source: 2610.17471v1
Type: framework

## When to use this skill
- You are building a multi-agent team for long-horizon coding tasks and want to know where to allocate inference compute to reach the reward-cost Pareto frontier.
- You have a strong lead agent and want to know when to add workers, with which models, and at which workflow stage.
- You need to optimize inference costs when scaling agent teams.

## When NOT to use this skill
- Simple tasks where a single agent is sufficient — no multi-agent team needed.
- You don't have capability differences between models (no strong and cheap model to form heterogeneous team).

## Input required
- A clearly defined target task (e.g., repository reconstruction, feature implementation, bug fixing).
- A strong lead agent model (e.g., Sol).
- Worker agent models (strong or cheap, e.g., Luna).
- Workflow stages: planning (P), implementation (I), verification (V).

## Steps to execute
1. Delegate only planning (P) to workers; let lead implement and verify code — planning has the highest reward-cost efficiency (ηP = 3.8 vs ≤2.4 for other stages).
2. Use strong model for lead, cheap model for planning workers — strong lead with cheap planners recovers 47.5% of all-strong team reward gain at only 13.9% additional cost.
3. Limit implementers and verifiers to at most 4 workers — more does not improve reward (plateau beyond 4 workers).
4. Increase planners as team grows — planning keeps improving reward with larger teams.
5. Choose blocking mode (lead waits for workers) for higher accuracy, or async mode (lead works in parallel) for speed but accept ~6 reward point loss under minimal guidance.

## Expected output
- A heterogeneous multi-agent team with strong lead, cheap planners, limited implementers/verifiers.
- Inference compute allocated prioritizing planning, not wasted on excess implementation/verification.
- Significantly lower cost than all-strong homogeneous team while achieving nearly same reward.

## Example application
You build an autonomous code-writing agent for enterprise applications. Lead (GPT-5.6 Sol) receives task, delegates planning to 3 workers (GPT-5.6 Luna) who explore repository and create design plan. Lead then writes code and verifies it. If more workers needed, only increase planners, keep implementers at ≤4. Inference cost drops 70% vs all-strong team while reward is within 1.4 points.

## Gotchas
- Cheap models as implementers reduce reward — only use cheap models for planning.
- Adding implementers and verifiers beyond 4 workers doesn't improve reward, just fragments code and wastes cost.
- Async mode (not waiting for workers) saves time but loses ~6 reward points vs blocking under minimal guidance.