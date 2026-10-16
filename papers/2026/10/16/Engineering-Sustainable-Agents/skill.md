# Skill: sustainable-agent-design-pareto
Source: 2610.03010v1
Type: framework

## Khi nào dùng skill này
- Xây dựng pipeline AI dev (code generation, technical debt detection, vulnerability detection, log analysis).
- Muốn cân bằng giữa độ chính xác, năng lượng và latency (chi phí).
- Cân nhắc xem có nên dùng multi-agent hay không.

## Tình huống KHÔNG nên dùng
- Tác vụ đơn giản chỉ cần một bước, không cần agent.
- Không quan tâm đến chi phí năng lượng/latency, chỉ quan tâm độ chính xác tuyệt đối.

## Input cần có
- Danh sách các tác vụ dev cần thực hiện.
- Các mô hình LLM có sẵn (từ nhỏ đến lớn).
- Chiến lược prompt (zero-shot, few-shot) có thể áp dụng.

## Các bước thực hiện
1. Xác định tác vụ dev và chọn mô hình LLM phù hợp (không nhất định là mô hình lớn nhất).
2. Thử cấu hình no-agent (NA) hoặc single-agent (SA) trước, không nhảy ngay đến multi-agent.
3. Áp dụng few-shot prompting với ví dụ cụ thể cho tác vụ định dạng đầu ra (ví dụ log parsing).
4. Đo énergie, latency và accuracy trên từng cấu hình, xây dựng Pareto front.
5. Chỉ thêm multi-agent (MA) nếu có bằng chứng rõ ràng là lợi ích về accuracy vượt trội hơn chi phí tăng 6.36× năng lượng, 6.07× thời gian.

## Output mong đợi
- Cấu hình nhẹ thường chiếm 55–90% các điểm Pareto-optimal (tối ưu Pareto).
- Tiết kiệm năng lượng và thời gian so với multi-agent mặc định.

## Ví dụ áp dụng
Solopreneur xây pipeline sửa lỗi code tự động: bắt đầu với single-agent + few-shot prompt (ví dụ 3 mẫu sửa lỗi), đo energy và latency. Chỉ xem xét multi-agent nếu single-agent không đạt đủ độ chính xác và chi phí thêm được chấp nhận.

## Gotchas
- Multi-agent tốn 6.36× năng lượng và 6.07× thời gian so với non-agentic, worst-case chậm 160×.
- MA chỉ xuất hiện trong 1/66 cấu hình Pareto-optimal — không nên là lựa chọn mặc định.
- Few-shot đôi khi gây ràng buộc hoặc làm nhiễu (ví dụ code generation tốt hơn ở zero-shot 97.3% vs 92.7%).
