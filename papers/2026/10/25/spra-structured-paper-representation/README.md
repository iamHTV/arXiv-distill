# [2610.21424v2] Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents

## Giá trị cốt lõi (1 câu)

SPRA (cấu trúc bài báo có cấu trúc cho tác tử) biến nghiên cứu khoa học thành các đối tượng có cấu trúc và quan hệ được trích lập (typed relations) để tác tử AI có thể tra cứu, duyệt và tái sử dụng nội dung bài báo một cách hiệu quả, giảm 28.5% token so với truy xuất đoạn văn (passage retrieval) và 95.3% so với văn bản đầy đủ (Full Compact).

## Problem

Prior work chưa giải quyết được việc kết nối các vấn đề nghiên cứu, phương pháp và kết quả phân tán qua các bài báo lý thuyết (narrative articles) cho tác tử khoa học. Các tác tử khoa học phải đọc toàn văn bài báo hoặc dựa trên truy xuất đoạn văn (passage retrieval), điều này tốn tokens và mất đi cấu trúc quan hệ giữa các đối tượng nghiên cứu (vấn đề, đóng góp, phương pháp, thiết lập thí nghiệm, thước đo, kết quả).

## Contribution

(i) SPRA (Structured Paper Representation for Agents): một biểu diễn bài báo cấp độ giấy báo của các đối tượng nghiên cứu bền vững và quan hệ được trích lập (typed relations), với bản hồ sơ AI thực nghiệm (empirical-AI profile) tổ chức Vấn đề, Đóng góp, Thành phần, Thiết lập thí nghiệm, Thước đo và Kết quả để truy vấn, duyệt và tái sử dụng.
(ii) Quan hệ trích lập cấp bài báo ghi lại sự phụ thuộc, sử dụng thành phần và so sánh với công trình trước; vị trí nguồn (source locations) hỗ trợ xác minh.
(iii) Triết khiển SPRA trên hơn 1 triệu bài báo AI, với 19,95 triệu đơn vị nghiên cứu và 24,07 triệu quan hệ nội bộ.
(iv) Đánh giá SPRA thông qua Schema-RAG với bằng chứng nhiệm vụ được cố định trước khi suy luận (inference).

## Method

Xây dựng SPRA qua 5 giai đoạn: (1) Đầu vào là bài báo nguồn được phân tích thành Markdown có nhận diện section với dấu chỉ nguồn (source markers). (2) Lịch kiểm tra (census) đơn vị chung trước khi lập kế hoạch quan hệ và điền nội dung theo vai trò. (3) Lậpipeliner quy ước (schema validity) kiểm tra hợp đồng quan hệ, và phân giải nguồn (source resolution) kiểm tra xem địa chỉ đã ghi có tới một mục nguồn hay không. (4) M Höhepunkt ba cuộc gọi LLM cốt lõi thiết lập lịch đơn vị chung, dự đoán quan hệ và điền nội dung Problem, Method và Evidence. Hai lần trích dẫn (citation passes) nối vai trò và tín hiệu nguyên văn (verbatim signals) với siêu dữ liệu bibliographic theo khóa trích dẫn. (5) Mã lắp ráp giải quyết dấu chỉ nguồn, bảng ghi lại nguyên văn (verbatim tables), điều định danh tính và kiểm tra kiểu, đầu cuối, nguồn gốc và phạm vi kiểm tra (census coverage).

Biểu diễn theo tham số luận khoa học của bài báo: một Vấn đề thúc đẩy một Đóng góp; Thành phần và Thiết lập thí nghiệm mô tả cái đã xây dựng và đã kiểm tra; Thước đo định nghĩa mục tiêu đánh giá; Kết quả ghi lại các quan sát đã báo cáo. Sáu vai trò này tổ chức hồ sơ AI thực nghiệm. Bảng quan hệ nêu rõ các quan hệ kết nối các đối tượng này và các điểm cuối chấp nhận được (admissible endpoints); vai trò trích dẫn biểu thị sự phụ thuộc bên ngoài trong một tầng riêng biệt.

## KNOWLEDGE — Số liệu & khái niệm

