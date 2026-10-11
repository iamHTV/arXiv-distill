# Skill: Multi-Agent Oracle với Hybrid Routing
Nguồn: 2605.30802v1
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) multi-agent system cho decision resolution (phân giải quyết định) với financial consequences (hậu quả tài chính)
- Khi cần reliable outcome resolution (phân giải kết quả đáng tin cậy) từ multiple AI models
- Khi design (thiết kế) hybrid AI-human systems (hệ thống lai AI-con người)

## KHÔNG nên dùng khi
- Task đơn giản, single model đủ
- Không có shared evidence (bằng chứng chung) — deliberation có thể useful
- Không có access (truy cập) đến multiple diverse LLMs
- Tasks requiring creative exploration (khám phá sáng tạo) — deliberation better

## Input cần có
- Multiple diverse LLMs (không cùng architecture/training data)
- Common evidence layer (tầng bằng chứng chung): retrieval system
- Questions/decisions cần resolve (phân giải)
- Confidence calibration data (dữ liệu hiệu chuẩn tin cậy)
- Human reviewers cho escalation cases

## Các bước thực hiện

### Bước 1 — Setup Independent Aggregation (thiết lập tổng hợp độc lập)
1. Deploy 3+ diverse LLMs (không cùng provider/architecture)
2. Common evidence retrieval: tất cả models cùng access evidence
3. Each model resolve independently — KHÔNG share reasoning
4. Collect: binary decision + confidence score per model

### Bước 2 — Compute Aggregation Signals (tính tín hiệu tổng hợp)
1. Majority vote: model nào có >50% votes → winner
2. Confidence-weighted vote: weight mỗi model's vote bằng confidence
3. Inter-agent agreement: unanimous (3-0) vs split (2-1)
4. Average confidence: mean của all models' confidence scores
5. Composite score = 1[unanimous] + confidence_mean (range 0-2)

### Bước 3 — Apply Routing Rules (áp dụng quy tắc định tuyến)
1. Unanimous + high confidence (≥0.91) → AUTO-RESOLVE (tự động phân giải)
   - Expected accuracy: ~97.87%
   - Coverage: ~47% questions
2. Unanimous + medium confidence → AUTO-RESOLVE with monitoring (giám sát)
3. Split (2-1 vote) → ESCALATE to human review
   - Expected accuracy nếu auto-resolve: ~57.82% — too risky
4. Low confidence regardless of agreement → ESCALATE

### Bước 4 — Monitor Error Correlations (giám sát tương quan lỗi)
1. Track error rates per model pair
2. Compute error correlation: r = correlation of failure patterns
3. If r > 0.6 → aggregation gains fundamentally limited
4. If r < 0.4 → aggregation can approach Condorcet ceiling
5. Diversify models if correlation too high

### Bước 5 — Handle Escalation (xử lý leo thang)
1. Route escalated questions to human reviewers
2. Provide: question, evidence, all model decisions + confidence, disagreement signal
3. DON'T provide model reasoning traces — increases acceptance regardless of correctness
4. Instead: show confidence scores + disagreement patterns (more actionable)
5. Track: human accuracy on escalated questions

## Output mong đợi
- Auto-resolved questions: ~47% coverage, ~97.87% accuracy
- Escalated questions: ~53%, routed to human review
- Overall system accuracy: 83-90% depending on escalation threshold
- Error correlation monitoring: alert if r > 0.6

## Ví dụ áp dụng
**Tình huống**: Financial prediction market cần resolve 1,000 questions/week. Current: single LLM oracle 82% accuracy. Muốn improve.

**Áp dụng**:
1. Deploy 3 diverse LLMs: GPT-5, DeepSeek, Llama
2. Common evidence: Exa retrieval, filtered by date
3. Independent resolution: each model answers independently
4. Routing:
   - 470 questions unanimous + high confidence → auto-resolve (97.87% accuracy)
   - 530 questions with disagreement → escalate to human review
5. Overall: 470 × 0.9787 + 530 × 0.95 (human accuracy) = 964/1000 = 96.4% accuracy
6. Cost: 3x API cost + human review cost for 53% questions

## Lưu ý quan trọng
1. **KHÔNG dùng deliberation cho evidence-based tasks**: Debate HẠI accuracy. Confidently wrong models flip correct ones. Chỉ dùng independent aggregation
2. **Error correlation is the bottleneck**: Nếu models cùng fail trên same questions → aggregation gains limited. Diversify models
3. **Disagreement > confidence**: Inter-agent disagreement là strongest predictor of error. Dùng nó làm escalation signal
4. **Don't show reasoning traces to humans**: Explanations increase acceptance regardless of correctness. Show confidence + disagreement instead
5. **Coverage-accuracy tradeoff**: Auto-resolve more → lower accuracy. Tune threshold based on financial stakes
6. **Cost consideration**: 3x API cost + human review cost. ROI depends on question volume và stakes
