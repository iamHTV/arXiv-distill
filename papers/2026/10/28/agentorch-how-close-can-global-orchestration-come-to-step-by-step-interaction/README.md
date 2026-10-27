# 2610.33375v1 AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction?

## Giá trị cốt lõi (1 câu)
Global orchestration sinh workflow hoàn chỉnh trước khi thực thi (không cần LLM calls trong quá trình chạy) và đã coết khoảng cách chính xác so với Step-by-Step xuống còn ~8.5 pp với mô hình mới nhất, đồng thời giảm 23.2 lần số lượng LLM calls và 3.64 lần token hoàn thành — các kỹ thuật như xây dựng workflow tăng dần, sửa workflow bằng phản hồi thực thi, và đào tạo mục tiêu giúp thu hẹp thêm khoảng cách này.

## Problem
Enterprise workflow agents thường dựa vào tương tác bước進 bộ (Step-by-Step): agent thực hiện một hành động, quan sát kết quả, rồi gọi LLM lại để quyết định bước tiếp theo. Global orchestration (Global) thay vào đó sinh một workflow thực thi hoàn chỉnh trước và thực thi nó mà không cần thêm LLM calls, giảm đáng kể chi phí suy luận, nhưng vẫn kém chính xác hơn Step-by-Step. Chưa rõ Global có thể gần Step-by-Step đến mức nào và những gì hẹp khoảng cách còn lại. Các nghiên cứu trước thường sinh workflow hoặc kế hoạch thực thi trước nhưng đánh giá chúng riêng lẻ thay vì so sánh trực tiếp với tương tác bước進 bộ trên cùng các workflow, công cụ, môi trường thực thi, và tiêu chí đánh giá.

## Contribution
1. Giới thiệu AgentOrch, một tiêu chí đánh giá so sánh trực tiếp global orchestration với tương tác bước進 bộ trên 650 enterprise SOPs (standard operating procedures — thủ tục vận hành doanh nghiệp) và 3,220 runtime variants (biến thể thời gian chạy) dưới cùng các công cụ, môi trường, và tiêu chí đánh giá.
2. Đánh giá việc xây dựng workflow tăng dần (incremental workflow construction) và sửa workflow bằng phản hồi thực thi (execution-feedback revision) như hai con đường làm mạnh Global orchestration. Xây dựng cải thiện một số models mà không cần phản hồi thực thi runtime; sửa cải thiện tất cả tám models được đánh giá, kể cả trên các biến thể chưa từng dùng cho phản hồi.
3. Đào tạo mô hình trên 3,000 công thức nguồn (source recipes) riêng biệt để sinh workflow hoàn chỉnh. Lấy cái tốt hơn của SFT và RL cho mỗi base model, Orchestration Accuracy cải thiện trung bình 12.18 pp trên tất cả năm models được đào tạo.
4. Khoảng cách giữa Global và Step-by-Step đã coết khoảng 79% từ các mô hình sơ khai (40.67 pp cho GPT-3.5 Turbo) đến mô hình mạnh nhất gần đây (8.53 pp cho Claude Opus 5 Thinking).
5. Global sử dụng trung bình 23.2 lần ít LLM calls và 3.64 lần ít completion tokens so với Step-by-Step.

## Method
Pipeline (dòng xử lý) của AgentOrch có các bước chính:
1. Xây dựng tiêu chí đánh giá từ các thực thể doanh nghiệp có thể thực thi (executable enterprise workflows). Mỗi SOP có một reference workflow (workflow tham chiếu) và nhiều runtime variants.
2. Task specification (thông số tác vụ): mỗi SOP có thông số tác vụ cố định chứa mô tả tác vụ, schemas đầu vào/đầu ra công khai, bối cảnh thực thi, tài nguyên không gian làm việc, mẫu giao tiếp khi cần, và 64 tool interfaces (giao diện công cụ). Yêu cầu được trình bày theo thứ tự không nhân quả (non-causal order), đòi hỏi model suy luận tool calls, dependencies, control flow, và argument bindings.
3. Môi trường thực thi và runtime variants: các thao tác recipe được映射 thành danh mục cố định 64 tool interfaces covers các dịch vụ như Slack, Jira, Salesforce, Google Sheets, Google Drive, Snowflake, và Workato. Các backend thực tế và mô phỏng (simulated) được triển khai sau cùng các giao diện.
4. Hai giao thức orchestration chính:
   - Global: model sinh một workflow hoàn chỉnh trước khi thực thi và trước khi quan sát đầu vào runtime cụ thể. Workflow sau đó được cố định và tái sử dụng trên tất cả các biến thể của SOP mà không cần thêm LLM interaction.
   - Step-by-Step: vòng lặp hành động–quan sát liên quan đến ReAct. Mỗi variant là một tập sự (episode) độc lập. Model nhận thông số tác vụ và đầu vào runtime cụ thể, sinh một tool call, quan sát kết quả, và chọn hành động tiếp theo cho khi chấm dứt hoặc đạt giới hạn thực thi.
   - Local: nhận cùng thông số tác vụ như Global và không quan sát đầu vào runtime cụ thể hay kết quả thực thi, nhưng xây dựng workflow tăng dần qua một trình chỉnh sửa chỉ thêm (append-only editor). Sau mỗi bản chỉnh sửa đề xuất, một validator hoặc chấp nhận nút và trả về bản nháp workflow đã cập nhật, hoặc từ chối với thông báo lỗi.
   - Replan: bắt đầu từ workflow Global, thực thi nó trên các runtime variants và cung cấp model với workflow và phản hồi thực thi, bao gồm tool calls, arguments, kết quả hoặc lỗi, kết quả luồng điều khiển, và kết quả cuối. Model sau đó sinh một workflow hoàn chỉnh đã sửa đổi.
