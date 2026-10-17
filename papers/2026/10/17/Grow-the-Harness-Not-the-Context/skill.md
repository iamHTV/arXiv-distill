# Skill: grow-the-harness-reusable-specialist-agents
Source: 2609.26760v2
Type: framework

## Khi nào dùng skill này
- Xây dựng agent cần xử lý nhiều tác vụ liên quan (streams of related tasks) cùng loại.
- Muốn giảm chi phí LLM calls và inference cost cho agent chạy nhiều lần trên cùng loại tác vụ.
- Có dữ liệu quỹ đạo (trajectory) từ các lần chạy agent trước đó.

## Tình huống KHÔNG nên dùng
- Nhiệm vụ đơn lẻ không phải chuỗi liên quan.
- Không có dữ liệu quỹ đạo (trajectory) từ các lần chạy trước.
- Không cần giảm chi phí LLM calls và inference cost.

## Input cần có
- Các quỹ đạo (trajectory) từ các lần chạy agent trước trên các tác vụ liên quan.
- Mô hình nhúng (embedding model) để tạo biểu diễn số từ quỹ đạo.
- Mô hình LLM để sinh code điều khiển.

## Các bước thực hiện
1. Phân tích các quỹ đạo (trajectory) từ các lần chạy agent trước trên các tác vụ liên quan.
2. Xây dựng Bidirectional Evidence Trace (BET) bền vững — kết nối cách harness tiêu thụ đầu vào với các điều kiện cần để một thao tác được chọn trở nên không an toàn.
3. Giữ các tương quan được nguồn minh chứng (source-supported correspondences) cùng với giả thiết (hypotheses) và câu hỏi mở (open questions) của agent.
4. Cung cấp lệnh đọc (reading), phân tích (analysis), và lưu trữ (persistence) để agent xây dựng và tái sử dụng bằng chứng này thay vì liên tục truy xuất và tái cấu trúc lại.
5. Đánh giá trên các benchmark và hai backbone (backbone) như Growing Harness đã làm trên BrowseComp-Plus và WebArena-Verified.

## Output mong đợi
- Hệ thống agent có khả năng xử lý nhiều tác vụ liên quan với chi phí LLM calls và inference cost thấp hơn đáng kể.
- Growing Harness đạt mean success cao nhất trong năm của sáu cấu hình benchmark-model và trails best mean bởi 0.7 pp. trong thứ sáu.
- So với Tool-Calling agent, nó giảm LLM calls bởi 76.0–91.8% và deployed-agent inference cost bởi 74.4–98.6%.
- Trên WebArena-Verified, thành công của nó vẫn ở mức 44.7–45.3% trên các model scales, trong khi Tool-Calling rơi xuống 6.7% với model 4B.

## Ví dụ áp dụng
- Xây dựng agent xử lý các tác vụ liên quan trên cùng loại dữ liệu (ví dụ: xử lý hóa đơn, kiểm tra tài liệu, v.v.). Dùng Grow the Harness để biến feedback thành code điều khiển tái sử dụng, giảm 76.0–91.8% LLM calls và 74.4–98.6% inference cost.

## Gotchas
- Đánh giá trên BrowseComp-Plus và WebArena-Verified với ba deployment models từ 4B đến 120B parameters.
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).
- Không mặc định multi-agent — cấu hình nhẹ thường Pareto-optimal hơn.
