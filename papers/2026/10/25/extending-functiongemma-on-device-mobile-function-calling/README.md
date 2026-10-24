# [2609.25373v2] Extending FunctionGemma for Practical On-Device Mobile Function Calling

## Giá trị cốt lõi (1 câu)

Một mô hình function-calling (gọi hàm) 270 triệu tham số có thể được điều chỉnh (fine-tune) để điều khiển Android cục bộ (on-device) với độ chính xác 76.5% trên 15 danh mục hành động thiết bị, chỉ cần tập dữ liệu tổng hợp ~9.500 mẫu và không cần mô hình đám mây lớn cho mỗi yêu cầu.

## Problem

Prior work chưa giải quyết được việc điều khiển thiết bị di động cục bộ (on-device device control) bằng mô hình nhỏ, vì các benchmark công khai (BFCL, Big-CodeBench, APIGen) tập trung vào web API (REST endpoints, search, calendars, SaaS tools) thay vì các hành động hệ thống Android (bật flashlight, gửi SMS, mở ứng dụng, tra pin). FunctionGemma 270M-it hiện chỉ hỗ trợ khoảng 7 workflow di động (tạo sự kiện lịch, tạo liên hệ, ánh xạ, email, cài đặt Wi-Fi, bật/tắt flashlight), bỏ sót các ý định phổ biến như cuộc gọi điện, SMS, điều chỉnh độ sáng, chụp ảnh, chụp màn hình và mở ứng dụng.

## Contribution

(i) Công khai tập dữ liệu MOBILEACTIONSEXTENDED: khoảng 9.500 mẫu cuộc gọi hàm (function-calling corpus) được tạo tổng hợp (synthetic prompting), kiểm định theo lược đồ (schema-validated), chia 90/10 giữa train và evaluation, covering 15 danh mục điều khiển thiết bị.
(ii) Hai mô hình FunctionGemma 270M đã điều chỉnh (fine-tuned): FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-EXTENDED và FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-COMBINED.
(iii) Đánh giá đa trục (multi-axis evaluation): so sánh 4 phiên bản mô hình trên 2 tập held-out bằng các chỉ số exact-match (tên hàm, đối số, độ chính xác từ đầu đến cuối).
(iv) Ứng dụng demo trên thiết bị (Handy Chat): ứng dụng Android đóng gói bằng Buildozer, chạy LiteRT-LM trên CPU của Pixel 8 Pro.

## Method

Pipeline có 5 giai đoạn: (1) Tạo cuộc hội thoại tổng hợp (schema-grounded synthetic generation) bằng mô hình giáo viên mạnh với danh sách công cụ JSON và ví dụ làm việc, sinh khoảng 300 câu hỏi mỗi công cụ đơn và khoảng 5.000 câu hỏi đa công cụ. (2) Kiểm định và hoàn thiện (validation and completion): một script validator kiểm tra tên hàm có trong danh mục, các đối số bắt buộc có mặt và đúng kiểu, bản ghi không đạt được loại bỏ hoặc sửa bằng json_repair. (3) Hợp nhất với MOBILEACTIONSGOOGLE của Google để tạo MOBILEACTIONSCOMBINED, giữ cờ train/eval riêng cho từng nguồn. (4) Điều chỉnh mô hình (fine-tuning): FunctionGemma 270M-it được fine-tuning toàn bộ (không LoRA/PEFT) qua TRL SFTTrainer dưới chế độ completion-only loss (mất mát chỉ tính trên phần assistants trả lời, không tính trên prompt), 2 epochs, learning rate 1×10⁻⁵, batch size 32, bf16 mixed precision. (5) Triển khai trên thiết bị: xuất mô hình .litertlm lượng tử hóa INT8 (dynamic_wi8_afp32: trọng số 8-bit, kích hoạt 32-bit float), chạy trong ứng dụng Handy Chat trên Android qua LiteRT-LM CPU backend.

## KNOWLEDGE — Số liệu & khái niệm

- FunctionGemma 270M-it (mô hình hàm gọi 270 triệu tham số, instruction-tuned): đạt 29.3% độ chính xác từ đầu đến cuối (end-to-end accuracy) trên MOBILEACTIONSEXTENDED.
- Google Mobile Actions variant (mô hình chuyên biệt 7 danh mục di động của Google): đạt 17.2% trên MOBILEACTIONSEXTENDED, 90.3% trên MOBILEACTIONSGOOGLE.
- FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-EXTENDED (mô hình chúng tôi điều chỉnh trên tập mở rộng): đạt 100% độ chính xác tên hàm (function-name accuracy), 76.5% end-to-end accuracy trên MOBILEACTIONSEXTENDED (+47.2 điểm so với base model).
- FUNCTIONGEMMA-270M-IT-MOBILE-ACTIONS-COMBINED (mô hình hợp nhất): duy trì 76.5% trên MOBILEACTIONSEXTENDED, đạt 82.3% trên MOBILEACTIONSGOOGLE (giảm 8.0 điểm so với specialist 90.3%).
- MOBILEACTIONSEXTENDED: khoảng 9.500 mẫu, chia 90/10 train/eval, 965 mẫu evaluation phân tán trên 15 danh mục, khoảng một trong ba prompt là multi-call (gọi nhiều hàm).
- Execution-aware accuracy (độ chính xác nhận thức thực thi): MA-Extended đạt 100.0% (từ 76.5% strict exact match), MA-Combined đạt 96.0% trên EXTENDED và 82.6% trên GOOGLE.
- .litertlm bundle: 285.6 MB trên thiết bị (sau lượng tử hóa INT8).
- Latency: khoảng 13 giây mỗi lượt gọi hàm trên Pixel 8 Pro (pass 1 ~9 giây, tool execution ~2 giây, pass 2 ~2 giây).

