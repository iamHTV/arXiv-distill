# Skill: agentrouter-step-level-model-routing
Source: 2609.22951v1
Type: framework

## Khi nào dùng skill này
- Agentic workflow có nhiều bước, mỗi bước khác nhau độ phức tạp (planning cần model lớn, định dạng cần model nhỏ).
- Muốn cắt chi phí inference vì hiện nay route mọi bước đến frontier model.
- Có dữ liệu quỹ đạo agent đã gán nhãn để train classifier nhẹ.

## Tình huống KHÔNG nên dùng
- Workflow chỉ 1 bước, không cần routing nhiều tier model.
- Không có dữ liệu quỹ đạo đã gán nhãn để train classifier.

## Input cần có
- Danh sách các model tiers có sẵn (từ frontier đến minimal, ví dụ GPT-5, 70B, 7B, 3B).
- Dữ liệu 5 features có thể trích xuất tại thời điểm routing cho mỗi bước (được nêu trong paper).
- Mô hình classifier nhẹ (có thể train từ 50.000 bước đã gán nhãn).

## Các bước thực hiện
1. Phân đoạn agentic workflow thành các bước (trajectory steps), mỗi bước có task type (planning/coding/research/data analysis).
2. Trích xuất 5 features routing-time cho mỗi bước.
3. Dùng classifier nhẹ (12M tham số) để map mỗi bước đến model tier phù hợp (tier 1 frontal đến tier 4 minimal).
4. Chỉ gọi frontier model cho bước được phân loại là cần reasoning sâu; bước còn lại dùng model nhỏ hơn.
5. Bật fallback nếu bước được đánh giá thấp chất lượng, gọi lại model cao hơn (kích hoạt dưới 4% quỹ đạo).

## Output mong đợi
- Giảm 72% chi phí inference so với dùng frontier model cho mọi bước, giữ 97.3% chất lượng (<3% suy giảm).
- Latency routing thấp (<5ms/bước trên A100).

## Ví dụ áp dụng
Solopreneur chạy pipeline viết bài đa kênh: bước 1 lên ý tưởng (dùng model nhỏ), bước 2 viết nội dung (dùng model lớn), bước 3 định dạng HTML (dùng model nhỏ). AgentRouter route tự động mỗi bước đến model tier phù hợp, cắt chi phí inference xuống còn khoảng 30% so với dùng model lớn cho mọi bước.

## Gotchas
- Cần dữ liệu quỹ đạo đã gán nhãn để train classifier; nếu không có, skill không chạy được.
- Khi test trên framework chưa thấy (ví dụ AutoGen), accuracy giảm 6–9%, tuy chi phí giảm vẫn đạt 58%.
