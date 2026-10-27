# 2610.34817v1 Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents

## Giá trị cốt lõi (1 câu)
Tích hợp sai prompt caching (prompt-caching mis-integration) trong agent LLM thường thất lặng (fail silently) — 90% khuyết điều không gây lỗi runtime mà chỉ làm tăng chi phí API và độ trễ, và CACHELINT (công cụ phân tích tĩnh) có thể phát hiện chúng với độ chính xác 0.86 trên các dự án thực tế.

## Problem
Prior work (các nghiên cứu trước) đã nghiên cứu lỗi prompt và hiệu suất prompt caching, nhưng đã bỏ qua các vấn đề tích hợp (integration issues) của prompt caching từ phía ứng dụng. Khi ứng dụng không tích hợp đúng cách với các API cache riêng của từng provider (Anthropic, Amazon Bedrock, OpenAI, Gemini...), cache có thể bị vô hiệu hóa mà không có bất kỳ thông báo lỗi nào. Agent tiếp tục đưa ra kết quả chính xác nhưng chi phí inference tăng rõ rệt vì mỗi lần chạy đều phải xử lý lại toàn bộ prompt thay vì tái sử dụng prefix đã cache. Các hoặc kiểm tra (test oracles) dựa trên crash hoặc assertion bỏ lỡ đa số khuyết điều vì chúng không phát hiện được sự suy thoái chi phí.

## Contribution
1. Nghiên cứu thực nghiệm đầu tiên (first empirical study) về prompt-caching mis-integration, phân tích 120 khuyết điều liên quan đến prompt caching từ 10 hệ thống agent mã nguồn mở phổ biến, đặc trưng về nguyên nhân gốc (root cause), triệu chứng (symptom) và chiến thuật sửa lỗi (fixing strategy).
2. Thiết kế CACHELINT, một kỹ thuật phân tích tĩnh (static analysis) để phát hiện prompt-caching mis-integration. CACHELINT mô tả mỗi mis-integration dưới dạng một cặp: một điểm gọi cache (invocation site) cùng với các điều kiện tiên quyết (preconditions) cần thiết để tích hợp cache đúng cách. CACHELINT xác định các điểm gọi bằng CodeQL và kiểm tra từng điều kiện tiên quyết bằng oracle khả năng nhà cung cấp thời đại (dated provider-capability oracle) hoặc kiểm tra guarda bằng LLM (LLM guard check).
3. CACHELINT đạt độ chính xác (precision) 0.71 và độ nhạy (recall) 0.78 trong việc xác định 120 khuyết điều đã gán nhãn trên 10 hệ thống agent đã nghiên cứu. Đánh giá thêm cho thấy hiệu quả của CACHELINT trong thực tế: xác định 32 mis-integration trên 571 dự án agent với precision 0.86. Những phát hiện này đã nhận 21 xác nhận từ nhà phát triển và dẫn đến 18 sửa lỗi upstream, bao gồm một lỗi trong SDK chính thức của Anthropic.

## Method
Pipeline (dòng xử lý) của CACHELINT có các bước chính:
1. Mô hình hóa tích hợp prompt caching: mỗi mẫu mis-integration được mô hình hóa dưới dạng cặp P = ⟨m, j⟩, trong đó m là một điểm gọi cache (prompt-caching invocation site) — một điểm trong chương trình gửi nội dung đến hoặc đọc trường kế toán từ cache — và j là một hợp của các điều kiện tiên quyết (caching-context precondition) thuộc 3 họ: độ ổn định của tiền tố (STAB), khả năng nhà cung cấp (CAP), và an toàn kế toán (ACCT).
2. Xác định các điểm gọi cache (LOCATE): CACHELINT sử dụng CodeQL để xác định các điểm gọi API lưu cache và trích xuất bối cảnh mã xung quanh chúng.
3. Kiểm tra từng điều kiện tiên quyết: đối với điều kiện CAP, CACHELINT so sánh giả định khả năng của mã với một dated provider-capability oracle (bảng tra cứu khả năng nhà cung cấp gắn ngày tháng); đối với điều kiện STAB hoặc ACCT, CACHELINT trích xuất bối cảnh xung quanh điểm gọi và hỏi một LLM (gpt-5.4-mini) xem có một rào cản giải phóng (discharging barrier) đến điểm gọi hay không (ví dụ: cắt ngắn ngày tháng hoặc sort_keys chuẩn hóa).
4. Khi một kiểm tra điều kiện tiên quyết thất bại, CACHELINT báo cáo điểm gọi tương ứng và gợi ý sửa lỗi (fix hint) dựa trên bản đồ nguyên nhân-gốc-đến-chiến-thuật-sửa từ nghiên cứu thực nghiệm.

