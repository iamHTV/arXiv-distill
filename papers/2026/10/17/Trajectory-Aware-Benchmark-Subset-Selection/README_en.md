# [2609.24928v2] Trajectory-Aware Benchmark Subset Selection for Cost-Efficient Software Engineering Agent Regression Testing

## Problem
- Autonomous software engineering agents (SWE-agents) automate complex coding tasks. Evaluating SWE-agents requires running large benchmarks over many real-world software tasks, but each agent update may require re-running the full benchmark to detect regressions, at a cost of hundreds of millions of LLM tokens per run, making evaluation a bottleneck. Simple approaches like random sampling risk producing high-variance, unrepresentative subsets.

## Contribution
- Trajectory-aware subset selection that replaces random sampling with deterministic selection based on trajectory embeddings.
- Groups test instances by test outcome from a recent full run, then selects subset using trajectory embedding space.
- Systematically evaluates 76 subset selection configurations across three regression scenarios: same-configuration reruns, model/configuration changes, and agent framework changes.

## Method (core summary)
- Parse raw trajectories into standardized format.
- Sanitize trajectories to remove outcome signals (passed/failed tokens) so embeddings cluster by behavior not result.
- Pass sanitized trajectories through an embedding model.
- Select subset based on trajectory embedding space: instances closest to centroid of each outcome group.
- Evaluate only the selected subset; use its resolve rate to estimate full suite's resolve rate.

## Key Findings
- 5 authors from Queen's University and Concordia University, arXiv category: cs.SE.
- 76 subset selection configurations evaluated across 3 regression scenarios.
- Best trajectory-aware method: select instances closest to centroid of each outcome group in embedding space.
- At 5% or 10% of test instances: reduces average estimation error by 3-11% and worst-case error by 4-11% vs typical draw, 38-46% vs 95th-percentile draw of strongest baseline.
- 10% trajectory-aware subset keeps median estimation error below 5% while cutting token cost by ~90%.
- Consistency Stratification (Consist-Strat) is strongest baseline: reduces median RMSE by 51% (Single-setup), 31-32% (Multi-model), 40-42% (Multi-agent) vs Random.

## Actionable Insights
1. Group instances by historical outcome before sampling. Application: when selecting a subset for agent regression evaluation, group instances by their test outcome in the most recent full run first.
2. Use trajectory embeddings to select samples closest to each outcome group's centroid. Application: instead of random sampling, use trajectory embedding to pick instances nearest each group's centroid.

## Assumptions & Limitations
- Evaluated on code-repair benchmarks from GitHub issues; may not transfer to agent benchmarks in other domains.
- Each configuration run once.
- Still requires a full regression run to obtain historical outcomes.

## Metadata
- Year: 2026, authors: Mahmoud Ayyad, Zehao Wang, Jiho Shin, Ying Zou, Bram Adams (Queen's University, Concordia University), arXiv category: cs.SE, PDF link: https://arxiv.org/pdf/2609.24928v2
