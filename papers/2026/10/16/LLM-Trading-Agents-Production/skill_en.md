# Skill: llm-trading-agents-production-lessons
Source: 2609.05663v1
Type: framework

## When to use this skill
- Building or using autonomous trading agents with real capital.
- Want to understand risks and effectiveness of LLM trading agents in production.
- Need lessons on configuring trading agents (leverage, stop/target, horizon).

## When NOT to use
- No real capital to trade.
- Just want automated trading without caring about失控 risk.

## Required input
- Real trading capital (ETH or other assets on Base/chain).
- A configurable trading agent system (leverage, stop, target).
- Real market data.

## Steps
1. Set a trading horizon longer than 24h (beneficial +0.23% median return) instead of scalpbing short-term (<1h, −0.15%).
2. Write concrete numeric instructions for the agent (e.g. stop-loss 2%, take-profit 4%) instead of vague descriptions.
3. Limit leverage: agents use median 5.0× leverage and get liquidated more when volatility rises (0.7% to 4.3%).
4. Don't follow leaderboard status (rendered symbols): 46.5% of entries in rendered symbols vs 8.9% random baseline — 5.2× over-selection without benefit.
5. Set rigid stop/target brackets (fixed bracket) when entering positions, don't let agents decide when to close (49.3% of positions with upside close negative).

## Expected output
- Understand: LLM trading agents only 41% win rate vs retail 50%, 16.2% of vaults profitable.
- Know how to configure agents to reduce risk (long horizon, concrete numeric instructions, limit leverage).

## Example application
Solopreneur using an agent to trade ETH on Base: set orders with stop 2%/target 4% (fixed bracket), hold positions at least 24h, write concrete numeric instructions ("if ETH price drops 2% then sell immediately"), don't follow leaderboard codes. Hope to reduce liquidation and capture more upside.

## Gotchas
- 43.2% of positions reached ≥ +300 bps potential upside yet 49.3% closed negative — agents don't capture upside, need stop/target rigid.
- Agents lean structurally long (∼78% of entries) and position sizing doesn't follow volatility (median 5.0× leverage every sextile) — easily liquidated when market moves sharply.
- Only 15% of agents net-positive vs 53% of retail accounts — agents not yet better than retail traders.
