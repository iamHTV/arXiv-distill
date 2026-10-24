# [2608.08621] Business Arena: Benchmarking LLM Agents in a Realistic Marketplace

## Core Value (1 sentence)

Business Arena is a controlled environment where an AI agent runs a cross-border shop, buying from suppliers and selling to buyers over a long horizon, evaluating 15 frontier LLM models and finding a 9.0× gap in mean final net worth — showing that running a business remains challenging for current LLM agents.

## Problem

Prior work has not solved evaluating business-related capabilities in existing agent benchmarks. Current agent benchmarks focus on short-horizon, verifiable tasks (code patching, web navigation, policy compliance), while real business operation requires decision-making under uncertainty, committing capital under uncertainty, adapting to delayed outcomes in a changing market, and satisfying regulatory obligations before trading legally.

## Contribution

(i) Business Arena: a controlled environment where an AI agent runs a cross-border shop, buying from suppliers and selling to buyers over a long horizon, grounded in real Alibaba.com sourcing data and market conditions calibrated from authoritative sources.
(ii) Business intelligence organized into four capabilities: decision-making under uncertainty, strategic planning under constraints, insight-to-action alignment, and cooperation & competition.
(iii) Skill-level metrics reveal strengths and weaknesses hidden behind aggregate outcomes; action-level attribution toolkit traces realized gains and losses back to the actions that produced them.
(iv) Mechanism ablations establish that strong arena results reflect genuine business intelligence rather than neglect or simulator-specific shortcuts.
(v) Evaluation of 15 frontier models: mean final net worth ranges from $20,856 to $188,488 (9.0× gap), 51% of runs lose money relative to $80,000 starting capital, only 4 models preserve starting capital in every trial, strongest expert-designed strategy earns $436,195 (more than 2× best model mean).

## Method

Business Arena places one agent-operated shop in a marketplace of suppliers, buyers, and competing sellers. The agent is responsible for operating the business end to end and adapting it over time. An episode begins with a pre-opening setup phase: the agent declares an initial shop focus (may revise later), inspects available opportunities, and decides whether to acquire an initial inventory portfolio or retain capital. Inventory selected during setup is available on day 0. After setup, the agent clears market requirements and configures listings.

During each simulated day, the agent may inspect the market, adjust offers, source or replenish inventory, allocate advertising spend, manage liquidity, and respond to buyers and suppliers before advancing the day. The arena then advances the rest of the market autonomously: buyers make purchasing decisions, competitors update operations, shipments progress, financial costs are deducted, and new events or market signals may emerge. The day's outcomes update the persistent world state. After the final day, remaining inventory contributes to final net worth at a discounted salvage value.

Four guiding principles: (i) incomplete and noisy evidence — the agent cannot directly observe latent market conditions but can gather evidence from public signals, competitors, counterparties, and its own operating history; (ii) delayed economic consequences — fixed daily overhead makes leaving capital idle costly, inventory holding fees and salvage discounts penalize reckless deployment; (iii) a changing market — the marketplace continues to evolve whether or not the agent acts; (iv) persistent operational obligations — agents must satisfy regulatory and operational obligations before trading legally.

Four business capabilities evaluated: (1) Decision-Making Under Uncertainty — forming a view of the market, gathering and cross-checking signals, testing expectations, updating beliefs; (2) Strategic Planning Under Constraints — turning market view into an operating plan: what shop to build, which opportunities to pursue, how much capital to deploy, how broadly to diversify; (3) Insight-to-Action Alignment — translating plan into concrete choices about suppliers, order quantities, prices, market entry, and timing; (4) Cooperation & Competition — working with buyers, suppliers, and competing sellers without losing sight of its own objective.

## KNOWLEDGE — Data & Concepts

