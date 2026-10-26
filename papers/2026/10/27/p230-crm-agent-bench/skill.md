# Skill: crm-agent-bench-contract-evaluation

Source: 2610.32004
Type: evaluation-method

## Khi nào dùng skill này

- Đánh giá agent sử dụng công cụ trong môi trường doanh nghiệp có trạng thái.
- Xây dựng hợp đồng thực thi để kiểm tra agent thực hiện đúng quy trình kinh doanh.
- Đo scored coverage, latency và cost của agent.

## Tình huống KHÔNG nên dùng

- Agent chỉ trả lời câu hỏi, không thực hiện hành động trên hệ thống.
- Không có quy tắc nghiệp vụ rõ ràng để viết hợp đồng thực thi.

## Input cần có

- Danh sách các tác vụ kinh doanh đa lượt với trạng thái.
- Các kiểm tra trên hành động, đối số, thứ tự, phản hồi, trạng thái mục tiêu và trạng thái được bảo vệ.
- Môi trường thực thi để chạy agent và thu thập dấu vết.

## Các bước thực hiện

1. Xây dựng hợp đồng thực thi (executable contract) cho mỗi tác vụ: định nghĩa các kiểm tra trên hành động, đối số, thứ tự, phản hồi, trạng thái mục tiêu và trạng thái được bảo vệ.
2. Chạy agent trên mỗi tác vụ, ghi lại toàn bộ dấu vết thực thi.
3. Chấm điểm strict success: thành công là sự kết hợp chặt chẽ của tất cả các kiểm tra được khai báo.
4. Báo cáo scored coverage (tỷ lệ kiểm tra đáp ứng), latency (độ trễ) và cost (chi phí).
5. Phân tích độ tin cậy theo từng miền và chi phí của từng hệ thống agent.

## Output mong đợi

- Điểm strict success cho mỗi agent.
- Scored coverage, latency và cost cho mỗi tác vụ.
- Phân tích độ tin cậy theo miền và chi phí triển khai.

## Ví dụ áp dụng

Đội xây dựng agent CRM nội bộ: trước khi triển khai agent xử lý quy trình chăm sóc khách hàng, hãy viết hợp đồng thực thi cho mỗi tác vụ (ví dụ: "cập nhật thông tin liên hệ" phải gọi đúng công cụ, truyền đúng tham số, không được thay đổi trạng thái bảo vệ như hạn mức tín dụng). Dùng CRM-Agent-Bench để đánh giá agent theo strict success, scored coverage, latency và cost.

## Gotchas

- Strict success yêu cầu TẤT CẢ các kiểm tra được đáp ứng, không chỉ phần lớn.
- Các hệ thống dẫn đầu khác biệt mạnh về chi phí và độ tin cậy theo miền — không có hệ thống nào tối ưu tất cả.
- Trạng thái được bảo vệ (protected state) không được phép agent thay đổi.
- Đánh giá toàn bộ hệ thống agent, không chỉ mô hình ngôn ngữ đơn lẻ.