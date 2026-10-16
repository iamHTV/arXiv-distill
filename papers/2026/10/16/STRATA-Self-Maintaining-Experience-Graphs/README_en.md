# [2610.19386v1] STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents

## Problem
LLM agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards. Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undifferentiated pool indexed by embedding similarity, with no typed abstraction hierarchy. They never forget or deduplicate, and are prone to negative transfer, where a superficially similar but directionally opposite experience is recalled and its concrete steps are copied verbatim, actively harming the agent.

## Contribution
- Introduce STRATA: a structured, outcome-grounded, self-maintaining memory that organizes experience into a three-level hierarchy.
- Evaluate STRATA on four interactive benchmarks across two frozen backbones, seven baselines and three seeds, with a component-wise ablation of every mechanism. STRATA obtains the best average score at the lowest latency and fewest environment steps of any memory baseline.
- Deletion precision: 13.2% → 4.8% (threefold improvement).
- Churn: 28.6% → 3.1%.
- Meta's members drawn from a single task family: 92.7%.
- Injection rate: 21.8% → 27.4%.
- 44% fewer lines of injected memory than the most context-hungry baseline.

## Method (core summary)
STRATA organizes experience into a three-level hierarchy: metas (high-level concepts), episodes (event sets), and traces (detailed footprints). STRATA has five maintenance mechanisms that grow, generalize, and forget experience, formulated precisely and reproducibly. Each mechanism handles a different aspect of memory maintenance.

## Key Findings
- STRATA obtains the best average score at the lowest latency and fewest environment steps of any memory baseline on four interactive benchmarks.
- Deletion precision: 13.2% → 4.8% (threefold improvement in deletion accuracy).
- Churn: 28.6% → 3.1% (memory churn reduced dramatically).
- Meta's members drawn from a single task family: 92.7%.
- Injection rate: 21.8% → 27.4% (fewer but better metas retrieved more often).
- 44% fewer lines of injected memory than the most context-hungry memory baseline.

## Actionable Insights
- Don't keep all agent experience in one undifferentiated pool: organize experience into a hierarchy (metas → episodes → traces) so the agent can retrieve accurately without interference from unrelated experience. Apply: solopreneur building self-evolving agents should design structured memory, not just store raw trajectories.
- Need mechanisms to forget and deduplicate old or irrelevant experience: don't keep everything in memory forever. Apply: when building self-learning agents, build mechanisms to delete useless experiences (low churn) to avoid negative transfer.

## Assumptions & Limitations
- Requires agent to have test-time self-evolution capability; doesn't apply if agent only runs once.
- Paper admits: evaluated on four interactive benchmarks, two frozen backbones; may differ on other tasks.
- Limitation paper doesn't mention: not evaluated on many domains beyond the benchmarks used, not tested on real maintenance cost.

## Metadata
- Year: 2026
- Authors: Guanhua Zhu, Hanwen Li, Zhi Wei, Mengnan Du, Chenxi Yuan (NJIT, CUHK-Shenzhen)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.19386
