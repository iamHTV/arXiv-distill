# Skill: harness-learning-reusable-specialist-agents
Source: 2609.26760v2
Type: framework

## Khi nào dùng skill này
- Agent xử lý luồng các tác vụ liên quan (ví dụ duyệt web, lấy dữ liệu, xử lý file liên tiếp).
- Muốn cắt chi phí inference vì LLM bị hỏi lại cùng các quyết định điều khiển mỗi lần.
- Có thể thu thập feedback từ các lần chạy trước để cải thiện harness.

## Tình huống KHÔNG nên dùng
- Tác vụ độc lập hoàn toàn, không có luồng liên quan.
- Không có cách thu thập feedback từ lần chạy trước.

## Input cần có
- Các tác vụ liên quan sẽ được agent xử lý liên tiếp.
- Hệ thống gọi tool (tool-calling agent) đã có sẵn.
- Cơ chế ghi nhận feedback (thành công/thất bại) từ mỗi lần chạy.

## Các bước thực hiện
1. Chạy agent trên các tác vụ đầu tiên, ghi nhận feedback (thành công/thất bại, sai sót ở đâu).
2. Chuyển các quyết định điều khiển lặp đi lặp lại từ LLM thành code tái sử dụng (harness), dựa trên feedback.
3. Thêm function-level guidance (hướng dẫn cấp hàm) để agent biết nên gọi hàm nào trong từng tình huống.
4. Thêm gate validation (xác thực cổng) trước khi agent chuyển sang bước tiếp theo.
5. Lặp lại: mỗi lần chạy mới, harness cải thiện bản thân từ feedback trước đó, giảm số lần gọi LLM.

## Output mong đợi
- Giảm 76–92% LLM calls và 74–99% inference cost so với Tool-Calling mặc định.
- Thành công duy trì ở mức cao (44.7–45.3% trên WebArena-Verified) ngay cả với mô hình nhỏ 4B.

## Ví dụ áp dụng
Solopreneur chạy agent thu thập dữ liệu từ nhiều trang web liên quan. Thay vì để LLM suy nghĩ lại cách duyệt mỗi trang, hãy lưu lại các bước duyệt thành code reusable (harness). Agent chỉ gọi LLM khi gặp trang mới có cấu trúc khác. Chi phí inference giảm hơn 75%.

## Gotchas
- Bỏ function-level guidance làm giảm thành công cuối cùng từ 36% xuống 18%.
- Không áp dụng cho tác vụ độc lập, không có luồng phản hồi để tích luỹ.
- Thành công trên các benchmark web vẫn ở mức trung bình (44–45%), cần đánh giá thêm trên tác vụ thực tế của bạn.
