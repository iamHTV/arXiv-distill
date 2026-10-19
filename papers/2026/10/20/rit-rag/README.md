# [2610.11370v2] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees

## Giá trị cốt lõi (1 câu)
RIT-RAG kết hợp lấy nội dung (content retrieval) với điều hướng cấu trúc (structure-aware navigation): dùng truy xuất để lun trong kho lớn, rồi dẫn agent đến cây con cấu trúc xung quanh các đoạn đã truy xuất để agent chọn đọc chọn lọc — lấy nội dung đề xuất "nơi tìm", agent quyết định "đọc gì".

## Problem
Prior work chưa giải quyết vấn đề đắn agentic RAG chạy ở cấp đoạn (chunk-level), không có biểu diễn rõ ràng cấu trúc tài liệu, nên khó phân biệt đoạn có bằng chứng thật khỏi đoạn chỉ tương tự về thuật ngữ; trong khi phương pháp nhận thức cấu trúc (structure-aware) như PageIndex không thể mở rộng lên corpus lớn (toàn bộ cấu trúc không vừa ngữ cảnh LLM) và phải cam kết sớm vào một tài liệu duy nhất trước khi xem nội dung.

## Contribution
- Giới thiệu RIT-RAG (Retrieval-Induced Tree RAG): khung kết hợp lấy nội dung với điều hướng cấu trúc; ngoại tuyến xây dựng cây cho mỗi tài liệu từ mục lục (ToC) hoặc sitemap; tại thời điểm truy vấn, lấy một tập rộng các đoạn và dùng vị trí của chúng để gây ra cây con dễ quản lý, có thể trải nhiều tài liệu.
- LLM agent điều hướng các cây con, đọc chọn lọc các nút hứa hẹn, và đổi câu hỏi khi cần; lấy nội dung đề xuất "nơi tìm", agent quyết định "đọc gì".
- Xây dựng EntQABench, benchmark mới trên EntDocs (2.84 triệu trang web tài liệu sản phẩm của một doanh nghiệp lớn) để đánh giá RAG tại quy mô corpus thực tế.
- Đánh giá trên ba tập công khai (WixQA, QASPER, FinanceBench) và EntQABench; RIT-RAG đạt độ chính xác cao nhất giữa vanilla, dựa trên đồ thị, và các cơ sở dựa trên agent.

## Method
Ngoại tuyến: xây dựng cây Ti cho mỗi tài liệu di từ ToC hoặc sitemap; mỗi nút v sở hữu văn bản nằm dưới nó nhưng không dưới nút con nào (cv); metadata gồm tiêu đề, tóm tắt từ khóa; hàm tuần tự hóa S(Ti) chuyển cây thành chuỗi JSON (mỗi nút có ID, metadata, danh sách nút con). Tại thời điểm truy vấn: lấy top-k′ đoạn từ chỉ mục tra cứu (k′ > k, ví dụ k′=200); mỗi đoạn thuộc đúng một nút; điểm số nút s(v, q~) = max sim(q~, c) qua các đoạn của nút; chọn n nút cao điểm (ví dụ n=50); mở rộng với tổ tiên của các nút đó để tạo câu con phụ Fq~; biểu diễn Fq~ dưới dạng chuỗi, liệt kê các cây theo thứ tự giảm điểm số cao nhất trong cây. Agent LLM làm việc theo vòng: mỗi vòng t, agent đưa ra câu truy vấn q~t, gọi GetToC để lấy S(Fq~t), lý luận qua S(Fq~t) để chọn bộ nút St, đọc văn bản cv của các nút qua Read tool; dựa trên nội dung, agent hoặc trả lời, đọc thêm nút từ cùng câu con, hoặc đổi câu truy vấn cho vòng sau. Agent dừng khi trả lời hoặc đạt ngân sách B công cụ (tối đa Bs = 3 cuộc gọi GetToC, B = 10 tổng cộng).

