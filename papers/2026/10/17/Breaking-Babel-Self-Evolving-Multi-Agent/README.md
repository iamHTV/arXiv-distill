# [2609.38660v2] Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation

## Problem
- Dịch phụ đề dài (long-form subtitle translation) còn gặp nhiều thách thức so với dịch câu đơn (sentence-level translation). Một phần phim có trăm câu (hundreds of sentences) mà ý nghĩa của chúng phụ thuộc vào ngữ cảnh ngữ văn (discourse) và văn hóa (cultural context) xuyên dài toàn bộ phần phim (episode) hay thậm chí toàn bộ bộ phim (series). Đồng thời, bản dịch cũng phải đảm bảo sự nhất quán về thuật ngữ (terminology) và phong cách (style) toàn bộ phim, đồng thời tuân thủ các ràng buộc trình bày nghiêm ngặt như số dòng (line length) và tốc độ đọc (reading speed).

## Contribtuion
- SMART (Self-evolving Multi-Agent system for long-form subtitle Translation) — một hệ thống đa agent tự phát triển (self-evolving multi-agent system) để dịch phụ đề dài.
- SMART hoạt động ở hai giai đoạn: trong thời gian kiểm thử (test-time training), nó xây dựng bộ nhớ cấp series (series-level memory) bền vững và dịch một tập con các câu (subset of sentences) thông qua bộ định tuyến động (dynamic graph router) và lớp dịch đa đại lý (Mixture-of-Agents translation layer), được trang bị các mô-đun gọi công cụ (tool-calling modules) để xác thực thuật ngữ (terminology verification), xác thực ràng buộc phụ đề (subtitle constraint validation), và truy xuất ngữ cảnh (contextual retrieval); một vòng lặp juez-refiner (judge-refiner loop) đánh giá từng bản dịch ứng viên (candidate translation) và truyền lại phê bình văn bản (textual critiques) để tinh chỉnh hướng dẫn agent (agent prompts) và chính sách định tuyến (routing policy), không cần đào tạo lại các mô hình LLM cơ bản (underlying LLMs).
- Trong thời gian suy luận (test-time inference), cấu hình đã tiến hóa (evolved configuration) dịch các câu còn lại của series.

## Method (tóm tắt cốt lõi)
- Giai đoạn ngoại tuyến (offline test-time training): xây dựng bộ nhớ cấp series (series-level memory) bền vững và dịch một tập con các câu thông qua định tuyến động (dynamic graph router) và lớp dịch đa đại lý (Mixture-of-Agents translation layer), được trang bị các mô-đun gọi công cụ (tool-calling modules) cho xác thực thuật ngữ (terminology verification), xác thực ràng buộc phụ đề (subtitle constraint validation), và truy xuất ngữ cảnh (contextual retrieval).
- Vòng lặp juez-refiner (judge-refiner loop) đánh giá từng bản dịch ứng viên (candidate translation) và truyền lại phê bình văn bản (textual critiques) để tinh chỉnh hướng dẫn agent (agent prompts) và chính sách định tuyến (routing policy), không cần retraining các mô hình LLM cơ bản.
- Giai đoạn thời gian suy luận (test-time inference): cấu hình đã tiến hóa (evolved configuration) dịch các câu còn lại của series.
- Đánh giá trên Subtitle Arena: 14 thể loại (genres), 2–198 tập phim (episodes) mỗi series, năm sản xuất từ 1959 đến 2023, và 15 vùng miền (locales), cùng với SubMQM — một khung đánh giá phụ đề (subtitle-adapted MQM framework) với 7 kích thước (dimensions) và 19 hạng mục lỗi (error categories).
- SMART đạt điểm tổng hợp MQM (MQM score) cao nhất trong tất cả 15 hướng (directions) của Subtitle Arena, giảm mức phạt (average penalty) xuống 6.9% so với hệ thống agent mạnh nhất cạnh tranh.
- Trên bản chuẩn công khai (public benchmark) MuSC, SMART đạt kết quả tốt nhất trên tất cả 4 cặp ngôn ngữ (4 language pairs).
- SMART cũng đạt kết quả tốt nhất trong đánh giá bằng con người (human evaluation) với điểm tổng hợp tổng thể (overall score) 4.50/5.

## Key Findings
- 7 tác giả từ Đại học Illinois Urbana-Champaign (University of Illinois Urbana-Champaign) và Amazon, category arXiv: cs.CL.
- SMART đạt điểm tổng hợp MQM cao nhất trong tất cả 15 hướng (directions) của Subtitle Arena, giảm mức phạt (average penalty) xuống 6.9% so với hệ thống agent mạnh nhất cạnh tranh.
- Trên bản chuẩn công khai (public benchmark) MuSC, SMART đạt kết quả tốt nhất trên tất cả 4 cặp ngôn ngữ (4 language pairs).
- SMART cũng đạt kết quả tốt nhất trong đánh giá bằng con người (human evaluation) với điểm tổng hợp tổng thể (overall score) 4.50/5.

## Actionable Insights
1. Dùng hệ thống đa agent tự phát triển (self-evolving multi-agent system) để dịch phụ đề dài (long-form subtitle translation). Áp dụng: dùng hệ thống multi-agent với dynamic graph router và lớp dịch đa đại lý (Mixture-of-Agents translation layer) để dịch phụ đề dài.
2. Dùng bộ nhớ cấp series (series-level memory) bền vững để duy trì thuật ngữ và phong cách qua nhiều tập phim. Áp dụng: dùng bộ nhớ cấp series để duy trì thuật ngữ và phong cách đồng bộ qua nhiều tập phim.

## Assumptions & Limitations
- Đánh giá trên 14 thể loại (genres), 2–198 tập phim (episodes) mỗi series, 15 vùng miền (locales).
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).

## Metadata
- Năm: 2026, tác giả: Haibo Jin, Tijana Stanic, Najmeh Sadoughi, Yang Liu, Yibo Wang, Zhu Liu, Yuzong Liu (Đại học Illinois Urbana-Champaign, Amazon), category arXiv: cs.CL, link PDF: https://arxiv.org/pdf/2609.38660v2