## KNOWLEDGE — Số liệu & khái niệm
- Prompt caching (lưu trữ lệnh nhắc): kỹ thuật tối giản chi phí và độ trễ suy luận LLM bằng cách tái sử dụng kết quả tính toán của các tiền tố lệnh nhắc đã xử lý trước; khi một lời lệnh mới bắt đầu bằng một tiền tố khớp chính xác với tiền tố đã cache, provider tái sử dụng kết quả tính toán đã cache thay vì tính toán lại tiền tố và tính phí token đã cache ở mức giảm đáng kể.
- Prompt-caching mis-integration (tích hợp sai lưu trữ lệnh nhắc): mã ứng dụng vi phạm các yêu cầu của nhà cung cấp để kích hoạt, định cấu hình, hoặc kế toán cho lưu trữ lệnh nhắc; có thể ngăn tái sử dụng cache, gây ra kế toán cache không chính xác, hoặc thậm chí kích hoạt lỗi runtime.
- 10 hệ thống agent được nghiên cứu: OpenClaw, Hermes-Agent, AutoGPT, OpenCode, LobeHub, OpenHands, Cline, Goose, Aider, Nanobot.
- 120 khuyết điều liên quan đến prompt caching từ 148.947 PR đã hợp nhất (merged PRs).
- 97 khuyết điều (81%) ở phía yêu cầu (request side), 23 (19%) ở phía đọc (read side).
- 108/120 khuyết điều (90%) thất lặng (fail silently): không gây ra ngoại lệ, không có assertion thất bại, không crash, đầu ra của model vẫn chính xác trong khi chỉ cache giảm hiệu quả.
- 86/108 (72%) là silenz waste (thấp phí lặng): cache ngừng hit và chạy tiếp không đổi, dấu vết duy nhất là chi phí thêm trên API được lưu trữ hoặc độ trễ thêm trên ứng dụng.
- 22/108 (18%) tạo sai số liệu viễn thông (wrong telemetry): cache hoạt động đúng nhưng số liệu token cache được trả về bị phân tích, cộng hoặc hiển thị sai.
- 12/120 (10%) gây crash, tập trung ở incompatible marker (8/12).
- 8 nguyên nhân gốc (root causes): provider compatibility (model-name gating 37, incompatible marker 10), prefix stability (prefix reassembly 15, volatile value 13, nondeterministic serialization 10, misplaced marker 3), cross-turn mutation (9), usage miscount (23).
- 6 chiến thuật sửa lỗi: capability lookup (22), marker guard (22), prefix canonicalization (15), usage-counter fix (23), cache-boundary fix (23), lifecycle guard (15).
- CACHELINT: precision 0.71, recall 0.78 trên 120 khuyết điều đã gán nhãn; precision 0.86 trên 571 repo thực tế; phát hiện 32 mis-integration mới; 21 xác nhận nhà duy trì, 18 sửa lỗi.

