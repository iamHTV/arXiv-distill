# Skill: patentagentbench-evaluation (đánh giá agent bằng sáng chế bằng PatentAgentBench)

Source: 2610.35031v1
Type: evaluation-method / framework

## Khi nào dùng skill này

- Đang xây dựng agent cho công việc bằng sáng chế (tìm kiếm tính mới, FTO, soạn thảo bằng sáng chế, phản hồi văn bản hành chính, v.v.) và cần đánh giá trước khi triển khai.
- Muốn đánh giá cặp model–agent harness làm một đơn vị, không đánh giá model đơn lẻ.
- Cần rubric đánh giá chuyên gia cho đầu ra tài liệu pháp lý/sở hữu trí tuệ.

Tình huống KHÔNG nên dùng:
- Chỉ cần đánh giá mô hình LLM đơn lẻ mà không quan tâm đến môi trường chạy.
- Không có dữ liệu bằng sáng chế thực tế hoặc chuyên gia bằng sáng chế để đánh giá rubric.

## Input cần có

- PatentAgentBench dataset (510 instance, 8 task suites).
- Model LLM và agent harness (Codex, Claude Code, OpenClaw, Hermes, hoặc tương đương).
- Môi trường chạy agent với khả năng truy xuất cơ sở dữ liệu bằng sáng chế (ví dụ qua MCP service).
- Chuyên gia bằng sáng chế để đánh giá rubric (hoặc rubric đã được xác định sẵn).
- Chỉ số đánh giá: Hit@100 (novelty), Recall (FTO/design FTO/invalidity), F1 (claim charting), rubric-weighted scores (drafting/OAR), category-specific metrics (translation).

## Các bước thực hiện

1. Chọn model và agent harness để đánh giá.
2. Chạy PatentAgentBench trên 8 task suite: novelty search, patent FTO, design FTO, invalidity search, claim charting, patent drafting, office-action response, patent translation.
3. Điểm số mỗi task suite theo chỉ số tương ứng (Hit@100, Recall, F1, rubric, category metrics).
4. Tính điểm trung bình (AVG) trên 8 task suite.
5. So sánh cặp model–harness với các cặp khác (ví dụ Claude Opus 5 + Hermes đạt 52.8/100).
6. Xác định điểm yếu: Design FTO recall thấp, invalidity search, claim organization, legal argumentation.
7. Quyết định có nên triển khai hay cần cải thiện model/harness/prompt trước.

## Output mong đợi

- Điểm trung bình trên 8 task suite (thang 0–100).
- Điểm chi tiết từng task suite.
- Nhận diện điểm yếu của agent trong từng loại tác vụ bằng sáng chế.
- Quyết định triển khai hoặc cải thiện trước khi đưa vào sản xuất.

## Ví dụ áp dụng

Doanh nghiệp IP muốn xây dựng agent hỗ trợ soạn thảo bằng sáng chế và phản hồi văn bản hành chính. Áp dụng skill: chạy PatentAgentBench với model đã chọn và harness Claude Code. Kết quả: điểm trung bình 45/100, điểm thấp nhất ở Design FTO (recall < 4) và invalidity search. Quyết định: không triển khai ngay, cần cải thiện khả năng truy xuất bằng chứng và rubric đánh giá trước khi đưa vào sử dụng thực tế.

## Gotchas

- Lợi thế của model và harness không chuyển đổi nhất quán qua các task — phải đánh giá cặp model-harness cùng lúc.
- Các tác vụ được đánh giá riêng biệt, không như một chu kỳ bằng sáng chế hoàn chỉnh.
- Đánh giá tập trung vào đầu ra cuối thay vì quy trình làm việc của agent.
- Cần chuyên gia bằng sáng chế để đánh giá rubric, chi phí cao.
- Design FTO (tìm kiếm thiết kế trực quan) là gap lớn nhất, recall dưới 4 trên mọi cấu hình.
