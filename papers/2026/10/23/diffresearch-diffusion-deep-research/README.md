# 2610.28909 DiffResearch: Tăng tốc deep research bằng diffusion language model

## Problem
Hệ thống deep research (nghiên cứu sâu — hệ thống tự lập lập kế hoạch, thu thập bằng chứng, tổng hợp và chỉnh sửa báo cáo dài) hiện nay hầu hết được xây dựng trên autoregressive language model (mô hình ngôn ngữ tự hồi quy — sinh văn bản theo thứ tự từ trái sang phải, một token một thời điểm). Điều này tạo độ trễ (latency) cao ở giai đoạn lập kế hoạch và viết bài dài, vì mỗi phần được viết tuần tự và khó sửa lỗi khi bằng chứng mới đến sau. Các hệ thống thương mại như OpenAI Deep Research, Gemini Deep Research, Perplexity Deep Research cùng mắc vấn đề này.

## Contribution
- DiffResearch: khung deep research đa agent (multi-agent — nhiều agent phối hợp) mã opens, đặt diffusion language model (mô hình ngôn ngữ diffusion — sinh văn bản qua quá trình lấy nhiễu lặp lại, cập nhật toàn bộ dãy song song trong ít bước) làm lõi tại mọi giai đoạn. Cho phép hoán đổi backbone (xương sống — mô hình tạo sinh chính) giữa diffusion và AR trong cùng một khung agentic scaffold (khung tác nhân) để so sánh trực tiếp.
- dFast: chế độ phân tích phân giải (decomposition — chia truy vấn lớn thành các truy vấn phụ) đọc trạng thái lấy nhiễu trung gian (intermediate denoising states) để trích xuất subqueries (truy vấn phụ) trước khi sinh xong, đưa ra 1.99× tốc độ trung vị (median) cho phân tích phân giải riêng lẻ, không làm giảm chất lượng báo cáo.
- Snapshot bảng xếp hạng (leaderboard): phiên bản DiffResearch costru trên diffusion model mạnh hơn (Mercury) xếp trên một số hệ thống deep research thương mại công khai.

## Method
Khung có 9 agent, mỗi agent là một instance của diffusion LLM, kế thừa backbone chung và triển khai một phương thức generate. Backbone có thể hoán đổi: google/diffusiongemma-26B-A4B-it cho diffusion-native deployment, google/gemma-4-26B-A4B-it cho AR baseline. Năm giai đoạn cốt lõi: phân loại ý định (intent classification), viết lại truy vấn (query reformulation), lập kế hoạch (planning), truy xuất (retrieval — tìm kiếm thông tin từ nguồn bên ngoài), viết (writing), thêm đánh giá (judging) tùy chọn. Truy xuất dùng Semantic Scholar API và Serper API, deterministik (không ngẫu nhiên), không LLM trong vòng lặp (in the loop). Hai chế độ chạy: full (dFull) và fast decomposition (dFast). Trong full mode, mô hình chạy đến hết rồi phân tích JSON. Trong fast mode, streamer tùy chỉnh quét từng trạng thái lấy nhiễu trung gian, chấp nhận bản nháp (draft) hợp lệ sớm khi xuất hiện đối tượng JSON đúng số lượng subqueries yêu cầu.

## KNOWLEDGE — Số liệu & khái niệm
- Trên 100 tác vụ Deep Research Bench (tiêu chí đánh giá deep research có 100 tác vụ nghiên cứu cấp cao học, 50 tiếng Trung, 50 tiếng Anh, trải 22 lĩnh vực), diffusion backbone nhanh khoảng 6× end-to-end so với AR (trung bình 71.45 giây vs 11.89 giây, p90 111.87 giây vs 16.13/16.33 giây).
- Giai đoạn lập kế hoạch nhanh 10.7× (39.32 giây → 3,6-3,7 giây), viết bài nhanh 11.7× (59,78 giây → 5,1-5,3 giây).
- dFast trích xuất subqueries từ trạng thái lấy nhiễu trung gian: 1.99× trung vị nhanh hơn (243,4 miligiây vs 484,9 miligiây); đối tượng ổn định khớp câu trả lời cuối trong 91/100 trường hợp.
- Chất lượng RACE (thang đánh giá báo cáo nghiên cứu, 0-1): dFast 0,3969, dFull 0,3895, AR 0,3904 — diffusion không làm giảm chất lượng.
- Bảng xếp hạng công khai: instance costru trên Mercury đạt 48,03 (thang 0-100), vượt OpenAI Deep Research (46,45), Dr. Tulu (45,49), Claude Research (45,00).
- Kiểm tra nguồn (source-grounded audit): chỉ 28% 주장 được hỗ trợ đầy đủ, 52% không được thiết lập bởi gói nguồn đã lưu — truy xuất lấy gốc (retrieval grounding — việc grounding kết quả vào nguồn thực) là vướng chung của toàn hệ thống.

