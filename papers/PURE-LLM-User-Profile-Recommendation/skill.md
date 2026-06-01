# Skill: PURE — Quản lý Hồ sơ Người dùng cho Đề xuất
Nguồn: 2502.14541
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) LLM-based recommendation systems
- Khi cần evolve (phát triển) user profiles từ reviews
- Khi manage token limitations trong recommendations

## KHÔNG nên dùng khi
- No user reviews available
- Static profiles sufficient
- Non-LLM recommendation systems

## Input cần có
- User reviews
- Product metadata
- LLM cho extraction
- Token budget constraints

## Các bước thực hiện

### Bước 1 — Extract User Representation (trích xuất biểu diễn)
1. LLM extracts từ reviews:
   - Items user likes
   - Items user dislikes
   - Key user features
2. Output: structured preferences

### Bước 2 — Update Profile (cập nhật hồ sơ)
1. Merge new extractions với existing profile
2. Remove redundancy
3. Manage token budget
4. Output: updated user profile

### Bước 3 — Recommend (đề xuất)
1. Use current profile
2. Predict next purchase
3. Output: personalized recommendations

## Output mong đợi
- Evolving user profiles
- Better recommendations than purchase-history-only
- Token-efficient profile management

## Ví dụ áp dụng
**Tình huống**: E-commerce platform with user reviews.

**Áp dụng**:
1. Extract: user likes "wireless headphones with bass", dislikes "cheap plastic"
2. Update: merge với existing profile, remove duplicates
3. Recommend: based on current profile
4. Result: better recommendations than purchase history alone

## Lưu ý quan trọng
1. **Reviews > purchase history**: Richer preference data
2. **Evolving profiles**: Update when new reviews arrive
3. **Token management**: Compress, deduplicate
4. **Cold-start limitation**: No reviews = poor profiles
5. **Privacy concerns**: Review data sensitive
