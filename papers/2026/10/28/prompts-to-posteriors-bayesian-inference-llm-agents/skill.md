# Skill: Kiểm toán chất lượng cập nhật niềm tin Bayesian của agent LLM (Bayesian belief-update audit)
Source: 2610.29331 (From Prompts to Posteriors)
Type: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Trước khi tin tưởng agent LLM tích lũy evidence (bằng chứng) qua nhiều turn (lượt hội thoại): forecasting (dự báo), chẩn đoán, giám sát vận hành, discovery khoa học.
- Khi bạn định dùng LLM thay thế strict harness (khung ràng buộc chặt — kiểu BED-LLM cố định mô hình xác suất ngoài model).
- KHÔNG nên dùng: task phân loại single-shot (1 lượt) không tích lũy evidence; hypothesis space (không gian giả thuyết) thực sự mở VÀ không thể specify (xác định) likelihood model (hàm hợp lý) — khi đó oracle không xây dựng được.

## Input cần có
- Hypothesis space Θ hữu hạn (hoặc subset Θ_k động quản lý được), prior p0 (phân phối tiên nghiệm) cố định từ ngoài.
- Likelihood model p(y|θ,ξ) — bắt đầu từ bản closed-form (dạng đóng) đơn giản; nếu cần phiên bản hard thì chuẩn bị MC (Monte Carlo) estimator.
- Experiment space Ξ (không gian thí nghiệm) + T (số bước cập nhật, ví dụ 6–20).
- Cùng 1 model LLM với 3 cấu hình: no reasoning, reasoning mode, reasoning + code execution tool.

## Các bước thực hiện
1. Elicit (khai thác) MỌI phán đoán xác suất trong MỘT dialogue duy nhất — tuyệt đối không hỏi rải rác nhiều hội thoại rồi ghép (cross-conversation Dutch-bookable >50% scenarios, within-dialogue còn 0–10%).
2. Self-check (tự kiểm tra) 3 tiên đề Kolmogorov trên ≥10 bộ kịch bản: normalization (N — tổng xác suất = 1), monotonicity (M — event chứa nhau thì xác suất monotone), extensionality (E — đánh giá nhất quán khi diễn đạt tương đương). Vi phạm → output không dùng được làm phân phối, dừng audit.
3. Chạy vòng sequential (tuần tự) T bước: chọn experiment ξ_k → observe outcome y_k → cập nhật posterior p^LLM_k. Song song tính oracle trajectory p^ora-pas bằng Bayes rule (Eq.1) với cùng prior + cùng outcomes.
4. Tính posterior fidelity: forward KL(p^ora-pas ∥ p^LLM) mỗi bước (clip p^LLM từ dưới 10^-6 rồi renormalize). Dùng forward KL — KHÔNG dùng reverse KL — để phạt việc loại bỏ sớm hypothesis còn hiệu lực.
5. Tính downstream gap: posterior-mass gap = p^ora-act(θ*) − p^LLM(θ*) (mass trên hypothesis đúng), θ* do environment giấu. Đây là thước end-to-end, ít bị ảnh hưởng độ khó môi trường hơn accuracy tuyệt đối.
6. Leo thang can thiệp 3 bậc, đo lại bước 4–5 mỗi bậc: (a) base; (b) bật reasoning mode; (c) thêm code execution sandbox. Quyết định: reasoning+tools mà KL ≈ 0 và gap ≈ 0 → bỏ strict harness, giữ explicit belief state (trạng thái niềm tin tường minh) lưu DB để nhất quán cross-conversation + human inspection (kiểm tra người); vẫn cao → giữ harness.
7. Audit output code ở bậc (c): reasoning model nhận ra intractable (không giải dạng đóng được) nhưng sẽ hallucinate (bịa) output simulation nếu không có tool thật — kiểm tra code có estimator numerically stable (ổn định về số) không, không chỉ đọc kết quả model report.

## Output mong đợi
- Bảng KL per-step + posterior-mass gap per-step cho 3 bậc can thiệp; verdict: "tin được posterior tự cập nhật" (reasoning+tools pass) hoặc "cần harness" (fail); danh sách vi phạm tiên đề (nếu có).

## Ví dụ áp dụng
- Agent giám sát churn (rời bỏ khách hàng): build thế giới 8 phân khúc khách hàng giả lập với thuộc tính ẩn + 6 phép đo; chạy audit 6 bước → base KL lớn + gap −30%; reasoning KL nhỏ; reasoning+sandbox gap ≈ 0 → production: agent churn lưu bảng posterior 8 phân khúc vào DB, mỗi tuần cập nhật với code sandbox tính posterior, người vận hành đọc belief state trực tiếp.

## Gotchas
- KHÔNG ghép phán đoán xác suất từ nhiều hội thoại riêng lẻ — >50% scenarios Dutch-bookable.
- Non-reasoning model collapse về ~0% trên 20Q-style task mở — đừng kết luận "model dở" mà thiếu reasoning.
- Reasoning-only trên likelihood intractable: model báo số MC nhưng thực chất bịa — bắt buộc code execution thật.
- 20Q-style: oracle dùng chính likelihood tự khai của LLM → audit đo internal consistency (nhất quán nội tại), không phải correctness với thế giới.
- Fixed compute budget khi so base vs reasoning: base chỉ đúng token output probabilities, không cho tự do compute — nếu không kiểm soát, so sánh lệch.
