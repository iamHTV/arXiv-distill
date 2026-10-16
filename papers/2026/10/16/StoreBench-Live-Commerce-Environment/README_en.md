# [2610.10942v1] StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents

## Problem
Most agentic benchmarks remain static: the world moves only when the agent acts, reward is a terminal verdict, pass bar is set arbitrarily. This does not reflect real commerce where customers order 24/7, suppliers reprice and fail, and market shocks arrive with partial or no warning.

## Contribution
- Introduce StoreBench: a live-commerce environment where an agent runs a mid-size online apparel store on a production-grade commerce backend, testing long-horizon planning and economic judgment under uncertainty.
- Agent acts through the same 29 merchant tools via MCP surface.
- 11 dense tasks × 3 seeds × 3 attempts, evaluating 7 frontier models.
- Composite score: Business 70%, Reliability 20%, Continuity 10%, calibrated against scripted policies.

## Method (core summary)
StoreBench simulates a mid-size apparel store with continuous customer orders, supplier repricing/failures, and market shocks. Agent receives task instruction and tool access, unaware of scoring mechanics or thresholds. Each trial is a "pass" if its composite score clears the task-seed threshold. Full-year task runs separately with Claude Code, context compaction, extended thinking, 365-window episode.

## Key Findings
- Best model (DeepSeek-V4-Pro) reaches 49% of task-seed cells vs heuristic's 97%.
- Human experts clear 97% of cells, ship 96% of orders on time, handle 93% of returns, reliability 0.944 (vs at most 0.85 for models).
- Every other model reaches at most 36% of cells.
- Trained policy: share of episodes ending at profit rises from 3% to 72%.
- Removing the clock raises GPT-5's score from 0% to 34.4%.

## Actionable Insights
- Agents cannot yet replace economic judgment: on live commerce, best model reaches 49% vs heuristic 97%. Apply: solopreneur using agents for online retail should use agents as assistants, not replacements for pricing and inventory decisions.
- Live-commerce benchmarks are valuable to evaluate agents before production deployment: StoreBench has 29 merchant tools, 11 dense tasks, usable as a test environment for store-running agents.

## Assumptions & Limitations
- Requires agent access to 29 merchant tools via MCP surface.
- Paper admits: full-year task uses different harness (Claude Code), not directly comparable to short-horizon suite.
- Limitation paper doesn't mention: not evaluated on multiple stores simultaneously, not tested on multi-agent collaboration.

## Metadata
- Year: 2026
- Authors: Daksh Raghuvanshi, Ved Vedere, Yifan Wang (AfterQuery)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.10942
