# [2502.14541] PURE: Quản lý Hồ sơ Người dùng dựa trên LLM cho Hệ thống Đề xuất

## Vấn đề
LLMs mở ra opportunities mới cho recommender systems bằng zero-shot recommendation. Nhưng existing works rely solely trên purchase histories — bỏ lỡ user-generated textual data (dữ liệu văn bản do người dùng tạo) như reviews và product descriptions. Pure purchase history không capture preferences đầy đủ.

## Đóng góp
1. **PURE framework**: LLM-based recommendation xây dựng và maintains evolving user profiles từ user reviews
2. **3 components**: Review Extractor (trích xuất sở thích, features), Profile Updater (cập nhật hồ sơ), Recommender (đề xuất)
3. **Continuous sequential recommendation**: Thêm reviews theo thời gian, cập nhật predictions incrementally

## Phương pháp (tóm tắt cốt lõi)
PURE: (1) Review Extractor: LLM extracts từ reviews — items user likes, dislikes, key features; (2) Profile Updater: merges new extractions với existing profile, removes redundancy; (3) Recommender: uses current profile để predict next purchase. Continuous: profile evolves theo thời gian khi new reviews arrive.

## Kết quả chính
- Outperforms existing LLM-based methods trên Amazon datasets
- Effectively leverages long-term user information
- Manages token limitations
- Continuous sequential recommendation task reflects real-world scenarios

## Insight có thể áp dụng ngay
1. **User profiles từ reviews**: Không chỉ dùng purchase history. Extract preferences từ reviews. Ví dụ: khi build recommendation system, parse user reviews để extract likes, dislikes, key features — richer than purchase history alone.

2. **Evolving profiles**: Update profiles khi new reviews arrive. Don't use static profiles. Ví dụ: when user posts new review, update their profile immediately — preferences change over time.

3. **Token management**: LLMs có token limits. Manage profile size bằng cách remove redundancy. Ví dụ: when maintaining user profiles, periodically compress và deduplicate preference data.

## Giả định & Hạn chế
**Điều kiện để method work:**
- User reviews available
- LLM capable enough cho extraction
- Amazon dataset tested

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn chế paper KHÔNG nói:**
- Review quality dependency — sparse reviews = poor profiles
- Cold-start users with no reviews
- Privacy concerns with review data
- Token costs for profile management
- Cross-domain transferability

## Metadata
- Năm: 2025
- Tác giả: Seunghwan Bang, Hwanjun Song
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2502.14541
- Citation count: [EXTRACTION FAILED]
