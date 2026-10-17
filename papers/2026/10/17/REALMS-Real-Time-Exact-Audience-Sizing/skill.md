# Skill: realms-schema-aware-nl2sql-audience-sizing
Source: 2609.30547v1
Type: framework

## Khi nào dùng skill này
- Cần xây dựng hệ thống truy vấn dữ liệu khách hàng bằng ngôn ngữ tự nhiên (conversational analytics) trên schema doanh nghiệp phức tạp, lồng nhau (nested schema).
- Muốn tính toán chính xác số lượng khán giả (exact audience sizing) thay vì ước tính bằng sampling hay mô hình dự đoán.
- Có dữ liệu hồ sơ khách hàng lớn (triệu hồ sơ, nghìn thuộc tính) và cần trả lời trong thời gian thực (giây, không phải giờ).

## Tình huống KHÔNG nên dùng
- Dữ liệu không có cấu trúc schema rõ ràng (ví dụ: văn bản tự do, hình ảnh).
- Không cần đếm chính xác, chỉ cần ước tính gần đúng là đủ.
- Không có nguồn dữ liệu khách hàng doanh nghiệp để chuẩn hóa scheme.

## Input cần có
- Hồ sơ khách hàng (profile data) từ nhiều nguồn (web, giao dịch, ngoại tuyến) với schema khác nhau.
- Danh sách yêu cầu truy vấn khán giả bằng ngôn ngữ tự nhiên.
- Trình lấy văn bản (retriever) có thể tính nhúng và tìm kiếm vector.
- Mô hình LLM để sinh SQL.
- Cơ sở dữ liệu phân tích có thể mở rộng để lưu biểu diễn cột.

## Các bước thực hiện
1. Tiền xử lý ngoại tuyến: xuất hồ sơ phân cấp từ nền tảng dữ liệu nguồn, làm phẳng sang biểu diễn cột (columnar representation), lưu trong cơ sở dữ liệu phân tích có thể mở rộng.
2. Tạo nhúng (embedding) cho schema attributes và xây dựng chỉ mục vector để tìm kiếm ngữ nghĩa.
3. Tại thời gian chạy: mã hóa truy vấn người dùng thành nhúng Dense, lấy thuộc tính scheme liên quan thông qua truy xuất ngữ nghĩa (schema-aware attribute retrieval).
4. Xây dựng prompt bằng ngữ cảnh scheme đã lấy và mẫu truy vấn có thể tái sử dụng (template-based in-context learning).
5. Dùng LLM dịch định nghĩa khán giả bằng ngôn ngữ tự nhiên thành truy vấn SQL thực thi được qua cấu trúc scheme lồng nhau.
6. Chuẩn hóa scheme: chuẩn hóa dữ liệu vào biểu diễn cột thống nhất, trừu tượng hóa sự khác biệt theo nguồn.
7. Thực thi truy vấn SQL trên cơ sở dữ liệu phân tích, trả về số lượng khán giả chính xác.
8. Tạo bản giải thích ngôn ngữ tự nhiên ngắn gọn kèm kết quả.

## Output mong đợi
- Hệ thống trả lời truy vấn khán giả bằng ngôn ngữ tự nhiên với số lượng chính xác, độ trễ dưới 10 giây trung bình.
- Recall@k 94%, Exact-match 93% cho lấy thuộc tính scheme; Execution match 90% cho sinh SQL.

## Ví dụ áp dụng
- Đội ngũ marketing muốn biết "Có bao nhiêu hồ sơ đã thăm ứng dụng di động trong 6 tháng qua và lớn hơn 30 tuổi?": dùng REALMS để lấy thuộc tính scheme liên quan (app_visit, age), sinh SQL đếm chính xác, trả về kết quả trong vài giây thay vì hàng giờ bằng cách tiếp cận sampling.

## Gotchas
- Hệ thống triển khai trên nền tảng dữ liệu khách hàng doanh nghiệp cụ thể; kết quả có thể không chuyển tiếp trực tiếp đến các môi trường khác.
- Chuẩn hóa scheme là bắt buộc cho triển khai độc lập ngành.
- Khi schema thay đổi, cần cập nhật chỉ mục nhúng và bộ mẫu truy vấn, có thể tốn chi phí lưu trữ và xử lý.
