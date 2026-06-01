# Skill: Ocean4Rec Offline Personality Profiling
Source: 2605.27429
Type: framework

## When to use this skill

- When enhancing recommendation systems with LLM-derived features WITHOUT calling LLM at request-time — latency and cost constraints require offline processing
- When having content metadata (titles, descriptions, tags) and wanting to create rich personality/feature profiles for items
- When user-item compatibility matters — matching user "taste personality" with item "content personality"

- Do NOT use when: no content metadata available; items don't have meaningful personality dimensions; recommendation is cold-start (no user behavior history)

## Input needed

- Content metadata per item (title, description, genre, tags, cast, etc.)
- User interaction history (clicks, views, purchases) with timestamps
- Base recommender scores (NCF, LightGCN, or collaborative filtering)
- LLM access for offline profile generation (batch processing OK)

## Steps

1. **Define Personality Dimensions** — Choose 5+ dimensions suited to domain. OCEAN works for entertainment. Other domains: complexity, formality, technical depth, humor, emotional tone. Prompt LLM: "Rate this item on [dimensions] from 0 to 1 based on metadata: {title}, {description}, {genre}."

2. **Offline Item Profiling** — Batch process all items through LLM. Generate personality scores (0-1) per dimension. Store as precomputed vectors. Validate consistency: sample 100 items, re-generate, check correlation >0.85. Cost: ~$0.001/item with GPT-4o-mini.

3. **Time-Decayed User Profiling** — User profile = weighted average of personality scores from interacted items. Weight = interaction_type_weight × time_decay(interaction_age). Recent interactions weighted more: decay = exp(-λ × days_since). Deep links/purchases > clicks.

4. **Numeric Reranking** — At request time: (a) Retrieve base candidates from collaborative filtering; (b) Join with precomputed item vectors + user vector; (c) Compute compatibility = cosine_similarity(user_vector, item_vector); (d) Final score = α×base_score + β×compatibility + γ×recency; (e) Sort, return top-K. ZERO LLM calls.

5. **Deployment Controls** — Monitor: confidence-aware weighting (weight compatibility less when user profile confidence low), fallback to base+recency when compatibility scores all similar, exposure shift monitoring (ensure no filter bubble).

## Expected output

- NDCG@20 improvement: +7.6% to +61.5% over base+recency
- Zero request-time latency overhead
- Auxiliary feature complementing base relevance

## Example application

Scenario: Music streaming platform. (1) Offline: GPT-4o-mini generates profiles for 5M tracks — dimensions: Energy, Mood, Complexity, Danceability, Focus; (2) User profile: weighted average from last 100 plays, time-decayed; (3) Request-time: blend CF scores with personality compatibility — high-Focus user → boost instrumental tracks; (4) Result: +12% NDCG@20, zero latency overhead. Cost: $5K one-time offline profiling.

## Gotchas

- OCEAN dimensions may not fit all domains — customize per domain
- LLM profile consistency: temperature=0 helps but batch drift possible. Validate with re-generation correlation.
- Time decay λ must be tuned: too aggressive → volatile; too slow → stale. Start λ=0.05 (half-life ~14 days).
- Auxiliary feature only: if base score weight too low, performance degrades.
