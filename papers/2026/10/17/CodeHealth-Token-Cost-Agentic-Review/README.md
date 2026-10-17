# [2610.21914v1] CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests

## Problem
- Các tổ chức ngày càng ủy quyền việc xem xét mã nguồn (code review) cho các ống dẫn đa agente (multi-agent LLM pipelines) được tính phí theo token. Chất lượng mã nguồn thấp tăng công việc bảo trì của con người, nhưng tác động của nó đến chi phí xem xét của agent chưa được đo lường. Prior work chưa giải quyết được việc liệu một chỉ số chất lượng mã nguồn (code quality metric) có dự đoán chi phí token của agent review và fix hay không.

## Contribution
- Nghiên cứu quan sát tiên nghiệm (pre-registered observational study) trên 465 PR do agent viết từ 246 kho lưu trữ (repositories) trong AIDev, phân tầng chung (jointly stratified) theo CodeHealth và diện tích PR (footprint) dưới giới hạn kho lưu trữ (repository caps).
- ống dẫn xem xét và sửa lỗi đa agente (five-agent review-and-fix pipeline) đóng băng (frozen) xử lý mọi PR với ba LLM khác nhau. Mỗi LLM, chúng tôi lắp một mô hình hỗn hợp (mixed model) của log tokens trên CodeHealth và log diện tích PR, với một ngẫu nhiên kho lưu trữ (repository random intercept).
- Cho tất cả ba LLM, hệ số CodeHealth là âm, với khoảng tin cậy 95% không bao gồm không; mỗi điểm CodeHealth được liên kết với 3.5% đến 6.1% chi phí token thấp hơn. CodeHealth không liên quan đến diện tích PR, nên kích thước PR không giải thích liên kết này. Hai trong ba mùi code (code smells) đã đăng ký dự đoán chi phí của giai đoạn sửa lỗi (fix stage); việc sửa lỗi theo lô (batch fixing) để lại trung vị CodeHealth không đổi. Các phân tích khám phá (exploratory analyses) định vị liên kết trong giai đoạn xem xét (review stage), nơi các agent lặp lại nhiều hơn trên mã nguồn không khỏe (unhealthy code) mà không viết thêm bình luận (comments). Điều chỉnh cho kích thước các tệp đã chấm điểm (size of scored files) hấp thụ liên kết (absorbed the association), chúng tôi diễn giải là sự trung gian bởi kích thước tệp (mediation by file size).

## Method (tóm tắt cốt lõi)
- Nghiên cứu quan sát tiên nghiệm (pre-registered observational study) lấy mẫu 465 PR do agent viết từ 246 kho lưu trữ trong AIDev, phân tầng chung theo CodeHealth và diện tích PR dưới giới hạn kho lưu trữ.
- Ống dẫn xem xét và sửa lỗi đa agente (five-agent review-and-fix pipeline) đóng băng xử lý mọi PR với ba LLM khác nhau.
- Mỗi LLM, lắp mô hình hỗn hợp (mixed model) của log tokens trên CodeHealth và log diện tích PR, với một ngẫu nhiên kho lưu trữ.
- CodeHealth™ (CH) là một điểm composite, deterministik giữa 1 và 10 tổng hợp nhiều tín hiệu chất lượng cấp nguồn (source-level quality signals) thành một điểm đo tệp (file-level measure) duy nhất.

## Key Findings
- 4 tác giả từ Đại học Lund (Lund University) và CodeScene AB, category arXiv: cs.SE.
- 465 PR, 246 kho lưu trữ, 3 LLM.
- Cho tất cả ba LLM, hệ số CodeHealth là âm, với khoảng tin cậy 95% không bao gồm không.
- Mỗi điểm CodeHealth được liên kết với 3.5% đến 6.1% chi phí token thấp hơn, giữ nguyên diện tích PR, ngôn ngữ và kho lưu trữ.
- Diện tích PR (footprint) vốn không liên quan đến CodeHealth cơ bản trong mẫu này (tối đa +0.014 trong log diện tích PR mỗi điểm CodeHealth, với mọi khoảng tin cậy bao gồm không).
- Hai trong ba mùi code đã đăng ký dự đoán chi phí sửa lỗi (fix cost); sửa lỗi theo lô (batch fixing) để lại trung vị CodeHealth không đổi.
- Liên kết được định vị trong giai đoạn xem xét (review stage), nơi các agent lặp lại nhiều hơn trên mã nguồn không khỏe mà không viết thêm bình luận.
- Điều chỉnh cho kích thước các tệp đã chấm điểm hấp thụ liên kết, diễn giải là sự trung gian bởi kích thước tệp (mediation by file size).

## Actionable Insights
1. Chất lượng mã nguồn (code quality) dự đoán chi phí token của agent review và fix. Áp dụng: theo dõi CodeHealth (hoặc chỉ số chất lượng tương tự) để dự đoán chi phí suy luận của agent review và fix.
2. Tác động nhỏ mỗi điểm (3.5% đến 6.1% giảm chi phí token mỗi điểm CodeHealth) và không do kích thước PR. Áp dụng: refactoring để cải thiện chất lượng code có thể giảm chi phí agent review, không chỉ vì PR nhỏ hơn.

## Assumptions & Limitations
- Nghiên cứu quan sát tiên nghiệm (pre-registered observational study) — không thể kết luận nhân quả (causal).
- Mỗi PR chỉ chạy một lần.
- Tập trung trên 3 LLM cụ thể.
- Điều chỉnh cho kích thước các tệp đã chấm điểm hấp thụ liên kết (mediation by file size).

## Metadata
- Năm: 2026, tác giả: Lo Gullstrand Heander, Markus Borg, Emma Söderberg, Christofer Rydenfält (Đại học Lund, CodeScene AB), category arXiv: cs.SE, link PDF: https://arxiv.org/pdf/2610.21914v1
