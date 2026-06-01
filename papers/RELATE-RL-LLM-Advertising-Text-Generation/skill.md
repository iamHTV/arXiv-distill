# Skill: Tạo Quảng cáo End-to-end bằng Học tăng cường
Nguồn: 2602.11780
Loại: framework (khung phương pháp)

## Khi nào dùng skill này
- Khi cần tạo quảng cáo text tự động mà tối ưu trực tiếp business metrics (chỉ số kinh doanh) như CTR (tỷ lệ nhấp chuột), CTCVR (tỷ lệ nhấp-chuyển đổi)
- Khi hệ thống hiện tại dùng hai giai đoạn tách rời (generate → align) và muốn unify (thống nhất) thành end-to-end (đầu cuối)
- Khi cần cân bằng quality (chất lượng), diversity (đa dạng), và compliance (tuân thủ) trong quảng cáo

## KHÔNG nên dùng khi
- Không có online feedback data (dữ liệu phản hồi trực tuyến) từ production system (hệ thống sản xuất)
- Budget (ngân sách) thấp — RL training tốn kém hơn supervised fine-tuning
- Cần real-time generation (tạo tức thời) với latency constraints (ràng buộc độ trễ) nghiêm ngặt

## Input cần có
- Base LLM (mô hình ngôn ngữ lớn gốc) đã fine-tune (tinh chỉnh) cơ bản
- Online feedback logs (nhật ký phản hồi): CTR, CTCVR data từ production
- Compliance rules (quy tắc tuân thủ): danh sách content policies (chính sách nội dung)
- Training data: quảng cáo text mẫu với metadata (siêu dữ liệu)
- Evaluation metrics (chỉ số đánh giá): quality, diversity, compliance, CTCVR

## Các bước thực hiện

### Bước 1 — Định nghĩa Reward Functions (hàm phần thưởng)
1. **Quality reward**: Structural quality (chất lượng cấu trúc) — length reward (kiểm tra độ dài phù hợp), format reward (kiểm tra định dạng). Semantic quality (chất lượng ngữ nghĩa) — correctness (đúng đắn), relevance (liên quan đến sản phẩm), risk-control (kiểm soát rủi ro nội dung)
2. **Diversity reward**: Reward quảng cáo khác biệt so với historical ads (quảng cáo lịch sử) — chống text fatigue (mệt mỏi văn bản)
3. **CTCVR reward**: Conversion-oriented metrics (chỉ số hướng chuyển đổi) trực tiếp từ online feedback

### Bước 2 — Thiết kế Credit Assignment Strategy (chiến lược phân bổ tín hiệu)
1. Sentence level (mức câu): structural quality + CTCVR reward — reward cho toàn bộ output
2. Token level (mức ký tự): diversity + semantic quality constraints — reward cho từng phần của output
3. Mục đích: giải quyết reward sparsity (thưa phần thưởng) và delayed feedback (phản hồi trễ)

### Bước 3 — RL Training với GRPO
1. Algorithm (thuật toán): GRPO (Group Relative Policy Optimization)
2. Composite reward (phần thưởng kết hợp): r = w1·quality + w2·diversity + w3·CTCVR
3. Train model end-to-end: generation và alignment thống nhất trong một model
4. Monitor (giám sát): compliance rate, diversity score, CTCVR convergence (hội tụ)

### Bước 4 — Online Deployment (triển khai trực tuyến)
1. A/B test: RELATE vs production baseline
2. Metrics theo dõi: CTCVR, compliance rate, diversity score, user engagement (tương tác người dùng)
3. Iterate (lặp lại): cập nhật reward weights dựa trên online performance

## Output mong đợi
- Quảng cáo text chất lượng cao, đa dạng, tuân thủ chính sách
- Cải thiện CTCVR so với production baseline
- Giảm text fatigue nhờ diversity reward
- End-to-end system đơn giản hơn hai giai đoạn tách rời

## Ví dụ áp dụng
**Tình huống**: E-commerce platform muốn AI tạo product ads cho Facebook/Google. Hiện tại dùng hai giai đoạn: (1) LLM generate ad text, (2) ranker chọn ad có CTR cao nhất. Vấn đề: ad text hay nhưng không convert, hoặc lặp lại gây fatigue.

**Áp dụng**:
1. Quality reward: check ad có mention đúng product features không, có đúng format Facebook/Google không
2. Diversity reward: reward ad khác biệt so với 100 ad gần nhất của cùng sản phẩm
3. CTCVR reward: reward trực tiếp từ conversion data (sau 7 ngày)
4. Credit assignment: quality check từng sentence, CTCVR cho toàn bộ ad
5. Train RELATE end-to-end → ad vừa hay, vừa đa dạng, vừa convert

## Lưu ý quan trọng
1. **Cold start**: Cần đủ historical data để train — nếu mới launch, dùng SFT trước rồi mới RL
2. **Reward model quality**: Nếu reward model sai → policy sai → ad kém chất lượng
3. **Latency**: End-to-end RL có thể slower inference so với rule-based generation
4. **Compliance risk**: Model có thể learn cách "cheat" reward — cần robust risk-control reward
5. **Platform-specific**: Reward functions cần customize theo từng platform (Facebook vs Google vs TikTok)
6. **Data freshness**: CTCVR data cần update thường xuyên — stale data → suboptimal policy
