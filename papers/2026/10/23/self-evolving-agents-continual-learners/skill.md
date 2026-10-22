# Skill: Tách biệt cập nhật harness theo tác vụ (self-evolving agent isolation)
Source: 2610.25858
Type: framework

## Khi nào dùng skill này
- Agent cần thích ứng liên tục với tác vụ mới mà không quên tác vụ cũ (học liên tục / continual learning).
- Harness agent dùng chung cho nhiều nhóm tác vụ khác nhau.
- KHÔNG dùng khi các tác vụ đến từ cùng domain nhưng đòi hỏi quy trình nghịch đảo (ví dụ hỏi suy cho cùng vs gọi công cụ trực tiếp) — cần cơ chế tách biệt rõ ràng hơn.

## Input cần có
- Harness agent ban đầu (system prompt, bộ nhớ, thư viện kỹ năng, mã điều khiển).
- Dòng tác vụ đến liên tục (streaming task stream).
- Cơ chế đánh giá hiệu suất trên mỗi nhóm tác vụ (hold-out sets).

## Các bước thực hiện
1. Thiết kế harness sao cho cập nhật cho tác vụ A không ảnh hưởng đến tác vụ B (ví dụ dùng namespace/module riêng cho từng nhóm tác vụ thay vì prompt toàn cục duy nhất).
2. Nếu dùng truy xuất ký tự kinh nghiệm (memory retrieval), thêm bộ lọc ngữ cảnh trước khi đưa ký tự vào prompt: kiểm tra xem quy trình làm việc của ký tự đã lưu có phù hợp với tác vụ đến hay không.
3. Tránh áp dụng chỉnh sửa toàn cầu vào system prompt hoặc workspace dùng chung cho mọi tác vụ tiếp theo.
4. Theo dõi độ ổn định (stability) qua các điểm kiểm tra (checkpoint) trên các nhóm tác vụ trước, không chỉ đo trên nhóm đang đào tạo.

## Output mong đợi
- Giảm can thiệp chéo tác vụ và quên sau block so với phương pháp sửa đổi prompt toàn cục (GEPA/Meta-Harness).
- Tăng độ ổn định trung bình (S = −1.9 vs −4.3 cho GEPA) với hy sinh phần linh hoạt (P = +3.3 vs +6.2 cho GEPA).

## Ví dụ áp dụng
- Agent hỗ trợ lập trình xử lý các tác vụ từ nhiều ngôn ngữ lập trình: mỗi ngôn ngữ có module skill riêng, cập nhật cho Python không ảnh hưởng đến JavaScript, truy xuất kỹ năng chỉ khi ngữ cảnh khớp quy trình làm việc.

## Gotchas
- Mô hình base cố định (Gemini 3.6 Flash), chưa quét rộng họ mô hình.
- Các block tác vụ là liên tiếp; tác vụ xen kẽ vẫn gây giảm sút (GEPA terminal advantage từ +5.8 xuống +0.9 khi xen kẽ).
- Truy xuất dựa trên độ tương đồng không tách được các tác vụ dùng cùng không gian embeddings nhưng đòi hỏi quy trình khác nhau.