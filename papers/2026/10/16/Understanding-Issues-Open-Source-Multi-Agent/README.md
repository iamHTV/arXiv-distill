# [2610.00905v1] Understanding Issues, Causes and Solutions in Open-Source LLM-based Multi-Agent Systems

## Problem
Với sự phát triển của hệ thống đa đại lý dựa trên LLM (LLM-based MAS), số lượng dự án mã nguồn mở tăng mạnh, nhưng chưa có nghiên cứu hệ thống về các vấn đề (issues), nguyên nhân (causes) và giải pháp (solutions) trong các dự án này.

## Contribution
- Phân tích 944 issues từ các dự án open-source MAS.
- Phân loại 17 loại vấn đề (issue categories), trong đó Orchestration & Execution Issue chiếm 22.0% (nhiều nhất).
- Xác định 540 nguyên nhân từ 57.2% của 944 issues, phân loại thành 14 loại nguyên nhân.
- Xác định 427 giải pháp, giải quyết 45.2% của 944 issues, phân loại thành 10 loại giải pháp.

## Method (tóm cốt lõi)
Thu thập 944 issues từ các dự án MAS mã nguồn mở (AutoGen, v.v.). Phân loại vấn đề theo 17 danh mục. Trích xuất nguyên nhân từ 57.2% issues, phân loại thành 14 loại nguyên nhân. Trích xuất 427 giải pháp từ 45.2% issues, phân loại thành 10 loại giải pháp.

## Key Findings
- Orchestration & Execution Issue: 22.0% (vấn đề phổ biến nhất).
- Memory & State Management Issue: 14.7%.
- Feature Request: 13.2%.
- Implementation Issue: 10.6%.
- Tool Issue: 9.2%.
- Integration Issue: 6.7%.
- Các vấn đề còn lại mỗi loại dưới 10%.
- Workflow Problem (WP): 29.4% (nguyên nhân phổ biến nhất).
- Tool Integration Problem (TIP): 11.7%.
- Memory Problem (MP): 11.1%.
- 427 giải pháp, giải quyết 45.2% của 944 issues.
- Optimize Workflow (OW): 26.0% (giải pháp phổ biến nhất).
- Adjust Configuration (AC): 15.0%.
- Optimize Tool Integration (OTI): 11.9%.
- Optimize Infrastructure (OI): 11.0%.
- Documentation Issue có resolution rate cao nhất (76.9%), Output Issue thấp nhất (24.1%).

## Actionable Insights
- Vấn đề lớn nhất trong MAS là orchestration & execution (điều phối và thực thi), chiếm 22.0%. Áp dụng: solopreneur xây MAS nên đầu tư vào thiết kế luồng thực thi và điều phối giữa các agent, không chỉ tập trung vào từng agent đơn lẻ.
- Nguyên nhân phổ biến nhất là Workflow Problem (29.4%). Áp dụng: khi gỡ lỗi MAS, hãy kiểm tra workflow trước, không phải trực tiếp vào code từng agent.
- Giải pháp phổ biến nhất là Optimize Workflow (26.0%). Áp dụng: tối ưu hóa workflow MAS sẽ giải quyết được phần lớn vấn đề, không cần thay đổi kiến trúc lớn.
- Documentation Issue có tỷ lệ giải quyết cao nhất (76.9%), Output Issue thấp nhất (24.1%). Áp dụng: đầu tư vào tài liệu tài liệu sẽ giúp giải quyết vấn đề nhanh hơn.

## Assumptions & Limitations
- Điều kiện: dựa trên 944 issues từ các dự án MAS mã nguồn mở cụ thể; có thể không đại diện cho tất cả các dự án.
- Paper thừa nhận: automated filtering approach đạt agreement rate 90.4%, còn 48 disagreements được xem xét lại.
- Limitation paper không nói: chưa đánh giá trên các dự án MAS proprietary (không mã nguồn mở), chưa test trên nhiều domen ngoài phần mềm kỹ thuật.

## Metadata
- Năm: 2026
- Tác giả: Asad Ur Rehman, Syed Mohammad Kashif, Ruiyin Li, Peng Liang, Zengyang Li, Arif Ali Khan (Wuhan University, Central China Normal University, University of Oulu)
- Category arXiv: cs.AI, cs.SE
- Link PDF: https://arxiv.org/pdf/2610.00905
