# Skill: LLM Strategic Foresight Screening (Lọc tầm nhìn chiến lược bằng LLM)
Nguồn: 2602.01684
Loại: workflow (quy trình làm việc)

## Khi nào dùng skill này
- Khi cần screen (lọc) large volume (khối lượng lớn) opportunities (cơ hội) — venture deals, acquisitions, R&D projects, partnerships
- Khi human evaluation capacity (năng lực đánh giá của con người) bị bottleneck (nút thắt)
- Khi cần consistent (ổn định), reproducible (có thể tái tạo) ranking (xếp hạng) under uncertainty (dưới bất确定性)

## KHÔNG nên dùng khi
- Task cần implementation capability (năng lực triển khai) — LLM chỉ evaluate, không execute
- Information environment quá noisy (nhiễu) hoặc unstructured (không có cấu trúc) — LLM cần standardized summaries
- Outcomes phụ thuộc vào evaluator's own actions — LLM không có skin in the game

## Input cần có
- List of opportunities (danh sách cơ hội) cần evaluate
- Standardized summary (tóm tắt tiêu chuẩn) cho mỗi opportunity — structured format
- Evaluation criteria (tiêu chí đánh giá) rõ ràng — success/failure definition
- Access to frontier LLM (GPT-5, Gemini 2.5, Claude 4.5+)

## Các bước thực hiện

### Bước 1 — Chuẩn bị Standardized Summaries (tóm tắt tiêu chuẩn)
1. Tạo template (mẫu) cho mỗi opportunity: problem, solution, team, market, traction (động lực), financials (tài chính)
2. Điền thông tin từ pitch deck, financial documents, market research
3. Đảm bảo same format cho tất cả opportunities — so sánh công bằng
4. Constraint: không include outcome information — chỉ pre-decision data

### Bước 2 — Pairwise Comparison Tournament (giải đấu so sánh từng cặp)
1. Tạo tất cả pairs (cả hai thứ tự A-B và B-A để tránh order bias — thiên vị thứ tự)
2. Prompt LLM: "Given these two ventures, which is more likely to succeed? [Summary A] vs [Summary B]"
3. Record winner cho mỗi pair
4. Aggregate (tổng hợp) thành full ranking bằng win rate

### Bước 3 — Benchmark against Humans (so sánh với con người)
1. Recruited evaluators (người đánh giá được tuyển): experienced managers, domain experts
2. Same task, same information, same prompts
3. Compare rank correlations với realized outcomes

### Bước 4 — Apply Screening Decision (áp dụng quyết định lọc)
1. LLM ranking → top N opportunities
2. Human review chỉ top N (không phải tất cả)
3. Final decision: human judgment trên filtered set
4. Track: LLM accuracy vs human accuracy trên same subset

## Output mong đợi
- Ranked list of opportunities theo predicted success probability (xác suất thành công)
- Top N filtered set cho human review
- Consistency metrics (chỉ số ổn định): LLM rankings stable qua multiple runs
- Accuracy benchmark: LLM vs human correlations

## Ví dụ áp dụng
**Tình huống**: Corporate VC nhận 500 startup pitches mỗi quarter. Hiện tại: 5 partners review mỗi pitch (2500 evaluations). Muốn automate first-pass screening.

**Áp dụng**:
1. Standardized summary cho mỗi startup: problem, solution, market size, team, traction, ask
2. Pairwise tournament: 500 startups → 124,750 pairs → LLM evaluate mỗi pair
3. Ranking by win rate → top 25 startups
4. Partners chỉ review 25 startups (giảm 95% workload)
5. Track: LLM top-25 overlap với partners' top-25 nếu partners review all 500

## Lưu ý quan trọng
1. **Augmentation trap**: KHÔNG thêm human vào AI pipeline nếu AI đã outperform human — có thể làm GIẢM performance. Human value nằm ở shaping inputs, không phải filtering outputs
2. **Order bias**: Phải test cả hai thứ tự A-B và B-A — LLM có thể bias toward first or second option
3. **Summary quality**: Garbage in, garbage out — standardized summary phải đủ chi tiết và công bằng
4. **Model selection**: Frontier models (GPT-5, Gemini 2.5) outperform smaller models rõ rệt — dùng frontier
5. **Domain specificity**: Kết��드 Venture screening — không chắc transfer sang domains khác (medical, legal)
6. **Cost**: 870 pairwise comparisons với frontier models tốn kha khá — tính budget trước
