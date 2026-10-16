# Skill: strata-self-maintaining-experience-graphs
Source: 2610.19386v1
Type: framework

## When to use this skill
- Building self-evolving agents at test time by accumulating experience from previous runs.
- Want the agent to retrieve relevant experience before acting and write new lessons back afterwards.
- Want to avoid negative transfer when old irrelevant experience harms results.

## When NOT to use
- Single-shot agents, no self-evolution process.
- No need for experience memory, agent only answers from internal knowledge.

## Required input
- Previous agent runs (trajectories, episodes, traces).
- A memory system to store and retrieve experience.
- A hierarchy mechanism (metas, episodes, traces) and maintenance mechanisms (grow, generalize, forget).

## Steps
1. Collect agent experience from previous runs (trajectories, episodes, traces).
2. Organize experience into a three-level hierarchy: metas (high-level concepts), episodes (event sets), traces (detailed footprints).
3. Build five maintenance mechanisms: grow, generalize, and forget experience.
4. Before agent acts, retrieve relevant experience from appropriate metas/episodes/traces.
5. After agent acts, write new lessons into memory and apply forgetting mechanisms to delete useless experiences.

## Expected output
- Deletion precision: 13.2% → 4.8% (threefold improvement in deleting irrelevant experience accuracy).
- Churn: 28.6% → 3.1% (memory churn reduced dramatically).
- Best average score at lowest latency and fewest environment steps vs any memory baseline.

## Example application
Solopreneur building a self-learning customer support agent: agent stores previous conversations as experiences, organizes into metas (issue types), episodes (specific conversations), traces (detailed steps). Before answering a new customer, agent retrieves relevant experience from appropriate metas/episodes. After each conversation, agent writes new lessons and deletes useless experiences.

## Gotchas
- Don't keep all experience in one undifferentiated pool: easy to get negative transfer when a superficially similar but directionally opposite experience is recalled.
- Need mechanisms to forget and deduplicate old/irrelevant experience: don't keep everything forever.
- Need to design a hierarchy (metas → episodes → traces) suitable for your domain.
