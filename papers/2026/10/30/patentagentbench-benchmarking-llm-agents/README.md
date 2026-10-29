# [2610.35031] PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites

## Giá trị cốt lõi (1 câu)

Trước khi triển khai agent cho công việc bằng sáng chế (patent practice), nên đánh giá cặp model–agent harness trên PatentAgentBench (510 instance, 8 task suite) — cặp mạnh nhất (Claude Opus 5 + Hermes) chỉ đạt điểm trung bình 52.8/100, cho thấy hệ thống agent hiện tại vẫn còn thiếu xa trong việc truy xuất bằng chứng và tạo tài liệu bằng sáng chế chất lượng chuyên nghiệp.

## Problem

Công việc bằng sáng chế nằm ở giao-triệu giữa công nghệ, pháp luật và ngôn ngữ, làm cho nó thách thức nhưng quan trọng cho đổi mới công nghệ. Những tiến bộ gần đây của LLM và hệ thống agent đã chứng minh tiềm năng hoàn thành các quy trình công việc thực tế và thậm chí công việc bằng sáng chế. Điều này đặt ra câu hỏi: các hệ thống AI hiện tại có thể thực hiện công việc bằng sáng chế một cách đáng tin cậy không? Các benchmark hiện có bao phủ một phạm vi hạn chế các tác vụ bằng sáng chế và đơn giản hóa việc lấy bằng chứng bằng cách cung cấp tài liệu tham khảo hoặc tài liệu ứng viên. Do đó, chưa có cách đánh giá toàn diện xem agent AI có thể thực hiện công việc bằng sáng chế chuyên nghiệp một cách đáng tin cậy hay không.

## Contribution

1. Giới thiệu PatentAgentBench, một benchmark gồm 510 instance trên tám task suite: novelty search (tìm kiếm tính mới), freedom-to-operate (FTO) search (tìm kiếm tự do vận hành), design FTO (tìm kiếm tự do vận hành thiết kế), invalidity search (tìm kiếm vô hiệu hóa), claim charting (biểu diễn yêu cầu), patent drafting (soạn thảo bằng sáng chế), office-action response (phản hồi văn bản hành chính của cơ quan bằng sáng chế), và patent translation (dịch bằng sáng chế).
2. Bộ dữ liệu được sưu trữ từ các bản ghi bằng sáng chế thực tế và tài liệu chuyên nghiệp, kết hợp chỉ số tác vụ cụ thể với chú thích và thước đo được đánh giá bởi chuyên gia.
3. Các tác vụ lấy bằng chứng (novelty search, FTO, v.v.) yêu cầu agent tìm kiếm và so sánh các bộ sưu tập bằng sáng chế mà không có nhóm ứng viên được cung cấp. Các tác vụ soạn thảo và OAR đánh giá chất lượng công việc của agent cho bản mở giá thành kỹ thuật và thông báo văn bản hành chính của cơ quan bằng sáng chế.
4. Đánh giá bảy LLM trên bốn agent harness trên PatentAgentBench, tìm ra rằng các hệ thống hiện tại vẫn gặp khó khăn trong việc nhận diện tính mới, đánh giá rủi ro, và hiểu ý định của thực hành viên trong suốt quy trình bằng sáng chế. Cặp model–harness mạnh nhất đạt điểm trung bình 52.8, còn lại nhiều không gian để cải thiện trên các tác vụ bằng sáng chế chuyên nghiệp.

## Method

PatentAgentBench tuân theo một quy trình soạn thảo dữ liệu bốn giai đoạn kết hợp quá trình tự động hóa với đánh giá bởi chuyên gia. Đầu tiên, định nghĩa input, kết quả dự kiến, bằng chứng tác vụ, và tiêu chí đánh giá cho mỗi tác vụ dựa trên thực hành bằng sáng chế chuyên nghiệp. Thứ hai, các chuyên gia thiết lập tiêu chí bao gồm và loại trừ để hướng dẫn việc lọc dựa trên quy tắc và hỗ trợ LLM từ các bản ghi bằng sáng chế, bản trình thủ tục chính thức, và tài liệu công việc chuyên nghiệp. Đội ngũ chuyên gia gồm 31 người chuyên nghiệp: năm giám khảo bằng sáng chế cao cấp, mười lăm đại lý bằng sáng chế cao cấp, ba luật sư có thể thải hai nước, và tám chuyên gia sở hữu trí tuệ cao cấp. Các chuyên gia xem xét các trường hợp ứng viên về tính liên quan, sự hoàn chỉnh, và sự phù hợp. Ba, phân tích và chuẩn hóa các tài liệu đã chọn, tái cấu trúc input tác vụ, và suy ra bằng chứng tham khảo hoặc tiêu chí chấm điểm từ các bản ghi nguồn. Điều chỉnh trước tự động hỗ trợ quy trình này, trong khi các chuyên gia sửa nhãn và xem xét các thước đo đánh giá cho sự hỗ trợ bằng chứng và sự liên quan chuyên nghiệp. Mỗi instance được chú thích bởi một chuyên gia và được xem xét bởi chuyên gia thứ hai. Cuối cùng, mỗi trường hợp được đóng gói với input, điều kiện bằng chứng, yêu cầu đầu ra, và neo đánh giá. Trước khi xác thực cuối cùng, kiểm tra rằng bằng chứng tham khảo có thể truy xuất được đến nguồn của nó và rằng input tác vụ không phơi bày đáp án.

