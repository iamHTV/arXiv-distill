# Skill: storebench-live-commerce-evaluation
Source: 2610.10942v1
Type: framework

## When to use this skill
- Evaluating e-commerce agents in a live-commerce environment.
- Need to evaluate agents under uncertainty: customers ordering around clock, suppliers repricing and failing, market shocks.
- Want to evaluate long-horizon stability and economic judgment of agent.

## When NOT to use this skill
- Evaluating agents on bounded tasks only.
- No live-commerce environment available.
- Don't need to evaluate long-horizon stability.

## Input needed
- Live-commerce environment with mid-size online apparel store.
- 29 merchant tools over Model Context Protocol.
- Customers ordering around the clock, suppliers repricing and failing, market shocks.
- Windowed operation budget.
- 11 scenarios of 30-45 days and a full simulated year.

## Steps to execute
1. Build live-commerce environment with mid-size online apparel store on production-grade commerce backend.
2. Set up 29 merchant tools over Model Context Protocol.
3. Set up customers ordering around the clock, suppliers repricing and failing, market shocks.
4. Set up windowed operation budget so simulated time is a function of actions taken.
5. Evaluate agent on 11 scenarios of 30-45 days and a full simulated year.
6. Use pass thresholds calibrated against scripted anchor policies.
7. Use reward hardened against reward hacks.
8. Every episode replays identically given a sequence of actions.

## Expected output
- Agent evaluated on live-commerce environment.
- Composite score of agent vs human experts and scripted smart-triage policy.
- Best model gets 49% vs heuristic 97%; humans get 0.708 vs models 0.700.

## Application example
- Build e-commerce agent: use live-commerce environment to evaluate agent under uncertainty, with customers ordering around clock, suppliers repricing and failing, market shocks. Evaluate agent based on composite score vs human experts and scripted smart-triage policy.

## Gotchas
- Evaluated on a single apparel business with scripted competitors and parametric demand.
- Environment engine withheld to keep benchmark uncontaminated.
- Post-training uses one base model and one run.
