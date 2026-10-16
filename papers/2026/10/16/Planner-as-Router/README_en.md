# [2609.32917v1] Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows

## Problem
Running LLM agents in production gets expensive fast. A frontier model (the largest, most capable tier) is accurate but can cost 25 times what a small model costs per token, and the gap compounds once a workflow chains several calls together.

## Contribution
- Introduce Planner-as-Router (PaR): joint plan-time model routing for cost-efficient multi-agent workflows.
- PaR cuts cost 44% against all-frontier routing (using the large model for every step) at the cost of only 2.9 accuracy points.
- PaR's measured plan mix: 45% small, 46% mid, 8% frontier, averaging 1.8 subtasks per plan.
- Complexity classifier labels 43% SIMPLE (a single small-tier subtask, no full planner call) and 57% COMPLEX.

## Method (core summary)
PaR routes models at plan time: the planner decides which model tier (small/mid/frontier) each subtask should use, instead of using the frontier model for every step. A complexity classifier classifies tasks as SIMPLE (43%) or COMPLEX (57%). Each plan averages 1.8 subtasks.

## Key Findings
- PaR cuts cost 44% vs all-frontier routing, trading off only 2.9 accuracy points.
- Plan mix: 45% small, 46% mid, 8% frontier; 1.8 subtasks per plan on average.
- 43% of task-runs are SIMPLE (small-tier only), 57% are COMPLEX.
- PaR achieves comparable accuracy to SinkFrontier (26.1% vs 25.4%) at comparable cost.
- Benchmark of 1,157 evaluations on SQL-Compose, Mongo-Gen, etc.

## Actionable Insights
- Don't use the frontier model for every step: route each subtask to the appropriate model tier (small/mid/frontier) based on complexity. Apply: solopreneur running multi-agent workflows should add a plan-time routing layer, only using the large model for subtasks that truly need deep reasoning.
- Use a complexity classifier to classify tasks as SIMPLE/COMPLEX before deciding model tier. Apply: before calling the large model, classify simple tasks (use small model) and complex tasks (use large model) to save cost.

## Assumptions & Limitations
- Requires the ability to estimate task complexity before routing; doesn't apply if complexity cannot be estimated.
- Paper admits: absolute accuracies are low (22-29%), reflecting how hard execution-based grading is on compositional tasks.
- Limitation paper doesn't mention: not evaluated on task types beyond SQL/Mongo, not tested on real deployment cost.

## Metadata
- Year: 2026
- Authors: Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick (Independent Researcher)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.32917
