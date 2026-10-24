# Skill: Evaluate autonomous business agents via simulated marketplace benchmark (E-Commerce Bench)

Source: 2608.30730v1
Type: evaluation-method

## When to use this skill

- You need to evaluate AI agents for commerce/retail operation or any application involving sequential decision-making over long horizons with financial consequences.
- You want to know where the agent is strong or weak in each dimension (profit, negotiation, fraud avoidance, cash flow, efficiency, execution, learning) rather than just one aggregate score.
- You need a deterministic evaluation environment given the same action sequence.

## When NOT to use this skill

- The agent only needs to perform short-horizon verifiable tasks without long-term capital management or adaptation to dynamic events.
- You don't have real or synthesizable commerce data.
- You don't need to evaluate the financial cost of agent decisions.

## Required inputs

- Real or synthesizable commerce data (product catalogs, suppliers, purchase history).
- A simulated market environment that runs independently from the agent (suppliers, customers, competitors).
- 18 tools covering merchant back office across 7 groups, each with simulated minute cost.
- LLM backbone capable of function calling and multi-step planning.
- 128K token context window with group-wise eviction, persistent memory store (max 20 entries).

## Steps to execute

1. Set up simulated commerce environment: 6,886 products in 60 categories, 576 suppliers (424 honest, 152 fraudulent), 12 store types, max 4 concurrent stores.
2. Provide 18 tools to the agent (open store, supplier search, negotiate price, place order, set price, ship orders, customer service, finance).
3. Run 365-day episodes: agent declares shop focus, purchases inventory, sets prices, responds to customers and suppliers, advances day by day.
4. Collect final assets (bank account + platform wallet + unsettled escrow), reported as asset multiplier over ¥100,000 opening stake.
5. Compute metrics across 7 dimensions: negotiation quality (CSE+), fraud avoidance (BadSpend%), cash flow/solvency (peak drawdown), operational efficiency (profit per tool call), operations execution (controllable return rate), learning over horizon (AnchorRatio).
6. Detect bankruptcy: 10 consecutive days with negative bank balance.
7. Perform multi-dimensional analysis: compare agent across each dimension, not just aggregate score.

## Expected output

- A business agent evaluation report with final assets, multi-dimensional profile, and action-level attribution.
- Recognition of where the agent is strong or weak in each business dimension.
- A basis for future training data and reinforcement learning.

## Example application

A Vietnamese solopreneur wants to evaluate an online sales agent: create a simulated environment where the agent must run an online store for a year (source inventory, negotiate prices, set prices, ship orders, handle returns, manage cash flow). Run 5 episodes, measure average final assets. Multi-dimensional analysis shows the agent is strong on profit (14.3× capital) but weak on fraud avoidance (ranks 16/18). Learning over horizon shows the agent doesn't bargain prices down on repeat orders from the same supplier.

## Gotchas

- 1,264× factor between best and worst model — no model dominates all dimensions.
- 10/90 episodes end insolvent — cash flow management is as important as profit.
- A single aggregate score can hide important weaknesses — multi-dimensional diagnosis is needed.
- No explicit Limitations section in the paper (ends at Conclusion then References).
- No evaluation on smaller models, no benchmark running cost evaluation, no evaluation on languages other than Chinese.