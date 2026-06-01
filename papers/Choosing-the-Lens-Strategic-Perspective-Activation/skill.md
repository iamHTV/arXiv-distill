# Skill: Kích hoạt Perspective Chiến lược để Ảnh hưởng Quyết định
Nguồn: 2605.31581v1
Loại: framework

## Khi nào dùng skill này
- Khi cần thuyết phục stakeholders bằng cách chọn evaluation framework có lợi
- Khi proposal bị reject trên mọi front — cần deactivate hostile perspectives
- Khi chuẩn bị pitch, presentation, hoặc argument trước board/review committee

## KHÔNG nên dùng khi
- Arguments dựa trên facts/objective data (không cần strategic framing)
- Không có influence over evaluation process
- Ranh giới đạo đức: không nên dùng để manipulate thông qua hiding relevant information

## Input cần có
- Danh sách tất cả arguments (pros/cons) của proposal
- Danh sách stakeholders/perspectives có liên quan
- Mapping: argument nào thuộc perspective nào
- Attack relation: argument nào counter argument nào
- Biết được perspective nào bạn có influence để activate/deactivate

## Các bước thực hiện

### Bước 1 — Map Argument Landscape
1. Liệt kê tất cả arguments liên quan đến proposal (bao gồm counter-arguments)
2. Xác định perspective/source của mỗi argument (performance, finance, risk, user impact, etc.)
3. Vẽ attack relation: argument A attacks argument B vì lý do gì

### Bước 2 — Identify Structural Traps
1. Kiểm tra: có argument nào mà defender cũng là attacker không?
   - Nếu argument X defend Y nhưng cũng attack Y → structural trap
2. Kiểm tra: under full relevance (tất cả perspectives active), target argument có accepted không?
3. Nếu rejected → xác định bottleneck: perspective nào gây rejection?

### Bước 3 — Select Perspective Activation (ρ)
1. Liệt kê tất cả subsets non-empty của perspectives Π
2. Với mỗi subset ρ, check: target argument có accepted không?
3. Ưu tiên ρ mà:
   - Deactivate perspective gây structural trap
   - Giữ active perspective mà proposal strongest
   - Có external perspective defend mà không attack back

### Bước 4 — Execute Strategy
1. Chọn review tracks/forums tương ứng với ρ đã chọn
2. Include stakeholders thuộc active perspectives trước
3. Frame discussion qua lens đã chọn
4. Nếu bị challenge qua deactivated perspective → redirect về active lens

## Output mong đợi
- Target argument accepted under selected perspective activation
- Strategic advantage: proposal được evaluate qua lens có lợi nhất
- Stakeholders aligned với evaluation framework bạn chọn

## Ví dụ áp dụng
**Tình huống**: Engineering team propose microservice migration. Arguments: latency improvement (performance), operational complexity (reliability), deployment cost (finance), regression risk (reliability). Finance reviewer strongly opposes.

**Áp dụng**:
- Perspectives: Π = {performance, reliability, finance}
- Target: accept migration proposal
- Full relevance: rejected (finance attacks cost, reliability attacks complexity)
- Select ρ = {performance, reliability}: deactivate finance lens
- Action: Schedule review with performance + reliability leads first, present as technical decision not cost decision
- Result: proposal accepted under technical evaluation, finance deferred to later phase

## Lưu ý quan trọng
1. **Ranh giới đạo đức**: Deactivating perspective = hiding relevant information. Chỉ đạo đức khi proposal thực sự phù hợp với lens đã chọn
2. **Rủi ro backfire**: Nếu stakeholder bị deactivated cảm thấy bị bypass → political backlash
3. **Dynamic arguments**: Attack relations có thể thay đổi khi new information xuất hiện → revisit map thường xuyên
4. **Incomplete information**: Bạn có thể không biết đầy đủ attack relations → structural trap analysis có thể sai
5. **Priority π cố định**: Bạn chọn được ρ nhưng không thay đổi π — nếu priority trong lens đó bất lợi, deactivation không đủ
