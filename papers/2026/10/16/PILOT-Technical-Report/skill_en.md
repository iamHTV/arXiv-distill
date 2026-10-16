# Skill: pilot-proactive-insight-learner-experiments
Source: 2608.18637v2
Type: framework

## When to use this skill
- Optimizing recommendation systems with LLM agents.
- Want agents to proactively design A/B tests and personalize strategies by user segment.
- Need deterministic guardrails for agents.

## When NOT to use
- No recommendation system or real transaction data.
- Only need simple parameter optimization, no agent experiment design needed.

## Required input
- Recommendation system and real transaction data.
- Deterministic services to enforce safety, statistical, and permission boundaries.
- LLM with experiment design capability.

## Steps
1. Set up Experiment Manager agent to manage the full experiment lifecycle (design, run, analyze, conclude).
2. Set up Insight Learner agent to learn from previous experiments and apply to new ones.
3. Set deterministic guardrails: exposure PV, transaction count, ad PVR, GMV guardrails, etc. so agents don't exceed safety boundaries.
4. Run experiments continuously; agents personalize strategies by user segment (e.g. visit_frequency ≥ 5/week).
5. Accumulate reusable experimental methodology to apply to future tasks.

## Expected output
- Improve IPV up to +1.40%, Core IPV +1.60%, transaction count +0.96%, transaction amount +1.50%.
- Raise search efficiency from 53.3% to 93.3%.
- No human intervention throughout the experiment.

## Example application
Solopreneur running a product recommendation system: use PILOT to have agents proactively design A/B tests for each user segment (e.g. users visiting ≥ 5 times/week), set GMV guardrails not to drop more than 0.5%, and accumulate experimental methodology for future campaigns.

## Gotchas
- Comparison in paper is before/after, not randomized — results may have bias.
- Need deterministic services to enforce guardrails; without them, agents may exceed safety boundaries.
- Not evaluated on many domains beyond recommendation systems.