## INSIGHT — Cơ chế & tại sao

[Fine-tuning hẹp (narrow fine-tuning) trên 7 danh mục gốc] gây hại cho khả năng mở rộng vì mô hình tự tin phát ra các lệnh gọi trong phân phối cũ (ví dụ open_wifi_settings) thay vì lệnh gọi đúng trong tập mở rộng → độ chính xác rơi từ 29.3% (base) xuống 17.2%. Điều này nghĩa là việc specialization quá hẹp làm quá khớp (overfit) vào công cụ cũ, bỏ lỡ các ý định mới.

[Huấn luyện miền kết hợp (combined-domain training)] trên cả hai tập dữ liệu giữ được 76.5% trên các hàm mở rộng và đạt 82.3% trên hàm gốc (giảm chỉ 8.0 điểm so với 90.3% specialist). Điều này nghĩa là hỗn hợp dữ liệu hai miền tốt hơn việc có hai mô hình chuyên biệt riêng lẻ, vì mô hình học được phân tách giữa các công cụ khác nhau mà không quên cũ.

[Completion-only loss] ẩn mất mát trên phần prompt (công cụ-block, tin nhắn nhà phát triển, lượt người dùng) nên mô hình chỉ được đánh giá trên phần trả lời của trợ lý. Điều này ổn định huấn luyện khi độ dài prompt chiếm ưu thế (danh sách công cụ riêng lẻ lên đến hàng trăm token).

[Strict exact match] thấp hơn thực tế vì nó phạt các mục chọn lỏng (đầu ra còn thực thi được); execution-aware re-scoring cho thấy MA-Extended đạt 100.0% (từ 76.5% strict), nghĩa là phần lớn lỗi chỉ là vấn đề định dạng có thể khắc phục (ví dụ boolean tùy chọn bị bỏ qua) chứ không phải chọn sai công cụ.

## IDEA — Áp dụng được gì

Áp dụng [schema-grounded synthetic generation] vào việc xây dựng agent điều khiển thiết bị cho doanh nghiệp nhỏ tại Việt Nam: bước đầu là liệt kê 10-15 hành động hệ thống phổ biến (gọi điện, nhắn tin, bật/tắt thiết bị, mở ứng dụng), tạo tập dữ liệu tổng hợp bằng LLM mạnh, kiểm định theo lược đồ trước khi fine-tuning mô hình nhỏ chạy cục bộ.

Áp dụng [execution-aware accuracy] vào đánh giá agent gọi hàm: thay vì chỉ dùng strict exact match, hãy phân loại lỗi thành "chọn sai công cụ" (nguy hiểm) và "sai định dạng đối số" (có thể sửa bằng safe default) để không phản ứng quá mức với các lỗi không ảnh hưởng đến kết quả thực tế.

Áp dụng [combined-domain training] vào việc duy trì nhiều năng lực cho một mô hình agent: thay vì trains separately cho từng tác vụ, hãy trộn dữ liệu các tác vụ liên quan vào một lần fine-tuning để tránh quên năng lực cũ (catastrophic forgetting) khi mở rộng phạm vi.

## WISDOM — Nguyên tắc tổng quát

Nguyên tắc: Huấn luyện miền kết hợp (dữ liệu nhiều miền trong một lần fine-tuning) thường tốt hơn việc có nhiều mô hình chuyên biệt hẹp, khi mục tiêu là duy trì khả năng hoạt động trên nhiều danh mục công cụ cùng lúc.

Khi nào dùng: Khi cần một mô hình nhỏ xử lý nhiều loại hành động thiết bị/công cụ khác nhau trên thiết bị cục bộ.

Khi nào KHÔNG dùng: Khi mỗi miền yêu cầu độ chính xác tuyệt đối trên một nhóm công cụ cố định và không chấp nhận việc chia sẻ trọng số.

Ví dụ áp dụng ngoài domain gốc: Ứng dụng cho chatbot hỗ trợ khách hàng đa kênh (email, chat, SMS, gọi điện) — cùng một mô hình nhỏ được fine-tuning trên dữ liệu cả 4 kênh thay vì 4 mô hình riêng lẻ, giữ được khả năng chuyển đổi kênh mà không cần reload mô hình.

## Assumptions & Limitations

- Điều kiện đúng: Dữ liệu tổng hợp có chất lượng cao và kiểm định theo lược đồ; thiết bị chạy Android với LiteRT-LM hỗ trợ; người dùng chấp nhận độ trễ khoảng 13 giây mỗi lượt gọi hàm.
- Limitation paper thừa nhận: MOBILEACTIONSEXTENDED được tạo tổng hợp chứ không thu thập từ người dùng thực; đánh giá dùng strict exact match có thể تحت Ước lượng thành công thực thi; chỉ đánh giá trên một họ mô hình (FunctionGemma 270M-it); tập dữ liệu và demo chủ yếu là tiếng Anh và Android.
- Limitation paper KHÔNG nói: Không có so sánh với mô hình khác cùng kích thước (Qwen, SmolLM2); không có đánh giá trên iOS; không có đánh giá độ mạnh trước các lệnh hủy hại (adversarial input); latency 13 giây có thể quá chậm cho một số tác vụ thời gian thực.

## Metadata

- Năm: 2026
- Tác giả: Ali Rezagholizadeh, Soheila Samiee
- Thể loại arXiv: cs.LG
- Link PDF: https://arxiv.org/pdf/2609.25373v2
- Số lượt trích dẫn: chưa có thông tin