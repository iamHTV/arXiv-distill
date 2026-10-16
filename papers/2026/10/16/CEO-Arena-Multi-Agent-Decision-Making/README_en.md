# [2609.34821v1] CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets

## Problem
Long-horizon competition tests agents' ability to coordinate business decisions under uncertainty and adapt to changing rival strategies. Existing benchmarks do not evaluate an agent's impact on rivals and the market simultaneously.

## Contribution
- Introduce CEO Arena: a benchmark using matched replacement evaluation to assess operating returns alongside an agent's effects on rivals and the market.
- Each CEO agent is compared with a reference policy under the same market conditions.
- Simulates 500 days, 9 companies, 8 CEO-agent LLM competing on pricing, marketing, R&D.

## Method (core summary)
CEO Arena simulates a market with 9 companies, each managed by a CEO agent. Each CEO agent makes decisions on price, volume, marketing, R&D over 500 days. Matched replacement evaluation: replace one agent with another under the same market conditions, measure changes in operating return and impact on rivals/market. Includes tender (enterprise bidding), inventory, production, marketing, R&D.

## Key Findings
- Many agents lose money (negative operating return) while still having private gain that can come with market loss.
- Win rate over 24 runs: GPT-6 Astra 66% ($1333.8k), GPT-5.6 Sol 64% ($1739.2k), Qwen 3.8 Max 61% ($1268.2k), DeepSeek V4 Pro 62% ($2818.0k), DeepSeek V4 Flash 59% ($1523.2k), Gemini 3.8 Flash 56% ($1144.5k), Claude Sonnet 5 56% ($2459.6k), Doubao Seed 1.8 54% ($2143.5k), Rule 55% ($650.5k).
- Median innovation delays consume 9–30% of the 500-day horizon.
- Initial unit margins are 35%, 36%, and 37.04% for products A/B/C before operating expenses.

## Actionable Insights
- Multi-agent business does not necessarily win: many agents lose while having private gain that can come with market loss. Apply: solopreneur using agents for business should measure whole-market impact, not just agent-specific profit.
- Evaluating agents in a realistic competitive environment (matched replacement) matters more than single-agent benchmarks. Apply: before deploying an agent for pricing/marketing, try replacing the current agent under the same market conditions to see real impact.

## Assumptions & Limitations
- Requires a simulated market with 9 companies over 500 days; results may differ on real markets with different company counts.
- Paper admits: matched replacement evaluation requires identical market conditions, hard to implement on real production.
- Limitation paper doesn't mention: not evaluated on horizons longer than 500 days, not tested on real-time rival strategy adjustments.

## Metadata
- Year: 2026
- Authors: An Yan, Yu Huo, Zhiwei Shang, Yiran Peng, Chenglin Wu (DeepWisdom, Fudan, CUHK, CUHK-Shenzhen, HKUST-GZ)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.34821
