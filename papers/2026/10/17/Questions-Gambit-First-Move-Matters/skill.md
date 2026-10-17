# Skill: questions-gambit-first-move-retrieval
Source: 2609.14412v1
Type: framework

## Khi nào dùng skill này
- Xây dựng tác nhân tìm kiếm sâu (deep search agent) trả lời câu hỏi phức tạp thông qua các vòng lặp tìm kiếm, đọc, và suy luận.
- Cần cải thiện bước truy xuất đầu tiên (first move) — ngữ cảnh mở (opening context) mà agent nhận được trước khi bắt đầu vòng lặp tìm kiếm.
- Có một tập hợp tài liệu (corpus) cố định để truy xuất và một công cụ truy xuất (retriever tool).

## Tình huống KHÔNG nên dùng
- Câu hỏi không đa-clue (không phải multi-clue — không có nhiều ràng buộc khác nhau cần bằng chứng từ các tài liệu khác nhau).
- Không có công cụ truy xuất (retriever) hoặc không thể xây dựng ngữ cảnh mở.
- Tìm kiếm trên web trực tiếp (live web search) thay vì trên tập dữ liệu cố định.

## Input cần có
- Câu hỏi phức tạp (complex question) với nhiều ràng buộc khác nhau (multi-clue).
- Tập hợp tài liệu (corpus) để truy xuất.
- Công cụ truy xuất (retriever tool) trả về danh sách xếp hạng các tài liệu.
- Mô hình ngôn ngữ lớn (large language model) để phân tích câu hỏi thành các clues và làm agent.

## Các bước thực hiện
1. Phân tích câu hỏi thành tập hợp các clues (mảnh thông tin/ràng buộc) — mỗi clue là một ràng buộc duy nhất mà câu trả lời phải thỏa mãn.
2. Truy xuất từng clue độc lập: đưa mỗi clue vào trình truy xuất, giữ các tài liệu trả về làm tập phản hồi (feedback set).
3. Mở rộng từng clue: dùng mô hình mở rộng (expansion model) viết lại clue dựa trên tập phản hồi, sau đó nối clue, sự mở rộng, và câu hỏi gốc thành một chuỗi tìm kiếm duy nhất.
4. Hợp nhất các danh sách theo từng clue vào một nhóm đã loại trùng lặp (deduplicated pool).
5. Xếp hạng lại nhóm theo câu hỏi gốc bằng bộ xếp hạng theo điểm (pointwise reranker) — mỗi tài liệu được đánh giá theo mức độ phục vụ câu hỏi như một toàn thể.
6. Lấy k tài liệu có điểm cao nhất tạo thành ngữ cảnh mở (opening context O).
7. Đưa ngữ cảnh mở vào quỹ đạo agent làm quan sát đầu tiên (o1), sau đó agent tiếp tục vòng lặp tìm kiếm và suy luận bình thường.

## Output mong đợi
- Độ chính xác câu trả lời cải thiện: GPT-5.5 từ 83.1% lên 90.5% (+7.4 pp), GPT-5.4-mini từ 68.1% lên 79.0% (+10.9 pp), DeepSeek-v4-pro từ 71.4% lên 76.9% (+5.5 pp).
- Sai số hiệu chuẩn (calibration error) giảm: GPT-5.5 từ 15.7 xuống 7.58.
- Khả năng lấy lại tài liệu vàng (gold recall) cải thiện ở mọi giai đoạn: surfaced từ 94.4 lên 98.1, previewed từ 72.9 lên 85.9, behavior từ 56.1 lên 75.9 (với GPT-5.5).

## Ví dụ áp dụng
- Tác nhân nghiên cứu sâu trả lời câu hỏi "Ai là vợ của Aman?" với nhiều ràng buộc (di cư từ 1890-1899, làm nông dân tại Washington, sự kiện lớn tại khách sạn cưới 1940-1944, tên xuất hiện trên danh sách sử tại Montana trước 2023): tách câu hỏi thành các clues riêng biệt, truy xuất từng clue, gộp và xếp hạng lại theo câu hỏi hoàn chỉnh, đưa ngữ cảnh mở cho agent trước khi bắt đầu vòng lặp tìm kiếm.

## Gotchas
- Đánh giá tập trung vào tìm kiếm sâu trên tập dữ liệu cố định (fixed-corpus); sự chuẩn hoá sang tìm kiếm trên web trực tiếp chưa được nghiên cứu.
- Module chạy một lần hoàn toàn trong hành động đầu tiên của agent — không yêu cầu đào tạo lại agent hay trình truy xuất.
- Số lượng lệnh gọi công cụ tăng 2.3–5.3 lần gọi tổng cộng nhưng chỉ tập trung chủ yếu ở hành động đầu tiên và việc đọc tài liệu tiếp theo; số lệnh gọi tìm kiếm do agent phát ra vẫn tương đương.
