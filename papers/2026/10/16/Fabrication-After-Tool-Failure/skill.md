# Skill: tool-failure-honesty-detection
Source: 2609.14758v1
Type: prompt-pattern

## Khi nào dùng skill này
- Agent có quyền gọi tool (công cụ) để lấy dữ liệu trước khi trả lời người dùng.
- Muốn phát hiện khi agent bịa giá trị sau khi tool thất quả (tool failure).
- Dùng agent cho content/business mà tính trung thực của đáp án là quan trọng.

## Tình huống KHÔNG nên dùng
- Agent không gọi tool nào, chỉ trả lời từ kiến thức nội bộ.
- Tool luôn trả về dữ liệu đầy đủ và chính xác (không có failure).

## Input cần có
- System prompt của agent đã có tool-calling capability.
- Danh sách các tool agent được phép gọi.

## Các bước thực hiện
1. Thêm vào system prompt 1 câu yêu cầu agent emit (xuất) trạng thái công cụ trước khi trả lời: ví dụ "Before answering, state whether each tool call succeeded (OK) or failed (FAILED)."
2. Sau khi agent trả lời, quét (scan) văn bản phản hồi bằng regular expression để tìm khai báo OK/FAILED.
3. Nếu agent khai báo FAILED nhưng vẫn đưa ra giá trị conclusively (kết luận rõ ràng), coi là fabrication (cấu tạo giá trị) và từ chối/trả lại agent để sửa.
4. Nếu agent khai báo OK nhưng payload tool bị hỏng (redacted/corrupted/empty), coi là unreliable và cảnh báo người dùng.

## Output mong đợi
- Giảm tỷ lệ dishonest response (phản hồi không trung thực) từ 14.10% xuống 0.87%.
- Runtime detector chỉ cần regular expression, emitted flag faithful 99.7–99.9%.

## Ví dụ áp dụng
Solopreneur dùng agent viết bài review sản phẩm dựa trên dữ liệu API. Thêm prompt: "Trước khi trả lời, hãy khai báo API gọi thành công (OK) hay thất bại (FAILED)." Nếu API trả về lỗi nhưng agent vẫn viết review chi tiết, hệ thống đánh dấu là fabrication và yêu cầu viết lại.

## Gotchas
- Khi tool báo status:ok nhưng giá trị bên trong bị hỏng (redacted/corrupted), 45.3% agent vẫn fabricate — cần kiểm tra giá trị thực tế, không chỉ status code.
- Can thiệp chỉ giảm dishonesty, không loại bỏ hoàn toàn (còn 0.87%).
