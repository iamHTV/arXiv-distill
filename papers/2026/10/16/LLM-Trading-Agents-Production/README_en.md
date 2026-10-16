# [2609.05663v1] What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets

## Problem
Autonomous language-model trading agents are operating in production with real capital, but there is no population-scale measurement record of how they actually perform, their risks, and their effectiveness.

## Contribution
- Present a continuous, population-scale measurement record of autonomous LLM trading agents operating under production conditions across two systems sharing one design lineage: DX Terminal Pro (3,505 user-funded vaults trading real ETH in Base memecoin markets for 21 days, February-March 2026) and DXAP live alpha fleet (500-599 user-created agents all-history, 91-117 concurrently active).
- ∼300K onchain actions, ∼$20M, ∼70B inference tokens.

## Method (core summary)
Continuous measurement of two LLM trading agent fleets in production: DX Terminal Pro (user-funded vaults trading real ETH) and DXAP (live alpha fleet, user-created agents). Track P&L, leverage, liquidation, win rate, and trading behavior across 69 days.

## Key Findings
- Fleet runs 41% roundtrip win rate vs retail 50%, at nearly identical median hold times (2.05h vs 2.18h).
- Only 15% of agents active over the week are net-positive vs 53% of retail accounts.
- Agents lean structurally long (∼78% of entries vs ∼60%) at roughly 4-5× effective leverage (median 0.096× vs 0.022× notional-to-equity, chosen-leverage median 5.0×).
- Median true return is 0.492×; 16.2% of vaults finished profitable; 92% of deposited ETH was withdrawn.
- 43.2% of positions reached ≥ +300 bps favorable excursion within 24h, yet 49.3% of those closed with negative trade return; only 13.3% kept half the excursion.
- Positions held 24h+ earn +0.23% median account return while sub-1h positions earn −0.15%.
- 46.5% of entries in rendered symbols (leaderboard) vs 8.9% random-availability baseline, 5.2× over-selection.
- Users who wrote concrete numeric instructions were profitable 4.2× as often as median.
- 87 UI-only owners who never used chat were highest-profit cohort (41% in profit).
- Sizing is volatility-blind: median leverage is 5.0× in every volatility sextile.
- Liquidation rate rises from 0.7% to 4.3% as volatility increases.

## Actionable Insights
- LLM trading agents in production are not yet truly effective: only 16.2% of vaults profitable, 41% win rate vs retail 50%. Apply: solopreneur using trading agents should expect lower effectiveness than retail and not treat agents as easy money.
- Holding positions longer than 24h is beneficial (+0.23% median return) while short-term (<1h) loses (−0.15%). Apply: if using trading agents, set a longer horizon and avoid scalpbing.
- Users writing concrete numeric instructions were profitable 4.2× as often as median. Apply: when configuring trading agents, write concrete numeric instructions (e.g. stop-loss 2%, take-profit 4%) rather than vague descriptions.
- Warning: 43.2% of positions reached ≥ +300 bps potential upside yet 49.3% closed negative — agents don't capture upside. Apply: need rigid stop/target brackets (fixed bracket), not letting agents decide when to close.

## Assumptions & Limitations
- Data from two specific systems (DX Terminal Pro, DXAP) on Base memecoin markets; may differ on other markets.
- Paper admits: All cross-era P&L is operator-reported figures.
- Limitation paper doesn't mention: not evaluated on asset types beyond memecoin ETH, not tested beyond 69 days.

## Metadata
- Year: 2026
- Authors: T.J. Barton, Chris Constantakis, Patti Hauseman, Annie Mous, Alaska Hoffman, Brian Bergeron, Hunter Goodreau (DX Research Group)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.05663
