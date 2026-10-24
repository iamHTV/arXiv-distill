# Skill: Evaluate business agents via simulated marketplace environment (Business Arena)

Source: 2608.08621
Type: evaluation-method

## When to use this skill

- You need to evaluate AI agents for business operation, e-commerce, or any application involving decision-making under uncertainty with delayed consequences.
- You want to know where the agent is strong or weak in each aspect (capital, pricing, customer service, compliance) rather than just one aggregate score.
- You need to create a simulated environment where the agent must run a real business and measure the final financial outcome.

## When NOT to use this skill

- The agent only needs to perform short-horizon, verifiable tasks (e.g., code patching, web navigation) without long-term capital management or market adaptation.
- You don't have real or simulatable commerce data.
- You don't need to evaluate the financial cost of agent decisions.

## Required inputs

- Real or simulatable commerce data (product catalogs, orders, customer interactions).
- A simulated market environment that runs independently from the agent (buyers, suppliers, competitors updating automatically).
- 60+ tools spanning the business cycle (supplier search, pricing, inventory management, advertising, customer service, finance, compliance).
- LLM backbone capable of function calling and multi-step planning.
- Measurement tools: final net worth, skill-level metrics, action-level attribution.

## Steps to execute

1. Set up the simulated market environment: buyers, suppliers, and competitors operate independently from the agent; market conditions change over time.
2. Provide 60+ tools to the agent: supplier search, pricing, inventory management, advertising, customer service, finance, compliance.
3. Run an episode: agent declares initial shop focus, purchases initial inventory, prices and lists products, responds to buyers and suppliers, advances day by day.
4. Collect final financial outcome (final net worth) after each episode.
5. Compute skill-level metrics: capital utilization, inventory turnover, order margin, sell-through rate, customer service conversion, compliance violations.
6. Perform action-level attribution: trace each financial gain/loss back to the specific decision that produced it (sourcing, pricing, service, financing, recovery).
7. Run mechanism ablations: compare intended policy with variants that neglect or misuse each mechanism (portfolio, market events, pricing, tariffs, customer service).

## Expected output

- A business agent evaluation report with final net worth, skill-level profile, and action-level attribution.
- Recognition of where the agent is strong or weak in each business aspect.
- A basis for future training data and reinforcement learning.

## Example application

A Vietnamese solopreneur wants to evaluate an online sales support agent: create a simulated environment where the agent must source products from suppliers, set prices, respond to customer inquiries, and comply with tax regulations. Run 10 episodes, measure average final net worth. Skill-level analysis shows the agent is strong on pricing (52% average order margin) but weak on customer service (only 57% inquiry conversion). Action-level attribution shows a pricing decision below realized cost stack caused a $34.15 loss on one order.

## Gotchas

- 51% of runs lose money vs $80,000 starting capital — consistent capital preservation matters more than offsetting frequent losses with a few exceptional runs.
- 9.0× gap between best and worst model — running a business remains challenging for current LLM agents.
- A single final score can hide important strengths and weaknesses — skill-level diagnosis is needed.
- Arena is limited to cross-border B2B commerce, not evaluated on other business scenarios/industries.
- Does not evaluate whether the agent can update a live storefront, submit offers through third-party platforms, or manage conversations through a real inbox and GUI.
- No evaluation of arena running cost, no evaluation of stability when market conditions change more severely than simulated.