# [2609.25373v1] Extending FunctionGemma for Practical On-Device Mobile Function Calling

## Problem
- Các trợ lý trên thiết bị (on-device assistants) yêu cầu các mô hình function-calling ánh xạ ngôn ngữ tự nhiên sang các hành động hệ thống cục bộ (local system actions), nhưng existing resources nhấn mạnh vào web API hoặc catalog hành động trên thiết bị (mobile-action catalogs) hẹp. Prior work chưa giải quyết được việc mở rộng một mô hình function-calling nhỏ (270M) đến các intent trên thiết bị rộng hơn mà không quên bản phân phối gốc (catastrophically forgetting the original distribution).

## Contribtuion
- MOBILEACTIONSEXTENDED — một tập dữ liệu (dataset) tổng hợp (synthetic), được xác thực bằng schema (schema-validated) gồm khoảng 9.500 cuộc trò chuyện (conversations) bao gồm mười lăm danh mục điều khiển thiết bị (device-control categories), bao gồm nhắn tin (messaging), cuộc gọi điện thoại (phone calls), máy ảnh/chụp màn hình (camera/screenshot), điều khiển độ sáng (brightness control), truy vấn trạng thái thiết bị (device-status queries), điều khiển đèn pin (flashlight control), và quản lý ứng dụng (application management).
- Điều chỉnh chi tiết (fine-tune) mô hình 270M với TRL supervised fine-tuning dưới độ mất hoàn thành (completion-only loss), tạo ra một chuyên gia mở rộng (extended specialist) và một mô hình kết hợp (combined model) được đào tạo cùng lúc với MOBILEACTIONSGOOGLE của Google.
- Trên MOBILEACTIONSEXTENDED, độ chính xác từ đầu đến cuối (end-to-end accuracy) cải thiện từ 29.3% của mô hình cơ bản (base model) và 17.2% của biến thể Mobile-Actions của Google lên 76.5%. Mô hình kết hợp (combined model) giữ nguyên 76.5% trên MOBILEACTIONSEXTENDED và đạt 82.3% trên MOBILEACTIONSGOOGLE, giảm từ 90.3% của biến thể chuyên gia (specialist) của Google, biểu diễn một sự đánh đổi (trade-off) 8.0 phần trăm điểm (percentage-point) đổi lại cho việc gấp đôi phạm vi báo danh (category coverage).
- Phát hành dataset, các mô hình đã fine-tuned, đường ống (pipeline) huấn luyện/đánh giá có thể tái tạo (reproducible training/evaluation pipeline), và một bản demo Android, nhấn mạnh việc gọi hàm cục bộ (local function calling) nhỏ gọn (compact) là một con đường thực tế hướng tới các trợ lý trên thiết bị (mobile assistants) có độ trễ thấp (low-latency) và bảo vệ sự riêng tư (privacy-preserving).

## Method (tóm tắt cốt lõi)
- Xây dựng dataset MOBILEACTIONSEXTENDED: tổng hợp khoảng 9.500 cuộc trò chuyện, chia 90/10 giữa tập train và tập đánh giá (evaluation). Tập đánh giá chứa 965 ví dụ phân tán trên 15 danh mục.
- Điều chỉnh chi tiết (fine-tune) FunctionGemma 270M-it bằng TRL supervised fine-tuning dưới độ mất hoàn thành (completion-only loss).
- Sử dụng mixed precision, gradient checkpointing được bật (enabled). Backbone 270M vừa ăn trên một thiết bị tăng tốc (accelerator) duy nhất (CUDA hoặc Apple Silicon MPS), do đó tránh độ phức tạp của bộ chuyển đổi LoRA (LoRA adapter complexity) và giữ việc triển khai đơn giản: một tập hợp trọng số (single set of weights) thay thế trọng số trước khi đào tạo (pretrained weights).
- Đánh giá trên ba cấp độ (three levels): độ chính xác tên hàm (function-name accuracy), ...

## Key Findings
- 2 tác giả từ UGrowAI, category arXiv: cs.LG.
- FunctionGemma 270M-it đạt 29.3% độ chính xác từ đầu đến cuối (end-to-end) trên MOBILEACTIONSEXTENDED.
- Biến thể được điều chỉnh chi tiết bởi Google (Google fine-tuned variant) đạt kém hơn (17.2%).
- Mô hình mở rộng (extended model) đạt 76.5% trên MOBILEACTIONSEXTENDED.
- Mô hình kết hợp (combined model) giữ nguyên 76.5% trên MOBILEACTIONSEXTENDED và đạt 82.3% trên MOBILEACTIONSGOOGLE, giảm từ 90.3% của biến thể chuyên gia (specialist) của Google, biểu diễn sự đánh đổi (trade-off) 8.0 phần trăm điểm (percentage-point) đổi lại cho việc gấp đôi phạm vi báo danh (category coverage).

## Actionable Insights
1. Điều chỉnh chi tiết (fine-tuning) một mô hình nhỏ (270M) trên các cuộc trò chuyện về hành động trên thiết bị (mobile-action conversations) có thể mở rộng đáng kể phạm vi báo danh (coverage). Áp dụng: khi cần mô hình function-calling chạy trên thiết bị (on-device), hãy điều chỉnh chi tiết model nhỏ (270M) trên dataset tổng hợp (synthetic dataset) covering các domain cụ thể.
2. Kết hợp model đã fine-tune trên domain mới với model gốc có thể giữ được hiệu suất trên cả hai domain với sự đánh đổi nhỏ (8.0 điểm phần trăm). Áp dụng: khi cần model xử lý cả domain cũ và domain mới, hãy train kết hợp (jointly train) trên cả hai phân phối (distribution).

## Assumptions & Limitations
- Dataset là tổng hợp (synthetic dataset).
- Tập trung vào việc gọi hàm trên thiết bị di động (on-device mobile function calling).
- Chỉ bao gồm mười lăm danh mục điều khiển thiết bị (15 device-control categories).
- Mô hình 270M tham số — mô hình nhỏ.

## Metadata
- Năm: 2026, tác giả: Ali Rezagholizadeh (UGrowAI), Soheila Samiee (UGrowAI), category arXiv: cs.LG, link PDF: https://arxiv.org/pdf/2609.25373v1
