# Skill: sustainable-agent-design
Source: 2610.03010v1
Type: framework

## Khi nào dùng skill này
- Xây dựng agent dev (developer agent) và cần tối ưu hóa chi phí năng lượng và thời gian.
- Cần chọn model và prompt phù hợp với từng tác vụ thay vì dùng một cấu hình duy nhất.
- Cân bằng giữa độ chính xác (accuracy), năng lượng (energy), và thời gian (time).

## Tình huống KHÔNG nên dùng
- Nhiệm vụ đơn giản không cần agent.
- Không cần tối ưu hóa chi phí năng lượng và thời gian.
- Không có nhiều model và prompt để lựa chọn.

## Input cần có
- Các tác vụ phần mềm (code generation, technical debt identification, code vulnerability detection, log parsing, log analysis).
- Các mô hình LLM (open-weight models).
- Các harness agent (agent harness).
- Các spec (skill specification) và test cases.

## Các bước thực hiện
1. Xác định tác vụ phần mềm cần thực hiện.
2. Chọn model LLM phù hợp với tác vụ.
3. Chọn prompt strategy phù hợp với tác vụ.
4. Chọn agent configuration (non-agentic, single-agent, multi-agent).
5. Chọn hardware platform (CPU, GPU, etc.).
6. Đánh giá mỗi cấu hình theo accuracy, inference latency, và energy consumption.
7. Chọn cấu hình Pareto-optimal (tiết kiệm năng lượng và thời gian mà không làm giảm accuracy quá nhiều).

## Output mong đợi
- Giảm chi phí năng lượng (energy consumption) và thời gian (inference latency) cho agent dev.
- Duy trì độ chính xác (accuracy) cho các tác vụ phần mềm.
- Chọn cấu hình Pareto-optimal cho từng tác vụ.

## Ví dụ áp dụng
- Xây dựng agent dev để viết code, sửa lỗi (bug fix), và viết test. Dùng sustainable agent design để chọn model và prompt phù hợp với từng tác vụ, giảm chi phí năng lượng và thời gian mà không làm giảm độ chính xác quá nhiều.

## Gotchas
- Đánh giá trên các benchmark code-repair từ các issue GitHub, kết quả có thể không chuyển tiếp sang các benchmark agent trong các miền khác.
- Đánh giá trên 4 backbone models.
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).
- Không mặc định multi-agent — cấu hình nhẹ thường Pareto-optimal hơn.
