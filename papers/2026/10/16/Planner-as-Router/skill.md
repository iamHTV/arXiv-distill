# Skill: planner-as-router-model-routing
Source: 2609.32917v1
Type: framework

## Khi nào dùng skill này
- Multi-agent workflow có nhiều bước (subtasks) khác nhau độ phức tạp.
- Muốn cắt chi phí inference vì hiện nay dùng frontier model cho mọi bước.
- Có thể ước lượng độ phức tạp của từng bước trước khi chọn model.

## Tình huống KHÔNG nên dùng
- Workflow chỉ có 1 bước, không cần routing nhiều tier model.
- Không thể ước lượng độ phức tạp của tác vụ trước khi chạy.

## Input cần có
- Danh sách các model tiers có sẵn (small/mid/frontier).
- Cơ chế phân loại độ phức tạp của từng subtask (complexity classifier).
- Workflow chia thành các subtask độc lập.

## Các bước thực hiện
1. Chia workflow thành các subtask, mỗi subtask có task type.
2. Dùng complexity classifier để phân loại từng subtask thành SIMPLE hoặc COMPLEX.
3. Định tuyến subtask SIMPLE đến model small, subtask COMPLEX đến model mid/frontier.
4. Theo dõi plan mix (tỷ lệ small/mid/frontier) để điều chỉnh classifier.
5. Chỉ dùng frontier model cho subtask thực sự cần reasoning sâu.

## Output mong đợi
- Giảm chi phí inference khoảng 44% so với dùng frontier model cho mọi bước.
- Mất chỉ khoảng 2.9 điểm độ chính xác.

## Ví dụ áp dụng
Solopreneur chạy pipeline viết báo cáo kinh doanh: bước 1 thu thập dữ liệu (dùng model small), bước 2 phân tích xu hướng (dùng model lớn), bước 3 viết báo cáo (dùng model mid). Planner-as-Router route tự động mỗi bước đến model tier phù hợp, cắt chi phí inference khoảng 44%.

## Gotchas
- Chỉ giảm 2.9 điểm độ chính xác so với all-frontier — có thể chấp nhận được đối với nhiều trường hợp.
- Cần complexity classifier hoạt động tốt; nếu phân loại sai, chất lượng sẽ giảm.
- Absolute accuracies thấp (22-29%) trên các tác vụ compositional khó.