## INSIGHT — Cơ chế & tại sao
- [Mis-integration thất lặng] xảy ra VÌ cache miss không gây ra lỗi runtime — model chỉ tính toán lại prefix và trả về kết quả đúng, nên không có ngoại lệ hay assertion nào được kích hoạt. Dấu hiệu duy nhất là chi phí API tăng hoặc độ trễ thêm, chỉ thấy trên bảng số liệu sử dụng. Nghĩa là các hoặc kiểm tra dựa trên crash bỏ lỡ 90% khuyết điều.
- [Heterogeneous provider APIs làm tăng nguy cơ] xảy ra VÌ các provider có các thiết lập kích hoạt (opt-in), giới hạn số lượng mục cache, và thời gian sống cache khác nhau (ví dụ: Anthropic yêu cầu chọn tham gia và giới hạn mục cache, Bedrock có thời gian sống 1 giờ gắn với model cụ thể, OpenAI và Gemini áp dụng tự động). Nghĩa là khi đổi model hay nâng cấp provider, caching có thể bị tắt lặng mà không có thay đổi mã nào.
- [Sửa lỗi thường đơn giản và có mô hình] xảy ra VÌ 68% bản vá là các sửa tĩnh, cục bộ, lặp lại qua các dự án dưới dạng mẫu có thể tái sử dụng. Gán mỗi nguyên nhân gốc với chiến thuật sửa phổ biến nhất dự đoán chính xác 95/120 (79%) bản vá. Nghĩa là việc chẩn đoán là phần khó, bản vá phần dễ.

## IDEA — Áp dụng được gì
1. Áp dụng CACHELINT vào codebase agent của doanh nghiệp: chạy phân tích tĩnh để xác định các điểm gọi cache không được bảo vệ và báo cáo các vi phạm điều kiện tiên quyết. Bước đầu: tích hợp CACHELINT vào CI pipeline, kiểm tra mỗi lần commit xem có điểm gọi cache nào thiếu guarda hay không.
2. Thay thế model-name gating bằng capability lookup: thay vì kiểm tra tên model cứng (hardcoded model name) để quyết định có bật cache hay không, hãy tra cứu khả năng cache của model từ một bảng khả năng nhà cung cấp (provider-capability matrix) được cập nhật định kỳ. Bước đầu: thay đổi câu lệnh `if model.id.startswith("claude")` thành `if registry.supports_cache(model.id)`.
3. Di chuyển các giá trị thay đổi mỗi lần yêu cầu (volatile value) như timestamp, UUID ra khỏi span đã cache: đặt timestamp vào tin nhắn người dùng thay vì prompt hệ thống, hoặc cắt ngắn timestamp về mức ngày (day granularity) bằng `.date().isoformat()`. Bước đầu: tìm các lệnh gọi `datetime.now().isoformat()` trong prompt hệ thống và di chuyển chúng ra khỏi chuỗi prefix đã cache.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: Cache miss lặng là loại lỗi đắt đỏ nhất vì nó không gây crash — chỉ làm tăng hóa đơn API; hãy theo dõi tỷ lệ cache-hit (cache-hit rate) làm chỉ số chính, không chỉ đợi lỗi runtime.
- Khi nào dùng: Khi triển khai agent LLM sử dụng prompt caching để giảm chi phí inference.
- Khi nào KHÔNG dùng: Khi provider bật caching tự động ở phía model và ứng dụng không cấu hình cache markers nào (implicit caching nằm ngoài phạm vi CACHELINT).

## Assumptions & Limitations
- Điều kiện phải đúng: Mỗi điểm gọi cache phải là một điểm chương trình có thể kiểm tra tĩnh đơn lẻ; các nguyên nhân gốc liên quan đến nhiều bản ảnh (multi-snapshot) như cross-turn mutation và prefix reassembly nằm ngoài phạm vi mô hình đơn điểm của CACHELINT.
- Limitation paper thừa nhận: CACHELINT chỉ covering 96/120 (80%) khuyết điều trong bộ dữ liệu; multi-snapshot defects nằm ngoài phạm vi; recall trên 571 repo không được đo vì tổng số khuyết điều chưa biết; kết quả phản ảnh chụp khả năng (capability snapshot) 2026-05-10.
- Limitation paper KHÔNG nói: Không giải quyết caching ngầm (implicit caching) khi provider bật caching tự động ở phía model — các khuyết điều request-side chỉ quan sát được qua phản hồi (ví dụ: cached tokens liên tục bằng 0).

## Metadata
- Năm: 2026
- Tác giả: Ying Zhang, Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Yepang Liu, Leo Zhang
- Category arXiv: cs.SE
- Link PDF: https://arxiv.org/pdf/2610.34817v1
- Classification: [applied]