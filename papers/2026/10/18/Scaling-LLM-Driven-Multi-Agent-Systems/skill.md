# Skill: Thiết kế Multi-Agent System khả dìng mở rộng theo 4 nguyên tắc

Source: 2607.27942v1
Type: framework

## Khi nào dùng skill này
- Bạn đang xây dựng hệ thống multi-agent (MAS) dựa trên LLM và muốn biết cách mở rộng mà không làm giảm hiệu quả.
- Bạn có một model LLM cơ bản đã đạt độ chính xác chấp nhận được trên task đơn lẻ và muốn biết khi nào nên thêm agent.
- Bạn cần thiết kế giao tiếp giữa các agent để tránh quá tải ngữ cảnh (context overload) khi hệ thống lớn lên.

## Tình huống KHÔNG nên dùng
- Model LLM cơ bản chưa đạt độ chính xác cơ bản trên task mục tiêu (kiến trúc phức tạp không bù đắp cho model yếu).
- Bạn cần một hệ thống đơn giản, chỉ 1 agent là đủ — không cần multi-agent.

## Input cần có
- Task mục tiêu rõ ràng (ví dụ: giải quyết tác vụ hệ thống kỹ thuật, viết code, quản lý dự án).
- Model LLM cơ bản đã được đánh giá trên task đơn lẻ.
- Danh sách vai trò agent cần thiết (ví dụ: Planner, Solver, Tester, Approver).

## Các bước thực hiện
1. Xác nhận model cơ bản đủ năng lực: chạy model đơn lẻ trên task mục tiêu, chỉ tiếp tục nếu accuracy đạt ngưỡng chấp nhận được.
2. Thiết kế workflow chủ yếu theo thứ tự tuyến tính (sequential workflow), chỉ chèn vòng lặp phản hồi (feedback loop) ở các giai đoạn thực sự cần refine (ví dụ: Tester → Solver).
3. Áp dụng truyền thông dựa trên tóm tắt (summary-based communication): mỗi agent hoàn thành xong thì viết tóm tắt ngôn ngữ tự nhiên 2–3 câu vào kênh chung, không chia sẻ toàn bộ reasoning trace.
4. Giới hạn mỗi agent tối đa 3 Nachfolger trong topology để kiểm soát độ phức tạp.
5. Mở rộng kiến trúc từng cấp độ (Singleton → MAS-S → MAS-M → MAS-L), theo dõi chi phí và độ chính xác ở mỗi cấp, dừng khi accuracy không còn tăng.

## Output mong đợi
- Một hệ thống multi-agent có kiến trúc rõ ràng, mỗi agent biết vai trò và ai là agent kế tiếp.
- Mỗi lượt agent chỉ sinh ra tóm tắt ngắn gọn, không dump toàn bộ context.
- Chi phí inference tăng tuyến tính (không exploding), độ chính xác đạt đỉnh ở độ phức tạp trung bình.

## Ví dụ áp dụng
Bạn xây dựng agent viết code tự động. Thay vì để 1 agent lớn làm tất cả, bạn chia thành: Planner (lập kế hoạch), Coder (viết code), Tester (chạy test), Reviewer (kiểm tra). Mỗi agent nhận tóm tắt từ agent trước, làm xong thì ghi tóm tắt vào kênh chung, và quyết định ai chạy tiếp. Nếu test thất bại, Reviewer kích hoạt vòng lặp quay lại Coder.

## Gotchas
- Không thêm agent để bù đắp cho model LLM yếu — kiến trúc MAS khai thác khả năng có sẵn, không tạo ra khả năng mới.
- Tính nhất quán (consistency) thường dưới 50% ở mọi cấp độ mở rộng — cần đo cả consistency cùng accuracy.
- Vòng lặp phản hồi chỉ có ích nếu agent chịu trách nhiệm thực sự kích hoạt chúng; nếu không, vòng lặp bị bỏ qua và không tạo giá trị.