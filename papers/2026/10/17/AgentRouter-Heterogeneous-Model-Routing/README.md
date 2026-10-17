# [2609.22951v1] AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows

## Problem
- Hệ thống agent doanh nghiệp định tuyến mọi bước trong quỹ đạo (trajectory step) đến một mô hình ngôn ngữ đại diện (frontier model) tốn 60–80% chi phí suy luận (inference budget) cho các tác vụ phụ mà các mô hình nhỏ xử lý được tương đương. Các giải pháp định tuyến hiện có tối ưu hóa việc gán truy vấn đơn lẻ (single-turn query assignment) nhưng bỏ qua một thuộc tính đặc thù của quy trình agentic: độ phức tạp của từng bước (subtask complexity) thay đổi mạnh innerhalb một quỹ đạo (trajectory). Một bước lập kế hoạch (planning step) có thể cần mô hình hạng cao nhất (frontier-class reasoning) trong khi một bước định dạng (formatting step) tiếp theo chỉ cần một mô hình 7B.

## Contribtuion
- AgentRouter — một bộ phân loại nhẹ (lightweight classifier) 12M tham số, chi phí mở rộng (overhead) dưới 5ms trên mỗi bước trên A100 GPU, ánh xạ mỗi bước trong quỹ đạo (trajectory step) đến một trong bốn cấp độ model (model tier) bằng năm đặc trưng (five features) có thể trích xuất tại thời điểm định tuyến (routing time).
- Được huấn luyện trên 50.000 bước quỹ đạo agent được gán nhãn (annotated agent trajectory steps) phânurar qua lập kế hoạch (planning), viết mã (coding), nghiên cứu (research), và phân tích dữ liệu (data analysis).
- AgentRouter đạt giảm chi phí 72% so với cơ sở chỉ dùng mô hình đại diện (frontier-only baselines), giữ 97.3% chất lượng của mô hình đại diện duy nhất (frontier-only quality) (ít hơn 3% suy giảm độ hoàn thành tác vụ từ đầu đến cuối); độ chính xác định tuyến từng bước đạt 91% trên các bước ít phức tạp (minimal-complexity steps) và 85% trên các bước cấp độ hiệu quả (efficient-tier steps), với 76–82% trên các bước cấp độ trung bình và cao hơn (mid-range and frontier tiers).
- Trên cùng các benchmark, RouteLLM và FrugalGPT (áp dụng theo từng bước per-step) chỉ đạt giảm chi phí 31% và 44% tương phản, vì tín hiệu huấn luyện đơn luân phiên (single-turn training signal) của chúng bỏ qua sự phụ thuộc về chất lượng ở cấp độ quỹ đạo (trajectory-level quality dependencies).

## Method (tóm tắt cốt lõi)
- Định tuyến theo từng bước (step-level model routing) được định thức hóa như một bài toán gán tiếp nối (sequential assignment problem) trên các quỹ đạo agent (agent trajectories).
- Mỗi bước st trong quỹ đạo agent τ = (s1, s2, ..., sT) đại diện cho một lần gọi LLM duy nhất với nội dung đầu vào (input context), hướng dẫn (instruction), và đầu ra mong đợi (expected output).
- Mỗi bước được định tuyến đến một trong bốn cấp độ model (model tier) bằng một bộ phân loại feedforward classifier với hai lớp ẩn (256 và 128 đơn vị), kích hoạt ReLU, và đầu ra softmax 4 lớp tương ứng với bốn cấp độ model.
- Đặc trưng đầu vào được nhúng (embedded): các đặc trưng loại (categorical features) được nhúng...
- Các đặc trưng được trích xuất tại thời điểm định tuyến (routing time): bao gồm các đặc trưng về ngữ cảnh tích lũy (accumulated context size) và các đặc trưng khác có thể trích xuất tại thời điểm chạy.
- Định tuyến theo từng bước (step-level routing) thay vì định tuyến mỗi truy vấn độc lập, nhận ra rằng việc định tuyến ở bước t ảnh hưởng đến chất lượng ngữ cảnh tại bước t+1.

## Key Findings
- 2 tác giả từ Đại học Boston (Boston University) và Đại học Texas tại Austin (University of Texas at Austin), category arXiv: cs.AI/cs.LG.
- Trên bốn benchmark và hai backbone (backbone), AgentRouter giảm chi phí suy luận (inference cost) bởi 72% so với cơ sở chỉ dùng mô hình đại diện (frontier-only baselines), giữ 97.3% chất lượng của mô hình đại diện duy nhất (frontier-only quality).
- Độ chính xác định tuyến từng bước đạt 91% trên các bước ít phức tạp (minimal-complexity steps) và 85% trên các bước cấp độ hiệu quả (efficient-tier steps), với 76–82% trên các bước cấp độ trung bình và cao hơn (mid-range and frontier tiers).
- RouteLLM và FrugalGPT chỉ đạt giảm chi phí 31% và 44% tương phản, vì tín hiệu huấn luyện đơn luân phiên (single-turn training signal) của chúng bỏ qua sự phụ thuộc về chất lượng ở cấp độ quỹ đạo (trajectory-level quality dependencies).
- Định tuyến theo từng bước (step-level routing) thay vì dùng mô hình đại diện (frontier model) cho mọi bước: chỉ dùng frontier model cho bước cần reasoning sâu, dùng model nhỏ cho bước định dạng.

## Actionable Insights
1. Định tuyến từng bước (step-level model routing) thay vì dùng mô hình đại diện (frontier model) cho mọi bước: chỉ dùng frontier model cho bước cần reasoning sâu, dùng model nhỏ cho bước định dạng. Áp dụng: chỉ dùng frontier model cho bước cần reasoning sâu, dùng model nhỏ cho bước định dạng, giảm 72% chi phí inference, giữ 97.3% chất lượng.
2. Định tuyến dựa trên đặc trưng của từng bước (trajectory-aware features) thay vì mỗi bước độc lập. Áp dụng: định tuyến từng subtask đến model tier phù hợp (small/mid/frontier) thay vì frontier cho mọi bước.

## Assumptions & Limitations
- Sự dịch chuyển phân phối (distributional shift): AgentRouter được đào tạo trên các quỹ đạo từ LangGraph và CrewAI. Kiểm tra trên AutoGen (khung agent chưa thấy/unseen framework) cho thấy giảm 6–9% độ chính xác, nhưng giảm chi phí vẫn đạt 58%. Sự chuyển hóa chung chung qua các khung agent (cross-framework generalization) còn cần nghiên cứu thêm.
- Đánh giá trên các benchmark cụ thể với các mô hình cụ thể.

## Metadata
- Năm: 2026, tác giả: Rudrendu Kumar Paul, Sourav Nandy (Đại học Boston, Đại học Texas tại Austin), category arXiv: cs.AI/cs.LG, link PDF: https://arxiv.org/pdf/2609.22951v1
