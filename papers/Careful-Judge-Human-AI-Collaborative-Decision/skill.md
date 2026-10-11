# Skill: CARE — Human-AI Escalation With Risk Control
Source: 2610.09043
Type: framework

## Khi nào dùng skill này
- Có model AI rẻ (cheap AI model) đưa ra quyết định nhị phân (binary decision) quan trọng về an toàn, và expert người đắt tiền phải review.
- Muốn giảm khối lượng review của người mà vẫn đảm bảo rủi ro (risk) dưới một dung sai (tolerance) ε cho trước.
- Model AI được cập nhật theo thời gian và bạn cần gate an toàn (safety gate) track kịp mỗi lần cập nhật.

Tình huống KHÔNG nên dùng:
- Task đa lớp (multi-class) hoặc regression — paper chỉ instantiate binary classification.
- Nhãn oracle (nguồn nhãn) không đáng tin — skill giả định expert luôn đúng.

## Input cần có
- AI model hộp đen (black-box) xuất probability p_A và confidence c_A (có thể overconfident, KHÔNG cần calibrated).
- Một luồng (stream) dữ liệu i.i.d. chưa gán nhãn.
- Human oracle: expert cho nhãn đúng khi được hỏi (mỗi lần hỏi tốn kém).
- Risk tolerance ε (ví dụ 5%) và loss function (zero–one loss hoặc Brier score).
- Fraction chuẩn bị (preparation fraction) 10–40% cho offline phase.

## Các bước thực hiện
1. Chia lịch trình offline–online: offline checkpoints refit lại rectifier và rebuild calibration; giữa checkpoint chạy online.
2. Residual Gauss: đặt GP (Gaussian process — quá trình Gauss) lên residual human–AI ở scale score; mean tuyến tính bắt systematic bias (lệch hệ thống), kernel kết hợp k_ϕ (tương quan residual) với k_A (uncertainty của AI). Fit tham số prior bằng MLE/EM tại checkpoint; online dùng assumed-density filtering (lọc mật độ giả định) sau mỗi label.
3. Confident Jack: hiệu chuẩn threshold escalation (escalation threshold) bằng weighted cross-conformal — trọng số account cho việc label được chọn adaptive — để kiểm soát marginal risk tại MỌI thời điểm, kể cả khi model cập nhật tùy ý.
4. Exacting Gates: chấp nhận decision AI đã hiệu chỉnh chỉ khi rectified confidence c_t > λ_t; nếu không thì escalation cho human.
5. Active Max: chọn query thông tin (epistemic uncertainty cao) để hỏi người, ưu tiên feedback giúp cải thiện decision tương lai.
6. Giám sát: empirical risk so ε và human query rate; nếu risk vượt ε → hạ threshold; nếu query rate cao → kiểm tra kernel GP có bắt được cấu trúc misalignment không.

## Output mong đợi
- Hệ thống decision người–AI: risk thực nghiệm ≤ ε trong mọi region, human query giảm 25–81% so với baseline selective escalation (SE).
- Rectified model ngày càng aligned: error tương đối giảm 15.5–70.5% (HateBench).

## Ví dụ áp dụng
Content moderation: AI duyệt bài viết, expert xử lý case khó. Dùng CARE với ε=5% → auto-approve ~78% bài (chỉ escalation 21.7%) thay vì 57.1% với SE thuần, trong khi risk giữ dưới 5%. Mỗi nhãn expert vừa sửa bias vừa recalibrate gate.

## Gotchas
- Đừng tách label thành 2 piles riêng cho training và calibration (PPI+SE) — tốn 26–48% query hơn; CARE tái dụng chung.
- Đừng dùng raw confidence của AI trực tiếp nếu overconfident: SE/PPI tăng query +28.0pp/+11.8pp khi đổi sang confidence trực tiếp; CARE rectify luôn cả confidence.
- Nếu uncertainty ban đầu > ε mà coi residual independent → query-all degradation; phải model tương quan cục bộ bằng GP kernel.
- Mọi guarantee cần oracle đúng nhãn; expert yếu → toàn bộ pipeline lệch.
