# Skill: mining-design-space-multi-agent-workflows

Source: 2610.31709
Type: framework

## Khi nào dùng skill này

- Thiết kế workflow multi-agent LLM cho tác vụ lý luận phức tạp đòi hỏi phối hợp giữa các agent.
- Muốn chọn cấu trúc liên lạc (communication topology) và mẫu prompt có thể cải thiện độ chính xác mà không cần thử sai nhiều lần.
- Có thể thu thập các dấu vết thực thi (execution trace) từ các lần tìm kiếm workflow trước đó.

## Tình huống KHÔNG nên dùng

- Tác vụ đơn giản không cần nhiều agent phối hợp (single-agent đủ).
- Không có dữ liệu tìm kiếmWorkflow trước (không có chuỗi tìm kiếm MCTS hoặc các workflow đã đánh giá).

## Input cần có

- Bộ sưu tập các workflow đã đánh giá với mã nguồn graph.py và prompt.py.
- Nhóm nhiệm vụ có điểm số xác định định mức (deterministically verified score).
- Công cụ để chạy các workflow và thu thập dấu vết thực thi.

## Các bước thực hiện

1. Chạy tìm kiếm workflow qua MCTS (ví dụ AFlow) qua N vòng trên mỗi nhiệm vụ, giữ lại TẤT CẢ các vòng trung gian (không chỉ giữ workflow tốt nhất).
2. Xây dựng bộ sưu tập các triplet (workflow, nhiệm vụ, điểm số) từ tất cả các vòng tìm kiếm, bao gồm cả các vòng thất bại.
3. Phân tích mã workflow (graph.py) và mẫu prompt (prompt.py) để trích xuất tính năng: toán tử bắt đầu (entry operator), độ dài chuỗi, số lượng placeholder, độ dài mẫu prompt, v.v.
4. Fit mô hình hồi quy từ tính năng workflow và mô tả nhiệm vụ đến điểm số, sử dụng mục tiêu bị phạt L0 (R² − λ||phi||₀) để chọn ít tính năng nhất có sức giải thích cao.
5. Xác thực các nguyên tắc được khai thác trên các vòng tìm kiếm riêng lẻ (held-out searches) không dùng trong quá trình đào tạo.
6. Áp dụng nguyên tắc xác thực: tránh bắt đầu bằng Star fan-out, dùng SharedMemory thay vì Debate, viết prompt cụ thể có named placeholder.

## Output mong đợi

- Danh sách các nguyên tắc thiết kế workflow được xác thực trên dữ liệu riêng lẻ.
- Công thức tính điểm và mục tiêu L0-penalized để đánh giá các thiết kế workflow mới.
- Khuyến nghị cụ thể về cấu trúc liên lạc và mẫu prompt cho tác vụ mục tiêu.

## Ví dụ áp dụng

Đội xây dựng agent chăm sóc khách hàng multi-agent: thay vì để 5 agent độc lập xử lý các khía cạnh khác nhau của một đơn hàng rồi tổng hợp (Star-first), hãy bắt đầu bằng một agent điều phối tuần tự (Sequential) và dùng một tài liệu chia sẻ liên tục (SharedMemory) để các agent cập nhật thông tin đơn hàng. Viết prompt template chi tiết với các ô trống như {order_details}, {customer_history} để định tuyến ngữ cảnh.

## Gotchas

- Star-first làm giảm hiệu quả (median Δ = −0.045) — không nên bắt đầu bằng fan-out độc lập.
- SharedMemory vượt trội hơn Debate (Δ = +0.135) — tài liệu liên tục tốt hơn luồng hội thoại nhiều vòng.
- Cấu trúc prompt cụ thể có lợi tương đương việc chọn cấu trúc liên lạc (Δ = +0.118) — không nên xem thường thiết kế mẫu prompt.
- R² chỉ từ graph.py = 0.521, cùng với prompt.py = 0.638 — cấu trúc dưới cấp (sub-topological) trong prompt quan trọng bằng cấu trúc宏觀.