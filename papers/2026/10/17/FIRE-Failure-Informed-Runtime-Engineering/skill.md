# Skill: fire-runtime-policies-for-agent-reliability
Source: 2609.26048v1
Type: framework

## Khi nào dùng skill này
- Agent đã có giải pháp hoạt động nhưng thất bại trong việc triển khai lại (delivered success) do lỗi thủ tục (procedural loss).
- Cần thêm tầng điều khiển nhẹ (lightweight harness layer) để bảo vệ khả năng model đã có, không cần retrain hay thay đổi prompt người dùng.
- Có thể quan sát được trạng thái thất bại trước khi verifier đánh giá (có observable pre-verifier intervention point).

## Tình huống KHÔNG nên dùng
- Thất bại do model thiếu năng lực hoặc kiến thức domain (không phải mất mát thủ tục).
- Không có trạng thái trung gian có thể quan sát trước khi verifier chạy.
- Muốn áp dụng trước khi biết các mode thất bại cụ thể (chính sách được suy luận từ thất bại đã quan sát).

## Input cần có
- Agent harness có thể can thiệp tại sự kiện: nộp prompt, trước mỗi lệnh gọi công cụ (before-tool-call), khi agent cố dừng (stop attempt).
- Nhiệm vụ có verifier (trình xác minh) trả về pass/fail rõ ràng.
- Nhật ký hành động (action history) và trạng thái chính sách (policy state) có thể truy xuất.
- Danh sách nhiệm vụ với mô tả để viết điều kiện đủ điều kiện (eligibility predicate).

## Các bước thực hiện
1. Chạy agent hai lần trên mỗi nhiệm vụ mà không có chính sách (policy-free), ghi lại từng lần thử.
2. Kiểm tra những nhiệm vụ thất bại một trong hai lần (1/2) và thất bại cả hai (0/2) để tìm bỏ sót thủ tục rõ ràng (concrete procedural omission).
3. Loại bỏ lỗi do nhà cung cấp (provider), lỗi trình xác minh (verifier), thiếu năng lực, và thất bại không có điểm can thiệp quan sát được.
4. Nhóm các thất bại theo cơ chế (mechanism) thay vì theo nhiệm vụ, đăng ký chuỗi: trạng thái → can thiệp → hành động → điều kiện verifier.
5. Viết predicate không ghi tên nhiệm vụ, kiểm tra ứng cử viên trên nhiệm vụ dương và gần-am (nearby-negative).
6. Sửa hoặc nghỉ hưu (retire) ứng cử viên vô dụng, quá rộng (over-broad), hoặc gây hại.
7. Chỉ thêm chính sách vào danh sách đóng băng (frozen portfolio) khi có: trạng thái thất bại quan sát được, kết quả tập trung tích cực, và kiểm tra định tuyến (routing audit) thỏa đáng.
8. Đóng băng mã nguồn, định tuyến, và quy tắc phân tích.

## Output mong đợi
- Danh sách chính sách đóng băng (frozen policy portfolio) có các quy tắc rõ ràng, mỗi quy tắc bao gồm điều kiện đủ điều kiện, điều kiện thời gian chạy, và hành động can thiệp.
- Giảm thất bại do mất mát thủ tục, tăng pass∧2 (lặp đi lặp lại thành công trên hai lần thử) mà không đổi pass@2 nhiều.

## Ví dụ áp dụng
- Nhiệm vụ gRPC server: agent khởi chạy server trong phiên làm việc (session) rồi dừng, server chết cùng phiên. Chính sách kích hoạt tại sự kiện stop: hướng dẫn agent khởi chạy lại server tách khỏi phiên (detached session) với luồng tiêu chuẩn được chuyển hướng, sau đó chạy lệnh kiểm tra (probe) từ một lệnh gọi công cụ sau.

## Gotchas
- Chính sách chỉ xử lý mất mát thủ tục (procedural loss), không cung cấp giải thuật hoặc kiến thức domain bị thiếu.
- Nội dung chính sách quan trọng hơn thời điểm kích hoạt — hướng dẫn chung chung như "xem lại công việc" không cải thiện kết quả.
- Danh sách chính sách là riêng cho từng model (model-specific portfolio), không chuyển tiếp trực tiếp giữa các tier.
- Việc xây dựng chính sách đòi hỏi quan sát thất bại trước (không thể áp dụng trước khi biết mode thất bại).
