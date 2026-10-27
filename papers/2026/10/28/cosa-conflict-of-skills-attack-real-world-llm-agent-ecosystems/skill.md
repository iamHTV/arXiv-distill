# Skill: Kiểm toán thành phần kỹ năng agent (agent skill composition audit)
Source: 2610.35082 (CoSA)
Type: workflow / evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Trước khi thêm Skill/plugin mới vào agent đang có sẵn pool Skill (tập hợp kỹ năng) — đặc biệt agent có thao tác write/send/execute (ghi, gửi, thực thi) thật.
- Khi nâng cấp agent bằng cách bổ sung capability (năng lực) từ marketplace (chợ kỹ năng, ví dụ Kiểu ClawHub) hay do team tự viết.
- KHÔNG nên dùng: agent single-tool (một công cụ duy nhất) không ghép Skill; task không có policy (quy tắc hành vi) ràng buộc gì để vi phạm; không có sandbox (môi trường cách ly) để chạy thử an toàn.

## Input cần có
- Inventory (bảng kê) Skill hiện tại: business function (chức năng nghiệp vụ), inputs/outputs (đầu vào/ra), permissions (quyền), side effects (hiệu ứng phụ), assessment signals (tín hiệu đánh giá/quyết định nó phát ra), authorization conditions (điều kiện được phép), role trong 6 vai trò: READ, TRANSFORM, ASSESS, EXTERNALIZE, MUTATE, EXECUTE.
- Candidate (Skill ứng viên) định thêm + kết quả pass scanner kiểm tra đơn lẻ.
- 10–20 task đại diện với request (yêu cầu), initial state (trạng thái đầu), policy Γ (quy tắc) cố định.
- Sandbox với controlled services (dịch vụ kiểm soát) để ghi nhận side effect thật; violation rubric (bảng tiêu chí vi phạm): DL=data leakage (rò rỉ dữ liệu), UA=unauthorized state modification (đổi trạng thái không phép), UE=unsafe execution (thực thi không an toàn).

## Các bước thực hiện
1. Kê contract (hợp đồng thao tác) từng Skill hiện tại theo Input trên; đánh dấu các cặp handoff (bàn giao) nơi output của Skill A (artifact — sản phẩm trung gian, hoặc decision signal — tín hiệu quyết định) làm input cho Skill B.
2. Với mỗi handoff, kiểm tra xem authorization (sự cho phép) và restriction (điều kiện giới hạn) của mục đích gốc có được mang theo khi tái sử dụng không; đánh dấu 4 cơ chế rủi ro: security-context attenuation (suy giảm ngữ cảnh bảo mật), semantic interface bridging (cầu nối giao diện ngữ nghĩa), semantic authority promotion (thăng quyền ngữ nghĩa), target/action binding drift (trôi dạt liên kết đích–hành động).
3. Phân loại candidate: capability supplementation (bổ sung năng lực còn thiếu) hay relationship reshaping (tái cấu trúc quan hệ giữa các Skill); dự đoán cơ chế nào có thể kích hoạt khi ghép.
4. Chạy paired test (kiểm thử đôi): cùng 10–20 task, 2 cấu hình pool V (gốc) vs V∪I (gốc+candidate), autonomous Skill selection (agent tự chọn kỹ năng), model/tools/permissions cố định; mỗi task nên chạy ≥2 lần để có ước lượng variance (phương sai).
5. Judge (phán xét) trajectory (dấu vết thực thi): chỉ đếm vi phạm khi có hiệu ứng cụ thể (nội dung cấm đến đích, thay đổi persistent — lâu dài — không phép, workload — khối công việc — không phép khởi chạy); tính ∆violation rate (chênh lệch tỷ lệ vi phạm) = augmented − baseline; trong các run vi phạm, tìm witness (bằng chứng): chuỗi thao tác ≥2 Skill có reuse thật (không chỉ thứ tự thời gian).
6. Nếu ∆violation > 0: hoặc loại candidate, hoặc cài pre-action hook (móc trước hành động) trước mọi externalize/mutate/execute — kiểm provenance (nguồn gốc) của payload và authorization gắn action+target cụ thể, trả ALLOW/BLOCK/CONFIRM (cho phép/chặn/yêu cầu xác nhận).

## Output mong đợi
- Go/no-go (đồng ý/từ chối) cho candidate kèm ∆violation rate đo được, danh sách cross-Skill dependency (phụ thuộc liên kỹ năng) rủi ro, và spec (đặc tả) pre-action gate (cổng kiểm tra trước hành động) nếu giữ candidate.

## Ví dụ áp dụng
- Thêm skill "soạn invoice (hóa đơn)" vào agent CSKH: chạy 15 ticket giống nhau ở 2 cấu hình → phát hiện agent dùng artifact "lịch sử thanh toán" từ skill finance để soạn invoice gửi khách mà không có approval flag (cờ phê duyệt) → ∆violation +20% → cài gate: node gửi email phải xác minh approval flag trước khi externalize (đưa ra ngoài).

## Gotchas
- Retrieval rate (tần suất Skill được gọi) KHÔNG phải proxy (chỉ báo thay thế) an toàn: tương quan yếu với mức tăng rủi ro (r=0.058 trong paper).
- Pass scanner đơn lẻ ≠ an toàn khi ghép: trong paper, severe-alert count (số cảnh báo nghiêm trọng) không đổi trong khi vi phạm +23.43 percentage point (điểm phần trăm).
- DL (rò rỉ dữ liệu) thường là risk category tăng nhất — ưu tiên test handoff liên dữ liệu khách hàng.
- Đừng judge bằng "agent có làm task xong không": functional success (thành công chức năng) có thể đồng thời tồn tại với vi phạm policy.