## KNOWLEDGE — Số liệu & khái niệm
- Tập dữ liệu: WixQA (200 câu hỏi hỗ trợ khách hàng chuyên gia qua 6.221 trang trung tâm trợ giúp), QASPER (1.372 câu hỏi trả lời được qua 416 bài báo NLP), FinanceBench (150 câu hỏi tài chính qua 364 báo cáo SEC dạng PDF), EntQABench (317 câu hỏi tạo bằng LLM qua 3 sản phẩm, corpus EntDocs 2,84 triệu trang web tài liệu sản phẩm doanh nghiệp lớn).
- Mô hình: Claude Haiku 4.5, GPT-5-mini, GPT-5.6-Luna; trích xuất biên loại ToC dùng Qwen3-32B (để giảm chi phí) hoặc Haiku.
- Retriever lai kết hợp BM25 và truy xuất denses với gte-modernbert-base + FAISS, đoạn tối đa 512 token.
- Siêu tham số: k′ = 200 đoạn, n = 50 nút, B = 10 công cụ, Bs = 3 cuộc gọi GetToC.
- Đo chính xác do LLM phán (Gemini 2.5 Flash) so sánh dự đoán với đáp án vàng; đo độ chính xác (precision), độ thu hồi (recall), F1 của đoạn đọc so với bằng chứng vàng; chi phí tiền xử lý, chi phí API, độ trễ mỗi truy vấn.
- Kết quả chính: RIT-RAG đạt độ chính xác cao nhất trên cả 3 tập công khai và cả 3 mô hình.
- So với Agentic Search (cùng bộ tra cứu, cùng LLM, cùng ngân sách B=10): +10.5, +5.0, +4.5 điểm trên WixQA; +2.4, +2.9, +3.5 điểm trên QASPER (Haiku, GPT-5-mini, Luna).
- So với PageIndex: +2.0–5.0 điểm trên WixQA; +12.2–13.3 điểm trên QASPER.
- FinanceBench (cấu trúc được gây ra): RIT-RAG vượt cơ sở tốt nhất 9.3, 8.0, 4.6 điểm; vượt PageIndex 8.7–18.6 điểm.
- EntQABench (2,84 triệu trang): RIT-RAG vượt cơ sở tốt nhất 6.6, 7.9, 11,4 điểm.
- Phân tích truy xuất: RIT-RAG đạt F1 cao nhất trên cả 3 tập; cân bằng độ chính xác (PageIndex cao hơn về độ chính xác) và độ thu hồi (Agentic Search cao hơn về độ thu hồi).
- Chi phí trực tuyến: RIT-RAG 5.7–13.3 cent/câu hỏi vs Agentic Search 1.3–6.3 cent; trên EntDocs khoảng bằng nhau (6.0 vs 6.2 cent).
- Chi phí ngoại tuyến xử lý trước: $20.4 (WixQA), $17.0 (QASPER), $773 (FinanceBench, gây ra ToC của 364 báo cáo dài), $0 (EntDocs, dùng cấu trúc hiện có và chỉ tiêu đề nút); phương pháp dựa trên đồ thị: $86–107 (WixQA), $1.3K–$1.7K (FinanceBench), $106K–$131K (EntDocs).
- Mã nguồn: chưa nêu URL rõ ràng trong abstract (benchmark và cây tài liệu sẽ được công bố).
- Danh mục arXiv: cs.AI

## INSIGHT — Cơ chế & tại sao
[Agentic RAG cao độ thu hồi nhưng thấp độ chính xác; PageIndex ngược lại; RIT-RAG cân bằng cả hai] VÌ [RIT-RAG dùng truy xuất để lun trong kho lớn (đảm bảo độ thu hồi) rồi dùng cây con cấu trúc truy xuất để agent đọc chọn lọc (đảm bảo độ chính xác)]. Điều này nghĩa là [phân cách khám phá bằng chứng khỏi đọc nội dung giúp tối ưu cả hai chỉ số].
[RIT-RAG không cam kết vào một tài liệu duy nhất] VÌ [mỗi lần tìm kiếm tạo ra một câu con mới có thể trải nhiều tài liệu; agent không bao giờ bị cam kết vào tài liệu của vòng trước, có thể đổi câu truy vấn để bề mặt tài liệu khác]. Điều này nghĩa là [tránh vấn đề cam kết sớm (early commitment) của PageIndex khi chọn sai tài liệu].
[RIT-RAG mạnh hơn PageIndex trên corpus lớn] VÌ [không cần phù hợp toàn bộ cấu trúc corpus vào ngữ cảnh LLM; kích thước cấu trúc trình bày bị giới hạn bởi số nút được chọn và tổ tiên của chúng, chứ không phải kích thước corpus]. Điều này nghĩa là [gây ra cây theo truy vấn mở rộng khả năng mở rộng lên triệu trang tài liệu].

## IDEA — Áp dụng được gì
Áp dụng RIT-RAG vào hệ thống RAG doanh nghiệp với kho tài liệu kỹ thuật lớn: bước đầu là xây dựng cây cấu trúc từ ToC/sitemap của mỗi tài liệu, dùng truy xuất để lun trong kho lớn, rồi dẫn agent đến cây con cấu trúc xung quanh các đoạn đã truy xuất.
Dùng cấu trúc truy xuất theo truy vấn thay vì chọn tài liệu duy nhất: bước đầu là liên kết mỗi đoạn trích với metadata cấu trúc (ID nút, tiêu đề, ID tổ tiên và tiêu đề) để tái cấu trúc cây con tại thời điểm suy luận.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Phân cách khám phá bằng chứng khỏi đọc nội dung — truy xuất đảm bảo độ phủ (recall), cấu trúc truy xuất đảm bảo độ chính xác (precision); không cam kết vào tài liệu duy nhất trước khi thấy nội dung.

## Assumptions & Limitations
- Điều kiện đúng: tài liệu có cấu trúc phân cấp (ToC, sitemap, breadcrumb) hoặc có thể gây ra cấu trúc; truy vấn cần điều hướng trong kho tài liệu lớn.
- Limitation paper thừa nhận: RIT-RAG tích lũy các nút đã lấy cho đến khi đạt ngân sách ngữ cảnh và hiện không có hỗ trợ nén bằng chứng hay loại bỏ lịch sử chat; bỏ qua các liên kết chéo giữa các nút cùng cấp trong cây; phương pháp phụ thuộc vào cấu trúc phân cấp khả dụng — việc gây ra cấu trúc có thể bị hạn chế bởi tiêu đề yếu hoặc phân tích kém.
- Limitation paper KHÔNG nói: chi phí vận hành nhiều vòng suy luận tại quy mô lớn; tính ổn định của độ chính xác qua nhiều lần chạy; tác động lên độ trễ khi gọi GetToC nhiều lần.

## Metadata
- Năm: 2026
- Tác giả: Meghanadh Pulivarthi, Swaraj Kumar Biswal, Kushagra Bhushan, Yatin Nandwani, Sachindra Joshi, Dinesh Raghu (IBM, IIT Kharagpur)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.11370v2
- arXiv ID: 2610.11370v2
- Nhãn: [applied]
- Skill: rit-rag | Test: [SKILL VALID]
