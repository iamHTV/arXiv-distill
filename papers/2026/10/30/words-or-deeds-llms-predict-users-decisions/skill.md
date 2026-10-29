# Skill: dialogue-user-decision-evaluation (đánh giá dự đoán quyết định người dùng từ hội thoại)

Source: 2610.36813v1
Type: evaluation-method / workflow

## Khi nào dùng skill này

- Bạn đang xây dựng agent/LLM dự đoán quyết định hành động của người dùng từ nội dung hội thoại (ví dụ agent bán hàng đoán user sẽ chấp nhận offer hay không).
- Bạn muốn đánh giá xem predictor có over-estimate lời hứa của người dùng hay không, và có bắt được sự thay đổi hành vi theo từng agent/persona hay không.
- Bạn cần báo cáo chất lượng dự đoán theo từng loại lời (giữ/phá) và theo từng agent, không chỉ accuracy tổng hợp.

Tình huống KHÔNG nên dùng:
- Chỉ cần ước lượng xu hướng hợp tác chung, không cần chi tiết từng người dùng.
- Agent không gọi công cụ bên ngoài, không có lời hứa hay cam kết trong hội thoại.

## Input cần có

- Bộ dữ liệu tương tác: cho mỗi vòng, có lời người dùng nói (stated decision), quyết định thực tế (cooperate/defect), agent người dùng đối diện, và lịch sử quyết định trước đó của cả hai bên.
- Các persona agent (ít nhất 2 agent có hành vi khác nhau) để so sánh.
- Một LLM predictor (hoặc nhiều) để chạy dự đoán.
- Công cụ tính AUC, accuracy, và prediction bias (dự đoán − thực tế).

## Các bước thực hiện

1. Thu thập dữ liệu liên kết: cho mỗi tương tác, ghi lại lời người dùng nói về quyết định của họ, quyết định thực tế sau đó, agent họ đối diện, và lịch sử quyết định trước đó của cả người dùng và agent.
2. Chia dữ liệu thành các nhóm: lời được giữ (statement kept), lời bị phá (statement broken), lời mâu thuẫn với quyết định trước đó, và theo từng agent/persona.
3. Chạy predictor trên từng tổ hợp thông tin (hồ sơ quyết định R và hội thoại D theo 19 tổ chức), tính AUC và accuracy trên mỗi nhóm.
4. Thêm một câu thông báo quyết định vào các vòng không có lời khai báo, đo sự thay đổi của dự đoán so với việc hoán đổi quyết định trước đó của người dùng.
5. Thêm điểm tính cách (BFI) hoặc điểm tương thích vào prompt, đo mức độ giảm sai số dự đoán (bias).
6. Báo cáo kết quả riêng cho lời giữ và lời bị phá, và riêng cho mỗi agent; không chỉ báo accuracy tổng hợp.

## Output mong đợi

- AUC và accuracy của predictor theo từng loại lời (giữ/phá) và theo từng agent.
- Mức predictor over-estimate tỷ lệ giữ lời (dự đoán giữ lời cao hơn thực tế bao nhiêu).
- Chênh lệch dự đoán (bias) giữa các agent (ví dụ +8.6 điểm với agent một loại, −6.0 điểm với loại khác).
- Khả năng dự đoán có thay đổi đáng kể khi thêm hội thoại hay không.

## Ví dụ áp dụng

Agent bán hàng cần quyết định ajuste giá dựa trên lời hứa của khách hàng ("Tôi sẽ mua nếu giảm 10%"). Áp dụng skill: (1) lưu mỗi lời hứa và liệu khách hàng có mua sau đó hay không; (2) chia thành lời giữ và lời phá; (3) chạy model dự đoán trên hồ sơ mua hàng trước + nội dung hội thoại; (4) đo AUC riêng cho lời giữ và lời phá; (5) nếu model dự đoán giữ lời .70 nhưng thực tế chỉ .40, giảm trọng số lời hứa mới trong quyết định nhượng giá. Kết quả: agent không nhượng quá mức dựa trên lời h unreliable.

## Gotchas

- Lời hứa trong hội thoại không nên được cân nặng bằng hành động thực tế; cần theo dõi tỷ lệ giữ lời của mỗi người dùng.
- Thêm nội dung hội thoại vào input model không nhất quán tăng AUC (từ .80 lên .79, không tăng đáng được) — không nên bỏ qua lịch sử quyết định thật để échanges thêm hội thoại.
- Accuracy tổng hợp gần zéro bias có thể ẩn giấu sai số lớn trên từng agent (chênh lệch lên đến 14.6 điểm giữa agent).
- Thêm điểm tính cách vào prompt chỉ giảm sai số khoảng một phần tư — phần lớn sai số còn lại.
- Nghiên cứu chỉ dùng 42 sinh viên Trung Quốc, ván chơi ngắn thấp rủi ro, tất cả đối tác là GPT-4o — kết quả có thể khác trên dữ liệu thực tế.
