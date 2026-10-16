# Skill: adcoevo-co-evolving-multi-agent-advertising
Source: 2610.19454v1
Type: framework

## When to use this skill
- Building an advertising delivery system for a business.
- Want the advertising system to co-evolve with market and user behavior.
- Need to reduce cost per acquisition (CPA) and increase advertiser value (ADV).

## When NOT to use
- No advertising delivery system.
- Only need static rules for advertising, no self-adapting agent needed.

## Required input
- Advertising delivery data (users, ads, results, costs).
- LLM agents that can co-evolve together.
- Reinforcement learning mechanism to optimize parameters and strategies.

## Steps
1. Build a multi-agent system for advertising delivery, with agents responsible for different roles (planner, optimizer, inspector, etc.).
2. Use reinforcement learning to optimize parameters and advertising strategies over time.
3. Add an Inspector agent to monitor and adjust decisions of other agents.
4. Use small model (low API cost) to reduce operational cost.
5. Monitor ADV (advertiser value) and CPA (cost per acquisition) to adjust the system.

## Expected output
- ADV +14.02%, CPA -7.07% (vs Rule, Sparse).
- ADV +3.96%, CPA -1.24% (vs multi-agent fixed parameters).
- API cost 65.59% lower than Gemini-3.1-Flash-Lite.

## Example application
Solopreneur running an e-commerce product advertising system: build a co-evolving multi-agent system, with agent planning advertising, agent optimizing price, agent Inspector monitoring results. Use small model to reduce API cost. System self-adapts to market and user behavior, increasing advertising value and reducing cost per purchase.

## Gotchas
- Need co-evolving multi-agent system, not static rules.
- Need Inspector agent to monitor and adjust, not just agents working independently.
- Need real advertising data to train and optimize the system.
