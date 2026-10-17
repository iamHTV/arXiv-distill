# Skill: functiongemma-on-device-extension
Source: 2609.25373v1
Type: framework

## Khi nào dùng skill này
- Cần một mô hình function-calling nhỏ (on-device, compact) chạy trên thiết bị di động (mobile device) cho các intent cụ thể (điện thoại, SMS, camera, flashlight, ứng dụng, ...).
- Có một bộ dataset tổng hợp (synthetic dataset) về các cuộc trò chuyện trên thiết bị.
- Muốn mở rộng khả năng của một model nhỏ (270M parameter) mà không quên bản phân phối gốc (catastrophic forgetting).

## Tình huống KHÔNG nên dùng
- Cần model chạy trên server (server-side), không phải on-device.
- Không có dữ liệu synthetic về các cuộc trò chuyện trên thiết bị.
- Không cần fine-tune model nhỏ (chỉ cần dùng model có sẵn).

## Input cần có
- Dataset tổng hợp (synthetic dataset) gồm các cuộc trò chuyện về các hành động trên thiết bị (device-control conversations).
- Mô hình FunctionGemma 270M-it (hoặc mô hình function-calling nhỏ tương tự).
- Thiết bị tăng tốc (accelerator): CUDA hoặc Apple Silicon MPS.
- TRL library cho supervised fine-tuning.

## Các bước thực hiện
1. Xây dựng dataset tổng hợp (synthetic dataset) gồm các cuộc trò chuyện bao gồm mười lăm danh mục điều khiển thiết bị (device-control categories).
2. Chia dataset thành 90% train và 10% evaluation (965 ví dụ trong tập evaluation).
3. Điều chỉnh chi tiết (fine-tune) FunctionGemma 270M-it bằng TRL supervised fine-tuning dưới độ mất hoàn thành (completion-only loss).
4. Bật mixed precision và gradient checkpointing.
5. Đánh giá trên ba cấp độ: độ chính xác tên hàm (function-name accuracy), độ chính xác đối số (argument accuracy), độ chính xác từ đầu đến cuối (end-to-end accuracy).
6. Để giữ hiệu suất trên cả domain cũ và domain mới, hãy train kết hợp (jointly train) mô hình đã fine-tune với model gốc (Google's MOBILEACTIONSGOOGLE).

## Output mong đợi
- Mô hình function-calling nhỏ (270M) đạt độ chính xác từ đầu đến cuối (end-to-end accuracy) 76.5% trên MOBILEACTIONSEXTENDED (tăng từ 29.3% của base model).
- Mô hình kết hợp (combined model) đạt 76.5% trên MOBILEACTIONSEXTENDED và 82.3% trên MOBILEACTIONSGOOGLE (giảm từ 90.3% của specialist của Google), biểu diễn sự đánh đổi (trade-off) 8.0 phần trăm điểm đổi lại cho việc gấp đôi phạm vi báo danh (category coverage).

## Ví dụ áp dụng
- Xây dựng trợ lý di động (mobile assistant) có thể thực hiện các hành động như gọi điện thoại, nhắn tin, điều khiển flashlight, chụp ảnh màn hình (screenshot), mở ứng dụng (application management) bằng ngôn ngữ tự nhiên. Hãy dùng FunctionGemma 270M-it fine-tuned trên dataset tổng hợp về các hành động này.

## Gotchas
- Dataset là tổng hợp (synthetic), không phải dữ liệu thực từ người dùng.
- Chỉ bao gồm mười lăm danh mục điều khiển thiết bị (15 device-control categories).
- Mô hình 270M tham số là mô hình nhỏ, có thể chạy trên thiết bị di động.
