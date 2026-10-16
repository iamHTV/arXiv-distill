# [2610.19386v1] STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents

## Problem
Các đại lý ngôn ngữ (LLM agents) có thể tự phát triển (self-evolve) tại thời điểm kiểm tra (test time) bằng cách tích lũy kinh nghiệm: truy xuất các ký ức liên quan trước khi hành động và viết lại các bài học mới sau đó. Tuy nhiên, hầu hết là single-level (cấp đơn): các quỹ đạo (trajectories), các quy trình đã rút kinh nghiệm (distilled workflows) và các mục suy luận (reasoning items) đều nằm trong một bế không phân biệt được (undifferentiated pool) được lập chỉ mục bởi sự tương đồng nhúng (embedding similarity), không có hệ thống phân cấp trừu tượng (typed abstraction hierarchy). Chúng không bao giờ quên hoặc loại trừ (deduplicate), và dễ bị negative transfer (chuyển consumo tiêu cực), khi một kinh nghiệm bề mặt tương tự nhưng hướng đi ngược lại được triệu hồi và các bước cụ thể được sao chép nguyên văn, chủ động làm hại đến agent.

## Contribution
- Giới thiệu STRATA: một bộ nhớ có cấu trúc (structured), dựa trên kết quả (outcome-grounded), tự bảo trì (self-maintaining) tổ chức kinh nghiệm vào một hệ thống phân cấp ba cấp (three-level hierarchy).
- STRATA đạt điểm số trung bình tốt nhất ở độ trễ thấp nhất (lowest latency) và ít bước môi trường nhất (fewest environment steps) so với mọi bộ nhớ (memory baseline) trên bốn benchmark tương tác (interactive benchmarks), hai cốt lõi đóng băng (frozen backbones), bảy cơ sở (baselines), ba hạt (seeds).
- Deletion precision (độ chính xác xóa): 13.2% → 4.8% (cải thiện gần ba lần).
- Churn (tỷ lệ thay đổi): 28.6% → 3.1%.
- Meta's members drawn from a single task family (các thành viên meta từ một họ tác vụ duy nhất): 92.7%.
- Injection rate (tỷ lệ tiêm): 21.8% → 27.4%.
- 44% ít dòng bộ nhớ tiêm (injected memory) hơn bộ nhớ tiêu tốn nhiều ngữ cảnh nhất.

## Method (tóm cốt lõi)
STRATA tổ chức kinh nghiệm vào một hệ thống phân cấp ba cấp (three-level hierarchy): metas (các khái niệm cấp cao), episodes (các tập sự kiện), và traces (các vết dấu). STRATA có năm cơ chế bảo trì (maintenance mechanisms) mà tạo ra, tổng quát hóa (generalize), và quên (forget) kinh nghiệm, được trình bày chính xác và có thể tái tạo (reproducibly). Mỗi cơ chế xử lý một khía cạnh khác nhau của bảo trì bộ nhớ.

## Key Findings
- STRATA đạt điểm số trung bình tốt nhất ở độ trễ thấp nhất và ít bước môi trường nhất so với mọi memory baseline trên bốn benchmark tương tác.
- Deletion precision: 13.2% → 4.8% (cải thiện gần ba lần trong độ chính xác xóa).
- Churn: 28.6% → 3.1% (tỷ lệ thay đổi bộ nhớ giảm mạnh).
- Meta's members drawn from a single task family: 92.7% (các thành viên meta đều từ một họ tác vụ).
- Injection rate: 21.8% → 27.4% (ít nhưng các metas tốt hơn được truy xuất nhiều lần hơn).
- 44% ít dòng injected memory so với memory baseline tiêu tốn nhiều ngữ cảnh nhất.

## Actionable Insights
- Không nên để tất cả kinh nghiệm agent nằm trong một bế không phân biệt: hãy tổ chức kinh nghiệm thành hệ thống phân cấp (metas → episodes → traces) để agent có thể truy xuất chính xác và không bị nhiễm bởi kinh nghiệm không liên quan. Áp dụng: solopreneur xây agent tự phát triển nên thiết kế bộ nhớ có cấu trúc, không chỉ lưu trữ các quỹ đạo (trajectories) thô.
- Cần cơ chế quên và loại trừ (deduplicate) kinh nghiệm cũ hoặc không liên quan: không nên giữ mọi thứ trong bộ nhớ vĩnh viễn. Áp dụng: khi xây agent tự học, hãy xây cơ chế xóa các kinh nghiệm không hữu ích (churn thấp) để tránh negative transfer.

## Assumptions & Limitations
- Điều kiện: agent cần có khả năng tự phát triển tại test time (test-time self-evolution); không áp dụng nếu agent chỉ chạy một lần duy nhất.
- Paper thừa nhận: đánh giá trên bốn benchmark tương tác, hai cốt lõi đóng băng; có thể khác trên các tác vụ khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen ngoài các benchmark đã dùng, chưa test chi phí thực tế của việc duy trì hệ thống phân cấp.

## Metadata
- Năm: 2026
- Tác giả: Guanhua Zhu, Hanwen Li, Zhi Wei, Mengnan Du, Chenxi Yuan (NJIT, CUHK-Shenzhen)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.19386
