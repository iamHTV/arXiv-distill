# [2608.18637v2] PILOT Technical Report

## Problem
Existing agentic approaches for recommendation system optimization remain fundamentally reactive — they adjust parameters in response to observed metric changes but lack the ability to proactively design controlled experiments, personalize strategies at the user-segment level, or accumulate reusable experimental methodology across tasks.

## Contribution
- Introduce PILOT (Proactive Insight Learner for Online Tree-Experiments): an LLM-agent framework that organizes three roles within a constrained control loop where deterministic services enforce all safety, statistical, and permission boundaries.
- PILOT achieves up to +1.40% IPV, +1.60% Core IPV, +0.96% transaction count, +1.50% transaction amount.
- Improving over ROAM's best results (+1.00% IPV, +0.90% Core IPV, +0.60% transaction count, +1.13% transaction amount).
- Raising search efficiency from 53.3% to 93.3% (+40pp), with no human intervention throughout the experiment.

## Method (core summary)
PILOT organizes three agent roles within a constrained control loop where deterministic services enforce all safety, statistical, and permission boundaries: Experiment Manager (drives the full experiment lifecycle), Insight Learner, and v.v. PILOT proactively designs controlled experiments, personalizes strategies at the user-segment level, and accumulates reusable experimental methodology.

## Key Findings
- PILOT achieves up to +1.40% IPV, +1.60% Core IPV, +0.96% transaction count, +1.50% transaction amount.
- Improves over ROAM's best results (+1.00% IPV, +0.90% Core IPV, +0.60% transaction count, +1.13% transaction amount).
- Raises search efficiency from 53.3% to 93.3% (+40pp).
- No human intervention throughout the experiment.
- Best-performing bucket reaches +1.40% IPV, +1.60% Core IPV, +0.96% transaction count, +1.50% transaction amount.

## Actionable Insights
- Use agents to proactively design and run A/B tests instead of just reacting to metric changes. Apply: solopreneur running recommendation systems should use agents to proactively design experiments, personalize by user segment, and accumulate experimental methodology.
- Set deterministic guardrails for agents: exposure PV, transaction count, ad PVR, GMV guardrails, etc. Apply: when using agents for optimization, set hard safety boundaries so agents don't harm business metrics.

## Assumptions & Limitations
- Requires a recommendation system and real transaction data; doesn't apply without real business data.
- Paper admits: comparison in §6.2 is before/after, not randomized.
- Limitation paper doesn't mention: not evaluated on many domains beyond recommendation, not tested on real agent deployment cost.

## Metadata
- Year: 2026
- Authors: PILOT Team
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2608.18637
