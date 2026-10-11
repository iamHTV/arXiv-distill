# Skill: Null Assumption cho Đánh giá LLM
Nguồn: 2605.31514v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi đánh giá AI capabilities (khả năng AI) và cần tránh anthropomorphic bias (thiên kiến nhân hình hóa)
- Khi vendor hoặc nghiên cứu claim LLM "hiểu", "suy luận", "sáng tạo" — cần verification framework (khung xác minh)
- Khi thiết kế experiment đánh giá AI system

## KHÔNG nên dùng khi
- Đánh giá technical performance (hiệu suất kỹ thuật) thuần túy (accuracy, latency, throughput)
- Đã có clear operational definition (định nghĩa vận hành) rõ ràng cho attribute cần đo
- Task chỉ cần behavioral benchmark (bài kiểm tra hành vi), không cần interpret internal states (trạng thái nội bộ)

## Input cần có
- AI system cần đánh giá
- Attribute X cần verify (ví dụ: understanding, reasoning, creativity, planning)
- Baseline systems (hệ thống cơ sở) để compare (ví dụ: rule-based, random, simple NN)
- Clear behavioral metrics (số liệu hành vi) có thể đo được

## Các bước thực hiện

### Bước 1 — Define Attribute Operationally (định nghĩa thuộc tính một cách vận hành)
1. Chọn attribute X cần verify (ví dụ: "understanding")
2. Define (định nghĩa) X bằng behavioral terms (điều kiện hành vi): "X = ability to do Y with Z% accuracy on unseen data"
3. KHÔNG define X bằng human analogy (loại suy con người): "X = AI hiểu như con người"
4. Output: operational definition (định nghĩa vận hành) có thể test

### Bước 2 — Apply Null Assume (áp dụng giả định không)
1. Default assumption: AI KHÔNG có attribute X
2. Burden of proof (gánh nặng chứng minh): phải demonstrate ngược
3. Ask: "Is X unique to this AI system, or can other substrates exhibit X?"

### Bước 3 — Substrate Comparison (so sánh nền tảng)
1. Build/choose baseline systems trên substrates khác:
   - Rule-based system
   - Simple neural network
   - Random baseline
   - Human baseline (nếu applicable)
2. Run same behavioral test trên tất cả systems
3. If baselines achieve comparable (tương đương) performance → X is NOT unique to LLM

### Bước 4 — Measure Substrate-Independently (đo lường độc lập nền tảng)
1. Define measurement criteria BEFORE interpreting behavior
2. Use objective metrics (số liệu khách quan), không subjective interpretation
3. Report: "System A achieves X% on metric M, System B achieves Y% — difference is Z%"
4. KHÔNG report: "System A understands better than System B"

### Bước 5 — Draw Conclusion (rút ra kết luận)
1. If LLM uniquely outperforms all baselines on operational definition → attribute may exist
2. If baselines match LLM → attribute is substrate-dependent, not unique
3. If no clear operational definition possible → attribute is non-measurable, suspend judgment

## Output mong đợi
- Clear verdict (kết luận): attribute X có unique cho LLM không?
- Evidence-based conclusion (kết luận dựa trên bằng chứng), không circular reasoning
- Actionable decision (quyết định có thể hành động) cho business/AI adoption

## Ví dụ áp dụng
**Tình huống**: Vendor claim AI chatbot "understands" customer intent và recommend (đề xuất) products.

**Áp dụng**:
1. Define "understanding" = correctly identify customer intent với >85% accuracy on unseen queries
2. Null assumption: chatbot KHÔNG understand, chỉ pattern match
3. Substrate comparison: rule-based keyword system vs simple classifier vs LLM chatbot
4. Results: rule-based 60%, classifier 72%, LLM 88%
5. Conclusion: LLM uniquely outperforms → "understanding" (operationally defined) exists. Nhưng: nếu classifier đạt 85% → "understanding" không unique, chỉ là better pattern matching

## Lưu ý quan trọng
1. **Avoid circular reasoning**: "AI hiểu vì nó trả lời đúng" → circular. Phải define "hiểu" independent of output
2. **Substrate choice matters**: Baselines quá yếu → unfair comparison. Baselines quá mạnh → attribute bị dismiss unfairly
3. **Operational definition quality**: Definition quá narrow → attribute always exists. Quá broad → never exists. Balance (cân bằng)
4. **Scale consideration**: Paper ignore rằng LLM có emergent capabilities (khả năng phát sinh) ở scale mà small NN không có → substrate comparison có thể unfair
5. **Practical vs philosophical**: Null assumption useful cho critical evaluation nhưng có thể slow down innovation (đổi mới) nếu apply quá strict
