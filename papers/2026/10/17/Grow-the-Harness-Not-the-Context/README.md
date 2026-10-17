# [2609.26760v2] Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents

## Problem
- Các agent LLM thường xử lý các tác vụ liên quan (streams of related tasks), nhưng standard harnesses lại yêu cầu agent tái thiết quyết định điều khiển (control decisions) bên trong mỗi tác vụ. Prior work chưa giải quyết được việc biến phản hồi (task feedback) thành code điều khiển tái sử dụng (reusable executable code), đồng thời giữ lại LLM calls cho tác vụ suy luận cụ thể (task-specific semantic reasoning).

## Contribtuion
- Grow the Harness — một phương pháp đào tạo được hướng dẫn bởi thất bại (failure-guided training paradigm) mà học tập agent harness (agent harness) từ một strategy-free scaffold mà expose các model và tool interfaces cố định nhưng không mã hóa bộ điều khiển giải quyết nhiệm vụ (task-solving controller).
- Function-level execution traces định địa phương (localize) mỗi thất bại đến một bề mặt mã nguồn (code surface) bị giới hạn, một optimizer sửa chữa (repair) một cửa sổ thất bại (window of failures) cùng nhau, và một success-first held-out gate lùi các chuỗi sửa chữa (repair sequences) làm tổn hại đến khả năng trước đó (prior capability).
- Các chỉnh sửa được chấp nhận (accepted edits) tích luỹ trong một harness chung (shared harness), cho phép cấu trúc điều khiển (control structure) phát sinh từ phản hồi tác vụ (task feedback).

## Method (tóm tắt cốt lõi)
- Strategy-free scaffold exposes các model và tool interfaces cố định nhưng không mã hóa bộ điều khiển giải quyết nhiệm vụ (task-solving controller).
- Function-level execution traces định địa phương mỗi thất bại đến một bề mặt mã nguồn (code surface) bị giới hạn.
- Optimizer sửa chữa (repair) một cửa sổ thất bại (window of failures) cùng nhau.
- Success-first held-out gate lùi các chuỗi sửa chữa (repair sequences) làm tổn hại đến khả năng trước đó (prior capability).
- Các chỉnh sửa được chấp nhận (accepted edits) tích luỹ trong một harness chung (shared harness), cho phép cấu trúc điều khiển (control structure) phát sinh từ phản hồi tác vụ (task feedback).
- Đánh giá trên BrowseComp-Plus và WebArena-Verified với ba deployment models từ 4B đến 120B parameters.
- Growing Harness đạt mean success cao nhất trong năm của sáu cấu hình benchmark-model và trails the best mean bởi 0.7 pp. trong thứ sáu.
- So với Tool-Calling agent, nó giảm LLM calls bởi 76.0–91.8% và deployed-agent inference cost bởi 74.4–98.6%.
- Trên WebArena-Verified, thành công của nó vẫn ở mức 44.7–45.3% trên các model scales, trong khi Tool-Calling rơi xuống 6.7% với model 4B.

## Key Findings
- 10 tác giả từ SII, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Shenzhen University of Advanced Technology, University of Macau, category arXiv: cs.AI.
- Growing Harness đạt mean success cao nhất trong năm của sáu cấu hình benchmark-model và trails best mean bởi 0.7 pp. trong thứ sáu.
- So với Tool-Calling agent, nó giảm LLM calls bởi 76.0–91.8% và deployed-agent inference cost bởi 74.4–98.6%.
- Trên WebArena-Verified, thành công của nó vẫn ở mức 44.7–45.3% trên các model scales, trong khi Tool-Calling rơi xuống 6.7% với model 4B.

## Actionable Insights
1. Thay vì để LLM tái thiết quyết định điều khiển mỗi tác vụ, hãy biến feedback thành code điều khiển tái sử dụng (reusable executable code). Áp dụng: biến feedback thành code điều khiển tái sử dụng, giảm 76.0–91.8% LLM calls và 74.4–98.6% inference cost.
2. Thay vì để LLM tái thiết quyết định điều khiển mỗi tác vụ, hãy biến feedback thành code điều khiển tái sử dụng, giảm 76.0–91.8% LLM calls và 74.4–98.6% inference cost. Áp dụng: biến feedback thành code điều khiển tái sử dụng, giảm 76.0–91.8% LLM calls và 74.4–98.6% inference cost.

## Assumptions & Limitations
- Đánh giá trên BrowseComp-Plus và WebArena-Verified với ba deployment models từ 4B đến 120B parameters.
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).

## Metadata
- Năm: 2026, tác giả: Laizhen Li, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, Peng Wang, Quanming Yao, Wenjin Wu, Peng Jiang (SII, Chinese Academy of Sciences), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.26760v2
