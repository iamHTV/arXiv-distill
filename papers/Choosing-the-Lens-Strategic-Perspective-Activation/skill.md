# Skill: Kích hoạt Perspective (góc nhìn) Chiến lược để Ảnh hưởng Quyết định
Nguồn: 2605.31581v1
Loại: framework (khung phương pháp)

## Khi nào dùng skill này
- Khi cần thuyết phục stakeholders (các bên liên quan) bằng cách chọn evaluation framework (khung đánh giá) có lợi
- Khi proposal (đề xuất) bị reject (từ chối) trên mọi front (mặt trận) — cần deactivate hostile perspectives (vô hiệu hóa góc nhìn thù địch)
- Khi chuẩn bị pitch (thuyết trình), presentation, hoặc argument (lập luận) trước board/review committee (hội đồng đánh giá)

## KHÔNG nên dùng khi
- Arguments dựa trên facts/objective data (dữ liệu khách quan) — không cần strategic framing (đóng khung chiến lược)
- Không có influence over evaluation process (ảnh hưởng lên quy trình đánh giá)
- Ranh giới đạo đức: không nên dùng để manipulate (thao túng) thông qua hiding relevant information (giấu thông tin liên quan)

## Input cần có
- Danh sách tất cả arguments (pros/cons — ưu/nhược) của proposal
- Danh sách stakeholders/perspectives (các bên liên quan/góc nhìn) có liên quan
- Mapping (ánh xạ): argument nào thuộc perspective nào
- Attack relation (quan hệ tấn công): argument nào counter (phản lại) argument nào
- Biết được perspective nào bạn có influence để activate/deactivate (kích hoạt/vô hiệu hóa)

## Các bước thực hiện

### Bước 1 — Map Argument Landscape (ánh xạ lập đồ arguments)
1. Liệt kê tất cả arguments liên quan đến proposal (bao gồm counter-arguments — lập luận phản đối)
2. Xác định perspective/source (góc nhìn/nguồn) của mỗi argument (performance — hiệu suất, finance — tài chính, risk — rủi ro, user impact — tác động người dùng, etc.)
3. Vẽ attack relation: argument A attacks argument B vì lý do gì

### Bước 2 — Identify Structural Traps (xác định bẫy cấu trúc)
1. Kiểm tra: có argument nào mà defender (người bảo vệ) cũng là attacker (người tấn công) không?
   - Nếu argument X defend Y nhưng cũng attack Y → structural trap (bẫy cấu trúc)
2. Kiểm tra: under full relevance (tất cả perspectives active), target argument có accepted không?
3. Nếu rejected → xác định bottleneck (nút thắt): perspective nào gây rejection?

### Bước 3 — Select Perspective Activation (chọn kích hoạt góc nhìn — ρ)
1. Liệt kê tất cả subsets non-empty (tập con không rỗng) của perspectives Π
2. Với mỗi subset ρ, check: target argument có accepted không?
3. Ưu tiên ρ mà:
   - Deactivate perspective gây structural trap
   - Giữ active perspective mà proposal strongest (mạnh nhất)
   - Có external perspective defend mà không attack back

### Bước 4 — Execute Strategy (thực thi chiến lược)
1. Chọn review tracks/forums tương ứng với ρ đã chọn
2. Include stakeholders thuộc active perspectives trước
3. Frame discussion qua lens đã chọn
4. Nếu bị challenge (thách thức) qua deactivated perspective → redirect (chuyển hướng) về active lens

## Output mong đợi
- Target argument accepted under selected perspective activation
- Strategic advantage (lợi thế chiến lược): proposal được evaluate qua lens có lợi nhất
- Stakeholders aligned (căn chỉnh) với evaluation framework bạn chọn

## Ví dụ áp dụng
**Tình huống**: Engineering team propose microservice migration (di chuyển kiến trúc microservice). Arguments: latency improvement (cải thiện độ trễ — performance), operational complexity (độ phức tạp vận hành — reliability — độ tin cậy), deployment cost (chi phí triển khai — finance), regression risk (rủi ro hồi quy — reliability). Finance reviewer strongly opposes (phản đối mạnh).

**Áp dụng**:
- Perspectives: Π = {performance, reliability, finance}
- Target: accept migration proposal
- Full relevance: rejected (finance attacks cost, reliability attacks complexity)
- Select ρ = {performance, reliability}: deactivate finance lens
- Action: Schedule review with performance + reliability leads first, present as technical decision not cost decision (trình bày là quyết định kỹ thuật, không phải quyết định chi phí)
- Result: proposal accepted under technical evaluation, finance deferred to later phase (hoãn sang giai đoạn sau)

## Lưu ý quan trọng
1. **Ranh giới đạo đức**: Deactivating perspective = hiding relevant information (giấu thông tin liên quan). Chỉ đạo đức khi proposal thực sự phù hợp với lens đã chọn
2. **Rủi ro backfire (phản tác dụng)**: Nếu stakeholder bị deactivated cảm thấy bị bypass (bỏ qua) → political backlash (phản ứng chính trị)
3. **Dynamic arguments (lập luận động)**: Attack relations có thể thay đổi khi new information xuất hiện → revisit map (xem lại bản đồ) thường xuyên
4. **Incomplete information (thông tin không đầy đủ)**: Bạn có thể không biết đầy đủ attack relations → structural trap analysis có thể sai
5. **Priority π cố định**: Bạn chọn được ρ nhưng không thay đổi π — nếu priority trong lens đó bất lợi, deactivation không đủ