PatentAgentBench bao gồm tám task suite trải dài việc khám phá bằng chứng, so sánh cấp tính năng, và chuẩn bị tài liệu. Novelty search, patent FTO, design FTO, và invalidity search yêu cầu agent truy xuất bằng chứng liên quan. Claim charting yêu cầu chúng ánh xạ tính năng kỹ thuật đến bằng chứng được cung cấp. Patent drafting, office action response, và translation yêu cầu chúng tạo ra các tài liệu chuyên nghiệp. Mỗi task suite có chỉ số đánh giá cụ thể: novelty search dùng Hit@100 (tỷ lệ có ít nhất một bản ghi tham chiếu được chú thích trong top 100 kết quả), patent FTO/design FTO/invalidity search dùng recall (độ nhede bao phủ các bản ghi tham chiếu được chú thích), claim charting dùng F1 score, patent drafting và office-action response dùng điểm rubric có trọng số, patent translation dùng chỉ số theo loại.

## KNOWLEDGE — Số liệu & khái niệm

- PatentAgentBench: 510 instance, 8 task suites, 7 LLMs × 4 agent harnesses (Codex, Claude Code, OpenClaw, Hermes).
- Mô hình được đánh giá: GPT-5.6-Sol, Qwen3.8-Max, Kimi K3, DeepSeek-V4-Pro, MiniMax-M3, GLM-5.3, Claude Opus 5.
- Cặp model–harness mạnh nhất: Claude Opus 5 + Hermes, đạt điểm trung bình 52.8/100.
- Cùng model Claude Opus 5 với Claude Code đạt 50.3.
- Design FTO: recall dưới 4 trên mọi cấu hình đã đánh giá — khớ gap lớn nhất.
- Invalidity search: switching Opus từ Claude Code sang Hermes nâng recall từ 28.7% lên 55.0% (+26.3 điểm phần trăm).
- GPT-5.6-Sol với OpenClaw đạt 50.0, với Claude Code đạt 49.3.
- GLM-5.3 vượt GPT-5.6-Sol dưới Codex (48.1 vs 43.8), nhưng thứ tự đảo ngược dưới OpenClaw (GPT 50.0 vs GLM 29.5).
- 31 chuyên gia soạn thảo dữ liệu: 5 examiners, 15 patent agents, 3 luật sư dual-qualified, 8 IPR specialists.
- Task suites và chỉ số: Novelty Search (80 instance, Hit@100), Patent FTO (60, Recall), Design FTO (80, Recall), Invalidity Search (80, Recall), Claim Charting (40, F1), Patent Drafting (80, rubric), Office Action Response (60, 57 rubric criteria), Patent Translation (80, category-specific metrics).
- Tổng số instance: 510.

## INSIGHT — Cơ chế & tại sao

[Lợi thế của model và harness không chuyển đổi nhất quán qua các cấu hình và tác vụ] xảy ra VÌ [GLM-5.3 vượt GPT-5.6-Sol dưới Codex nhưng thứ tự đảo ngược dưới OpenClaw; lợi thế của harness cũng riêng biệt theo tác vụ]. Điều này nghĩa là [lựa chọn model và harness phải được xem xét cùng nhau, không riêng lẻ].

[Agent hiện tại khōng truy xuất được bằng chứng liên quan và tạo tài liệu bằng sáng chế chất lượng chuyên nghiệp] xảy ra VÌ [cặp mạnh nhất chỉ đạt 52.8/100, và Design FTO recall dưới 4 trên mọi cấu hình]. Điều này nghĩa là [khoảng cách giữa tạo tài liệu trông hợp lý và cung cấp công việc bằng sáng chế đáng tin cậy].

