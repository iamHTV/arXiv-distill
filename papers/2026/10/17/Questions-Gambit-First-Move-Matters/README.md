# [2609.14412v1] Question's Gambit: The First Move Matters in Agentic Deep Search

## Problem
- Các tác nhân nghiên cứu sâu (deep research agents) trả lời các câu hỏi phức tạp qua các vòng lặp lặp đi lặp lại của tìm kiếm, đọc, và suy luận. Prior work chưa giải quyết được việc chất lượng của bước truy xuất đầu tiên (first move) trong quá trình tìm kiếm của agent — nếu các tìm kiếm sớm chỉ bềnh bằng chứng (evidence) cho một số clues (mảnh thông tin), agent có thể bị dẫn hướng một giả thuyết không hoàn chỉnh và bỏ vòng sau đó đi theo nó.

## Contribution
- Question's Gambit — một module truy xuất bước đầu tiên (first-move retrieval module) phân tích câu hỏi thành một tập hợp các clues (mảnh thông tin), định dạng lại chúng thành các tìm kiếm bổ sung (complementary searches), tổng hợp (consolidate) kết quả được truy xuất, và xếp hạng lại (rerank) nhóm ứng viên trước khi agent bắt đầu quá trình tìm kiếm và suy luận lặp đi lặp lại (iterative search-and-reasoning process).
- Điều này tạo ra một ngữ cảnh mở (opening context) được thiết kế để hỗ trợ cả việc tổng hợp clues và xác minh câu trả lời cuối cùng.
- Đánh giá thêm trên MultiHop-RAG để kiểm tra xem những lợi ích này có chuyển giao (transfer) vượt qua BrowseComp-Plus sang một cấu trúc câu hỏi đa bước (multi-hop question structure) thông thường hơn hay không.

## Method (tóm tắt cốt lõi)
- Bài toán: Cho một câu hỏi phức tạp q và một tập hợp tài liệu D, nhiệm vụ là tạo ra một câu trả lời y khớp với câu trả lời tham chiếu y⋆. Các câu hỏi này được đặc trưng là đa-clue (multi-clue): mỗi câu hỏi chứa một tập tiềm ẩn các yếu tố thông tin khác nhau (heterogeneous information elements), như mô tả một phần, ngày tháng, địa điểm, tiêu đề, hoặc liên kết, mà cùng nhau ràng buộc câu trả lời.
- Một tác nhân tìm kiếm sâu (deep search agent) sử dụng một mô hình ngôn ngữ lớn Sθ hoạt động thông qua chính sách của nó πθ, đưa ra các truy vấn văn bản x của nó, và nộp chúng cho một công cụ truy xuất (retriever tool) R, który trả về một danh sách xếp hạng các tài liệu.
- Question's Gambit tiến hành ba giai đoạn:
  1. Phân tích câu hỏi (Question Decomposition): một bộ phân tích (decomposer) trích xuất tập hợp các clues từ câu hỏi, tách biệt các ràng buộc mà một truy vấn toàn bộ câu hỏi sẽ trộn lẫn lại với nhau.
  2. Truy xuất theo từng clue (Per-Clue Retrieval): mỗi clue được đưa ra cho trình truy xuất, và các tài liệu nó trả về đóng vai trò là ngữ cảnh cho việc mở rộng clue đó, vì vậy truy vấn được dùng cho truy xuất được căn cứ trên thuật ngữ mà tập hợp tài liệu chứa (corpus) thay vì trên kiến thức tham số (parametric knowledge) của mô hình mở rộng (expansion model).
  3. Xếp hạng lại theo câu hỏi (Question-Conditioned Reranking): các danh sách theo từng clue được hợp nhất thành một nhóm đã loại trùng lặp và xếp hạng lại theo câu hỏi gốc, và các tài liệu có điểm số cao nhất tạo thành ngữ cảnh mở.
