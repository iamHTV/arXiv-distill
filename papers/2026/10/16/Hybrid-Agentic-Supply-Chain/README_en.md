# [2609.13561v1] A Hybrid Agentic AI Framework for Intelligent Supply Chain Analytics

## Problem
Efficient utilization of supply chain analytics for decision making remains a significant challenge for planners, as critical tasks such as database querying, KPI analysis, demand forecasting, and performance diagnosis require heterogeneous expertise spanning data engineering, operations research, and domain knowledge.

## Contribution
- Introduce an agentic system for supply chain analytics.
- Multi-agent design achieves 90% accuracy, competitive with single agent baseline.
- Reasoning models achieve scores above 90%, non-reasoning models achieve around 65%.

## Method (core summary)
The hybrid agentic system for supply chain analytics includes a coordinator and specialist agents. Each specialist is responsible for a domain (database querying, KPI analysis, demand forecasting, performance diagnosis). The coordinator coordinates between specialists to make the final decision.

## Key Findings
- Multi-agent design achieves 90% accuracy, competitive with single agent baseline.
- Reasoning models achieve scores above 90%, non-reasoning models achieve around 65%.
- Mean Score: 0.932 ± 0.012 (highest), 0.904 ± 0.011, 0.655 ± 0.027, 0.661 ± 0.018.
- Relative Input Token Usage: 5.5×, 1.0×, 8.4×, 2.5× (lowest = 1×).

## Actionable Insights
- Use reasoning models for complex supply chain tasks: achieve >90% accuracy vs around 65% for non-reasoning. Apply: solopreneur building a supply chain analytics system should use models with reasoning capability rather than simple models.
- Combine multi-agent (coordinator + specialists) to handle tasks requiring diverse expertise. Apply: when building an analytics system, split into specialist agents (each responsible for a domain: demand forecasting, KPI analysis, etc.) and a coordinator to aggregate.

## Assumptions & Limitations
- Requires supply chain data and clear analysis tasks; doesn't apply without real business data.
- Paper admits: architectural effects differ by model type.
- Limitation paper doesn't mention: not evaluated on many domains beyond supply chain, not tested on real deployment cost.

## Metadata
- Year: 2026
- Authors: Xian Yeow Lee, Teppei Inoue, Haiyan Wang, Chetan Gupta (Hitachi America, Industrial AI Lab)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.13561
