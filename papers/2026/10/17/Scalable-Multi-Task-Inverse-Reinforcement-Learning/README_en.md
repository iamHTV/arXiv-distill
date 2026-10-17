# [2610.00758v1] Scalable Multi-Task Inverse Reinforcement Learning

## Problem
- Inverse reinforcement learning aims to recover rewards that rationalize behavior in expert demonstrations, serving as revealed preferences, enabling imitation learning, and supporting alignment from human feedback. Many settings feature heterogeneous tasks — each task maps one-to-one to an agent-specific reward function. Shutting down a train line leads commuters with distinct preferences over speed, cost, and crowding to re-route accordingly. A planner must anticipate this re-optimization despite limited state coverage by each commuter. We consider N independent tasks, that is N agent-specific reward functions, for each of which we observe the induced soft-optimal behavior in a source environment. We then seek to learn these rewards so as to anticipate how the behavior of agents would transfer to a target environment.
- Single-task demonstrations typically concentrate on a narrow region of the state space, so partial coverage weakens reward identification. Specifically, in the maximum-entropy RL framework, this materializes as temperature varies: high temperature improves coverage but flattens choice probabilities, while low temperature sharpens the reward signal but narrows coverage. Fitting N tasks independently inherits the single-task support problem.

## Contribution
- Scalable multi-task inverse reinforcement learning method that pools data across multiple agents with different rewards in the same environment under a low-rank assumption.
- Learning across tasks together to learn a common-across-tasks low-dimensional representation of the task's input (in our context, agents' preferences).

## Method (core summary)
- Multi-task inverse reinforcement learning method that pools data across multiple agents with different rewards in the same environment under a low-rank assumption.
- Learning together across tasks a common-across-tasks low-dimensional representation of the task's input (in our context, agents' preferences).

## Key Findings
- 4 authors from Netflix, Cornell Tech, MIT, arXiv category: cs.LG.
- Evaluates the method on multiple tasks under new environments.
- The method is robust to limited coverage.
- Recovers rewards on and off of each task's support.
- Transfers to target environments at lower regret than baselines.
- Computational advantage over per-task methods widening as tasks grow.

## Actionable Insights
1. Use multi-task inverse reinforcement learning to learn from multiple related tasks in the same environment under a low-rank assumption. Application: when you have multiple related tasks in the same environment, use multi-task inverse reinforcement learning to learn how to compute rewards for each task.
2. Use a low-rank form to learn a common-across-tasks low-dimensional representation of the task's input (in our context, agents' preferences). Application: use a low-rank form to learn a common-across-tasks low-dimensional representation of the task's input when there are multiple related tasks.

## Assumptions & Limitations
- Evaluation on multiple tasks in the same environment under a low-rank assumption.
- No detailed information about training time and computational cost.

## Metadata
- Year: 2026, authors: Allen Tran, Jia Wan, Nathan Kallus, Aurélien Bibaut (Netflix, Cornell Tech, MIT), arXiv category: cs.LG, PDF link: https://arxiv.org/pdf/2610.00758v1
