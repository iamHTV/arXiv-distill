# [2610.09043] Careful Judge: Ra quyết định hợp tác người–AI an toàn và hiệu quả

## Problem
Prior work có 2 nhánh, không nhánh nào giải quyết đồng thời an toàn + hiệu quả: (1) selective escalation (chuyển có chọn lọc) với conformal prediction (hiệu chuẩn đảm bảo coverage) đảm bảo an toàn nhưng KHÔNG học từ feedback → model lệch (biased) phải chuyển gần như mọi human query (lượt hỏi chuyên gia) khi risk tolerance (dung sai rủi ro) nhỏ; (2) các method học từ human feedback (RLHF, prediction-powered inference/PPI) cải thiện hiệu quả nhưng KHÔNG có safety guarantee → học adaptive vô hiệu hóa guardrail đã hiệu chuẩn. Kết hợp naïve hai nhánh còn tệ hơn: chia sẻ feedback khan hiếm khiến học nhiễu hơn, an toàn bảo thủ hơn.

## Contribution
- Formalize human-AI collaboration thành bài toán statistical decision với lịch trình offline–online linh hoạt.
- Phân rã rủi ro Brier chính xác thành 4 nguồn — aleatoric ambiguity (mơ hồ ngẫu nhiên, không khử được), excess risk (rủi ro dư), epistemic uncertainty (bất định tri thức, học được), systematic bias (lệch hệ thống) — mỗi nguồn thúc đẩy 1 module.
- Residual Gauss: rectifier (bộ hiệu chỉnh) Bayesian GP (Gaussian process — quá trình Gauss) lan truyền feedback qua các trường hợp tương tự.
- Confident Jack: hiệu chuẩn cross-conformal có trọng số, kiểm soát rủi ro tại MỖI thời điểm, tái dùng label đã chọn adaptive, chịu được mọi cập nhật model hộp đen (black-box).

## Method
Pipeline 4 module: (1) Residual Gauss fit GP lên residual human–AI — mean tuyến tính bắt lệch hệ thống, kernel bắt tương quan cục bộ; (2) Confident Jack hiệu chuẩn escalation threshold (ngưỡng chuyển người); (3) Exacting Gates: chấp nhận decision AI đã hiệu chỉnh chỉ khi confidence đã hiệu chỉnh > threshold; (4) Active Max chọn query thông tin để hỏi người. Giữa checkpoint online dùng assumed-density filtering (lọc mật độ giả định); offline refit lại rectifier + calibration.

## Key Findings
- 4 dataset an toàn-critical thật: nuPlan (lái xe, 10,000 stream), HateBench (hate speech, 7,054), iSafetyBench (hazard video, 1,100), ASIMOV (robot tool, 1,437).
- iSafetyBench tại tolerance 5%: CARE chuyển 21.7% query vs SE 57.1% (−62%).
- HateBench: tiết kiệm query 49–66% vs SE, 26–48% vs PPI+SE; giảm error tương đối 15.5–70.5% trên 8 model hộp đen (error thô 14.5–44.7%).
- Tổng: giảm 25–81% human query vs baseline. SE/PPI tăng query +28.0pp/+11.8pp khi đổi sang confidence trực tiếp (overconfident); CARE ổn định.

## Actionable Insights
- Route review by risk, not confidence: đặt confidence gate ở tolerance ε; content moderation có thể auto-approve ~78% thay vì ~43%.
- Tái dùng mỗi label chuyên gia cho CẢ cải thiện model lẫn hiệu chuẩn gate — đừng chia label khan hiếm thành 2 piles riêng biệt.
- Model tương quan cục bộ (GP kernel) để 1 correction sửa cả neighborhood: 1 giao lộ flagged → sửa các giao lộ tương tự.

## Assumptions & Limitations
- Binary classification; stream i.i.d.; oracle (nguồn nhãn đúng) luôn chính xác.
- Hiệu quả cao nhất khi AI đã train tốt và misalignment có cấu trúc rõ ràng.
- Paper KHÔNG có mục Limitations; chưa test multi-class, regression, stream non-stationary.
- GP feature dim tối đa 256 trong experiment — scaling feature rất cao chưa kiểm chứng.

## Metadata
- Năm 2026, arXiv 2610.09043, category stat.ML (cs.AI, cs.LG), PDF: https://arxiv.org/pdf/2610.09043, citation: không tìm được (submitted 6 Oct 2026).
