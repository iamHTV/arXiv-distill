# [2610.21424v1] Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents

## Problem
Các agent khoa học phải kết nối vấn đề nghiên cứu, phương pháp, và phát hiện phân tán qua các bài báo văn trình. Các bài báo truyền thống biểu thị cấu trúc nghiên cứu qua văn ngôn, bảng, và biểu đồ; agent phải tự khôi phục vai trò và phụ thuộc nghiên cứu từ các đoạn văn. Việc truy xuất dựa trên đoạn văn (passage-based retrieval) cung cấp văn bản nguồn liên quan nhưng agent phải kết nối phát hiện với phương pháp, điều kiện, và so sánh. Việc nhập toàn bộ bài báo nhiều lần tạo phí API dựa trên token và chiếm ngữ cảnh cần cho thêm bài báo và lịch sử tác vụ.

## Contribution
- Giới thiệu SPRA (Structured Paper Representation for Agents), một biểu diễn cấp bài báo của các đối tượng nghiên cứu bền vững và quan hệ gõ (typed relations).
- Hồ sơ AI thực nghiệm (empirical-AI profile) tổ chức Vấn đề (Problems), Đóng góp (Contributions), Thành phần (Components), Thiết lập thí nghiệm (ExperimentSetups), Đo lường (Measures), và Kết quả (Findings) để truy vấn, duyệt, và tái sử dụng.
- Quan hệ trích dẫn cấp bài báo ghi lại sự phụ thuộc, sử dụng thành phần, và so sánh với công trình trước; vị trí nguồn (source locations) hỗ trợ xác thực.
- Triển khai SPRA qua hơn một triệu bài báo AI, với 19,95 triệu đơn vị nghiên cứu và 24,07 triệu quan hệ nội bộ.
- Đánh giá qua Schema-RAG với bằng chứng tác vụ được cố định trước khi suy luận.

## Method
- SPRA lưu trữ các đối tượng nghiên cứu độc lập với truy vấn cụ thể. JSON có cấu trúc mã hóa mỗi phiên bản; hồ sơ phiên bản quy định vai trò khoa học, chữ ký quan hệ, cardinality, và quy tắc liên kết nguồn.
- Biểu diễn tuân theo lập luận khoa học của bài báo: Vấn đề động lực Đóng góp; Thành phần và Thiết lập thí nghiệm mô tả cái đã xây dựng và kiểm tra; Đo lường định nghĩa mục tiêu đánh giá; Kết quả ghi lại quan sát được báo cáo.
- Sáu vai trò organizes hồ sơ AI thực nghiệm: Vấn đề, Đóng góp, Thành phần, Thiết lập thí nghiệm, Đo lường, Kết quả.
- Quan hệ nội bộ (Table 1): part_of, co_contribution, compares_to, evaluates, about, supports, motivates, resolves với các chữ ký đầu cuối cho phép.
- Quan hệ trích dẫn: builds_on, uses_component, compares_with kết nối báo cáo nghiên cứu với công trình trước.
- Công khai qua Paper Schema API trên nền tảng Scholarly Dữ liệu SciVerse.

## Key Findings
- Khai báo SPRA trên hơn 1 triệu bài báo AI (1965–2026), 19,95 triệu đơn vị nghiên cứu, 24,07 triệu quan hệ nội bộ.
- Trên 7 lĩnh vực con: SPRA cải thiện QA khoa học điều kiện nguồn bằng 0,381/5 so với truy xuất đoạn văn, ở gần Full Compact (0,078/5 thấp hơn trung bình).
- Suy luận chéo bài báo có hướng: sự muốn improve by 0,184/5 so với truy xuất đoạn văn; Top-5 synthesis cho hiệu quả chất lượng pha trộn.
- Trên tất cả các tác vụ RQ2 đã ghép, bao gồm Top-5, số token đầu vào+đầu ra giảm 28,5% so với truy xuất đoạn văn và 95,3% so với Full Compact.
- Trong việc tạo ý tưởng, điểm Overall thấp hơn 0,067 điểm so với Full Compact kèm theo 93,7% ít hơn số token đầu vào+đầu ra.

## Actionable Insights
1. Biểu diễn bài báo có cấu trúc cho agent truy vấn và tái sử dụng. Áp dụng: khi xây dựng hệ thống nghiên cứu AI, hãy trích xuất bài báo thành các đối tượng có cấu trúc (vấn đề, đóng góp, thành phần, thiết lập thí nghiệm, đo lường, kết quả) thay vì chỉ lưu văn bản thô. Bước đầu: Thiết lập schema JSON cho bài báo với các vai trò nghiên cứu và quan hệ gõ giữa chúng.
2. Dùng Schema-RAG thay vì passage retrieval để giảm token và cải thiện chất lượng. Áp dụng: khi xây dựng hệ thống trả lời câu hỏi khoa học, hãy truy xuất các đối tượng nghiên cứu có cấu trúc thay vì đoạn văn thô. Bước đầu: Xây dựng hệ thống truy xuất có thể truy vấn các đối tượng nghiên cứu theo vai trò và quan hệ.
3. Giảm số token đầu vào+đầu ra bằng cách sử dụng biểu diễn có cấu trúc. Áp dụng: khi xây dựng quy trình nghiên cứu AI, hãy dùng biểu diễn có cấu trúc để giảm chi phí API so với việc nhập toàn bộ bài báo. Bước đầu: So sánh chi phí token giữa việc truy xuất đoạn văn và truy xuất đối tượng có cấu trúc trên tác vụ của bạn.

## Assumptions & Limitations
- Đánh giá trên bộ dữ liệu AI (1965–2026), có thể khác trên domain ngoài AI.
- Chỉ đánh giá trên 7 lĩnh vực con AI, không generalize sang tất cả các lĩnh vực khoa học.
- Bộ mẫu đánh giá gồm 9.849 bài báo có nguồn tương ứng, có thể không đại diện cho toàn bộ corpus 1 triệu bài báo.
- Các kết quả tạo ý tưởng cho điểm Overall thấp hơn hơi Full Compact (0,067/5), trade-off chất lượng với hiệu quả token.

## Metadata
- Năm: 2026, tác giả: Yutong Leng, Haojiong Chen, Xiaoyang Wang, Mindong Liu, Runyuan Ma, Fukai Shang, Jiantao Qiu (Shanghai Artificial Intelligence Laboratory; Shanghai Jiao Tong University), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2610.21424v1