## INSIGHT — Cơ chế & tại sao
[Diffusion backbone sinh văn bản qua lấy nhiễu lặp lại] xảy ra VÌ diffusion cập nhật toàn bộ dãy văn bản song song trong ít bước denoising thay vì sinh tuần tự một token một thời điểm như AR. Điều này nghĩa là [các giai đoạn bị gánh bởi mô hình (model-bound stages) như lập kế hoạch và viết dài được giảm thẳng sharply, trong khi truy xuất deterministik (không dùng mô hình sinh) giữ nguyên chi phí].
[dFast đọc trạng thái lấy nhiễu trung gian] xảy ra VÌ diffusion xuất ra bản nháp (draft) ở các bước giữa của quá trình denoising, và đối với đầu ra có cấu trúc như danh sách subqueries, nội dung đề cập (topical coverage) quan trọng hơn cách diễn đạt chính xác từng từ. Điều này nghĩa là [có thể dừng sớm và gửi các cuộc gọi truy xuất trước khi sinh hoàn tất, nhưng vì phân tích phân giải chỉ chiếm một phần nhỏ tổng thời gian, không giúp giảm độ trễ end-to-end].

## IDEA — Áp dụng được gì
1. Áp dụng diffusion backbone vào hệ thống deep research / viết báo cáo nội bộ: bước đầu là thay LLM autoregressive hiện tại bằng diffusion LLM (ví dụ LLaDA, Dream, Mercury) giữ nguyên agent scaffold, đo latency trước sau trên cùng bộ tác vụ.
2. Áp dụng dFast vào bước sinh danh sách truy vấn tìm kiếm: bước đầu là đọc trạng thái diffusion trung gian để trích xuất subqueries sớm, gửi các cuộc gọi truy xuất song song thay vì chờ sinh xong.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Thay thế backbone sinh văn bản là cách nhanh nhất để giảm độ trễ ở các giai đoạn bị gánh bởi mô hình, nhưng không giải quyết vướng vấn về chất lượng truy xuất hoặc bằng chứng. Khi nào dùng: khi latency là vấn đề chính và truy xuất đã ổn định. Khi nào KHÔNG: khi vấn đề là độ chính xác của nguồn thông tin hoặc cần sinh văn bản cuối cùng chính xác từng từ.

## Assumptions & Limitations
- Đo trên H200 pod (hệ thống GPU mạnh), truy xuất cục bộ, Semantic Scholar chỉ — trên phần cứng khác hoặc ngân sách độ trễ chặt chẽ, kết quả sẽ khác.
- Chỉ một cặp backbone (diffusiongemma-26B vs gemma-4-26B), chưa quét rộng họ mô hình và kích thước.
- dFast không giảm độ trễ end-to-end trong thiết lập hiện tại vì truy xuất bị giới hạn 1 request/giây.
- Kiểm tra nguồn là mẫu nhỏ (10 báo cáo), không đủ để so sánh giữa các chế độ.
- Chưa đánh giá gửi truy xuất song song (parallel retrieval dispatch).

## Metadata
- Năm 2026; tác giả: Alan-Barsag Gazzaev, Alexey Gavrilov, Mikhail Mozikov, Sergey Muravyov (ITMO University, Nga); category: cs.AI; PDF: https://arxiv.org/pdf/2610.28909v1; accepted to EMNLP 2026 Industry Track; code: https://github.com/alanrbtx/DiffResearch; citation count: [NO DATA — paper 2026-10-20]