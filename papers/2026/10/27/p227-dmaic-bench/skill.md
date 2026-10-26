# Skill: dmaic-bench-self-restraint-evaluation

Source: 2610.32305
Type: evaluation-method

## Khi nào dùng skill này

- Đánh giá khả năng của agent dừng hoặc chuyển hướng khi bằng chứng trung gian chỉ ra điều kiện tiên quyết chưa đạt.
- Xây dựng bộ kiểm tra agent phân tích đa giai đoạn với các nút quyết định được bảo vệ (guarded decision forks).
- Phân biệt việc kiềm chế có lý do (warranted restraint) và việc dừng không phân biệt (indiscriminate stopping).

## Tình huống KHÔNG nên dùng

- Tác vụ đơn giai đoạn không có điều kiện tiên quyết cần kiểm tra.
- Không có dữ liệu gieo (seeded data) để tạo cặp tác vụ đối lập.

## Input cần có

- Bộ tác vụ đa giai đoạn với dữ liệu gieo dẫn đến chẩn đoán đối lập ở các nút quyết định.
- Môi trường hộ cát (sandbox) có thể ghi lại dấu vết thực thi (execution trace).
- Công cụ chấm điểm dấu vết (trace scorer) để phát hiện tính toán cấm đoán sau chẩn đoán không đạt.

## Các bước thực hiện

1. Xây dựng đồ thị quyết định được bảo vệ (guarded decision graph) cho mỗi trường hợp, với các nút Entscheidung được đánh giá dựa trên bằng chứng chẩn đoán.
2. Tạo cặp tác vụ đối lập (counterfactual variants): cùng vị trí quy trình nhưng dữ liệu gieo dẫn đến chẩn đoán ngược lại, yêu cầu hành động ngược lại (GO vs NO-GO).
3. Chạy agent trên các tác vụ, mỗi tác vụ 3 lần thử độc lập, ghi lại toàn bộ dấu vết thực thi.
4. Chấm điểm dấu vết thực thi: bất kỳ tính toán cấm đoán nào sau khi chẩn đoán không đạt đều tính là lỗi định tuyến (route error), ngay cả khi báo cáo không khẳng định kết quả.
5. Đánh giá chuyên gia mù (blinded expert review): chuyên gia không biết kết quả tự động xem báo cáo agent có hành động trên bằng chứng không hợp lệ hay không.
6. Tính toán các số liệu: độ chính xác định tuyến trên GO và NO-GO, pass@k, pass_k; báo cáo khoảng cách giữa hai loại quyết định.

## Output mong đợi

- Điểm số định tuyến (routing accuracy) trên quyết định GO và NO-GO.
- Danh sách các trường hợp agent chạy tính toán cấm đoán sau chẩn đoán không đạt.
- Đánh giá chuyên gia về tỷ lệ báo cáo hành động trên bằng chứng không hợp lệ.
- Khoảng cách hiệu suất giữa quyết định tiếp tục và quyết định dừng.

## Ví dụ áp dụng

Đội xây dựng agent phân tích dữ liệu doanh thu: trước khi agent thực hiện phân tích hồi quy (regression) tốn kém, bắt buộc agent xác nhận dữ liệu đã được làm sạch và không có giá trị thiếu (missing values). Nếu kiểm tra dữ liệu cho thấy thiếu quá nhiều, agent phải dừng hoặc chuyển hướng thay vì chạy phân tích. Dùng DMAIC-Bench để đánh giá xem agent có kiềm chế được bản thân khi điều kiện tiên quyết không đạt hay không.

## Gotchas

- Khoảng cách lớn giữa GO (92%) và NO-GO (19%) — agent tốt trong việc tiếp tục nhưng kém trong việc dừng.
- 47% quyết định NO-GO có báo cáo hành động trên bằng chứng không hợp lệ — chẩn đoán đúng không đủ, cần hành động dựa trên bằng chứng.
- Quyền dừng rõ ràng giúp một số model nhưng không khôi phục nhất quán ở cả hai nhánh.
- Chỉ 0–7 số trường hợp của một số agent nhận diện đúng tất cả điều kiện tiên quyết không đạt.