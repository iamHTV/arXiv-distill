# Skill: trajectory-aware-subset-selection
Source: 2609.24928v2
Type: framework

## Khi nào dùng skill này
- Chọn mẫu subset để đánh giá SWE-agent regression testing mà cần giảm chi phí token.
- Có dữ liệu quỹ đạo (trajectory) từ các lần chạy trước của agent trên các instance benchmark.
- Cần ước tính tỷ lệ giải quyết (resolve rate) của toàn bộ suite dựa trên một tập con nhỏ.

## Tình huống KHÔNG nên dùng
- Không có dữ liệu quỹ đạo (trajectory) từ các lần chạy trước.
- Không cần ước tính resolve rate của toàn bộ suite, chỉ cần đánh giá trên subset.
- Không có khả năng chạy full regression run để có historical outcomes.

## Input cần có
- Các quỹ đạo (trajectory) từ các lần chạy agent trước đó trên các instance benchmark.
- Kết quả test (pass/fail) của từng instance trong lần chạy đầy đủ gần nhất.
- Mô hình nhúng (embedding model) để tạo biểu diễn số từ quỹ đạo.
- Tập hợp các instance benchmark cần đánh giá.

## Các bước thực hiện
1. Phân tích các quỹ đạo thô (raw trajectories) thành định dạng chuẩn hóa (standardized JSON schema).
2. Lọc sạch (sanitize) các quỹ đạo để loại bỏ các tín hiệu kết quả (outcome signals) như passed/failed tokens, exit code 0, tên kho lưu trữ (repository names), và các artifact của test-harness.
3. Truyền các quỹ đạo đã lọc sạch vào mô hình nhúng (embedding model) để tạo các biểu diễn số (numerical representations).
4. Nhóm các instance test set theo kết quả test (test outcome) trong lần chạy đầy đủ gần nhất (recent full test run) để bảo toàn tỷ lệ thành công/thất bại quá khứ (historical pass/fail rate).
5. Chọn subset nhỏ bằng cách lấy các instance gần trọng tâm (centroid) nhất của mỗi nhóm kết quả (outcome group) trong không gian nhúng (embedding space).
6. Trong các lần chạy sau, chỉ đánh giá subset đã chọn và dùng tỷ lệ giải quyết (resolve rate) của subset để ước tính tỷ lệ giải quyết của toàn bộ suite.

## Output mong đợi
- Subset nhỏ (5% hoặc 10% của toàn bộ test instances) giữ median estimation error dưới 5%.
- Giảm chi phí token khoảng 90% so với chạy toàn bộ suite.
- Giảm sai số ước tính (estimation error) 3–11% và sai số trường hợp tồi tệ nhất (worst-case error) 4–11% so với typical draw, 38–46% so với 95th-percentile draw của strong baseline.

## Ví dụ áp dụng
- Đánh giá SWE-agent trên SWE-Bench: thay vì chạy toàn bộ 2,200 instances, hãy chọn subset 10% (~220 instances) dựa trên trajectory embedding gần trọng tâm của mỗi nhóm kết quả (passed/failed), đánh giá trên subset này và dùng tỷ lệ giải quyết của subset để ước tính tỷ lệ giải quyết của toàn bộ suite.

## Gotchas
- Đánh giá trên các benchmark code-repair từ các issue GitHub; kết quả có thể không chuyển tiếp sang các benchmark agent trong các miền khác.
- Mỗi cấu hình chỉ chạy một lần.
- Vẫn cần chạy full regression run để có historical outcomes.
- Việc loại bỏ outcome signals từ quỹ đạo là rất quan trọng để tránh embeddings nhóm theo kết quả thay vì theo hành vi.