- Khoản SPRA (tháng 9/2026): 1,059,112 bản ghi bài báo có cấu trúc trải dài 1965–2026, lấy từ văn học hội nghị AI và bản trước in (preprints) bao gồm arXiv.
- 19,949,289 đơn vị nghiên cứu (core units), 24,073,381 quan hệ nội bộ (typed relations).
- 6 vai trò nghiên cứu: Problem (Vấn đề), Contribution (Đóng góp), Component (Thành phần), ExperimentSetup (Thiết lập thí nghiệm), Measure (Thước đo), Finding (Kết quả).
- 7 loại quan hệ: part_of, co_contribution, compares_to, evaluates, about, supports, motivates, resolves.
- Mẫu đánh giá: 9,849 bài báo đủ điều kiện trên 7 lĩnh vực AI, công báo năm 2025, 1,407 bài báo mỗi lĩnh vực.
- RQ1 (QA khoa học điều kiện nguồn): Schema-RAG đạt 2.342/5 trên G-U1 (chất lượng câu trả lời ngữ nghĩa), vượt Text-RAG 1.961/5 (+0.381/5), kém Full Compact 2.420/5 (−0.078/5). G-U3 (Vấn đề + Đóng góp): Schema-RAG 3.216/5, cao nhất so với Full Compact 3.201/5.
- RQ2 (Suy luận xuyên bài báo, 3,070 nhiệm vụ đôi): Schema-RAG dùng 9.51M tokens đầu vào+đầu ra, giảm 28.5% so với Text-RAG (13.30M) và 95.3% so với Full Compact (203.26M). Đánh giá định hướng (directed judgment): qualification +0.184/5, correctness +0.026/5, grounding +0.045/5 so với Text-RAG.
- RQ3 (Sinh ý tưởng, 1,001 biến thể): SPRA-Full Compact Overall −0.067 điểm, SPRA-Text-RAG Overall +0.011 điểm. SPRA dùng 93.7% ít tokens hơn Full Compact, 17.7% ít hơn Text-RAG.
- Mở rộng trích dẫn (citation expansion): thêm tối đa 2 hàng xóm trích dẫn đã giải quyết cải thiện tích hợp xuyên bài báo +0.253/5.
- Kiểm định cấu trúc: 203,628/214,239 đơn vị cốt lõi (95.0%) có dấu chỉ nguồn; 106,439/109,591 quan hệ (97.1%) nối tới cả hai đầu cuối.
- Khảo sát ngữ nghĩa: điểm sắp xếp ngữ nghĩa mức đóng góp 84.49/100 từ GPT-4.1; sự tương đương đơn vị thông tin 4.436/5.

## INSIGHT — Cơ chế & tại sao

[Biểu diễn có cấu trúc (structured representation) với quan hệ được trích lập] giúp tác tử truy cập trực tiếp vào cấu trúc nghiên cứu thay vì phải đọc toàn văn → Schema-RAG vượt Text-RAG +0.381/5 trên G-U1 và giảm 28.5% tokens trên RQ2. Điều này nghĩa là việc tách nội dung bài báo thành các đối tượng có vai trò rõ ràng và quan hệ được trích lập làm giảm tải trí tuệ (cognitive load) cho tác tử.

[Liên kết nguồn (source bindings) và quan hệ trích dẫn] cho phép tác tử truy vết và xác minh các kết quả → chỉ số qualification cải thiện +0.184/5 trên RQ2 directed judgment. Điều này nghĩa là khi các phát hiện (Findings) được kết nối với điều kiện và hạn nợ (qualifications), tác tử đánh giá chính xác hơn về mức độ tin cậy của các phát hiện.

[Văn bản đầy đủ (Full Compact) chưa nhất định là tối ưu] cho tất cả nhiệm vụ: trên RQ3 Top-5 synthesis, SPRA kém Full Compact −0.067/5 trên Overall, và grounding/qualification giảm trên Top-5. Điều này nghĩa là cấu trúc thu gọn (compact structure) phải được đánh giá theo nhu cầu thông tin của từng tác vụ — không phải lúc nào cấu trúc đầy đủ cũng tốt hơn.