5. Các chỉ số đánh giá:
   - Orchestration Accuracy: trung bình của Execution Trace Accuracy và Side-Effect Accuracy cho mỗi runtime variant.
   - Execution Trace Accuracy: đo sự đồng nhất với execution trace tham chiếu và trung bình năm thành phần nhị phân: tool selection, tool order, tool execution, required arguments, control path.
   - Side-Effect Accuracy: đo liệu việc thực thi có tạo ra các thay đổi trạng thái bắt buộc mà không thiếu, trùng lặp, hoặc không mong muốn.
   - Final Accuracy: đo xem cả các side effects bắt buộc và đầu ra terminal có đúng không. Được đếm là đúng chỉ khi cả Side-Effect Accuracy và Terminal Output Accuracy đều đúng.
   - Error Rate: đo tỷ lệ các runtime variants không tạo ra một điểm có thể đánh giá (scoreable execution) do lỗi lập kế hoạch, model, cơ sở hạ tầng, hoặc đánh giá.

## KNOWLEDGE — Số liệu & khái niệm
- Global orchestration (orchestration toàn cầu): LLM构建 một workflow thực thi hoàn chỉnh trước khi quan sát đầu vào runtime cụ thể, sau đó workflow thực thi mà không cần thêm LLM calls.
- Step-by-Step interaction (tương tác bước tiến bộ): model chọn một hành động, quan sát kết quả thực thi, và sau đó quyết định hành động tiếp theo.
- Runtime variant (biến thể thời gian chạy): instantiates đầu vào cụ thể và điều kiện thực thi, tập hợp các đường đi điều khiển khác nhau, độ dài vòng lặp, và điều kiện lỗi trong khi giữ mô tả tác vụ và reference workflow không đổi.
- Orchestration Accuracy (độ chính xác orchestration): trung bình của Execution Trace Accuracy và Side-Effect Accuracy.
- Execution Trace Accuracy (độ chính xác vết 따른 thực thi): đo sự đồng nhất với vết 따르면 tham chiếu, trung bình 5 thành phần nhị phân: tool selection, tool order, tool execution, required arguments, control path.
- Side-Effect Accuracy (độ chính xác tác dụng phụ): đo liệu việc thực thi có tạo ra các thay đổi trạng thái bắt buộc hay không.
- Local (cục bộ): xây dựng workflow tăng dần với phản hồi validator, không cần đầu vào runtime hay kết quả thực thi.
- Replan (lập kế hoạch lại): sửa workflow hoàn chỉnh bằng phản hồi thực thi, thực thi mà không cần thêm LLM calls tại thời điểm thực thi.
- 650 enterprise SOPs, 3,220 runtime variants, 64 tool interfaces.
- 3,000 training source recipes, disjoint từ AgentOrch benchmark.
- 1,033 tool operations spanning 305 namespaces trong tập huấn luyện.
- Khoảng cách Global–Step-by-Step coết 79% từ 40.67 pp (GPT-3.5 Turbo) xuống 8.53 pp (Claude Opus 5 Thinking).
- Incremental construction (Local): cải thiện Orchestration Accuracy trung bình 9.98 pp mà không cần phản hồi thực thi runtime.
- Execution-feedback revision (Replan): cải thiện tất cả 8 models được đánh giá trung bình 6.18 pp, và 6.13 pp trên các biến thể runtime chưa từng dùng (held-out).
- Targeted training (đào tạo mục tiêu): cải thiện Orchestration Accuracy trung bình 12.18 pp (6.84–19.88 pp) trên 5 models được đào tạo.
- Error Rate giảm 13.02–40.99 pp sau khi đào tạo.
- 92.6% tổng thể Replan gain đến từ việc sửa các workflow ban đầu không hợp lệ (invalid workflows).

