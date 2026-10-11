# [2601.20316] Less is More: Benchmarking LLM Based Recommendation Agents

## Problem
LLMs are increasingly deployed for personalized product recommendations. Practitioners commonly assume that longer user purchase histories lead to better predictions. But this assumption has not been tested systematically. Is the "more context is better" paradigm correct?

## Contribution
1. **Challenge "more context is better"**: Systematic benchmark of 4 LLMs across context lengths 5-50 items. Finding: NO significant quality improvement with longer context.
2. **88% cost savings**: Using 5 items instead of 50 → 88% token cost reduction, no quality loss.
3. **Universal pattern**: Finding holds across 4 different providers — fundamental limitation.

## Method (core summary)
Benchmark: 4 LLMs (GPT-4o-mini, DeepSeek-V3, Qwen2.5-72B, Gemini 2.5 Flash). Context lengths: 5, 10, 15, 25, 50 items. Dataset: REGEN. 50 users, within-subject design. Metrics: quality scores, token usage, latency. Cost analysis.

## Key Findings
- Quality scores flat: 0.17-0.23 across ALL conditions, ALL models
- Average quality change 5→50 items: -0.01 (essentially zero)
- All confidence intervals overlap — no statistically significant differences
- Token costs: 8.2× increase from 5 to 50 items
- 88% potential cost savings using 5 items instead of 50
- Latency varies by provider — model-specific patterns

## Actionable Insights
1. **Use minimal context (5-10 items)**: Don't feed 50-item purchase histories. 5-10 items = same quality, 88% cheaper. Example: when building product recommendation system, only take 5-10 recent purchases instead of entire history.

2. **88% cost savings**: Token costs 8.2× higher with 50 items vs 5 items. Quality same. Example: e-commerce platform processing 1M recommendations/day → save ~88% API costs by limiting context.

3. **Model-specific latency**: Different providers have different latency patterns. Choose model based on your latency requirements. Example: real-time recommendations → choose lowest latency model. Batch processing → choose cheapest.

## Assumptions & Limitations
**Conditions for benchmark to work:**
- REGEN dataset specific
- 50 users, within-subject design
- 4 specific LLMs tested

**Limitations the paper acknowledges:**
- Limited to REGEN dataset
- 50 users sample size

**Limitations the paper does NOT mention:**
- Quality metric specific (0.17-0.23 range) — may not capture all recommendation aspects
- Different product categories may have different optimal context lengths
- User behavior patterns may vary by domain
- Long-tail items may benefit from longer context
- Cold-start users may need different treatment

## Metadata
- Year: 2026
- Authors: Kargi Chauhan, Mahalakshmi Venkateswarlu
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2601.20316
- Citation count: [EXTRACTION FAILED]