- 15 frontier models evaluated (proprietary: GPT 5.6 Sol, GPT-5.5, Claude Fable 5, Opus 4.6 and 4.8, Gemini 3.1 Pro and 3.5 Flash, Qwen 3.7 Max; open-weight: GLM 5.2, Kimi K2.6 and K3, DeepSeek V4 Pro, MiniMax M2.5 and M3, Qwen-3.8-Max-Preview).
- Mean final net worth: $188,488 (Gemini 3.1 Pro) to $20,856 (MiniMax M2.5), 9.0× gap.
- 51% of all runs lose money vs $80,000 starting capital.
- Only 4 models preserve starting capital in every trial.
- Strongest expert-designed strategy: $436,195, more than 2× best model mean.
- ICC = 0.944 (reliable 10-run means), ρ = 0.898 (ranking preserved in disjoint 5-run subsets), 98.7% same leading group.
- Capital utilization: Gemini 3.1 Pro 199%, GPT-5.6 Sol 167%, Fable 5 150%; Qwen 3.7 Max only 22.3% (underinvested).
- Order margin: Gemini 3.1 Pro 52.0% (Premium House); GPT-5.6 Sol and Opus 4.6 >93% sell-through (Volume Wholesalers); MiniMax M2.5 12.1% margin, <40% sell-through (Stranded Shop).
- Customer service conversion: Opus 4.8 84%, Fable 5 81%, Qwen 3.8 74%, Gemini 3.1 Pro 57%.
- Compliance: Fable 5 and GPT-5.5 no penalized violations; MiniMax M2.5 averages 22.7 violations and $51,750 fines; DeepSeek V4 Pro 17.4 violations and $39,650.
- Mechanism ablations (mean change in final net worth vs baseline): Portfolio (demand-guided) +$63.6k vs blind bulk buying -$14.6k; Market events (evidence checked) +$6.6k vs ignore events -$17.3k; Pricing (full-cost) +$50.3k vs price near cost -$58.1k; Tariffs (tariff-aware routes) +$25.9k vs tariff-blind US focus -$3.7k; Customer service (evidence-based replies) +$5.6k vs generic replies 0.
- More than 60 tools spanning the business cycle, supporting multi-step reasoning and individual actions, typed MCP calls, back-end APIs and persistent workspace.

## INSIGHT — Mechanism & Why

[9.0× gap between best and worst model] shows running a business remains challenging for current LLM agents — the difference is not just reasoning depth but the ability to combine capital deployment, pricing, customer service, and operational obligations. This means business benchmarks can differentiate models where short-horizon benchmarks cannot.

[51% of runs lose money] shows consistent capital preservation matters more than offsetting frequent losses with a few exceptional runs. This means a commercially useful agent must preserve capital consistently rather than achieve high profitability at some runs.

[Strongest expert strategy earns >2× best model mean] shows substantial headroom remains — current LLM agents don't yet exploit all available market opportunities. This means there's large room for improvement through better training data and RL.

[Skill-level analysis reveals recognizable operating styles]: from margin-focused premium sellers to high-turnover wholesalers and customer-service specialists. This means a single final score can hide important strengths and weaknesses — skill-level diagnosis is needed to understand where an agent is strong or weak.

[Action-level attribution] traces realized gains and losses back to the actions that produced them. This means instead of just observing that one model earns more, we can identify the behavioral difference behind the gap and measure its economic importance — providing a natural basis for RL credit assignment at the level of individual business actions.

## IDEA — Actionable Applications

Apply [Business Arena] to evaluating business agents for Vietnamese solopreneurs: instead of just testing whether an agent can answer questions, create a simulated environment where the agent must run a real business (source inventory, set prices, serve customers, comply with regulations) and measure the final financial outcome.

Apply [skill-level metrics] to diagnosing your own agent: instead of only tracking one aggregate score, measure capital deployment, sales performance, compliance, and customer service separately to know where your agent is strong or weak.

Apply [action-level attribution] to improving your agent: trace each decision back to its financial result to know which decisions to reinforce and which to correct — creating a basis for future training data and reinforcement learning.

## WISDOM — General Principle

Principle: Evaluating business agents through final financial outcome combined with skill-level analysis and action-level attribution is more effective than using a single aggregate score, because similar outcomes can arise from different operating choices and the value of those choices depends on available market opportunities.

When to use: When evaluating AI agents for business operation, e-commerce, or any application involving decision-making under uncertainty with delayed consequences.

When NOT to use: When the agent only needs to perform short-horizon, verifiable tasks (e.g., code patching, web navigation) without long-term capital management or market adaptation.

Example outside original domain: Building a benchmark for personal finance agents — the agent must manage budget, investing, saving, and debt repayment over time, with outcomes measured by final net worth and skill-level analysis for each financial decision.

## Assumptions & Limitations

- Conditions for success: Real or simulatable commerce data available; agent can use 60+ tools spanning the business cycle; simulated environment can run independently from the agent.
- Paper's acknowledged limitations: Arena focuses on end-to-end business decision-making and therefore abstracts external operating systems behind structured tools. It evaluates what an agent chooses to do, but not whether it can reliably update a live storefront, submit offers through third-party platforms, or manage customer conversations through a real inbox and GUI. The current arena is also limited to cross-border B2B commerce, while business spans more diverse scenarios and industries.
- Limitations paper does NOT mention: No evaluation on smaller models (under 7B parameters); no evaluation of arena running cost (compute cost, time per episode); no evaluation of stability when market conditions change more severely than simulated.

## Metadata

- Year: 2026
- Authors: Yijun Pan, Yukun Lian, Kunyu Shi, Junbo Li, Hongwei Xue, Sicong Xie, Guannan Zhang, Xiaoying Xing
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2608.08621
- Citation count: no information available