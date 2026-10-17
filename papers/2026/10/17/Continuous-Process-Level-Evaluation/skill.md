# Skill: continuous-process-level-evaluation
Source: 2610.01833v1
Type: framework

## Khi nào dùng skill này
- Kỹ năng agent doanh nghiệp được sửa đổi liên tục (tool API thay đổi, phiên bản LLM cập nhật, spec tinh chỉnh từ phản hồi vận hành).
- Cần phát hiện sai lệch hành vi quy trình (process-level behavioral drift) dù kết quả đầu ra cuối cùng vẫn đúng.
- Có thể gọi lại API thực qua đường dẫn độc lập để tính căn cứ thực sự (ground truth).

## Tình huống KHÔNG nên dùng
- Kỹ năng có đầu ra không phải định lượng (non-quantitative output) không thể kiểm tra bằng con số.
- Không có cách gọi API thực độc lập để tính ground truth.
- Không cần đánh giá liên tục qua nhiều lần sửa đổi spec.

## Input cần có
- Kỹ năng agent với spec rõ ràng (SKILL.md hoặc Skill.txt).
- Danh sách test case mẫu (template test cases) mô tả hành vi mong muốn.
- Connector gọi API thực qua đường dẫn độc lập (standalone script).
- Agent harness có thể cung cấp dấu vết gọi công cụ (tool-call trace): tool name, arguments, return value, turn index.
- Trình xác minh (verifier) hoặc quy trình review người dùng cho lỗi gốc.

## Các bước thực hiện
1. Thêm dòng vào bước đầu của spec skill để agent ghi lại tất cả tham số đầu vào (portfolio, khoảng thời gian, doanh thu) vào log có cấu trúc.
2. Bắt toàn bộ dấu vết gọi công cụ từ harness execution log: tên công cụ, đối số, giá trị trả về, chỉ số lượt trò chuyện.
3. Chạy script Python độc lập gọi cùng API thực qua đường dẫn thực thi riêng, tính giá trị dự kiến cho mỗi ứng dụng (ground truth).
4. Viết template test case dùng chỗ trống giải quyết tại runtime (ví dụ: $k8s_host_date_calls) thay vì giá trị hardcode; mở rộng template thành các kiểm tra hiện diện, đối số, phạm vi, thực thi, dư thừa, số lần gọi.
5. Định nghĩa liên kết phụ thuộc (depends_on) giữa các test case để phân biệt thất bại gốc và hiệu ứng cascading.
6. Đánh giá theo ba lớp: L1 giá trị số cuối cùng định trước, L2 bảy kiểm tra trạng thái cuối cùng per skill, L3 kiểm tra quỹ đạo trên 4 chiều: tool selection, tool arguments, tool ordering, argument scope.
7. Dùng LLM judge chỉ cho các kiểm tra dễ gãy khi khớp chính xác không ổn định; thực hiện so sánh số qua calculator tool.
8. Khi kiểm tra thất bại, đi qua đồ thị phụ thuộc để phân biệt lỗi gốc từ thất bại cascading; báo cáo gốc với các hậu quả cascading để giảm tập đánh giá ban đầu.

## Output mong đợi
- Pipeline đánh giá liên tục phát hiện sai lệch quy trình dù kết quả cuối đúng.
- Giảm số lượng kiểm tra thất bại cần chẩn đoán ban đầu (từ trung bình 6.34 xuống 2.65 gốc, −58%).
- Test case mẫu tái sử dụng qua các spec, model, và harness khác nhau.

## Ví dụ áp dụng
- Kỹ năng phân bổ doanh thu (Revenue Apportionment): khi spec được rút gọn hoặc API công cụ thay đổi, model thay đổi hành vi ở các bước mơ áng nhưng con số cuối vẫn đúng. Thêm kiểm tra quy trình: bắt buộc trình tự giai đoạn (fetch → stage → readback → allocate → write), kiểm tra đối số ngày tháng và bộ lọc bằng ràng buộc kiểu, kiểm tra phạm vi gọi công cụ trên mỗi cluster và host.

## Gotchas
- Khung chỉ đánh giá một hệ thống enterprise duy nhất và hai kỹ năng liên quan; khái quát hóa đến các loại kỹ năng khác vẫn chưa rõ.
- 10 lần thử mỗi ô hạn chế sức mạnh thống kê cho hiệu ứng nhỏ.
- Nhãn gốc không được độc lập xác nhận là giải thích nhân quả (mô tả, không phải nhân quả xác thực).
- LLM judge chỉ bổ sung, không thay thế, bộ kiểm tra chương trình và không phát hiện các lệnh gọi ứng viên.
