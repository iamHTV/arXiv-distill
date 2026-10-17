# [2610.03010v1] Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows

## Problem
- Các tác nhân tự lý phần mềm (autonomous software engineering agents — SWE-agents) ngày càng có khả năng sửa lỗi chương trình, gỡ lỗi hệ thống phần mềm, và tạo và chạy thử nghiệm. Nhưng mỗi bản cập nhật agent có thể đòi hỏi chạy lại toàn bộ benchmark để phát hiện hồi quy và cải tiến, với chi phí hàng trăm triệu token mỗi lần, làm cho việc đánh giá trở nên bottleneck trong quá trình phát triển. Prior work chưa giải quyết việc so sánh hệ thống một cách hệ thống các agent LLM khác nhau trên các tác vụ phần mềm.

## Contribtuion
- Nghiên cứu so sánh hệ thống (systematic comparison) agentic LLM trên năm tác vụ phần mềm: code generation, technical debt identification, code vulnerability detection, log parsing, và log analysis.
- Đánh giá mỗi cấu hình dựa trên accuracy, inference latency, và energy consumption.
- Kết quả cho thấy multi-agent designs tốn trung bình 6.36× năng lượng và chạy 6.07× thời gian so với non-agentic baseline, với worst-case slowdowns lên đến 160× cho từng task-hardware pair.
- Accuracy gains từ việc thêm agents là limited và task-specific: multi-agent cải thiện accuracy vulnerability-detection, nhưng lightweight non-agentic và single-agent configurations vẫn dominanter Pareto front, chiếm 59/66 Pareto-optimal configurations.
- Model và prompt chọn là các chùm اليد (task-specific levers) có hướng hiệu quả thay đổi theo tác vụ (task-specific levers) thay vì là global defaults.

## Method (tóm tắt cốt lõi)
- Năm tác vụ phần mềm: code generation, technical debt identification, code vulnerability detection, log parsing, và log analysis.
- Bốn yếu tố chính: agent configuration, hardware platform, prompt strategy, và LLM model.
- Sáu open-weight LLMs, hai prompt strategies, ba hardware platforms.
- Đánh giá mỗi cấu hình theo accuracy, inference latency, và energy consumption.
- Multi-agent designs consume trung bình 6.36× năng lượng và chạy 6.07× thời gian so với non-agentic baseline, với worst-case slowdowns lên đến 160× cho từng task-hardware pair.
- Accuracy gains từ additional agents là limited và task-specific: multi-agent cải thiện average vulnerability-detection accuracy, nhưng lightweight non-agentic và single-agent configurations vẫn dominanter Pareto front, chiếm 59/66 Pareto-optimal configurations.

## Key Findings
- 8 tác giả từ SINTEF, Singapore Management University, Ozyegin University, category arXiv: cs.SE.
- Multi-agent designs consume trung bình 6.36× năng lượng và chạy 6.07× thời gian so với non-agentic baseline, với worst-case slowdowns lên đến 160×.
- Accuracy gains từ additional agents là limited và task-specific: multi-agent cải thiện average vulnerability-detection accuracy, nhưng lightweight non-agentic và single-agent configurations vẫn dominanter Pareto front, chiếm 59/66 Pareto-optimal configurations.
- Model và prompt chọn là các lever task-specific có hiệu quả thay đổi theo task thay vì là global defaults.

## Actionable Insights
1. Không mặc định multi-agent — MA tốn 6.36× năng lượng, 6.07× thời gian vs non-agentic, chỉ 1/66 cấu hình Pareto-optimal là MA; few-shot mạnh hơn việc thêm agent. Áp dụng: không mặc định multi-agent — cấu hình nhẹ thường Pareto-optimal hơn.
2. Model và prompt chọn là các lever task-specific thay vì global defaults. Áp dụng: chọn model và prompt phù hợp với từng tác vụ thay vì dùng một cấu hình cho tất cả các tác vụ.

## Assumptions & Limitations
- Đánh giá trên các benchmark code-repair từ các issue GitHub, kết quả có thể không chuyển tiếp sang các benchmark agent trong các miền khác.
- Đánh giá trên 4 backbone models.
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).

## Metadata
- Năm: 2026, tác giả: Merve Astekin, Yan Naing Tun, Arda Goknil, Erik Johannes Husom, Lwin Khin Shar, Hasan Sözer, Ratnadira Widyasari, Hui Song (SINTEF, Singapore Management University, Ozyegin University), category arXiv: cs.SE, link PDF: https://arxiv.org/pdf/2610.03010v1