- Module chạy một lần, hoàn toàn trong hành động đầu tiên của agent, và trả về một ngữ cảnh mở O có kích thước k mà vào quỹ đạo (trajectory) như quan sát đầu tiên o1. Nó không yêu cầu đào tạo lại (retraining) agent hay trình truy xuất và để vòng lặp tìm kiếm sau đó không thay đổi.

## Key Findings
- 7 tác giả từ Đại học Toronto, Mila – Viện Trí tuệ Nhân tạo Quebec, Đại học Waterloo, Đại học California Berkeley, Đại học McGill, category arXiv: cs.AI, cs.CL, cs.IR.
- Thí nghiệm trên BrowseComp-Plus cho thấy Question's Gambit cải thiện việc lấy lại văn bản (retrieval recall) và độ chính xác của tác nhân phía sau (downstream agent accuracy) so với các bước tham chiếu mạnh (strong baselines), cải thiện độ chính xác câu trả lời từ 83.1% lên 90.5% với gpt-5.5 qua Pi-Serini, bước tham chiếu agentic mạnh nhất được báo cáo.
- DeepSeek-v4-pro: 71.4% → 76.9% (+5.5 điểm phần trăm); GPT-5.4-mini: 68.1% → 79.0% (+10.9 điểm phần trăm); GPT-5.5: 83.1% → 90.5% (+7.4 điểm phần trăm).
- Sai số hiệu chuẩn (calibration error) giảm từ 7.0 xuống 3.99 cho DeepSeek-v4-pro, từ 13.7 xuống 7.90 cho GPT-5.4-mini, và từ 15.7 xuống 7.58 cho GPT-5.5. Tất cả ba sự cải thiện độ chính xác đều có ý nghĩa thống kê.
- Lợi ích cũng mở ra ngoài kết quả truy xuất ban đầu. Với GPT-5.5, surfaced gold recall tăng từ 94.4 lên 98.1, previewed gold recall từ 72.9 lên 85.9, và behavior gold recall từ 56.1 lên 75.9.
- MultiHop-RAG: Question's Gambit cải thiện độ chính xác GPT-5.4-mini từ 76.0% lên 77.0% và GPT-5.5 từ 81.0% lên 81.5%.

## Actionable Insights
1. Bước truy xuất đầu tiên (first move) trong các tác nhân tìm kiếm sâu (deep search agents) là một quyết định thiết kế quan trọng — chất lượng của ngữ cảnh mở quan trọng hơn các công cụ có sẵn bên trong vòng lặp. Áp dụng: đưa vào cho agent một ngữ cảnh mở đã chuẩn bị chứa bằng chứng cho các clues, thay vì để agent tự tìm kiếm từ câu hỏi nguyên bản.
2. Phân tích câu hỏi thành các clues riêng biệt và truy xuất mỗi clue độc lập, sau đó gộp và xếp hạng lại theo câu hỏi hoàn chỉnh. Áp dụng: trước khi agent bắt đầu vòng lặp tìm kiếm, tách câu hỏi thành các ràng buộc riêng biệt, truy xuất từng ràng buộc, gộp kết quả và xếp hạng lại theo câu hỏi hoàn chỉnh.

## Assumptions & Limitations
- Đánh giá tập trung vào tìm kiếm sâu trên tập dữ liệu cố định (fixed-corpus deep research), dùng toàn bộ chuẩn mốc BrowseComp-Plus và một tập kiểm soát 200 câu hỏi MultiHop-RAG; sự chuẩn hoá (generalization) sang các tập dữ liệu khác và tìm kiếm trên web trực tiếp (live web search) vẫn cần được nghiên cứu.
- Đánh giá ba tác nhân (agent models).

## Metadata
- Năm: 2026, tác giả: Radin Hamidi Rad, Amin Bigdeli, Negar Arabzadeh, Sajad Ebrahimi, Charles L. A. Clarke, Benjamin C. M. Fung, Ebrahim Bagheri (Đại học Toronto, Mila – Quebec AI Institute, Đại học Waterloo, Đại học California Berkeley, Đại học McGill), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.14412v1
