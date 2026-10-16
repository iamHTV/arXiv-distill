# [2609.32917v1] Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows

## Problem
Chạy LLM agents trong production tốn kém nhanh: frontier model (mô hình lớn nhất, mạnh nhất) chính xác nhưng có thể tốn 25 lần chi phí một model nhỏ trên mỗi token, và khoảng cách này trỗi lên cao khi một workflow chain (xâu chuỗi) nhiều lệnh gọi cùng nhau.

## Contribution
- Giới thiệu Planner-as-Router (PaR): định tuyến mô hình tại thời điểm lập kế hoạch (joint plan-time model routing) cho multi-agent workflows.
- PaR cắt chi phí 44% so với all-frontier routing (dùng mô hình lớn cho mọi bước) với giá chỉ giảm 2.9 điểm độ chính xác.
- PaR's measured plan mix: 45% small, 46% mid, 8% frontier, averaging 1.8 subtasks per plan.
- Complexity classifier labels 43% SIMPLE (một subtask small-tier duy nhất, không gọi planner đầy đủ) và 57% COMPLEX.

## Method (tóm cốt lõi)
PaR định tuyến mô hình tại thời điểm lập kế hoạch: planner quyết định từng subtask nên dùng model tier nào (small/mid/frontier) thay vì dùng frontier model cho mọi bước. Complexity classifier phân loại tác vụ thành SIMPLE (43%) và COMPLEX (57%). Mỗi plan trung bình có 1.8 subtasks.

## Key Findings
- PaR cắt chi phí 44% so với all-frontier routing, đánh đổi chỉ 2.9 điểm độ chính xác.
- Plan mix: 45% small, 46% mid, 8% frontier; 1.8 subtasks/trung bình mỗi plan.
- 43% task-runs là SIMPLE (chỉ small-tier), 57% là COMPLEX.
- PaR đạt độ chính xác tương đương SinkFrontier (26.1% vs 25.4%) với chi phí tương đương.
- Benchmark 1,157 evaluations trên SQL-Compose, Mongo-Gen, v.v.

## Actionable Insights
- Không dùng frontier model cho mọi bước: định tuyến từng subtask đến model tier phù hợp (small/mid/frontier) dựa trên độ phức tạp. Áp dụng: solopreneur chạy multi-agent workflow nên thêm lớp routing tại thời điểm lập kế hoạch, chỉ dùng model lớn cho subtask thực sự cần reasoning sâu.
- Dùng complexity classifier để phân loại tác vụ thành SIMPLE/COMPLEX trước khi deciding model tier. Áp dụng: trước khi gọi model lớn, hãy phân loại tác vụ đơn giản (dùng model nhỏ) và phức tạp (dùng model lớn) để tiết kiệm chi phí.

## Assumptions & Limitations
- Điều kiện: có thể phân loại độ phức tạp của tác vụ trước khi routing; không áp dụng nếu không thể ước lượng độ phức tạp.
- Paper thừa nhận: absolute accuracies thấp (22-29%), phản ánh độ khó của execution-based grading trên compositional tasks.
- Limitation paper không nói: chưa đánh giá trên nhiều loại tác vụ ngoài SQL/Mongo, chưa test chi phí triển khai thực tế.

## Metadata
- Năm: 2026
- Tác giả: Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick (Independent Researcher)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.32917