[Khai phá bằng chứng liên quan đến thiết kế (visual search) là gap tồn tại] xảy ra VÌ [độ nhede cao trên FTO văn bản không mở rộng sang cài đặt tìm kiếm thiết kế trực quan, khiến việc khám phá bằng chứng liên quan đến thiết kế vẫn là một khoảng trắng bền bỉ]. Điều này nghĩa là [các agent hiện tại chưa hỗ trợ tốt việc trích xuất đặc điểm hình ảnh và tìm kiếm thiết kế tương tự].

[Soạn thảo bằng sáng chế tuân thủ cấu trúc dự kiến nhưng có điểm yếu trong tổ chức yêu cầu, hiểu vụ án, và lập luận pháp lý] xảy ra VÌ [mặc dù bản thảo thường tuân theo cấu trúc mong đợi, điểm yếu vẫn tồn tại trong sự tổ chức của yêu cầu, sự hiểu về vụ án, và lập luận pháp lý]. Điều này nghĩa là [cần có sự kiểm soát tốt hơn trên nội dung thực thể, không chỉ định dạng].

## IDEA — Áp dụng được gì

1. Áp dụng PatentAgentBench làm tiêu chuẩn đánh giá agent trước khi triển khai trong công việc bằng sáng chế: đánh giá cặp model–harness làm một đơn vị, không riêng lẻ. Cho ai: doanh nghiệp pháp lý sở hữu trí tuệ muốn triển khai agent bằng sáng chế. Bước đầu: chạy benchmark trên 8 task suite với model và harness đã chọn, so sánh điểm trung bình.

2. Áp dụng đánh giá theo rubric chuyên gia (expert-reviewed rubrics) cho đầu ra của agent pháp lý/sở hữu trí tuệ: không chỉ chấm điểm tự động mà cần rubric chi tiết về hiểu vấn đề, chiến lược phản hồi, chất lượng sửa đổi. Cho ai: đội đánh giá đầu ra của agent trong lĩnh vực pháp lý. Bước đầu: xây dựng rubric đánh giá cho từng loại tài liệu pháp lý agent tạo ra (bản thảo, văn bản phản hồi, biểu diễn yêu cầu).

3. Áp dụng kiểm tra bằng chứng truy xuất trước khi chấp nhận đầu ra của agent: agent thường không truy xuất được bằng chứng liên quan, cần cross-check bằng chứng trích dẫn với nguồn gốc. Cho ai: hệ thống agent hỗ trợ quyết định pháp lý. Bước đầu: thêm bước xác minh nguồn tham khảo trong pipeline agent — yêu cầu agent trích dẫn nguồn và kiểm tra trích dẫn có đúng với tài liệu gốc hay không.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Lựa chọn model và agent harness phải được xem xét cùng nhau, vì lợi thế của chúng thay đổi theo nhiệm vụ — không có cặp model-harness duy nhất tối ưu cho tất cả tác vụ pháp lý. Áp dụng khi xây dựng hệ thống agent cho lĩnh vực chuyên môn cao (pháp lý, y tế, tài chính). Không áp dụng khi chỉ cần đánh giá mô hình đơn lẻ mà không quan tâm đến môi trường chạy.

## Assumptions & Limitations

- Điều kiện phải đúng: có sưu tập dữ liệu bằng sáng chế thực tế, có chuyên gia bằng sáng chế để đánh giá rubric, có môi trường agent harness để chạy đánh giá.
- Limitation paper thừa nhận: PatentAgentBench bao gồm 8 tác vụ bằng sáng chế chuyên nghiệp. Tuy nhiên, các tác vụ được đánh giá riêng biệt thay vì như một chu kỳ bằng sáng chế hoàn chỉnh. Quá trình đánh giá tập trung vào đầu ra cuối hoặc giao hàng của agent thay vì quy trình làm việc của agent. Trong tương lai, họ dự định mở rộng benchmark để bao gồm nhiều tác vụ hơn và đánh giá chu kỳ bằng sáng chế hoàn chỉnh.
- Limitation paper KHÔNG nói: hiệu quả trên các agent lớn hơn hoặc mô hình mới hơn sau ngày xuất bản, chi phí vận hành của benchmark trên quy mô lớn, và khả năng mở rộng sang các lĩnh vực pháp lý khác ngoài bằng sáng chế.

## Metadata

- Năm: 2026
- Tác giả: Yijie Hu, Wei Li, Junjie Zhou, Zhiqi Jiang, Yi Jin, Licong Xu, Xinkai Sun, Kai Duan, Lisha Zhang (PatSnap Ltd. Co.)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.35031v1
- Citation count: [không tìm được]