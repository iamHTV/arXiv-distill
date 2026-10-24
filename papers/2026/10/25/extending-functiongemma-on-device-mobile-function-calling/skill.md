# Skill: Huấn luyện mô hình gọi hàm thiết bị cục bộ (on-device function-calling fine-tuning)

Source: 2609.25373v2
Type: workflow

## Khi nào dùng skill này

- Cần một mô hình nhỏ (dưới 1 tỷ tham số) điều khiển các hành động thiết bị cục bộ (bật/tắt flashlight, gửi SMS, gọi điện, mở ứng dụng, tra pin) mà không gửi yêu cầu lên đám mây.
- Có danh sách công cụ (tool catalog) với lược đồ JSON rõ ràng và muốn mở rộng mô hình gọi hàm hiện có sang nhiều danh mục hành động mới.
- Muốn duy trì khả năng gọi hàm trên các công cụ cũ trong khi thêm công cụ mới (tránh quên năng lực cũ).

## Tình huống KHÔNG nên dùng

- Mỗi danh mục công việc yêu cầu độ chính xác tuyệt đối trên một nhóm công cụ cố định và không chấp nhận chia sẻ trọng số giữa các danh mục.
- Thiết bị mục tiêu là iOS hoặc không hỗ trợ LiteRT-LM / chạy mô hình cục bộ.
- Nhu cầu phản hồi dưới 1 giây mỗi lượt (latency ~13 giây trên Pixel 8 Pro có thể quá chậm).

## Input cần có

- Danh sách công cụ (tool catalog) dưới dạng JSON: tên hàm, mô tả bằng tiếng tự nhiên, lược đồ tham số (parameter schema).
- Mô hình backbone gọi hàm (function-calling model) đã instruction-tuned (ví dụ: FunctionGemma 270M-it).
- LLM mạnh làm giáo viên (teacher LLM) để tạo cuộc hội thoại tổng hợp.
- Script kiểm định (validator) để kiểm tra tên hàm có trong danh mục, đối số bắt buộc có mặt và đúng kiểu.
- Môi trường huấn luyện với GPU đơn (CUDA hoặc Apple Silicon MPS), Hugging Face Transformers + TRL.

## Các bước thực hiện

1. Xác định 10-15 hành động thiết bị mục tiêu và viết lược đồ JSON cho mỗi hàm (tên, mô tả, tham số bắt buộc/tùy chọn).
2. Sinh dữ liệu tổng hợp: nhắc LLM mạnh với danh sách công cụ JSON và ví dụ làm việc, tạo khoảng 300 câu hỏi mỗi công cụ đơn và 5.000 câu hỏi đa công cụ (multi-call).
3. Kiểm định dữ liệu: chạy script validator qua mọi bản ghi assistant — loại bỏ hoặc sửa bằng json_repair những bản ghi có tên hàm không hợp lệ, thiếu đối số bắt buộc, hoặc sai kiểu dữ liệu.
4. Hoàn thiện bản ghi: thêm metadata (train/eval), khai báo công cụ (tools), tin nhắn (developer, user, assistant) theo định dạng chat của mô hìnhFunctionGemma.
5. (Tuỳ chọn) Hợp nhất với tập dữ liệu công cụ cũ (ví dụ MOBILEACTIONSGOOGLE) để tạo tập kết hợp (combined), giữ cờ train/eval riêng cho từng nguồn.
6. Điều chỉnh mô hình: full fine-tuning (không LoRA/PEFT) qua TRL SFTTrainer dưới chế độ completion-only loss, 2 epochs, learning rate 1×10⁻⁵, batch size 32, bf16 mixed precision, gradient checkpointing.
7. Xuất mô hình nhẹ (.litertlm) với lượng tử hóa INT8 (trọng số 8-bit, kích hoạt 32-bit float) để triển khai trên thiết bị cục bộ.
8. Đánh giá: tính độ chính xác tên hàm, đối số, và từ đầu đến cuối (end-to-end) trên tập held-out; sử dụng execution-aware scoring để phân loại lỗi chọn sai công cụ vs lỗi định dạng đối số.

## Output mong đợi

- Một mô hình gọi hàm nhỏ đã điều chỉnh, chạy cục bộ trên thiết bị, đạt độ chính xác từ đầu đến cuối trên 70%+ trên tập kiểm tra mới.
- Tập dữ liệu tổng hợp đã kiểm định theo lược đồ, sẵn sàng dùng để huấn luyện hoặc đánh giá.
- Ứng dụng demo trên thiết bị (Android) có thể gọi các hàm hệ thống thông qua giao diện natural language.

## Ví dụ áp dụng

Doanh nghiệp nhỏ tại Việt Nam muốn xây dựng trợ lý gọi hàm cho nhân viên bán hàng ở ngoài trống: liệt kê 12 hành động (gọi điện khách hàng, nhắn tin xác nhận đơn hàng, bật/tắt flashlight chụp ảnh sản phẩm, tra tình trạng đơn hàng, mở ứng dụng quản lý kho). Sinh dữ liệu tổng hợp bằng LLM mạnh, kiểm định theo lược đồ, fine-tuning mô hình 270M tham số chạy trên điện thoại nhân viên. Kết quả: nhân viên nhập bằng giọng nói "gọi cho Nguyễn Văn A về đơn hàng #123", mô hình phát sinh lệnh gọi hàm điện thoại đúng số và tên liên hệ.

## Gotchas

- Strict exact match thấp hơn thực tế: việc bỏ qua đối số tùy chọn (ví dụ dial_call, create_chooser) được tính là sai dù hành động vẫn thực thi được. Hãy dùng execution-aware scoring để không phản ứng quá mức.
- Fine-tuning hẹp trên một nhóm công cụ có thể làm giảm khả năng trên công cụ khác (Google Mobile Actions variant rơi từ 29.3% xuống 17.2% trên tập mở rộng). Luôn dùng tập kết hợp (combined-domain training) nếu cần giữ nhiều danh mục.
- Dữ liệu tổng hợp không bắt được âm thanh thực (ASR errors), yêu cầu không rõ ràng, hoặc cách diễn đạt đa dạng của người dùng thực.
- Latency khoảng 13 giây mỗi lượt trên thiết bị cỡ trung (Pixel 8 Pro) có thể không phù hợp cho tác vụ cần phản hồi tức thì.
- Chỉ đã đánh giá trên tiếng Anh và Android; chưa kiểm trên iOS hay các ngôn ngữ khác.