# Skill: structural-retrieval-evaluation
Source: 2609.01556v1
Type: evaluation-method

## Khi nào dùng skill này
- Đánh giá hệ thống truy xuất (retrieval system) trên các trường hợp cấu trúc (structural cases) — truy xuất mục tiêu chia sẻ cấu trúc cơ bản nhưng không chia sẻ cách viết (wording).
- Cần kiểm tra xem hệ thống truy xuất có neo chặt vào nội dung bề mặt (literal surface content) hay cấu trúc cơ bản (underlying structure).
- Có hai miền dữ liệu khác nhau để kiểm tra (ví dụ: toán học và quỹ đạo tác nhân hóa thân).

## Tình huống KHÔNG nên dùng
- Chỉ đánh giá trên các truy vấn có hình thức bề mặt và ý nghĩa hướng cùng cách.
- Không có dữ liệu cấu trúc (cấu trúc cơ bản nhưng cách viết khác nhau).
- Không cần đánh giá khả năng nhận diện cấu trúc (structure-awareness).

## Input cần có
- Bộ truy vấn có cấu trúc (structural queries) — truy vấn nơi hình thức bề mặt và ý nghĩa bị tách rời.
- Corpus mục tiêu (target corpus) với các mục chia sẻ cấu trúc cơ bản nhưng cách viết khác nhau.
- Nhãn vàng (gold labels) cho các mục đúng.
- Bộ reranker từ vựng (lexical reranker) và LLM reranker để so sánh.

## Các bước thực hiện
1. Xây dựng bộ truy vấn cấu trúc (structural queries) với các mức độ lừa (disguise tiers): dễ, trung bình, nặng.
2. Xây dựng corpus với các mục tương đương cách thức (semantically equivalent) nhưng cách viết khác nhau, cùng các near-miss decoys giữ lại hình thức bề mặt.
3. Chạy truy xuất nhúng (embedding retrieval) và đo strict Hit@k và lenient Hit@10.
4. Chạy điều khiển từ vựng (lexical control/reranker) và quan sát xem nó giúp hay hỏng.
5. Chạy LLM reranker (có thể dùng nhiều bảng xét xử/judges) và đo phần khoảng có thể phục hồi (recoverable gap) được khôi phục.
6. Phân tích kết quả: xem việc nhúng truy xuất có neo chặt vào nội dung bề mặt hay không, xem điều khiển từ vựng có lật dấu (sign flip) hay không.
7. Kiểm tra sự nhiễm độc (contamination): xem lời gọi reranking có tập trung vào các mục nổi tiếng (well-known items) hay không.

## Output mong đợi
- Điểm số strict Hit@k và lenient Hit@10 cho hệ thống truy xuất.
- Xác định xem hệ thống truy xuất có neo chặt vào nội dung bề mặt hay không.
- Đánh giá xem điều khiển từ vựng có giúp hay hỏng, và điều đó cho biết gì về chế độ biến thiên bề mặt của chuẩn mốc.

## Ví dụ áp dụng
- Đánh giá hệ thống truy xuất cho câu hỏi toán học: tạo các truy vấn có cùng cấu trúc toán học nhưng cách viết khác nhau, kiểm tra xem hệ thống truy xuất có chọn mục đúng hay chọn mục có từ vựng tương tự hơn.

## Gotchas
- Toán học sử dụng một hạt giống (single fixed seed) duy nhất; khoảng tin cậy bootstrap chỉ định lượng sự không chắc chắn trong mẫu.
- Ba bảng xét xử (three judges) là một mẫu nhỏ; kích thước tác động thay đổi hơn bát lần giữa chúng.
- Mỗi miền (domain) có một ngoại lai (outlier) khác nhau và hồ sơ cấp (tier profile) khác nhau.
