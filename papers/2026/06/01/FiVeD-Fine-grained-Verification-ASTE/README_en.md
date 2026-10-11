# [2605.31446v1] FiVeD: Fine-grained Verification via Diagnostic Reasoning Supervision for ASTE

## Problem
Aspect Sentiment Triplet Extraction (ASTE) identifies aspect terms, opinion terms, and sentiment polarities as structured triplets. Prior work mainly focuses on end-to-end extraction, but post hoc verification of extracted triplets remains underexplored. Predicted triplets may be locally plausible but globally invalid. Candidate invalidity is multi-faceted and usability is inherently graded.

## Contribution
1. **FiVeD framework**: Fine-grained Verification with Diagnostic reasoning supervision. Plug-and-play verifier assesses reliability of candidate triplets from base extractors.
2. **Diagnostic reasoning supervision**: Hierarchical error categories, plausible incorrect triplets under semantic/syntactic constraints, LLM-generated quality scores and diagnostic rationales.
3. **Results**: +3.53 F1 points across multiple ASTE baselines. Adjustable precision-recall tradeoffs.

## Method (core summary)
2 stages: (1) Construction: counterfactual candidate mining — synthesize plausible invalid triplets under semantic/syntactic constraints. Hierarchical error types per candidate. LLM with task-specific rubrics generates quality scores + rationales. (2) Training: multi-task learning — validity classification + quality score estimation (main tasks), error type classification + rationale generation (auxiliary tasks). Auto-learned task weights. Inference: quality scores filter/rerank extractor outputs.

## Key Findings
- +3.53 F1 points across multiple ASTE baselines
- Plug-and-play: model-agnostic, works with diverse ASTE architectures
- Adjustable precision-recall control through quality score thresholding
- Consistent improvements across 4 benchmark datasets
- Fine-grained verification > binary validity classification

## Actionable Insights
1. **Post-hoc verification for extraction systems**: When building AI extraction pipeline (sentiment, entities, relations), add verification stage. Don't just extract — verify extracted outputs. Example: when building review analysis system, extract sentiment triplets, then verify each triplet: "Is aspect 'battery life' + opinion 'great' + positive sentiment actually supported by review text?"

2. **Hierarchical error categories**: Define error types specific to your task. Don't just binary valid/invalid. Example: for sentiment extraction — error types: boundary error, aspect error, opinion error, polarity error, compound error. Fine-grained error diagnosis helps fix specific issues.

3. **LLM-generated rubrics for verification**: Use off-the-shelf LLM with task-specific rubrics to generate quality scores. No need to train verifier from scratch. Example: when verifying AI-generated reports, use LLM with rubrics: "Does claim X have source support? Is data Y correctly cited?"

## Assumptions & Limitations
**Conditions for method to work:**
- Gold ASTE annotations available for supervision construction
- Off-the-shelf LLM available for rubric-based scoring
- Base extractor produces candidate triplets

**Limitations the paper acknowledges:**
- Focused on generative extractors — other architectures less explored
- LLM dependency for quality scores and rationales

**Limitations the paper does NOT mention:**
- LLM as scorer has bias — circular evaluation risk
- Counterfactual mining quality affects verifier training
- Error categories manually defined — may not cover all cases
- 4 benchmarks specific — domain transfer unclear
- Multi-task learning weight auto-tuning stability unclear

## Metadata
- Year: 2026
- Authors: Wenna Lai, Haoran Xie, Guandong Xu, Qing Li, S. Joe Qin
- Category: cs.CL, cs.AI
- PDF: https://arxiv.org/pdf/2605.31446v1
- Citation count: [EXTRACTION FAILED]
