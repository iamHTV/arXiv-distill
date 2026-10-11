# 2605.27429 Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking

## Problem

Industrial VOD recommenders need richer content understanding, but LLM-as-reranker designs repeat prompt construction, token generation, model invocation, output parsing, and fallback handling PER REQUEST. In high-volume latency-sensitive services, these operations complicate throughput planning, tail-latency control, capacity isolation, and predictable operation. Calling LLM at request-time is too expensive and unpredictable for production VOD systems.

## Contribution

1. Propose Ocean4Rec — reranking layer using LLM only OFFLINE to materialize item OCEAN personality profiles from content metadata. Items mapped to 5 dimensions: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism. Request-time: ZERO LLM calls.
2. User profiles built via time-decayed aggregation of recently clicked items in the same 5D OCEAN space.
3. Demonstrate OCEAN as bounded auxiliary feature — not standalone ranker, but complementing base relevance scores + recency.

## Method (core summary)

Offline: (1) LLM processes content metadata (title, description, genre, cast) per VOD item, generates 5 OCEAN personality scores (0-1 scale); (2) Item profiles materialized and stored. Online: (3) User profile = time-decayed weighted average of OCEAN scores from recently clicked/deep-linked items; (4) Reranking: join precomputed item OCEAN profiles + user OCEAN profiles + base recommender scores (NCF/LightGCN) + catalog recency → numeric reranking (NO LLM call); (5) Deployment controls: confidence-aware weighting, fallback treatment, exposure shift monitoring.

## Key Findings

- Samsung Smart TV VOD logs, temporal-holdout offline evaluation, Top1000 candidates
- Ocean4Rec vs Base+Recency: NDCG@20 improved 7.6% (NCF), 61.5% (LightGCN)
- HR@20: inconclusive for NCF, +67.3% for LightGCN
- vs Base-score-only: HR@20 +21.8% (NCF), +74.6% (LightGCN); NDCG@20 +15.0% (NCF), +67.9% (LightGCN)
- 95% bootstrap CIs: NDCG@20 delta +3.6% to +12.1% (NCF), +45.8% to +77.6% (LightGCN)
- OCEAN as standalone ranker: inconsistent, sometimes hurts MRR — works best as AUXILIARY feature
- Zero request-time LLM calls — preserves deployability

## Actionable Insights

1. When deploying LLM-enhanced recommendations, use LLM OFFLINE to precompute item features, DON'T call LLM at request-time. Example: e-commerce platform uses GPT-4 offline to generate personality/style profiles for 100K products, store as vectors, only numeric join at request time → latency <10ms instead of 500ms+ LLM call.
2. Personality dimensions (OCEAN) work well as auxiliary compatibility features between user and item, NOT standalone. Example: user watches high-Openness content → boost high-Openness items, but DON'T override base relevance score.
3. Time-decayed user profiles capture preference drift — recent clicks weighted more than old clicks. Example: user recently watches documentaries (high-Conscientiousness) → temporary boost, then decays when behavior changes.

## Assumptions & Limitations

- Assumption: OCEAN personality framework applicable to content items — may not capture all relevant dimensions
- Limitation (paper acknowledges): Offline evidence only — no online A/B test, latency measurement, business outcomes
- Limitation (paper acknowledges): Total system cost not measured
- Limitation: Data from Samsung Smart TV VOD — may not generalize to other platforms
- Limitation (observed): LLM personality assignment may be inconsistent — no validation that OCEAN scores are semantically meaningful

## Metadata

- Year: 2026
- Authors: Wonkyun Kim, Sehyun Bae, Kwanki Ahn, Mungyu Bae, Saeun Choi, Soyeon You, Chandra Prabhakar, Sehyun Kim
- Institution: Samsung Research
- Category: cs.IR, cs.AI
- PDF: https://arxiv.org/pdf/2605.27429
- Citation count: N/A
- Classification: [applied]
- Skill: ocean4rec-offline-personality-profiling
