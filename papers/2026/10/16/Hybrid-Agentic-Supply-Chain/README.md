# [2609.13561v1] A Hybrid Agentic AI Framework for Intelligent Supply Chain Analytics

## Problem
Việc sử dụng hiệu quả supply chain analytics (phân tích chuỗi cung ứng) để đưa ra quyết định remains (còn là) một thách thức đáng kể cho các lập kế hoạch, vì các tác vụ quan trọng như database querying (truy vấn cơ sở dữ liệu), KPI analysis (phân tích chỉ số hiệu suất chính), demand forecasting (dự báo nhu cầu), và performance diagnosis (chẩn đoán hiệu suất) đòi hỏi heterogeneous expertise (chuyên môn đa dạng) trải dài qua data engineering (kỹ thuật dữ liệu), operations research (nghiên cứu vận hành), và domain knowledge (kiến thức chuyên ngành).

## Contribution
- Giới thiệu một agentic system (hệ thống đa đại lý) cho supply chain analytics.
- Multi-agent design đạt 90% accuracy (độ chính xác), cạnh tranh với single agent baseline.
- Reasoning models đạt điểm số trên 90%, non-reasoning models đạt khoảng 65%.

## Method (tóm cốt lõi)
Hệ thống agentic hybrid (kombinator) cho supply chain analytics bao gồm coordinator (điều phối viên) và specialist agents (đại lý chuyên gia). Mỗi specialist phụ trách một vùng chuyên môn (database querying, KPI analysis, demand forecasting, performance diagnosis). Coordinator phối hợp giữa các specialist để đưa ra quyết định cuối cùng.

## Key Findings
- Multi-agent design đạt 90% accuracy, cạnh tranh với single agent baseline.
- Reasoning models đạt điểm số trên 90%, non-reasoning models đạt khoảng 65%.
- Mean Score (điểm trung bình): 0.932 ± 0.012 (cao nhất), 0.904 ± 0.011, 0.655 ± 0.027, 0.661 ± 0.018.
- Relative Input Token Usage (sử dụng token nhập tương đối): 5.5×, 1.0×, 8.4×, 2.5× (thấp nhất = 1×).

## Actionable Insights
- Dùng reasoning models cho tác vụ supply chain phức tạp: đạt >90% accuracy so với ≈65% của non-reasoning. Áp dụng: solopreneur làm hệ thống phân tích chuỗi cung ứng nên dùng model có khả năng reasoning (suy luận) thay vì model đơn thuần.
- Kết hợp multi-agent (coordinator + specialists) để xử lý các tác vụ đòi hỏi chuyên môn đa dạng. Áp dụng: khi xây hệ thống analytics, hãy chia thành các specialist agent (mỗi specialist phụ trách một vùng: dự báo nhu cầu, phân tích KPI, v.v.) và một coordinator tổng hợp.

## Assumptions & Limitations
- Điều kiện: có dữ liệu chuỗi cung ứng và các tác vụ phân tích rõ ràng; không áp dụng nếu không có dữ liệu doanh nghiệp thực tế.
- Paper thừa nhận: architectural effects differ by model type (tác động kiến trúc khác nhau theo loại mô hình).
- Limitation paper không nói: chưa đánh giá trên nhiều lĩnh vực ngoài supply chain, chưa test chi phí triển khai thực tế.

## Metadata
- Năm: 2026
- Tác giả: Xian Yeow Lee, Teppei Inoue, Haiyan Wang, Chetan Gupta (Hitachi America, Industrial AI Lab)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2609.13561
