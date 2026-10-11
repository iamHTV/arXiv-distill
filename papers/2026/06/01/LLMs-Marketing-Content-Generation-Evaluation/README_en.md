# [2506.17863] LLMs for Customized Marketing Content Generation and Evaluation at Scale

## Problem
Prior work fails to generate effective offsite marketing content because: most current content is overly generic, template-based, and poorly aligned with landing pages. Manual approaches are costly, not scalable, and lead to limited audience engagement.

## Contribution
1. **MarketingFM**: Retrieval-augmented system integrating multiple data sources to generate keyword-specific ad copy with minimal human intervention
2. **AutoEval-Main**: Automated evaluation system combining rule-based metrics + LLM-as-a-Judge — 89.57% agreement with human reviewers
3. **AutoEval-Update**: LLM-human collaborative framework to dynamically refine evaluation prompts as criteria shift

## Method (core summary)
MarketingFM uses RAG (Retrieval-Augmented Generation) with search page products context to ground ad generation in real-time product data. Task chaining: generate → rewrite → evaluate. AutoEval-Main: rule-based checks + LLM-as-a-Judge scoring on relevance and generalization scales 0-5. AutoEval-Update: active sampling → human review → critic LLM generates alignment report → refine evaluation prompt → iterate until convergence.

## Key Findings
- Online A/B test (10,000 keywords): +9% CTR, +12% impressions, -0.38% CPC
- Mobile: +121 bps CTR lift (p=0.055), +8% clicks (p=3.89e-6)
- Desktop: +9% clicks (p=2.56e-3), +12% impressions (p=1.01e-5)
- AutoEval-Main: 89.57% agreement with human reviewers on 150,000 ad copies
- Rejection rate reduced from 15% (semantic retriever) to 2.79% (products context retriever)
- "Stanley Cup problem": semantic retriever confuses hockey games with trending water bottles → products context retriever solves it
- AutoEval-Update: uncertainty-based sampling best for reducing errors, diversity-based sampling best for coverage

## Actionable Insights
1. **RAG for keyword-specific ads**: Instead of generic templates, use RAG with real product data to create ad copy specific to each keyword. Example: user searches "wireless headphones gym" → RAG retrieves actual gym headphones from catalog → ad mentions specific features, price, reviews. Result: +9% CTR.

2. **LLM-as-a-Judge for ad quality**: Use LLM to evaluate ad copy before publishing, reducing human review cost. Example: 10,000 ads generated → AutoEval-Main filters → only ads passing threshold go to human review. 89.57% agreement ≈ human judgment.

3. **AutoEval-Update for criteria drift**: Evaluation criteria change over time → need iterative refinement. Example: when customer concern about product safety increases → AutoEval-Update automatically refines evaluation prompt to include stricter accuracy metrics, no rebuild needed.

## Assumptions & Limitations
**Conditions for the method to work:**
- Needs search infrastructure with product catalog for RAG to work
- Needs large-scale human annotations to establish AutoEval benchmark
- Domain-specific design — general LLMs lack understanding of ad network preferences

**Limitations the paper acknowledges:**
- LLM tends to be more conservative than humans — may reject acceptable content
- Semantic retriever limitations in retail domain — "Stanley Cup problem"
- Human oversight still essential for setting thresholds and validating refinements

**Limitations the paper does NOT mention:**
- Does not discuss RAG pipeline latency — real-time ad generation needs fast retrieval
- Does not address cost of running LLM-as-a-Judge at scale (20M keywords/day)
- Not tested on non-English markets
- Does not compare with simpler baselines (are rule-based templates good enough for most cases?)
- AutoEval-Update convergence time unclear — how many iterations needed?

## Metadata
- Year: 2025
- Authors: Haoran Liu (Texas A&M), Amir Tahmasbi, Ehtesham Sam Haque, Purak Jain (Amazon)
- Category: cs.CL, cs.AI
- PDF: https://arxiv.org/pdf/2506.17863
- Citation count: [EXTRACTION FAILED]
