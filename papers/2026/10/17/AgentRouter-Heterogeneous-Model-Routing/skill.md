# Skill: agentrouter-step-level-model-routing
Source: 2609.22951v1
Type: framework

## Khi nào dùng skill này
- Xây dựng multi-agent system chạy trên quy trình nhiều bước (multi-step agentic workflows).
- Có các bước khác nhau về độ phức tạp: một số bước cần reasoning sâu (frontier model), một số bước chỉ cần định dạng (small model).
- Muốn giảm chi phí suy luận (inference cost) cho agent system chạy liên tục.

## Tình huống KHÔNG nên dùng
- Nhiệm vụ chỉ có một bước duy nhất (single-turn task).
- Không có mô hình nhỏ (small model) để định tuyến.
- Không cần giảm chi phí suy luận (chỉ quan tâm đến chất lượng tuyệt đối).

## Input cần có
- Danh sách các cấp độ model (model tiers) từ nhỏ đến lớn.
- Các đặc trưng của mỗi bước (step features) có thể trích xuất tại thời điểm định tuyến (routing time).
- Mô hình định tuyến nhẹ (lightweight classifier) như AgentRouter.
- Agent workflow với nhiều bước (multi-step agent workflow).

## Các bước thực hiện
1. Xác định các cấp độ model (model tiers) có sẵn (ví dụ: small, mid, frontier).
2. Trích xuất các đặc trưng (features) của mỗi bước tại thời điểm định tuyến (routing time), bao gồm ngữ cảnh tích lũy (accumulated context) và các đặc trưng khác.
3. Sử dụng bộ phân loại nhẹ (lightweight classifier) để ánh xạ mỗi bước đến một trong bốn cấp độ model.
4. Chỉ gọi mô hình đại diện (frontier model) cho bước cần reasoning sâu, dùng mô hình nhỏ cho bước định dạng.
5. Giám sát chi phí suy luận (inference cost) và độ chính xác (accuracy).

## Output mong đợi
- Giảm chi phí suy luận (inference cost) bởi 72% so với cơ sở chỉ dùng mô hình đại diện (frontier-only baselines).
- Giữ 97.3% chất lượng của mô hình đại diện duy nhất (frontier-only quality).
- Độ chính xác định tuyến từng bước: 91% trên các bước ít phức tạp, 85% trên các bước cấp độ hiệu quả, 76–82% trên các bước trung bình và cao hơn.

## Ví dụ áp dụng
- Xây dựng agent workflow để xử lý tài liệu: bước 1 phân tích truy vấn (cần LLM lớn), bước 2 truy xuất tài liệu (có thể dùng model nhỏ), bước 3 tổng hợp kết quả (cần LLM lớn), bước 4 trích xuất trường (có thể dùng model nhỏ), bước 5 tạo tóm tắt (có thể dùng model nhỏ), bước 6 xác thực định dạng (có thể dùng model nhỏ). Áp dụng AgentRouter để định tuyến từng bước đến model tier phù hợp.

## Gotchas
- Được đào tạo trên các quỹ đạo từ LangGraph và CrewAI. Kiểm tra trên AutoGen (khung agent chưa thấy) cho thấy giảm 6–9% độ chính xác, nhưng giảm chi phí vẫn đạt 58%.
- Sự chuyển hóa chung chung qua các khung agent (cross-framework generalization) còn cần nghiên cứu thêm.
