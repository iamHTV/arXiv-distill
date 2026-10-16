# [2609.22951v1] AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows

## Problem
Enterprise agentic systems route every trajectory step to a frontier model, wasting 60–80% of inference budget on subtasks smaller models handle equally well. Existing routing solutions optimize single-turn query assignment but ignore that subtask complexity varies within a single trajectory.

## Contribution
- Introduce AgentRouter: lightweight 12M-parameter classifier, <5ms overhead per step on A100 GPU, maps each trajectory step to one of four model tiers using five routing-time features.
- Trained on 50,000 annotated agent trajectory steps across planning, coding, research, and data analysis.

## Method (core summary)
Formulates step-level model routing as a sequential assignment problem over agent trajectories. Each step is evaluated with 5 features extractable at routing time; a 12M-parameter classifier selects the appropriate model tier (tier 1 frontier to tier 4 minimal). Includes dependency-aware routing and budget-aware mode; fallback activates on fewer than 4% of trajectories.

## Key Findings
- AgentRouter achieves 72% cost reduction vs frontier-only baseline, retains 97.3% quality (<3% end-to-end task completion degradation).
- Per-step routing accuracy: 91% minimal-complexity, 85% efficient-tier, 76–82% mid-range and frontier tiers.
- 55–70% of agent trajectory steps need no frontier model; only 14.2% steps truly need frontier but consume 48.3% of remaining cost.
- Outperforms FrugalGPT (44%), RouteLLM (31%), DAAO (36%) with 72% cost reduction at 97.3% quality.
- Cost reduction by domain: document analysis 76.4%, data analysis 74.1%, research synthesis 69.2%, code generation 63.8%.

## Actionable Insights
- Don't route every step to the largest model: split agentic workflow into steps, use frontier model only for steps needing deep reasoning, smaller model for formatting/presentation. Apply: solopreneur running AI agent pipeline can cut ~70% inference cost.
- Use a lightweight classifier (12M parameters, <5ms/step) to route each step instead of hardcoded rules. Apply: when building AI content pipeline, add a small routing layer before each agent to pick the right model tier.

## Assumptions & Limitations
- Requires annotated trajectory data to train the classifier; doesn't work well without labeled trajectory data.
- Paper admits: testing on unseen AutoGen framework shows 6–9% accuracy degradation; cross-framework generalization is open.
- Limitation paper doesn't mention: not evaluated on sub-7B models, not tested on very long workflows.

## Metadata
- Year: 2026
- Authors: Rudrendu Kumar Paul, Sourav Nandy
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.22951
