# [2610.17471v1] Scaling Inference-Time Compute with Teams of Coding Agents

## Problem
Multi-agent systems promise a new axis for scaling inference-time compute: rather than having one agent think longer or sample more attempts, a task is split across many agents working in parallel and coordinating. However, in practice, more agents easily produce duplicate work, coordination failures, and higher costs. We therefore formulate team design as a compute allocation problem: starting from a solo agent, where should additional inference compute go to reach the reward-cost Pareto frontier?

## Contribution
- Frame team design as a compute allocation problem: from a solo agent, where should additional inference compute be allocated to reach the reward-cost Pareto frontier.
- Build a minimal multi-agent harness from scratch and trace this frontier by varying, one at a time, the workflow stage at which a lead delegates to workers (planning, implementation, or verification), the models forming the team, and the number of workers.
- Identify three core findings: (1) planning is the most valuable use of workers; (2) cheap models pay off as planners but not as implementers; (3) planners keep improving reward as the team grows, while implementers and verifiers plateau beyond four workers.

## Method
- Hierarchical harness: lead agent decomposes task, delegates subtasks to workers, consolidates results. Workers run in shared sandbox. Lead uses delegate_agent(task, agent_id=None) tool to spawn new workers or resume existing ones.
- Models: three tiers of GPT-5.6 family (Sol, Terra, Luna), medium reasoning effort. Homogeneous teams use same model for lead and workers. Heterogeneous teams pair Sol or Terra lead with Luna workers.
- Datasets: ProgramBench (200 from-scratch repository reconstruction tasks), Commit0-Lite (16 Python libraries).
- Four delegation stage configurations: P (planning), I (implementation), V (verification), PIV (all three stages). Blocking (lead waits) and async (lead continues working) scheduling modes.

## Key Findings
- Teams outperform solo agents but cost 3–7× more in inference dollars.
- A heterogeneous 17-agent team comes within 1.4 points of a strong homogeneous 5-agent team at 70% lower cost.
- ηP = 3.8 (reward pts / $100) vs at most 2.4 for any other stage — each dollar spent on planning buys roughly 1.6× more reward than the same dollar spent on implementation, verification, or full workflow.
- Planning alone matches the reward of heavy PIV guidance at half the cost.
- A strong lead with cheap planners recovers 47.5% of the reward gain of an all-strong team for only 13.9% of its additional cost; cheap implementers lower reward.
- Planners keep improving reward as team grows, while implementers and verifiers plateau beyond four workers.

## Actionable Insights
1. Invest compute in the planning stage before writing code — planning offers the highest reward-cost efficiency. Apply: in multi-agent coding, let workers specialize in planning and repository exploration, while the lead writes and verifies code itself. First step: Change lead prompt to only delegate planning to workers, keeping implementation and verification with the lead.
2. Use cheap models for planning, strong models for implementation. Apply: in heterogeneous teams, use a strong model (Sol) for lead, cheap model (Luna) for planning workers. First step: Set up team with high-end lead model and low-end planner workers only for the planning stage.
3. Limit implementers and verifiers to at most 4 workers — adding more does not improve reward. Apply: when scaling the team, only increase planners, not implementers/verifiers beyond 4. First step: Set maximum of 4 workers for implementation and verification stages.

## Assumptions & Limitations
- Evaluated on ProgramBench (from-scratch repository reconstruction); results may differ on Commit0 or domains outside software engineering.
- Only three GPT-5.6 models (Sol, Terra, Luna); does not generalize to Claude, Gemini, or open-source models.
- Maximum 16 workers studied; teams of hundreds or thousands not examined.
- 84% of messages go to lead, only 4% between workers — unclear how workers coordinate when projects outgrow what a single agent can track.

## Metadata
- Year: 2026, Authors: Keenan Samway, Marzieh Fadaee, Daniel D'souza, Tan Yi-Chern, Omar Darwiche Domingues, Nouha Dziri (Cohere Labs), arXiv category: cs.MA, PDF link: https://arxiv.org/pdf/2610.17471v1