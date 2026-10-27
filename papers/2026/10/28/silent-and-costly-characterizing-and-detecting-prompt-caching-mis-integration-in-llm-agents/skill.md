# Skill: cachelint-prompt-caching-misintegration-detection
Source: 2610.34817v1
Type: evaluation-method

## Khi nào dùng skill này
- Cần phát hiện prompt-caching mis-integration trong codebase agent LLM (vi phạm yêu cầu kích hoạt, định cấu hình, hoặc kế toán cho lưu trữ lệnh nhắc).
- Muốn tìm các điểm gọi cache không có guarda (unguarded cache invocation sites) trước khi chúng gây ra chi phí API tăng lặng.
- Muốn so sánh các nguyên nhân gốc (root cause) với chiến thuật sửa lỗi phổ biến nhất để sửa nhanh các khuyết điều cache.

## Tình huống KHÔNG nên dùng
- Provider bật caching tự động ở phía model và ứng dụng không cấu hình cache markers nào (implicit caching nằm ngoài phạm vi).
- Muốn phát hiện lỗi cần lý luận qua nhiều điểm gọi hoặc nhiều lượt (cross-turn mutation, prefix reassembly) — nằm ngoài phạm vi mô hình đơn điểm.

## Input cần có
- Mã nguồn của agent application (Python, JavaScript/TypeScript, Ruby, Go, C#).
- Danh sách các điểm gọi cache (invocation sites): nơi gắn cache directive (cache_control, cachePoint, ttl, cachedContent, v.v.) hoặc đọc trường kế toán (cached_tokens, cache_read, cache_creation).
- Dated provider-capability oracle: bảng tra cứu khả năng cache của từng nhà cung cấp gắn ngày tháng (last_verified date).

## Các bước thực hiện
1. Xác định các điểm gọi cache bằng CodeQL: trích xuất các điểm gọi API lưu cache và bối cảnh mã xung quanh.
2. Đối với mỗi điểm gọi, trích xuất giả định khả năng (capability assumption): ⟨điểm gọi, phạm vi nhà cung cấp, khả năng, điều kiện⟩.
3. Diệt (discharge) điều kiện CAP: so sánh giả định khả năng của mã với dated oracle; nếu mã coi model là có khả năng nhưng oracle không → BUG (provider từ chối) hoặc SUSPECTED (không rõ); nếu oracle coi model là có khả năng nhưng mã loại trừ → LATENT miss (tích cache bị bỏ lặng).
4. Diệt điều kiện STAB hoặc ACCT: trích xuất bối cảnh xung quanh điểm gọi và hỏi LLM guard check (gpt-5.4-mini) xem có rào cản giải phóng (discharging barrier) đến điểm gọi hay không (ví dụ: cắt ngắn ngày tháng, sort_keys, null check).
5. Khi kiểm tra thất bại, báo cáo điểm gọi, bản phán quyết (verdict), và gợi ý lớp sửa (fix hint) từ bản đồ nguyên nhân-gốc-đến-chiến-thuật-sửa.

## Output mong đợi
- Cảnh báo (warning) cho mỗi điểm gọi cache không được bảo vệ.
- Loại điểm gọi, nguyên nhân gốc, chiến thuật sửa được đề xuất.
- Precision và recall trên bộ dữ liệu gán nhãn.

## Ví dụ áp dụng
Đoàn phát triển có agent code dùng Anthropic cache_control. Mã kiểm tra `if model.id.startswith("claude")` để quyết định bật cache. Khi Anthropic đổi tên model, kiểm tra này không khớp và cache bị tắt lặng. Áp dụng CACHELINT: CodeQL xác định điểm gọi cache_control, guard check hỏi xem có capability lookup trước điểm gọi không, oracle đánh giá xem model mới có hỗ trợ cache không. Nếu không → báo cáo BUG với gợi ý thay bằng `registry.supports_cache(model.id)`.

## Gotchas
- Guard check không chính xác (not sound): LLM có thể bỏ qua một guarda thật hoặc ghi số một guards giả, dẫn đến cảnh báo sai hoặc bỏ lỡ khuyết điều.
- CACHELINT chỉ phát hiện các khuyết điều tại một điểm chương trình xác định (single deterministic program point); cross-turn mutation và prefix reassembly cần lý luận qua nhiều lượt và nằm ngoài phạm vi.
- Oracle gắn ngày tháng — khi provider thay đổi hành vi caching, cần cập nhật affected entries và chạy lại CACHELINT.
- Mỗi cảnh báo kèm gợi ý sửa từ bản đồ nguyên nhân-gốc-đến-chiến-thuật-sửa (modal repair).