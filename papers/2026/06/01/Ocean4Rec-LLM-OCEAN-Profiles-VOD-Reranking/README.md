# 2605.27429 Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking

## Problem

Industrial VOD (Video-on-Demand — video theo yêu cầu) recommenders cần richer content understanding, nhưng LLM-as-reranker designs phải repeat prompt construction, token generation, model invocation, output parsing, và fallback handling MỖI REQUEST. Trong high-volume latency-sensitive services (dịch vụ nhạy cảm độ trễ), các operations này complicate throughput planning (kế hoạch thông lượng), tail-latency control (kiểm soát độ trễ đuôi), capacity isolation (cách ly tài nguyên), và predictable operation (vận hành dự đoán được). Tóm lại: calling LLM at request-time quá expensive và unpredictable cho production VOD systems.

## Contribution

1. Propose Ocean4Rec — reranking layer dùng LLM chỉ ở OFFLINE để materialize (hóa cứng) item OCEAN personality profiles (đặc tính tính cách) từ content metadata. Items mapped vào 5 dimensions: Openness (cởi mở), Conscientiousness (tận tâm), Extraversion (hướng ngoại), Agreeableness (dễ chịu), Neuroticism (thần kinh). Request-time: ZERO LLM calls.
2. User profiles built bằng time-decayed aggregation (tổng hợp giảm dần theo thời gian) của recently clicked items trong cùng 5D OCEAN space.
3. Demonstrate OCEAN as bounded auxiliary feature — KHÔNG standalone ranker, mà complement base relevance scores + recency.

## Method (tóm tắt cốt lõi)

Offline: (1) LLM processes content metadata (title, description, genre, cast) cho mỗi VOD item, generates 5 OCEAN personality scores (0-1 scale); (2) Item profiles materialized và stored. Online: (3) User profile = time-decayed weighted average của OCEAN scores từ recently clicked/deep-linked items; (4) Reranking: join precomputed item OCEAN profiles + user OCEAN profiles + base recommender scores (NCF/LightGCN) + catalog recency → numeric reranking (KHÔNG LLM call); (5) Deployment controls: confidence-aware weighting, fallback treatment, exposure shift monitoring.

## Key Findings

- Samsung Smart TV VOD logs, temporal-holdout offline evaluation, Top1000 candidates
- Ocean4Rec vs Base+Recency: NDCG@20 improved 7.6% (NCF generator), 61.5% (LightGCN generator)
- HR@20: inconclusive for NCF (+small), +67.3% for LightGCN
- vs Base-score-only: HR@20 +21.8% (NCF), +74.6% (LightGCN); NDCG@20 +15.0% (NCF), +67.9% (LightGCN)
- 95% bootstrap CIs: NDCG@20 delta +3.6% to +12.1% (NCF), +45.8% to +77.6% (LightGCN)
- OCEAN as standalone ranker: inconsistent, sometimes hurts MRR — works best as AUXILIARY feature alongside base+recency
- Zero request-time LLM calls — preserves deployability of traditional serving path

## Actionable Insights

1. Khi deploy LLM-enhanced recommendation, dùng LLM OFFLINE để precompute item features, KHÔNG call LLM at request-time. Ví dụ: e-commerce platform dùng GPT-4 offline để generate personality/style profiles cho 100K products, store as vectors, chỉ numeric join at request time → latency <10ms thay vì 500ms+ LLM call.
2. Personality dimensions (OCEAN) hoạt động tốt làm auxiliary compatibility feature (tính năng tương thích phụ trợ) giữa user và item, KHÔNG standalone. Ví dụ: user hay xem phim high-Openness → boost items có high-Openness score, nhưng KHÔNG override base relevance score.
3. Time-decayed user profiles capture preference drift (trôi sở thích) — recent clicks weighted hơn old clicks. Ví dụ: user gần đây xem nhiều documentary (high-Conscientiousness) → temporary boost Conscientiousness-matching content, sau đó decay khi behavior thay đổi.

## Assumptions & Limitations

- Giả sử: OCEAN personality framework applicable cho content items — có thể không capture all relevant content dimensions
- Limitation (paper thừa nhận): Offline evidence only — không có online A/B test, latency measurement, business outcomes
- Limitation (paper thừa nhận): Total system cost not measured
- Limitation: Data từ Samsung Smart TV VOD — may not generalize to other platforms (music, books, e-commerce)
- Limitation (tự thấy): LLM personality assignment có thể inconsistent across items — no validation that OCEAN scores are semantically meaningful for recommendation. Human evaluation needed.

## Metadata

- Năm: 2026
- Tác giả: Wonkyun Kim, Sehyun Bae, Kwanki Ahn, Mungyu Bae, Saeun Choi, Soyeon You, Chandra Prabhakar, Sehyun Kim
- Institution: Samsung Research
- Category: cs.IR, cs.AI
- Link PDF: https://arxiv.org/pdf/2605.27429
- Citation count: N/A
- Nhãn: [applied]
- Skill: ocean4rec-offline-personality-profiling
