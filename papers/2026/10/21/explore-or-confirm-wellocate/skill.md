# Skill: explore-or-confirm-wellocate

Source: 2610.25111v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần đo lường cách agent LLM phân bổ ngân sách thí nghiệm ồn ào giữa khám phá ứng cử viên mới và xác nhận ứng cử viên hứa hẹn.
- Khi muốn phát hiện agent over-confirm (kiểm tra lại quá nhiều) hoặc under-confirm (kiểm tra lại quá ít) trong thí nghiệm costly.
- Khi cần cung cấp danh sách ứng viên chưa thử để agent không cạn kiệt không gian tìm kiếm.

## Tình huống KHÔNG nên dùng
- Khi không có landscape với giá trị thực Known để so sánh.
- Khi thí nghiệm không có ồn ào đo l량 (đọc số xác định).
- Khi chỉ cần một quy tắc cố định cho mọi tình huống thí nghiệm.

## Input cần có
- Landscape với giá trị thực Known cho mỗi ứng viên (hoặc dữ liệu protein thực đã xáo trộn tên).
- Mô hình ồn ào mô phỏng sai số thí nghiệm thực (độ lệch chuẩn 7.3% của giá trị đọc).
- Ngân sách đo l量 cố định (ví dụ 60 đo l量 = 15 vòng × 4 slot).
- Danh sách ứng viên khả thi (top 7% landscape).
- Ứng viên khởi đầu (trung vị khả thi).

## Các bước thực hiện
1. Thiết lập Wellocate: tạo landscape với giá trị thực Known, xáo trộn tên ứng viên để không model trả lời từ ký ức.
2. Chạy agent: mỗi vòng agent orders 4 ứng viên, môi trường trả về đọc ồn ào (giá trị thực + ồn ào 7.3%), agent thấy toàn bộ bản ghi trước mỗi vòng.
3. Theo dõi tỷ lệ kiểm tra lại (re-testing share): tỷ lệ slot dùng cho ứng viên agent đã order trước đó.
4. Đánh giá ứng viên cuối: chia sự thiếu hụt từ ứng viên tốt nhất thành exploration loss (ứng viên tốt nhất agent đã đo vs tốt nhất landscape) và selection loss (ứng viên nominate vs tốt nhất agent đã đo).
5. So sánh với 3 quy tắc scripted: guessing rule (kiểm tra lại ứng viên tốt nhất cố định số lần mỗi vòng), model-guided rule (học từ các đọc của bản thân), informed rule (biết ứng viên nào khả thi).
6. Áp dụng hỗ trợ nếu cần: Menu (danh sách 10 ứng viên chưa thử, một chữ thay đổi từ 3 ứng viên tốt nhất, xếp hạng bởi mô hình đơn giản fit từ các đọc), ledger (tóm tắt các đọc), landscape note (mô tả cách landscape xây dựng).
7. Thử thay thế vòng cuối bằng kiểm tra lại các ứng viên hàng đầu (cho under-confirmer).

## Output mong đợi
- Tỷ lệ kiểm tra lại cho từng mô hình.
- Giá trị ứng viên cuối cho từng mô hình.
- Phân tích exploration loss và selection loss.
- Hiệu ứng của các hỗ trợ (ledger, landscape note, Menu) trên kiểm tra lại và chọn cuối.

## Ví dụ áp dụng
Một phòng thí nghiệm sử dụng agent LLM để chọn biến thể protein cho thí nghiệm深 độ đột biến. Agent có 60 đọc lượng (15 vòng × 4 puits). Với Wellocate, phòng thí nghiệm đo được agent over-confirm (kiểm tra lại 94% slot) và chọn biến thể cuối kém hơn quy trình scripted đơn giản nhất. Cung cấp Menu danh sách biến thể chưa thử giúp agent cắt kiểm tra lại và chọn biến thể tốt hơn hơn 3 đơn vị giá trị thực.

## Gotchas
- Không có chi phí inference thực tế của agent.
- Không đánh giá agent có công cụ hoặc bộ nhớ ngoài.
- Không so sánh trực tiếp với các phương pháp thiết kế thí nghiệm cổ điển ngoài 3 quy tắc scripted.
- Kết quả trên 3 landscape (1 tổng hợp, 2 protein) có thể không general hoá sang mọi loại thí nghiệm.
- Chỉ đánh giá 5 mô hình ngôn ngữ.