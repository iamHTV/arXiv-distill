# [2601.20316] Less is More: Benchmarking LLM Based Recommendation Agents (Ít hơn là Nhiều hơn)

## Vấn đề
LLMs increasingly deployed cho personalized product recommendations. Practitioners commonly assume (giả định thông thường) rằng longer user purchase histories (lịch sử mua hàng dài hơn) lead to better predictions. Nhưng assumption này chưa được test systematically. "More context is better" paradigm (paradigm nhiều ngữ cảnh hơn là tốt hơn) có đúng không?

## Đóng góp
1. **Challenge "more context is better"**: Systematic benchmark 4 LLMs across context lengths 5-50 items. Finding: NO significant quality improvement with longer context
2. **88% cost savings**: Using 5 items instead of 50 → 88% token cost reduction, no quality loss
3. **Universal pattern**: Finding holds across 4 different providers — fundamental limitation

## Phương pháp (tóm tắt cốt lõi)
Benchmark: 4 LLMs (GPT-4o-mini, DeepSeek-V3, Qwen2.5-72B, Gemini 2.5 Flash). Context lengths: 5, 10, 15, 25, 50 items. Dataset: REGEN. 50 users, within-subject design. Metrics: quality scores, token usage, latency. Cost analysis.

## Kết quả chính
- Quality scores flat: 0.17-0.23 across ALL conditions, ALL models
- Average quality change 5→50 items: -0.01 (essentially zero)
- All confidence intervals overlap — no statistically significant differences
- Token costs: 8.2× increase from 5 to 50 items
- 88% potential cost savings using 5 items instead of 50
- Latency varies by provider — model-specific patterns

## Insight có thể áp dụng ngay
1. **Use minimal context (5-10 items)**: Don't feed 50-item purchase histories. 5-10 items = same quality, 88% cheaper. Ví dụ: khi build product recommendation system, chỉ lấy 5-10 recent purchases thay vì entire history.

2. **88% cost savings**: Token costs 8.2× higher with 50 items vs 5 items. Quality same. Ví dụ: e-commerce platform processing 1M recommendations/day → save ~88% API costs bằng cách limit context.

3. **Model-specific latency**: Different providers have different latency patterns. Choose model based on your latency requirements. Ví dụ: real-time recommendations → choose lowest latency model. Batch processing → choose cheapest.

## Giả định & Hạn chế
**Điều kiện để benchmark work:**
- REGEN dataset specific
- 50 users, within-subject design
- 4 specific LLMs tested

**Hạn chế paper thừa nhận:**
- Limited to REGEN dataset
- 50 users sample size

**Hạn chế paper KHÔNG nói:**
- Quality metric specific (0.17-0.23 range) — may not capture all recommendation aspects
- Different product categories may have different optimal context lengths
- User behavior patterns may vary by domain
- Long-tail items may benefit from longer context
- Cold-start users may need different treatment

## Metadata
- Năm: 2026
- Tác giả: Kargi Chauhan, Mahalakshmi Venkateswarlu
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2601.20316
- Citation count: [EXTRACTION FAILED]
