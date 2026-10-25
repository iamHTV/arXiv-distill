# Skill: inhibitory-message-passing-router

Source: 2610.24718
Type: framework

## Khi nào dùng skill này

- Nhóm agent cần tổng hợp bằng chứng phân tán để đưa ra quyết định được chấm điểm (nghiên cứu, phân tích, chẩn đoán).
- Muốn giữ độ chính xác ổn định khi nhóm agent lớn hơn mà không tăng token theo cấp số nhân.
- Có thể xác định được câu bằng chứng mỗi agent nắm giữ và khớp chúng với nội dung tin nhắn gửi đi.

## Tình huống KHÔNG nên dùng

- Công việc đòi hỏi agent trao đổi kết quả trung gian không chứa trong bằng chứng gốc (lập trình, lập kế hoạch, tính toán phân tán).
- Nhiệm vụ không có bằng chứng rõ ràng để khớp (viết sáng tạo, tư thảo).

## Input cần có

- Danh sách các câu bằng chứng mỗi agent nắm giữ (liệt kê rõ, có mã nguồn/source tag).
- Tin nhắn mỗi agent viết mỗi vòng (dưới 100 từ/tin nhắn).
- Bộ quy tắc router: truyền bằng chứng gốc, một lần mỗi vòng, chỉ nếu người nhận chưa có.

## Các bước thực hiện

1. Mỗi agent viết tin nhắn chứa lý luận và câu trả lời, đồng thời diễn giải lại câu bằng chứng nó nắm giữ (dùng từ hiếm để router khớp được).
2. Router cho mỗi người nhận: lấy tất cả câu bằng chứng được diễn giải lại trong tin nhắn của người gửi, giữ lại chỉ câu gốc (không lấy lý luận/câu trả lời của người gửi).
3. Trừ đi các câu bằng chứng người nhận đã có trong bằng chứng riêng của mình.
4. Giới hạn mỗi câu bằng chứng được gửi tối đa một lần mỗi vòng cho mỗi người nhận (bất kể bao nhiêu người gửi diễn giải lại).
5. Gửi hộ thư (inbox) đã lọc cho mỗi người nhận; agent đọc inbox và viết tin nhắn mới vòng tiếp theo.

## Output mong đợi

- Hộ thư của mỗi người nhận chỉ chứa câu bằng chứng gốc nó chưa có, không kèm lý luận hay câu trả lời của người gửi.
- Kích thước hộ thư không tăng theo số lượng agent trong nhóm.
- Độ chính xác nhóm ổn định hoặc tăng khi nhóm lớn hơn, token mỗi chạy giảm.

## Ví dụ áp dụng

Nhóm 4 agent chẩn đoán bệnh nhân đau ngực: tất cả đọc biểu đồ (bằng chứng chung đề xuất đau tim), 3 agent dùng công cụ riêng mỗi người nhận một kết quả (bằng chứng riêng). Truyền thông chuẩn gửi toàn bộ tin nhắn (kèm kết quả "đau tim" của đa số) → bệnh nhân được chẩn đoán sai. Router inhibitory truyền chỉ kết quả công cụ mỗi agent chưa biết (troponin bình thường, chênh lệch huyết áp tay) → cùng kết luận là phế đại mạch chủ, đúng.

## Gotchas

- Router không đánh giá độ tin cậy của bằng chứng nó truyền: câu bằng chứng sai được gieo vào sẽ làm giảm độ chính xác (không thể rút lại bằng chứng sau khi sửa lỗi).
- Cần liên kết đáng tin cậy giữa tin nhắn và bằng chứng nó đề cập (provenance); sai sót sẽ dùng bằng chứng hữu ích hoặc để lại đầu vào dư thừa.
- Không thiết lập được khi loại trừ lý luận/câu trả lời sẽ cản trở hợp tác trên công việc cần trao đổi kết quả trung gian (code, kế hoạch).
