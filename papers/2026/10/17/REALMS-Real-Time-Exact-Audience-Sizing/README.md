# [2609.30547v1] REALMS: An AI-Assistant Conversational System for Real-Time Exact Audience Sizing over High-Dimensional Nested Profiles

## Problem
- Quy ước kích thước khán giả (audience sizing) là thành phần quan trọng của marketing số nhưng các cách tiếp cận truyền thống (khán giả xương reste, sampling, mô hình dự đoán) bị trễ lớn, sai số ước tính và khả năng mở rộng kém trên dữ liệu hồ sơ đa chiều cao. Prior work chưa giải quyết được truy vấn chính xác (exact counting) trên hàng triệu hồ sơ và hàng nghìn thuộc tính bằng ngôn ngữ tự nhiên trong thời gian thực.

## Contribution
- REALMS (Real-time Exact Audience sizing via LLM-based Multi-attribute Search) — hệ thống hội thoại cho quy ước kích thước khán giả chính xác, đã triển khai production trên nền tảng dữ liệu khách hàng doanh nghiệp (enterprise customer data platform).
- Ba thành phần chính: (1) cơ chế lấy thuộc tính phân loại (categorical attribute retrieval) bằng tìm kiếm vector nhúng (embedding-based vector search) để xác định động thuộc tính scheme liên quan mà không cần cấu hình thủ công; (2) ống dẫn NL2SQL do LLM cung cấp với học trong bối cảnh dựa trên mẫu (template-based in-context learning) để sinh truy vấn chính xác qua schema lồng nhau phức tạp; (3) chuẩn hóa scheme (schema standardization) cho việc triển khai độc lập ngành (industry-agnostic) trên nhiều môi trường doanh nghiệp đa dạng.

## Method (tóm tắt cốt lõi)
- Tiền xử lý ngoại tuyến (offline pre-processing): xuất và làm phẳng hồ sơ phân cấp thô từ nền tảng dữ liệu nguồn sang biểu diễn cột (columnar representation) lưu trữ trong cơ sở dữ liệu phân tích có thể mở rộng; đồng thời tạo nhúng (embedding) và xây dựng chỉ mục.
- Lấy thuộc tính có ý thức về scheme (schema-aware attribute retrieval): mã hóa truy vấn thành nhúng Dense, khớp với thuộc tính scheme ứng cử viên thông qua truy xuất ngữ nghĩa thay vì quy tắc làm tay hoặc mapping scheme cụ thể.
- Sinh truy vấn có cấu trúc do LLM lái (LLM-driven structured query generation): xây dựng prompt bằng ngữ cảnh scheme đã lấy và mẫu truy vấn có thể tái sử dụng; LLM dịch định nghĩa khán giả bằng ngôn ngữ tự nhiên thành truy vấn SQL thực thi được qua cấu trúc hồ sơ lồng nhau phức tạp.
- Chuẩn hóa scheme (schema standardization): chuẩn hóa dữ liệu vào biểu diễn cột thống nhất trừu tượng hóa sự khác biệt theo nguồn, tách việc sinh query khỏi tổ chức dữ liệu vật lý, cho phép tính toán chính xác quy mô lớn.
- Ống dẫn thời gian chạy 5 giai đoạn: truy xuất thuộc tính có ý thức về scheme, sinh tạo tăng cường được dẫn dắt bởi đồ thị tri thức (KG-RAG), phân tích ngữ nghĩa do LLM cung cấp, thực thi truy vấn có quy mô lớn, và giải thích kết quả.

## Key Findings
- 4 tác giả từ Adobe Inc., category arXiv: cs.CL, cs.IR.
- Tập đánh giá 600 yêu cầu quy ước kích thước khán giả bằng ngôn ngữ tự nhiên, bao gồm 3 ý định truy vấn (count, top-k, percentage) và độ phức tạp 1–3 thuộc tính.
- Bảng III: Lấy thuộc tính scheme — Recall@k 94%, Exact-match rate@k 93%; Đúng truy vấn có cấu trúc — Execution match 90%, LLM-as-a-judge 95%.
- Bảng IV nghiên cứu loại bỏ (ablation): REALMS đầy đủ — Execution Match 90%, LLM-Judge 95%; không KG-RAG — 68%, 72%; không Schema Retrieval — 57%, 63%; Random Example Retrieval — 72%, 75%.
- Bảng V độ phức tạp: 1 thuộc tính — Recall 100%, Exec 100%, LLM 99%; 2 thuộc tính — Recall 98%, Exec 94%, LLM 97%; 3 thuộc tính — Recall 93%, Exec 88%, LLM 93%.
- Bảng VI ý định truy vấn: Count — Recall 96%, Exec 95%, LLM 97%; Top-k — Recall 95%, Exec 88%, LLM 90%; Percentage — Recall 93%, Exec 92%, LLM 93%.
- Bảng II kiểm tra tải: 10–30 yêu cầu/phút (RPM) — không lỗi, trung bình phản hồi dưới 9 giây; 60 RPM với 10 người dùng đồng thời — trung bình 10,0 giây, P95 14,0 giây, 2 lỗi/105 yêu cầu.

## Actionable Insights
1. Kết hợp lấy thuộc tính có ý thức về scheme với NL2SQL để sinh truy vấn chính xác trên scheme phức tạp lồng nhau. Áp dụng: dùng nhúng để lấy các thuộc tính scheme liên quan trước khi sinh SQL, giảm kích thước prompt và cải thiện độ chính xác.
2. Dùng học trong bối cảnh dựa trên mẫu (template-based in-context learning) thay vì fine-tune cho từng scheme để làm di dòng NL2SQL qua các miền doanh nghiệp khác nhau. Áp dụng: xây dựng thư viện mẫu truy vấn có thể tái sử dụng, kết hợp với ngữ cảnh scheme đã lấy để sinh SQL thực thi được.

## Assumptions & Limitations
- Hệ thống triển khai trên nền tảng dữ liệu khách hàng doanh nghiệp cụ thể; kết quả có thể không chuyển tiếp trực tiếp đến các môi trường khác.
- Chuẩn hóa scheme là bắt buộc cho triển khai độc lập ngành.
- Không nói rõ: chi phí lưu trữ và cập nhật chỉ mục nhúng khi scheme thay đổi.

## Metadata
- Năm: 2026, tác giả: Haixu Ma, Aditya Bansal, Shubham Lohiya, Sumit Ranjan (Adobe Inc.), category arXiv: cs.CL, cs.IR, link PDF: https://arxiv.org/pdf/2609.30547v1
