# [2610.03010v1] Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows

## Problem
Hệ thống agentic LLM (LLM đa đại lý) đang được dùng trong phần mềm kỹ thuật (software engineering) nhưng tốn chi phí tính toán và môi trường cao hơn hẳn so với single-agent. Việc dùng multi-agent không phải lúc nào cũng mang lại lợi ích đáng một khi so với chi phí tăng thêm.

## Contribution
- Nghiên cứu thực nghiệm tổng hợp (comprehensive empirical study) so sánh các cấu hình agentic LLM trên 5 tác vụ dev, 6 model, 2 chiến lược prompt, 3 nền tảng phần cứng.
- Xác định các cấu hình tối ưu trên efficiency frontier (ranh giới hiệu quả) giữa độ chính xác, năng lượng và latency (thời gian chậm trễ).
- Khảo sát ảnh hưởng của agentic complexity (độ phức tạp đa đại lý) đến năng lượng và latency.

## Method (tóm cốt lõi)
Thử nghiệm 5 tác vụ phát triển phần mềm (code generation, technical debt detection, vulnerability detection, log parsing, log analysis), 6 mô hình LLM, 2 chiến lược prompt (zero-shot, few-shot), 3 nền tảng phần cứng. So sánh 4 cấu hình agentic: NA (No Agent - không agent), SA (Single Agent), DA (Delegation Agent), MA (Multi Agent). Đánh giá theo accuracy, năng lượng (kWh), latency (giây). Xây dựng Pareto front (ranh giới tối ưu đa tiêu chí).

## Key Findings
- Multi-agent designs (thiết kế đa đại lý) tốn trung bình 6.36× năng lượng và chạy 6.07× thời gian so với non-agentic baseline, worst-case slowdown (chậm trễ tối đa) lên đến 160×.
- Trong 66 cấu hình Pareto-optimal (tối ưu Pareto): 36 (55%) dùng NA, 23 (35%) dùng SA, 6 (9%) dùng DA, chỉ 1 (2%) dùng MA.
- Few-shot prompting tăng độ chính xác log parsing từ 3.4% lên 54.3%, giảm năng lượng 24–41%.
- G3-4B đạt Pass@1 cao nhất cho code generation (99.8%); GPT-OSS đạt Macro F1 cao nhất cho technical debt detection (58.6%); Q3-4B tốt nhất vulnerability detection (57.8%); Q2.5C-7B tốt nhất log parsing (42.2%) và log analysis (8.5%).
- MA đạt F1-score cao nhất (55.4%) cho technical debt detection nhưng NA có năng lượng và latency thấp nhất.

## Actionable Insights
- Không mặc định dùng multi-agent: cấu hình nhẹ (single agent hoặc no-agent) thường dominates Pareto front (ph-arرة ranh giới tối ưu), trực tiếp tiết kiệm tiền và thời gian. Áp dụng: solopreneur xây pipeline AI nên bắt đầu từ single agent, chỉ thêm multi-agent khi có bằng chứng rõ ràng về lợi ích.
- Few-shot prompting là lever (cònzeugung) mạnh mẽ hơn agentic configuration cho nhiều tác vụ: tăng log parsing từ 3.4% lên 54.3% và giảm năng lượng 24–41%. Áp dụng: trước khi thêm agent phức tạp, hãy thử few-shot prompt với ví dụ cụ thể.

## Assumptions & Limitations
- Điều kiện: cần có 5 tác vụ dev cụ thể và 6 mô hình LLM đã chọn; kết quả có thể khác trên các tác vụ/mô hình khác.
- Paper thừa nhận: hardware effects (tác động phần cứng) nhỏ đối với workload nhẹ nhưng lớn hơn đối với workload nặng; lowest-energy model thay đổi tùy theo tác vụ.
- Limitation paper không nói: chưa đánh giá trên mô hình lớn hơn 70B, chưa test workflow länger (dài hơn) nhiều bước.

## Metadata
- Năm: 2026
- Tác giả: Merve Astekin, Yan Naing Tun, Arda Goknil, Erik Johannes Husom, Lwin Khin Shar, Hasan Sozer, Hasan Sözer, Ratnadira Widyastari, Hui Song
- Category arXiv: cs.AI, cs.SE
- Link PDF: https://arxiv.org/pdf/2610.03010
