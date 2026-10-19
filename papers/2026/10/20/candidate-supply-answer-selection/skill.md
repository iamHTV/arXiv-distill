# Skill: candidate-supply-answer-selection
Source: 2608.25937v2
Type: framework

## Khi nào dùng skill này
- Hệ thống đa agent tạo ra nhiều ứng viên câu trả lời nhưng cần chọn một đáp án cuối.
- Muốn biết khi nào nên dùng LLM judge để xếp hạng ứng viên thay vì chỉ bình chọn đa số.
- Có banco ứng viên cố định (hoặc có thể tạo) và muốn đánh giá độ tin cậy của judge trước khi triển khai.

## Tình huống KHÔNG nên dùng
- Đáp án đúng chiếm đa số banco ứng viên (ppool ≥ 0.25) → bình chọn đa số đã đủ tốt, judge thậm chí làm giảm độ chính xác.
- Giả định độ tin cậy của judge là tính chất cố định, áp dụng mọi tác đơn và generator.

## Input cần có
- Banco ứng viên (candidate bank) gồm nhiều đáp án ứng viên và lý thuyết hỗ trợ, tạo ra từ các agent hoặc gọi lại generator.
- LLM judge có thể xếp hạng các lý thuyết ứng viên ẩn danh (không thấy đáp án/nhãn đúng-sai).
- Mức độ sẵn có đáp án đúng pgen (tỉ lệ thực nghiệm ứng viên đúng trong banco).
- Kích thước banco k (ví dụ k=8) và ngưỡng trùng hợp ứng viên đúng ppool.

## Các bước thực hiện
1. Tạo banco ứng viên: gọi lại generator nhiều lần trên mỗi câu hỏi, thu thập đáp án ứng viên + lý thuyết hỗ trợ; tính pgen (tỉ lệ ứng viên đúng).
2. Chạy bình chọn đa số làm đọc đầu tiên (t=0): chọn đáp án phổ biến nhất.
3. Chạy LLM judge xếp hạng các ứng viên ẩn danh trong banco; đo rank ASEAN (xác suất ứng viên đúng được xếp hạng trên sai).
4. Đánh giá độ tin cậy của judge theo pgen: rank ASEAN dưới 0.5 ở khả năng thấp means judge không tin được khi đáp án đúng hiếm; half-rise midpoint cho biết mức pgen khi judge bắt đầu đáng tin cậy.
5. Áp dụng quy tắc chọn cuối kết hợp tần suất bình chọn + xếp hạng judge (trọng số rank wi = (k−i)^t, t=2–4 cho độ ổn định cao nhất): chọn đáp án kết hợp cả hai tín hiệu.
6. Đánh giá theo kích thước banco: banco nhỏ (k=2–6) judge selection hiệu quả nhất (vượt bình chọn +13.52 pp ở k=2); banco lớn (k≥14) bình chọn càng cạnh tranh, judge chi phí cao hơn.
7. Phân loại theo ppool (tỷ lệ đáp án đúng thực tế trong banco): ppool < 0.25 (thiểu số đúng nhỏ) → judge vượt bình chọn nhiều (+40.1 pp ở k=6); ppool ≥ 0.25 → bình chọn vượt judge (−4.0 pp ở k=6).
8. Theo dõi chi phí: giud selection hiệu quả chi phí ở banco nhỏ (US$0.10–0.39 trên 1.000 câu trả lời đúng bổ sung k=2–6), chi phí leo thang ở banco lớn (US$6.28 ở k=14).

## Output mong đợi
- Quy tắc chọn câu cuối tối ưu (kết hợp tần suất bình chọn + xếp hạng judge) biết khi nào cứu đáp án đúng thiểu số, khi nào dùng bình chọn đa số; đánh giá độ tin cậy của judge trong régime thực tế.

## Ví dụ áp dụng
- Hệ thống trả lời hỏi đáp y khoa đa agent: tạo 8 ứng viên đáp án từ 8 agent; chạy bình chọn đa số; chạy LLM judge xếp hạng 8 ứng viên; kết hợp cả hai (t=3) để chọn đáp án cuối — câu đúng ít phổ biến có cơ hội được chọn hơn bình chọn thuần túy.

## Gotchas
- Không dùng judge khi đáp án đúng chiếm đa số banco (ppool ≥ 0.25): bình chọn đã tốt, judge làm giảm độ chính xác (−3.22 pp ở pgen > 0.625).
- Không coi điểm benchmark tĩnh của judge là bảo đảm toàn cầu: độ tin cậy thay đổi theo generator, tác đơn và pgen.
- Không cho rằng tạo thêm ứng viên luôn tốt: giá trị phụ thuộc vào liệu mẫu mới làm câu đúng hiện diện, phổ biến hay để lại thiểu số.
- Không bỏ qua chi phí judge: tại k lớn chi phí leo thang nhanh và có thể không xứng đáng.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 8 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 4 (đánh giá độ tin cậy judge theo pgen) cần tính pgen chính xác từ banco ứng viên.
- Input section có đủ không? [YES] — banco ứng viên, judge, pgen, kích thước banco k, ppool.

## Dry run (tình huống giả)
- Tình huống: Hệ thống y khoa đa agent trả lời câu hỏi chẩn đoán; tạo 8 ứng viên từ 8 agent chạy song song.
- Chạy skill: (1) Thu thập 8 ứng viên + lý thuyết cho mỗi câu hỏi; (2) tính pgen (tỉ lệ ứng viên đúng theo đáp án chuẩn); (3) chạy bình chọn đa số; (4) LLM judge xếp hạng 8 ứng viên ẩn danh; (5) đo rank ASEAN theo pgen; (6) kết hợp tần suất + xếp hạng (t=3) chọn đáp án cuối; (7) so sánh độ chính xác với bình chọn thuần túy; (8) nếu pgen thấp (đáp án đúng hiếm) và judge rank ASEAN > 0.5 → dùng kết hợp judge; nếu pgen cao → dùng bình chọn đa số.

## Verdict: [SKILL VALID]
