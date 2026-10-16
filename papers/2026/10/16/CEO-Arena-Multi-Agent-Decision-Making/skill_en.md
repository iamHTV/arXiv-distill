# Skill: ceo-arena-multi-agent-business-competition
Source: 2609.34821v1
Type: evaluation-method

## When to use this skill
- Evaluating business management agents (pricing, marketing, R&D) in long-horizon competitive environments.
- Want to know an agent's impact on rivals and the whole market, not just agent-specific profit.
- Can simulate a market with multiple competing companies.

## When NOT to use
- Evaluating a single agent without competitors.
- Cannot simulate identical market conditions for replacement comparison.

## Required input
- A simulated business environment (price, volume, marketing, R&D, inventory).
- Multiple CEO-agent LLMs that can be configured.
- A long simulation horizon (e.g. 500 days) to see long-term impact.

## Steps
1. Set up a simulated market with N companies, each managed by a CEO agent.
2. Run the simulation over a long horizon (e.g. 500 days), each agent making decisions on price, marketing, R&D.
3. Apply matched replacement evaluation: replace one agent with another under the same market conditions, measure changes in operating return and impact on rivals/market.
4. Compare win rate and operating return of each agent under the same conditions.
5. Analyze whether an agent has private gain but causes market loss.

## Expected output
- Win rate and operating return of each CEO agent under the same market conditions.
- Identify agents with private gain but causing market loss.

## Example application
Solopreneur using an agent to manage pricing for an online store: instead of only measuring the agent's profit, simulate the market with competitors and replace the pricing agent with another strategy under the same conditions, see the impact on whole-market revenue.

## Gotchas
- Many agents have private gain but cause market loss — don't just measure agent-specific profit.
- Matched replacement evaluation requires identical market conditions, hard to implement on real production.
- A 500-day horizon may not be enough to see full long-term impact.
