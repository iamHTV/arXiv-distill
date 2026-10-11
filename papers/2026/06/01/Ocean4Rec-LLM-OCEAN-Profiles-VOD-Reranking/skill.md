# Skill: Ocean4Rec Offline Personality Profiling
Source: 2605.27429
Type: framework

## Khi nào dùng skill này

- Khi cần enhance recommendation system với LLM-derived features mà KHÔNG muốn call LLM at request-time — latency và cost constraints bắt buộc offline processing
- Khi có content metadata (titles, descriptions, tags) và muốn tạo rich personality/feature profiles cho items
- Khi user-item compatibility (tương thích) là important — matching user "taste personality" với item "content personality"

- KHÔNG dùng khi: không có content metadata; items không có meaningful personality dimensions; recommendation là cold-start (không có user behavior history)

## Input cần có

- Content metadata cho mỗi item (title, description, genre, tags, cast, etc.)
- User interaction history (clicks, views, purchases) với timestamps
- Base recommender scores (NCF, LightGCN, hoặc collaborative filtering)
- LLM access for offline profile generation (batch processing OK)

## Các bước thực hiện

1. **Define Personality Dimensions** — Chọn 5+ dimensions phù hợp với domain. OCEAN (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) work cho entertainment. Domain khác có thể dùng: complexity, formality, technical depth, humor, emotional tone. Prompt LLM: "Rate this item on [dimensions] from 0 to 1 based on metadata: {title}, {description}, {genre}."

2. **Offline Item Profiling** — Batch process all items qua LLM. Generate personality scores (0-1) cho mỗi dimension. Store as precomputed vectors. Validate consistency: sample 100 items, re-generate profiles, check correlation >0.85 across runs. Cost: ~$0.001/item with GPT-4o-mini.

3. **Time-Decayed User Profiling** — User profile = weighted average của personality scores từ interacted items. Weight = interaction_type_weight × time_decay(interaction_age). Recent interactions weighted more: decay = exp(-λ × days_since). Deep links / purchases > clicks.

4. **Numeric Reranking** — At request time: (a) Retrieve base candidates from collaborative filtering; (b) Join with precomputed item OCEAN vectors + user OCEAN vector; (c) Compute compatibility score = cosine_similarity(user_vector, item_vector); (d) Final score = α×base_score + β×compatibility + γ×recency; (e) Sort, return top-K. ZERO LLM calls.

5. **Deployment Controls** — Monitor: confidence-aware weighting (weight compatibility less when user profile confidence low), fallback to base+recency when compatibility scores all similar, exposure shift monitoring (ensure new feature doesn't cause filter bubble).

## Output mong đợi

- NDCG@20 improvement: +7.6% to +61.5% over base+recency (depending on base generator)
- Zero request-time latency overhead (all precomputed)
- Auxiliary feature that complements but doesn't replace base relevance

## Ví dụ áp dụng

Scenario: Music streaming platform. (1) Offline: GPT-4o-mini generates personality profiles for 5M tracks based on title, artist, genre, lyrics snippet — dimensions: Energy, Mood, Complexity, Danceability, Focus; (2) User profile: weighted average from last 100 plays, time-decayed; (3) Request-time: blend base CF scores with personality compatibility — user high-Focus → boost instrumental/acoustic tracks; (4) Result: +12% NDCG@20, zero latency overhead. Cost: $5K one-time offline profiling (5M items × $0.001).

## Gotchas

- OCEAN dimensions may not fit all domains — must customize dimensions per domain. Entertainment ≠ e-commerce ≠ education.
- LLM profile consistency: temperature=0 helps but batch profiling across sessions may drift. Validate with re-generation correlation check.
- Time decay λ must be tuned: too aggressive → user profile too volatile; too slow → stale preferences. Start λ=0.05 (half-life ~14 days).
- Auxiliary feature only: if α (base score weight) too low, performance degrades. OCEAN supplements, doesn't replace, collaborative filtering signal.
