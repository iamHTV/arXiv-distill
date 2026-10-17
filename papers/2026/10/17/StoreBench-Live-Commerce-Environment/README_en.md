# [2610.10942v1] StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents

## Problem
- Current agent benchmarks evaluate predefined goals in controlled environments that reset between runs. They rarely measure what ongoing work requires: sustained reliability, adaptation to change, and the ability to operate with limited human supervision.

## Contribution
- StoreBench — a live-commerce environment where an agent runs a mid-size online apparel store on a production-grade commerce backend, testing long-horizon planning and economic judgment under uncertainty.
- Customers order around the clock, suppliers reprice and fail, and market shocks arrive with partial or no warning.
- The agent acts through the same 29 merchant tools a human operator would use, under a windowed operation budget that makes simulated time a function of actions taken, so model latency cannot influence simulated time.
- Pass thresholds calibrated against scripted anchor policies, reward hardened against reward hacks, every episode replays identically given a sequence of actions.

## Method (core summary)
- Agent placed in charge of Ostrelle, a fictional mid-size online apparel store, for a contiguous shift of 30-365 simulated days.
- Store runs on Medusa v2, a production-grade open-source commerce backend.
- Agent interacts through 29 tools over Model Context Protocol, spanning catalog, pricing, inventory, fulfillment, returns, sourcing, and reporting.
- Environment combines 18 months of operating history, 40-vendor supplier market, 29 merchant tools, hidden demand, and scripted shocks to suppliers, costs, and competitors.
- Evaluate 7 frontier LLMs on 11 scenarios of 30-45 days and a full simulated year, over three world seeds at matched reasoning effort.
- Pass thresholds calibrated against scripted anchor policies, reward hardened against reward hacks, every episode replays identically.

## Key Findings
- 3 authors from AfterQuery, arXiv category: cs.AI.
- 7 frontier LLMs evaluated: DeepSeek-V4-Pro, Claude Opus 4.8, Claude Fable 5, Qwen3.8-Max, Gemini 3.8 Flash, GPT-5.6 Sol, Muse Spark 1.2.
- Best model (DeepSeek-V4-Pro) passes 49% vs heuristic's 97%.
- Human experts outscore every model (mean composite 0.708 vs 0.700).
- GRPO post-training: Qwen3.5-27B trained on 5 tasks raises mean composite from 0.136 to 0.373 (+0.237 per cell).
- Improves 31 of 33 cells.

## Actionable Insights
1. Agent cannot replace economic judgment: best model gets 49% vs heuristic 97%; use agent as assistant, not replacement for pricing/inventory decisions. Application: when building e-commerce agent, use agent as assistant for pricing and inventory decisions, not full replacement for human judgment.
2. Use live-commerce environment to evaluate agent under uncertainty. Application: when building agent for online retail, use simulated environment with customers ordering around clock, suppliers repricing and failing, and market shocks to evaluate long-horizon stability.

## Assumptions & Limitations
- Evaluates one enterprise system (single apparel business) with scripted competitors and parametric demand.
- Environment engine withheld to keep benchmark uncontaminated.
- Post-training uses one base model and one run.

## Metadata
- Year: 2026, authors: Daksh Raghuvanshi, Ved Vedere, Yifan Wang (AfterQuery), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2610.10942v1
