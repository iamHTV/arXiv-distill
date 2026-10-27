# Skill: lessons-from-luck-memory-writing-test
Source: 2610.33029v1
Type: evaluation-method

## Khi nào dùng skill này
- Cần kiểm tra xem hướng dẫn viết bài học (memory-writing instruction) của agent tự cải tiến có mang kết quả do ngẫu nhiên vào quyết định sau hay không.
- Muốn so sánh các hướng dẫn viết memory (ví dụ: định tuyến theo kết quả vs hướng dẫn duy nhất) theo khả năng chống lại luck-carrying.
- Muốn đánh giá xem bài học viết sau sự cố ngẫu nhiên có làm agent chọn công cụ kém hơn trong lần chạy sau hay không.

## Tình huống KHÔNG nên dùng
- Agent không ghi memory từ các lần chạy trước (read-only, không tự cải tiến).
- Muốn ước lượng tần suất agent thực tế gặp tình huống luck-carrying — nghiên cứu không ước lượng điều này.

## Input cần có
- Hai công cụ hoán đổi được (interchangeable tools) với độ tin cậy đã ghi nhận (tỷ lệ thành công của từng công cụ qua các lần chạy trước).
- Một bộ thế giới giả lập (synthetic worlds), mỗi thế giới có tác vụ vận hành lặp lại, log chạy trước (run log), và 4 lần chạy scripted: quyết định tốt/xấu chéo với thành công/sự cố.
- 3 hướng dẫn viết bài học (ví dụ: RB, RBD, N) để tạo bài học từ từng lần chạy.
- Một model làm người viết (writer) và cùng model làm người đọc (reader) trong phiên mới.

## Các bước thực hiện
1. Scripted 4 lần chạy trước cho mỗi thế giới: quyết định tốt (gọi công cụ tốt) hoặc quyết định xấu (gọi công cụ kém), kết quả thành công hoặc sự cố瞬arna (transient failure).
3. Mỗi model viết bài học từ lần chạy với một trong các hướng dẫn viết (RB, RBD, N); lưu toàn bộ phản hồi viết làm một khối memory.
4. Một phiên mới của cùng model đọc memory item (bài học đó, bài học từ kết quả khác, item không liên quan, hoặc chỉ thị không suy luận PLANTED) cùng với log quyền thẩm quyền và kết quả lần chạy trước.
5. Người đọc chọn công cụ sẽ gọi đầu tiên cho lần chạy tiếp theo (trả về JSON first_tool).
6. Tính đối số chính P2 (quyết định tốt) và P3m (quyết định xấu): sự tương tác giữa kết quả và mục ký úcu, so sánh so với item không liên quan (NEUTRAL).
7. Xác định reading: luck-carrying (phát hiện, cả 2 qualifier A và L mạnh dương), outcome-dependent (phát hiện nhưng 1 qualifier không mạnh dương), hoặc bounded below 0.10 (giữ tương tác dưới 0.10).

## Output mong đợi
- P2 estimate với khoảng tin cậy 95% (đăng ký): dương và cả 2 Holm-adjusted p-values dưới 0.05 → luck-carrying.
- P3m estimate: dưới 0.10 → bounded.
- Worse-tool rate cho mỗi ô (decision × outcome × memory arm).
- Biện pháp khắc phục được công nhận nếu cả sự khác biệt P và sự khác biệt A đều có khoảng tin cậy dưới 0.

## Ví dụ áp dụng
Công ty có agent viết bài học sau mỗi lần xử lý đơn hàng và đọc bài học trước lần sau. Hướng dẫn viết hiện tại định tuyến theo thành công/thất bại. Kiểm tra luck-carrying: tạo thế giới với hai công cụ xử lý đơn hàng (công cụ A tỷ lệ thành công 0.85, công cụ B 0.60), scripted một lần chạy gọi công cụ A (quyết định đúng) nhưng kết quả thất bại do ngẫu nhiên. Agent viết bài học từ sự cố đó. Phiên mới đọc bài học và chọn công cụ cho lần sau. Nếu tỷ lệ chọn công cụ B tăng đáng kể so với item không liên quan → luck-carrying phát hiện, cần áp dụng biện pháp khắc phục (ghi chú chất lượng quyết định hoặc hướng dẫn duy nhất với tùy chọn không thay đổi).

## Gotchas
- Bài học và sự cố báo cáo được đọc cùng nhau — không thể tách lời khuyên của bài học khỏi báo cáo lần thứ hai về sự cố.
- Biện pháp khắc phục chỉ được kiểm tra với kết quả không báo hiệu sự thay đổi trong độ tin cậy của công cụ (sự cố transient, công cụ tốt vẫn tốt hơn sau kết quả bất kỳ).
- N vs RB là một so sánh phức hợp (N khác ở 2 điểm: không định tuyến theo kết quả và có tùy chọn không thay đổi).
- Mỗi endpoint viết bài học mà chính endpoint đó đọc, nên sự khác biệt giữa endpoint không thể gán riêng cho viết hay cho đọc.
- Mỗi ô chỉ có một lần sinh (one generation), nghiên cứu chưa được sao chép (replicated).