## INSIGHT — Cơ chế & tại sao
- [Model quy mô lớn không nhất quán hẹp khoảng cách] xảy ra VÌ Global Orchestration Accuracy và khoảng cách không thay đổi đơn điệu theo quy mô model. VD: Qwen2.5, Global Orchestration Accuracy giảm từ 16.18% tại 32B xuống 9.91% tại 72B. Nghĩa là chỉ đơn thuần dùng model lớn hơn không đủ — cần thay đổi cách xây dựng workflow.
- [Thêm đầu vào runtime một mình không giải thích khoảng cách] xảy ra VÌ Input-Conditioned Global nhận đầu vào runtime nhưng sinh workflow hoàn chỉnh trước khi thực thi, không có kết quả thực thi trung gian. Khoảng cách trung bình thay đổi từ 30.92 pp lên 31.09 pp (không đổi đáng kể). Nghĩa là kết quả thực thi trung gian (intermediate execution results) là yếu tố then chốt, không chỉ đầu vào runtime.
- [Hầu hết Replan gain đến từ sửa workflow không hợp lệ] xảy ra VÌ 92.6% tổng thể Replan gain đến từ việc chuyển các workflow ban đầu không hợp lệ thành hợp lệ. Global phải quy định arguments và references trước khi thực thi, trong khi Step-by-Step có thể sử dụng kết quả đã quan sát để xây dựng các lệnh gọi tiếp theo. Nghĩa là việc chỉ định đúng cách mỗi tool được gọi và dữ liệu luồng giữa các calls trước khi thực thi là chướng ngại vật lớn của global orchestration.

## IDEA — Áp dụng được gì
1. Áp dụng Local (xây dựng workflow tăng dần) vào hệ thống workflow doanh nghiệp: thay vì sinh toàn bộ workflow một lần, hãy xây dựng nó tăng dần qua trình chỉnh sửa chỉ thêm, sau mỗi chỉnh sửa một validator kiểm tra và chấp nhận hoặc từ chối. Bước đầu: triển khai một trình chỉnh sửa workflow có validator kiểm tra schema, type, và reference checks cho tool arguments trước khi thực thi.
2. Áp dụng Replan (sửa workflow bằng phản hồi thực thi): thực thi workflow Global trên một vài runtime variants, thu thập phản hồi thực thi (tool calls, arguments, kết quả, lỗi), và yêu cầu model sửa đổi workflow hoàn chỉnh. Bước đầu: chọn 2 variants đại diện cho mỗi SOP, thực thi workflow Global, cung cấp phản hồi cho model, và sinh workflow đã sửa.
3. Áp dụng đào tạo mục tiêu (targeted training): đào tạo model trên 3,000 source recipes, mỗi mẫu kết hợp thông số tác vụ với workflow tham chiếu hoàn chỉnh. Lấy cái tốt hơn của SFT và RL cho mỗi base model. Bước đầu: thu thập 3,000 công thức nguồn từ các workflow doanh nghiệp đã thực thi thành công, tạo cặp huấn luyện (thông số tác vụ → workflow tham chiếu).

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: Global orchestration không chỉ cần chọn công cụ đúng, mà cần chỉ định trước khi thực thi mỗi công cụ được gọi như thế nào và dữ liệu luồng giữa các calls như thế nào — việc chỉ định đúng là THEN THEN (thì thì) then chốt (key lever) cho công việc orchestrator doanh nghiệp.
- Khi nào dùng: Khi triển khai agent workflow doanh nghiệp muốn giảm chi phí LLM calls nhưng vẫn duy trì độ chính xác cao.
- Khi nào KHÔNG dùng: Khi workflow có quá nhiều nhánh điều khiển phụ thuộc vào kết quả runtime không thể dự đoán trước (như các tác vụ cần quyết định động dựa trên phản hồi bên ngoài không xác định).

## Assumptions & Limitations
- Điều kiện phải đúng: Cần có reference workflow cho mỗi SOP và môi trường thực thi có thể mô phỏng (simulated backend) để đánh giá tái tạo được.
- Limitation paper thừa nhận: Khoảng cách vẫn chưa đóng hoàn toàn — Step-by-Step vẫn giữ lợi thế chính xác trên tất cả các model được đánh giá. Mô hình quy mô lớn không nhất quán hẹp khoảng cách. Reasoning không cung cấp lợi ích nhất quán tuyệt đối cho Global cũng không nhất quán hẹp khoảng cách.
- Limitation paper KHÔNG nói: Không đánh giá chi phí đào tạo (training cost) so với chi phí eingespar (tiết kiệm) từ việc giảm LLM calls trong thực thi.

## Metadata
- Năm: 2026
- Tác giả: Zijie Liu, Yueh Che Lee, Qi Yang Huang, Zayne Turner, Adam Seligman, Tianlong Chen, Zhaozhuo Xu, Jinhao Duan, Thomas A. Joseph
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.33375v1
- Classification: [applied]