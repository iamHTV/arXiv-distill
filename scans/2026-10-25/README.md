# Báo cáo distill arXiv — ngày 2026-10-25

Tổng hợp 5 bài paper đã distill hôm nay (chọn từ top 10 bài tốt nhất của scan arXiv).
Mỗi bài đã qua 6 bước distill, commit+push GitHub.

## Tổng quan
- Tổng bài distill: **5**
- Tất cả đều có ứng dụng thực tế cho doanh nhân làm một mình (solopreneur).

## Danh sách 5 bài đã distill hôm nay

### [1] Extending FunctionGemma: Điều khiển Android cục bộ bằng mô hình gọi hàm nhỏ (arXiv 2609.25373v2)
- Làm gì: Mở rộng mô hình FunctionGemma (270 triệu tham số / tham số là biến nhớ trong mô hình AI, càng nhiều càng nặng) để điều khiển thiết bị Android cục bộ (chạy ngay trên điện thoại, không gửi lên đám mây) như bật đèn pin, gửi tin nhắn, mở ứng dụng, chụp ảnh — thay vì chỉ gọi API web (đường dẫn mà ứng dụng gọi để lấy dữ liệu).
- Học được gì: Mô hình nhỏ đạt 76.5% độ chính xác trên 15 danh mục hành động thiết bị, chỉ cần khoảng 9.500 mẫu dữ liệu tổng hợp (dữ liệu do máy tạo), không cần gọi mô hình đám mây lớn cho mỗi yêu cầu. Độ chính xác tăng từ 29.3% (mô hình gốc) lên 76.5% (+47.2 điểm).
- Áp dụng cho bạn: Xây một trợ thủ trên điện thoại tự thực hiện các hành động cố định (mở app Zalo, soạn tin, lưu liên lạc, đặt lịch gọi lại) mà không gửi tin nhắn khách hàng lên server đám mây — phù hợp bảo mật dữ liệu khách. Vì 76.5% nghĩa là khoảng 1 lệnh trên 4 bị sai, hãy yêu cầu xác nhận trước các thao tác liên quan tiền (mã giảm giá, xác nhận đơn) và đo độ chính xác theo từng loại hành động thay vì một điểm tổng quát.

### [2] SPRA: Biểu diễn bài báo có cấu trúc cho tác tử AI (arXiv 2610.21424v2)
- Làm gì: Biến bài báo nghiên cứu thành các đối tượng có cấu trúc (vấn đề, đóng góp, thành phần, thiết lập thí nghiệm, thước đo, kết quả) với quan hệ gán nhãn giữa chúng, giúp tác tử AI tra cứu, duyệt và tái sử dụng nội dung bài báo mà không cần đọc toàn văn.
- Học được gì: Giảm 28.5% token (đơn vị xử lý văn bản của AI) so với truy xuất đoạn văn và 95.3% so với văn bản đầy đủ; đạt điểm đánh giá ngữ nghĩa 2.342/5, vượt cơ sở truy xuất đoạn văn 1.961/5. Khoản dữ liệu có hơn 1 triệu bài báo AI, 19,95 triệu đơn vị nghiên cứu và 24,07 triệu quan hệ.
- Áp dụng cho bạn: Thay vì lưu toàn văn tài liệu, hãy trích xuất 6 vai trò (vấn đề, đóng góp, thành phần, thiết lập, thước đo, kết quả) và quan hệ giữa chúng để trợ thủ AI tra cứu nhanh và xác minh nguồn — giảm chi phí xử lý văn bản và trả lời chính xác hơn về vấn đề kinh doanh hay luật.

### [3] Agentic RAG cho quy trình bán lẻ doanh nghiệp trên nhiều nguồn dữ liệu (arXiv 2610.25096v1)
- Làm gì: Xây dựng RetailRAG, hệ thống RAG tự hành (tự quyết định tìm kiếm và tổng hợp thông tin từ nhiều nguồn) nhận thức bán lẻ, định tuyến truy vấn qua nhiều nguồn dữ liệu (bảng có cấu trúc + văn bản không cấu trúc) thay vì ném hết vào một kho dữ liệu duy nhất.
- Học được gì: RetailRAG đạt điểm LLM-judge (điểm đánh giá do AI chấm, thang 0-1) 0.429 trung bình, vượt cơ sở mạnh nhất HetaRAG (0.336), và dùng ít hơn 3 lần gọi API (lần gọi mô hình AI, mỗi lần tốn chi phí) (7.45 vs 25.21) trên benchmark (bộ bài kiểm tra chuẩn) RetailBridge với 1.680 truy vấn đa nguồn. Kết nối bằng chứng qua nhiều nguồn là điểm yếu dominant (bẫy cấu trúc khiến hệ thống thất bại nhất) của tác tử bán lẻ.
- Áp dụng cho bạn: Thay vì ném toàn bộ thông tin sản phẩm, lịch sử chat khách và bảng giá vào một prompt (lệnh nhắc: hướng dẫn gửi cho AI) AI, hãy sắp xếp dữ liệu theo từng "thùng" (danh mục sản phẩm, đánh giá khách, chính sách) và để AI biết nên tìm trong thùng nào cho từng loại câu hỏi — trả lời chính xác hơn và tốn ít chi phí gọi API hơn.

