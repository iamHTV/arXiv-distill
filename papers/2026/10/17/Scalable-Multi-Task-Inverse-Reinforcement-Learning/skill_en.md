# Skill: scalable-multi-task-irl
Source: 2610.00758v1
Type: framework

## When to use this skill
- Building multi-task inverse reinforcement learning systems in the same environment.
- Need to learn from multiple related tasks in the same environment under a low-rank assumption.
- Want to transfer to target environments with lower regret than baselines.

## When NOT to use this skill
- Single tasks not related to each other.
- No data from multiple related tasks in the same environment available.
- Don't need to transfer to target environments.

## Input needed
- Data from multiple agents with different rewards in the same environment.
- Low-rank assumption for related tasks.

## Steps to execute
1. Pool data from multiple agents with different rewards in the same environment.
2. Apply low-rank assumption to learn a common-across-tasks low-dimensional representation of the task's input (in our context, agents' preferences).
3. Learn rewards for each task from the pooled data.
4. Transfer to target environments with lower regret than baselines.
5. Monitor regret and computational cost.

## Expected output
- Multi-task inverse reinforcement learning system able to learn from multiple related tasks in the same environment.
- Robust to limited coverage.
- Transfers to target environments with lower regret than baselines.
- Computational advantage over per-task methods widening as tasks grow.

## Application example
- Build an inverse reinforcement learning system to learn from multiple related tasks in the same environment (e.g., product recommendations for multiple different customers on the same e-commerce platform). Use low-rank assumption to learn a common-across-tasks low-dimensional representation of the task's input (in our context, customers' preferences).

## Gotchas
- Evaluation on multiple tasks in the same environment under a low-rank assumption.
- No detailed information about training time and computational cost.