[Schema-RAG gần Full Compact trên G-U3] (3.216 vs 3.201/5) cho thấy việc xác định vấn đề và đóng góp của bài báo không cần toàn văn, chỉ cần cấu trúc có trích lập. Điều này nghĩa là các tác tử có thể nhanh chóng nắm bắt cốt lõi của bài báo mà không cần đọc toàn bộ.

## IDEA — Áp dụng được gì

Áp dụng [biểu diễn bài báo có cấu trúc] vào việc xây dựng knowledge base cho tác tử nghiên cứu doanh nghiệp: thay vì lưu trữ toàn văn bài báo, hãy trích xuất 6 vai trò (vấn đề, đóng góp, thành phần, thiết lập thí nghiệm, thước đo, kết quả) và các quan hệ giữa chúng để tác tử có thể tra cứu nhanh chóng.

Áp dụng [Schema-RAG] vào hệ thống trả lời câu hỏi khoa học cho doanh nghiệp: thay vì truy xuất đoạn văn (passage retrieval), hãy truy xuất các đối tượng có cấu trúc và quan hệ trích lập để giảm chi phí token và cải thiện độ chính xác của câu trả lời điều kiện nguồn.

Áp dụng [citation expansion] vào việc mở rộng bằng chứng cho nghiên cứu: bắt đầu từ các đối tượng giống nhau (seed objects), sau đó thêm tối đa 2 hàng xóm trích dẫn đã giải quyết để thu thập bằng chứng bổ sung dưới một trần bám ngữ cảnh (context ceiling) chung.

## WISDOM — Nguyên tắc tổng quát

Nguyên tắc: Biểu diễn nghiên cứu có cấu trúc với quan hệ được trích lập và ràng buộc nguồn (source bindings) thường hiệu quả hơn văn bản thô (raw text) cho tác tử AI khi mục tiêu là tra cứu, duyệt và tái sử dụng nội dung khoa học, bởi vì cấu trúc giảm tải trí tuệ và cho phép xác minh.

Khi nào dùng: Khi cần xây dựng hệ thống truy vấn knowledge base cho nội dung nghiên cứu hoặc tài liệu kỹ thuật, đặc biệt là khi cần tra cứu nhanh và xác minh nguồn gốc.

Khi nào KHÔNG dùng: Khi nhiệm vụ yêu cầu hiểu rõ ngữ cảnh đầy đủ của bài báo (ví dụ: tổng hợpTop-5 cần toàn văn), hoặc khi không cần xác minh nguồn gốc và chỉ cần tóm tắt nhanh.

Ví dụ áp dụng ngoài domain gốc: Xây dựng kho kiến thức cho luật và quy định — trích xuất 6 vai trò (vấn đề pháp lý, đóng góp, thành phần, thiết lập, thước đo, kết quả) và quan hệ giữa các điều khoản pháp luật để luật sư AI có thể tra cứu và xác minh.

## Assumptions & Limitations

- Điều kiện đúng: Bài báo nguồn có thể được phân tích thành Markdown có nhận diện section; có quyền truy cập vào Sciverse platform hoặc cài đặt cục bộ cho Paper Schema API; tác tử có thể gọi LLM để trích xuất cấu trúc.
- Limitation paper thừa nhận: Đánh giá chỉ bao gồm hồ sơ AI thực nghiệm và các tác vụ đánh giá đã chỉ định; chuyển giao sang các domain khác, tái sử dụng tác vụ liên tiếp và ổn định dưới các bản viết lại bảo lưu ý nghĩa (meaning-preserving rewrites) còn là hướng đánh giá trong tương lai. So sánh không tách biệt đóng góp của từng nhãn vai trò hoặc từ khóa quan hệ.
- Limitation paper KHÔNG nói: Không có đánh giá trên các domain ngoài AI (ví dụ: y học, vật lý); không có đánh giá chi phí lưu trữ và bảo trì (storage, retrieval, maintenance) do Sciverse cung cấp; không có đánh giá độ ổn định của dịch vụ lưu trú khi cập nhật.

## Metadata

- Năm: 2026
- Tác giả: Yutong Leng, Haojiong Chen, Xiaoyang Wang, Mindong Liu, Runyuan Ma, Fukai Shang, Jiantao Qiu
- Thể loại arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.21424v2
- Số lượt trích dẫn: chưa có thông tin