### [4] Business Arena: Đánh giá tác tử LLM trong mô hình chợ mua bán thực tế (arXiv 2608.08621)
- Làm gì: Xây dựng môi trường mô phỏng cửa hàng bán xuyên biên giới để đánh giá 15 mô hình LLM chạy doanh nghiệp theo thời gian dài (nhập hàng, định giá, phục vụ khách hàng, tuân thủ quy định).
- Học được gì: Trị giá ròng cuối cùng dao động từ 20.856 USD đến 188.488 USD (khoảng cách 9.0×); 51% lần chạy lỗ tiền; chỉ 4 mô hình bảo toàn vốn; chiến lược chuyên gia đạt 436.195 USD (gấp hơn 2 lần mô hình tốt nhất). Đánh giá đa chiều (dòng tiền, tránh gian lận, dịch vụ khách hàng, tuân thủ) quan trọng hơn một điểm tổng quát.
- Áp dụng cho bạn: Khi thuê hoặc đánh giá một tác tử AI cho doanh nghiệp của bạn, đừng chỉ nhìn một số liệu tổng hợp — hãy đo riêng rẽ năng lực giữ vốn, định giá sản phẩm, chăm sóc khách hàng và tuân thủ quy định để biết tác tử mạnh hay yếu ở đâu.

### [5] E-Commerce Bench: Đánh giá tác tử bán hàng tự động trên một năm (arXiv 2608.30730v1)
- Làm gì: Xây dựng benchmark mã nguồn mở đầu tiên để đánh giá tác tử hoạt động cửa hàng thương mại điện tử một năm (365 ngày), kết hợp đàm phán đối tác, sự kiện động và quản lý đa cửa hàng.
- Học được gì: Hệ số 1,264 giữa mô hình tốt nhất và kém nhất; một mô hình đạt tài sản cuối năm 1.431.425 Yuan (14,3× vốn) nhưng xếp hạng 16/18 về tránh gian lận; không mô hình nào đứng đầu mọi chiều, nên cần chẩn đoán đa chiều thay vì một điểm số duy nhất.
- Áp dụng cho bạn: Khi đánh giá một trợ thủ bán hàng tự động, hãy thiết lập một môi trường thử nghiệm cố định (giống hệt nhau cho mỗi lần chạy) và đo nhiều chiều (lợi nhuận, tránh nhà cung cấp gian lận, dòng tiền, học hỏi từ kinh nghiệm) thay vì chỉ nhìn một con số, để tránh bị đánh lừa bởi may rắn hoặc điểm tổng quát che điểm yếu.

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN
1. Mô hình nhỏ chạy trên thiết bị có thể tự điều khiển các hành động cố định (mở app, gửi tin) mà không gửi dữ liệu khách hàng lên đám mây — nhưng chỉ đúng khoảng 76.5%, nên xác nhận trước thao tác liên quan tiền.
2. Thay vì ném toàn bộ dữ liệu vào một prompt AI, hãy sắp xếp theo từng loại và định nguồn tìm kiếm — trả lời chính xác hơn, tốn ít chi phí gọi API hơn.
3. Đánh giá tác tử AI doanh nghiệp qua nhiều chiều (giữ vốn, định giá, chăm sóc khách, tuân thủ) thay vì một điểm tổng quát — tránh che điểm yếu quan trọng.
4. Thiết lập môi trường thử nghiệm cố định (giống nhau mỗi lần) khi đánh giá trợ thủ bán hàng, để sự khác biệt kết quả do chính sách tác tử chứ không phải may rắn.
5. Trích xuất cấu trúc tài liệu (vấn đề, đóng góp, kết quả...) thay vì lưu toàn văn để trợ thủ tra cứu nhanh và xác minh nguồn, giảm chi phí xử lý văn bản.
