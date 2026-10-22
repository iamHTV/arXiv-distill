# Skill: Điều phối công cụ cho agent đa domaine định lượng (methane framework)
Source: 2608.18473
Type: framework

## Khi nào dùng skill này
- Cần tự động hóa quy trình đa bước có thành phần định lượng (phân tích dữ liệu trường, báo cáo doanh nghiệp).
- Có các thao tác xử lý xác định (deterministic routines) hiện có cần điều phối.
- Dữ liệu nhạy cảm cần xử lý cục bộ.
- KHÔNG dùng khi cần quyết định tự động cuối cùng mà không xem xét con người, hoặc khi mô hình phân tán không phù hợp với môi trường.

## Input cần có
- Lệnh tự nhiên từ người dùng hoặc file dữ liệu (CSV).
- Các thao tác xử lý cảm biến và mô hình vật lý hiện có.
- Nguồn dữ liệu khí tượng (API hoặc dữ liệu cục bộ).
- Mô hình LLM cục bộ (Llama 3.1 8B, Qwen 30B, Qwen-VL 8B qua Ollama).

## Các bước thực hiện
1. Xây dựng lớp nhập dữ liệu: nhận lệnh tự nhiên hoặc file CSV, chuyển thành規格 công việc có cấu trúc (Request Parser + Task Classifier).
2. Xây dựng lớp điều phối (Agent Router): chuyển yêu cầu đến agent và công cụ phân tích phù hợp.
3. Xây dựng lớp lập kế hoạch trutica: trích xuất thời gian, vị trí mục tiêu, loại cơ sở; lấy điều kiện khí tượng; ước kê khu vực dưới gió.
4. Xây dựng lớp phân tích dữ liệu: tiền xử lý đo đạc (đơn vị, nền), áp dụng mô hình cột feather Gaussian stead-state cho định vị nguồn và ước lực phát thải.
5. Xây dựng lớp hỗ trợ quyết định và báo cáo: Validity Agent tính điểm số độ tin cậy từ các yếu tố chẩn đoán; Report Generator Agent tạo báo cáo có thể chỉnh sửa.
6. Triển khai cục bộ: giữ dữ liệu nhạy cảm trong môi trường tính toán cục bộ, truy xuất dịch vụ bên ngoài chỉ khi cần.

## Output mong đợi
- 92.0% độ chính xác điều phối quy trình, 85.0% thành công ước lực phát thải/dự báo cột feather, 95.0% thành công tạo báo cáo.
- Thời gian quy trình từ cấp giờ xuống cấp phút.
- Điểm số báo cáo trung bình 9,0/10.

## Ví dụ áp dụng
- Hệ thống phân tích dữ liệu cảm biến trường doanh nghiệp: agent LLM điều phối các thao tác xử lý dữ liệu xác định, tạo báo cáo có thể chỉnh sửa, dữ liệu giữ cục bộ không gửi lên đám mây.

## Gotchas
- Định vị nguồn kém trong môi trường đông kết cấu (cơ sở xử lý nước thải 50%) — cần xem xét của con người.
- Kết quả là thông tin hỗ trợ quyết định, không phải quyết định tự động cuối cùng.
- Phụ thuộc vào chất lượng đo đạc và mô hình phân tán dưới-jacent.