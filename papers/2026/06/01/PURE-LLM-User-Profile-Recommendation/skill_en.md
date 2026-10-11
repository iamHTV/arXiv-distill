# Skill: PURE — User Profile Management for Recommendations
Source: 2502.14541
Type: workflow

## When to use this skill
- When building LLM-based recommendation systems
- When needing to evolve user profiles from reviews
- When managing token limitations in recommendations

## When NOT to use
- No user reviews available
- Static profiles sufficient
- Non-LLM recommendation systems

## Required inputs
- User reviews
- Product metadata
- LLM for extraction
- Token budget constraints

## Steps

### Step 1 — Extract User Representation
1. LLM extracts from reviews:
   - Items user likes
   - Items user dislikes
   - Key user features
2. Output: structured preferences

### Step 2 — Update Profile
1. Merge new extractions with existing profile
2. Remove redundancy
3. Manage token budget
4. Output: updated user profile

### Step 3 — Recommend
1. Use current profile
2. Predict next purchase
3. Output: personalized recommendations

## Expected output
- Evolving user profiles
- Better recommendations than purchase-history-only
- Token-efficient profile management

## Example application
**Scenario**: E-commerce platform with user reviews.

**Application**:
1. Extract: user likes "wireless headphones with bass", dislikes "cheap plastic"
2. Update: merge with existing profile, remove duplicates
3. Recommend: based on current profile
4. Result: better recommendations than purchase history alone

## Gotchas
1. **Reviews > purchase history**: Richer preference data
2. **Evolving profiles**: Update when new reviews arrive
3. **Token management**: Compress, deduplicate
4. **Cold-start limitation**: No reviews = poor profiles
5. **Privacy concerns**: Review data sensitive
