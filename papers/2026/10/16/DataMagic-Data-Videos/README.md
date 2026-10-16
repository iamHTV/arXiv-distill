# [2609.33403v1] DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration

## Problem
Data videos (video dữ liệu) truyền tải các insight dữ liệu thông qua các biểu đồ động (dynamic charts), giọng văn phân lai (voice narration), và hoạt ảnh đồng bộ (synchronized animations), đã trở thành một hình thức kể chuyện dữ liệu (data storytelling) được áp dụng rộng rãi. Tuy nhiên, sản xuất chúng đòi hỏi chuyên môn đa dạng (multidisciplinary expertise) spanning phân tích dữ liệu, thiết kế chính sách (narrative design), và chỉnh sửa video (video editing). Các công cụ trực quan tĩnh (static visualization tools) thiếu khả năng kể chuyện và hoạt ảnh; các công cụ viết tác (authoring tools) dựa trên các biểu đồ đã chuẩn bị sẵn thay vì dữ liệu thô (raw data); và các mô hình tạo ảnh cấp pixel (pixel-level generation models), trong khi có thể tổng hợp end-to-end, không thể đảm bảo...

## Contribution
- Giới thiệu DataMagic: một hệ thống đa đại lý (multi-agent) khai báo (declarative) để viết tác video dữ liệu (authoring data videos).
- DataMagic improves quality to 3.89 (+83%) with success rates above 95%, compared to direct generation methods that achieve only 2.13/5 with execution success rates between 48.62% and 86.24%.
- DataMagic significantly improves creation efficiency (79.7% reduction in task time) and reduces perceived cognitive load.
- Animation scores increase from 1.84 to 4.03 (+120%); Narrative scores improve from 2.00 to 3.43 (+72%); Intent and Aesthetic dimensions improve by more than 50%; Insight improves by 49.5%.
- DeepSeek-V3.2 improves its execution rate from 48.62% to 96.33%.

## Method (tóm cốt lõi)
DataMagic là một hệ thống đa đại lý khai báo (declarative multi-agent) để viết tác video dữ liệu. Các agent phụ trách các vai trò khác nhau (planner, coordinator, v.v.) và cùng phân phối (orchestrate) việc tạo video dữ liệu. Hệ thống sử dụng declarative specification (thông số khai báo) để định cấu trúc video dữ liệu.

## Key Findings
- Direct generation methods: 2.13/5 quality, execution success 48.62%–86.24%.
- DataMagic: 3.89/5 quality (+83%), execution success rates above 95%.
- Creation efficiency: 79.7% reduction in task time (39.2 → 8.0 minutes).
- Animation: 1.84 → 4.03 (+120%); Narrative: 2.00 → 3.43 (+72%); Intent and Aesthetic: >50%; Insight: +49.5%.
- DeepSeek-V3.2: execution rate 48.62% → 96.33%.

## Actionable Insights
- Dùng hệ thống đa đại lý khai báo (declarative multi-agent) để viết tác video dữ liệu thay vì dùng công cụ trực quan tĩnh hoặc công cụ viết tác dựa trên biểu đồ đã chuẩn bị sẵn. Áp dụng: solopreneur làm video dữ liệu nên dùng DataMagic để tự động hóa quy trình tạo video, giảm thời gian và chi phí.
- Tách biệt việc lập kế hoạch (planning) và thực thi (orchestration) để ổn định tỷ lệ thực thi (execution rate) trên 95%. Áp dụng: khi xây hệ thống tạo video bằng agent, hãy dùng agent lập kế hoạch và agent điều phối để đảm bảo tính ổn định.

## Assumptions & Limitations
- Điều kiện: có dữ liệu thô (raw data) và yêu cầu video dữ liệu; không áp dụng nếu không có dữ liệu.
- Paper thừa nhận: đánh giá trên user study với số lượng người dùng nhất định; có thể khác trên các tập dữ liệu khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen khác ngoài dữ liệu số, chưa test chi phí thực tế của hệ thống multi-agent.

## Metadata
- Năm: 2026
- Tác giả: Yupeng Xie, Zhenyang Wang, Liangwei Wang, Jiayi Zhu, Zhouan Shen, Yuyu Luo
- Category arXiv: cs.HC
- Link PDF: https://arxiv.org/pdf/2609.33403
