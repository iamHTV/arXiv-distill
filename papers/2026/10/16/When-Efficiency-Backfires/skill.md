# Skill: cascade-attack-awareness
Source: 2605.17288v1
Type: framework

## Khi nào dùng skill này
- Xây hoặc dùng hệ thống cascade LLM (mô hình nhẹ xử lý truy vấn đơn giản, mô hình mạnh xử lý truy vấn phức tạp).
- Muốn đánh giá độ bền (robustness) của hệ thống cascade trước tấn công đối thủ.
- Cần thêm các cơ chế phòng thủ cho hệ thống cascade LLM.

## Tình huống KHÔNG nên dùng
- Chỉ dùng một mô hình LLM đơn lẻ, không có hệ thống cascade.
- Không cần đánh giá độ bền, chỉ cần hiệu năng.

## Input cần có
- Hệ thống cascade LLM (mô hình nhẹ + mô hình mạnh).
- Dữ liệu truy vấn thật hoặc giả để thử nghiệm tấn công.
- Cơ chế tấn công đối thủ (adversarial attack) để thử nghiệm.

## Các bước thực hiện
1. Xây hệ thống cascade LLM: mô hình nhẹ xử lý truy vấn đơn giản, mô hình mạnh xử lý truy vấn phức tạp (escalation).
2. Thử nghiệm hệ thống với các tấn công đối thủ (adversarial attacks): adversarial suffixes, jailbreak prompts, v.v.
3. Đo độ chính xác dự đoán, chi phí token, thời gian thực thi, và tỷ lệ thành công tấn công trước và sau tấn công.
4. Thêm các cơ chế phòng thủ: input sanitization (làm sạch đầu vào), output validation (xác thực đầu ra), rate limiting (giới hạn tỷ lệ), adversarial training (huấn luyện chống tấn công).
5. Thử nghiệm lại hệ thống sau khi thêm phòng thủ để xác nhận hiệu quả.

## Output mong đợi
- Giảm việc giảm accuracy (giảm từ 84.6% xuống mức thấp hơn).
- Giảm việc tăng token cost (tăng từ 148.9% xuống mức thấp hơn).
- Giảm việc tăng execution time (tăng từ 108.9% xuống mức thấp hơn).
- Giảm attack success rate (tăng từ 81.4% xuống mức thấp hơn).

## Ví dụ áp dụng
Solopreneur xây hệ thống cascade LLM cho chatbot khách hàng: mô hình nhẹ xử lý câu hỏi đơn giản, mô hình mạnh xử lý câu hỏi phức tạp. Thử nghiệm với các tấn công đối thủ (ví dụ câu hỏi có chứa lệnh nhúng, jailbreak prompts). Thêm input sanitization và output validation để giảm rủi ro. Giảm việc hệ thống bị lừa hoặc tạo ra nội dung không mong muốn.

## Gotchas
- Hệ thống cascade LLM có thể bị kích hoạt thất bại lan rộng (cascade failure) dưới tấn công đối thủ.
- Tấn công có thể giảm accuracy lên đến 84.6%, tăng token cost lên 148.9%, tăng execution time lên đến 108.9%.
- Nên đánh giá độ bền trước khi triển khai production, không nên tin tưởng cascade là an toàn tự động.
