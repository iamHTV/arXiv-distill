# [2502.14541] PURE: LLM-based User Profile Management for Recommender System

## Problem
LLMs open new opportunities for recommender systems via zero-shot recommendation. But existing works rely solely on purchase histories — missing user-generated textual data like reviews and product descriptions. Pure purchase history doesn't capture preferences fully.

## Contribution
1. **PURE framework**: LLM-based recommendation that builds and maintains evolving user profiles from user reviews.
2. **3 components**: Review Extractor (extract preferences, features), Profile Updater (update profile), Recommender (recommend).
3. **Continuous sequential recommendation**: Adds reviews over time, updates predictions incrementally.

## Method (core summary)
PURE: (1) Review Extractor: LLM extracts from reviews — items user likes, dislikes, key features; (2) Profile Updater: merges new extractions with existing profile, removes redundancy; (3) Recommender: uses current profile to predict next purchase. Continuous: profile evolves over time as new reviews arrive.

## Key Findings
- Outperforms existing LLM-based methods on Amazon datasets
- Effectively leverages long-term user information
- Manages token limitations
- Continuous sequential recommendation task reflects real-world scenarios

## Actionable Insights
1. **User profiles from reviews**: Don't just use purchase history. Extract preferences from reviews. Example: when building recommendation system, parse user reviews to extract likes, dislikes, key features — richer than purchase history alone.

2. **Evolving profiles**: Update profiles when new reviews arrive. Don't use static profiles. Example: when user posts new review, update their profile immediately — preferences change over time.

3. **Token management**: LLMs have token limits. Manage profile size by removing redundancy. Example: when maintaining user profiles, periodically compress and deduplicate preference data.

## Assumptions & Limitations
**Conditions for method to work:**
- User reviews available
- LLM capable enough for extraction
- Amazon dataset tested

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- Review quality dependency — sparse reviews = poor profiles
- Cold-start users with no reviews
- Privacy concerns with review data
- Token costs for profile management
- Cross-domain transferability

## Metadata
- Year: 2025
- Authors: Seunghwan Bang, Hwanjun Song
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2502.14541
- Citation count: [EXTRACTION FAILED]
