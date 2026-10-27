# Skill: Vòng tối ưu cấu hình agent bằng insight có điều kiện (conditional-insight routing loop)
Source: 2610.35690 (EvoRouter)
Type: workflow / evaluation-method (bản không cần huấn luyện — thích ứng manual từ expert loop của paper)

## Khi nào dùng skill này
- Hệ thống agent dùng nhiều model (model pool) hoặc nhiều cấu hình MAS (multi-agent system — hệ thống đa tác nhân: collaboration mode — chế độ cộng tác, agent count, interaction rounds, skills) và bạn chưa biết cấu hình nào tối ưu cho loại task nào.
- Chi phí inference (suy luận) tăng nhanh khi mở rộng agent nhưng accuracy (độ chính xác) không tăng tương ứng.
- KHÔNG nên dùng: agent single-model/single-tool (một model, một công cụ) — không có configuration space (không gian cấu hình) để tối ưu; task đồng nhất 100% một loại; không log được cost (chi phí) per execution.

## Input cần có
- Execution log (nhật ký thực thi): mỗi record gồm task type (loại task), difficulty (độ khó), budget (ngân sách), config đã dùng (model, mode, agent count, rounds, skills), outcome (kết quả pass/fail từ verifier — bộ kiểm chứng), cost (FLOPs hoặc token hoặc tiền — chọn 1 đơn vị thống nhất).
- Config catalog (danh mục cấu hình): tất cả model/mode/agent/round/skill khả dụng kèm mô tả.
- Verifier per task type: sandbox test (code), exact-match (QA), rubric đánh giá (nl).
- Reference budget (ngân sách tham chiếu) per task type = cost của config baseline tốt nhất hiện tại.

## Các bước thực hiện
1. Log đủ 3 field quality–cost–config tối thiểu 50–100 executions across task types Trước khi distill gì (single trajectory — dấu vết đơn lẻ không đủ chứng cứ, chính là gap của paper).
2. Định kỳ (weekly), chạy expert LLM (chuyên gia) cảm nạp quy tắc theo 3 bước của paper: (i) rule induction (cảm nạp quy tắc) — so sánh trajectory trong cùng loại task across success/failure và cost spectra để rút quy tắc điều kiện về capability alignment, scaling saturation (bão hòa mở rộng), configuration interaction; (ii) precondition refinement (tinh chỉnh điều kiện tiên quyết) — khi 2 quy tắc mâu thuẫn, siết boundary (thêm dimension độ khó/domain); (iii) capacity pruning (cắt tỉa dung lượng) — gộp quy tắc trùng, giữ ceiling ~20 quy tắc để tránh context inflation (phình ngữ cảnh).
3. Mỗi quy tắc MUST có dạng "IF <điều kiện task> THEN <config>" kèm applicability condition (điều kiện áp dụng) tường minh — KHÔNG có quy tắc vô điều kiện (Insight 1: benefit đảo ngược theo task type).
4. Routing policy (chính sách định tuyến) thủ công: task mới → match conditions của quy tắc → dùng config đó; no-match → config default rẻ nhất + log để bổ sung sau.
5. Thiết kế cost penalty (phạt chi phí) theo paper: penalty = log2(1 + cost/budget); quy tắc chọn config chỉ hợp lệ khi success rate (tỷ lệ thành công) của nó cao hơn failed — tức ưu tiên "thành công với giá rẻ" hơn "thành công bằng mọi giá".
6. Sau mỗi batch (lô) ~50 executions: re-verify (kiểm chứng lại) từng quy tắc against outcome mới; quy tắc stale (lỗi thời) → prune; pattern mới → đưa vào bước 2.

## Output mong đợi
- Ruleset (tập quy tắc) {điều kiện → cấu hình} với avg accuracy + avg cost đo được per rule, + config default cho no-match, + log saturation point (điểm bão hòa) rounds/agents per task type.

## Ví dụ áp dụng
- Agency content workflow: log 120 bài (blog/social/email) × 3 cấu hình → quy tắc "IF social AND độ dài <300 từ THEN 1 agent nhỏ + IO (input-output); IF blog AND need data THEN 2 agent + Debate"; Áp dụng → accuracy giữ nguyên nhưng cost giảm ~40% theo analog 50.95% của paper.

## Gotchas
- KHÔNG tin outcome 1 lần chạy: paper chỉ ra 1 trajectory chỉ phản ánh 1 cấu hình cụ thể — cần ≥5-10 runs per cell trước khi rút quy tắc.
- Scaling KHÔNG tỉ lệ: rounds/agents tăng có saturation point (Insight 2) — đặt cap mặc định (ví dụ 3 rounds), mở only khi verifier fail.
- Ranking model composition đảo ngược theo collaboration mode (Insight 3) — test tổ hợp, không test từng thành phần riêng lẻ.
- Insight cũ mâu thuẫn insight mới → phải có bước precondition refinement, nếu không policy bị nhiễu 2 chiều.
- Đơn vị cost phải thống nhất (đừng trộn token với tiền trong 1 log).
