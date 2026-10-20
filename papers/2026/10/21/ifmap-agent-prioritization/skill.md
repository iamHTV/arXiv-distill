# Skill: Ưu tiên agent cần cải thiện bằng influence probing (IF-MAP)
Source: 2610.24383
Type: evaluation-method

## Khi nào dùng skill này
- Multi-agent system (hệ thống đa tác nhân) có nhiều agent, budget (ngân sách) upgrade/tối ưu hạn chế, cần biết đầu tư vào agent nào.
- Cần ranking (xếp hạng) agent theo potential (tiềm năng) cải thiện system-level, không chỉ theo lỗi.
- KHÔNG dùng cho single-agent system hoặc khi có thể nâng cấp mọi agent mà không lo cost (chi phí).

## Input cần có
- Workflow cố định + end-to-end metric (metric đầu-cuối) hoặc loss + probing set (tập dò) representative (đại diện).
- Fixed embedding model (mô hình nhúng cố định) cho prompt.
- Khả năng chạy full system nhiều lần (mỗi probe 1 lần chạy).

## Các bước thực hiện
1. Với mỗi agent i: tạo ≤10 semantic prompt perturbations (nhiễu loạn ngữ nghĩa) — static/adaptive/structure-preserving — giữ role và output interface; loại bản trùng/không dùng được.
2. Mỗi probe: chỉ đổi prompt agent i, chạy full system, ghi loss L(m). Tính signed effect (hiệu ứng có dấu) Δ = L0 − L(m).
3. Embed prompt: displacement v = E(p(m)) − E(p); direction u = v/||v||; y = (L(m) − L0)/||v||.
4. Fit regularized local response model (mô hình phản hồi địa phương chính quy) trong low-dimensional prompt-embedding subspace (không gian con nhúng prompt số chiều thấp).
5. Priority score (điểm ưu tiên) = response norm (chuẩn phản hồi) ước lượng → xếp hạng agent.
6. Dùng budget cho top agent: prompt optimization hoặc model upgrade — KHÔNG nâng cấp mọi agent.

## Output mong đợi
- Bảng xếp hạng agent theo priority score + ước lượng gain (lợi nhuận) macro-average khi cải thiện top agent; so sánh uniform selection làm đường cơ sở.

## Ví dụ áp dụng
- Pipeline hỗ trợ khách hàng 4 agent (phân loại, nghiên cứu, soạn thảo, xác minh): probe 10 biến thể/agent (40 lần chạy), IF-MAP xếp "soạn thảo" cao nhất → upgrade model chỉ agent đó: +9 pp macro (chọn ngẫu nhiên +4 pp), tiết kiệm ~64% target-model tokens.

## Gotchas
- Probe coverage kém → priority sai: perturbation phải đa dạng (static + adaptive + structure-preserving).
- Local linearity giả định — agent có response phi tuyến mạnh thì ước lượng lệch.
- Gain phụ thuộc intervention khả dụng: nếu không thể upgrade model agent đó, priority vô nghĩa — phải kiểm tra alignment với hướng giảm loss.
