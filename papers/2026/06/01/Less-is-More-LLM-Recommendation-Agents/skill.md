# Skill: LLM Recommendation Context Optimization (Tối ưu Hóa Ngữ cảnh Đề xuất LLM)
Nguồn: 2601.20316
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) LLM-based recommendation systems
- Khi optimize (tối ưu hóa) context length cho cost efficiency
- Khi challenge (thách thức) "more context is better" assumption

## KHÔNG nên dùng khi
- Non-LLM recommendation systems
- Cold-start users (cần different treatment)
- Long-tail items may need longer context

## Input cần có
- User purchase history
- LLM API access
- Quality evaluation metric
- Cost tracking

## Các bước thực hiện

### Bước 1 — Test Context Lengths (kiểm tra độ dài ngữ cảnh)
1. Test 5, 10, 15, 25, 50 items
2. Measure quality scores per length
3. Expected: flat quality curve (0.17-0.23 range)
4. All confidence intervals overlap

### Bước 2 — Analyze Cost Tradeoff (phân tích đánh đổi chi phí)
1. Measure token usage per context length
2. Expected: 8.2× cost increase from 5 to 50 items
3. Calculate: 88% savings using 5 items
4. Quality same across all lengths

### Bước 3 — Choose Optimal Length (chọn độ dài tối ưu)
1. Recommended: 5-10 items
2. Same quality as 50 items
3. 88% cost savings
4. Faster latency

### Bước 4 — Deploy with Minimal Context (triển khai với ngữ cảnh tối thiểu)
1. Limit context to 5-10 recent items
2. Monitor quality — should remain stable
3. Track cost savings
4. Adjust if specific domains need more

## Output mong đợi
- 88% cost savings
- Same recommendation quality
- Faster response times
- Actionable deployment guidelines

## Ví dụ áp dụng
**Tình huống**: E-commerce platform processes 1M recommendations/day. Currently using 50-item histories.

**Áp dụng**:
1. Test: 5, 10, 50 items → quality same (0.17-0.23)
2. Cost: 50 items = 2,371 tokens avg. 5 items = 288 tokens avg.
3. Switch: use 5 items instead of 50
4. Result: 88% cost savings, same quality, faster response

## Lưu ý quan trọng
1. **Less is more**: 5-10 items = same quality as 50. Don't waste tokens
2. **88% savings**: Significant cost reduction. Apply immediately
3. **Universal pattern**: Holds across 4 different LLM providers
4. **Model-specific latency**: Choose model based on latency needs
5. **Domain-specific may differ**: Some domains may need longer context — test yours
6. **Cold-start exception**: New users may need different treatment
