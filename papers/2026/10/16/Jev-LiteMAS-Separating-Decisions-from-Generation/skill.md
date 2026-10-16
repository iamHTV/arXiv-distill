# Skill: jev-litemas-multi-agent-decision-routing
Source: 2610.21411v1
Type: framework

## Khi nào dùng skill này
- Pipeline AI có nhiều agent chuyên gia liên tiếp, mỗi agent tạo artifact rồi chuyển cho agent sau.
- Muốn cắt chi phí LLM vì routing (chọn agent tiếp theo) và review (kiểm tra artifact) chiếm 30%+ token.
- Có thể định danh trước các expert roles và legal actions (pass/escalate, accept/revise).

## Tình huống KHÔNG nên dùng
- Tác vụ đòi hỏi tạo chuyên gia mới hoặc reconfig (cấu hình lại) vai trò cho tác vụ chưa từng thấy.
- Workflow chỉ có 1 agent, không cần điều phối nhiều agent.

## Input cần có
- Danh sách expert roles và legal actions có sẵn.
- Task rubric (thang đánh giá tác vụ) để Jev screen artifact.
- Mô hình generative backbone (ví dụ DeepSeek-V4-Flash, GPT-5) cho expert execution và LLM review.
- Jev decision model (có thể fine-tune SLM nhỏ).

## Các bước thực hiện
1. Xây dựng Jev decision model nhận task và accumulated context, chọn chuyên gia tiếp theo từ expert pool (ra quyết định PASS/ESCALATE cho artifact trung gian).
2. Nếu PASS, chuyển artifact trực tiếp cho chuyên gia được chọn qua handoff; nếu ESCALATE, gọi LLM review để ACCEPT/REVISE và gắn feedback semantic (phản hồi ngữ nghĩa).
3. Cập nhật state chung sau mỗi bước để chuyên gia sau tiếp nhận artifact và công việc đã làm.
4. Chỉ bật generative review cho artifact thực sự cần sửa hoặc xét duyệt, tránh gọi LLM cho mọi bước điều phối.

## Output mong đợi
- Giảm 12.7–54.6% token generative-LLM so với baseline all-generative (như LAS), giữ độ chính xác trong khoảng 1.34 phần trăm điểm.
- Latency thấp hơn, Jev chỉ chiếm 2.92–6.85% latency end-to-end.

## Ví dụ áp dụng
Solopreneur chạy pipeline sinh nội dung đa kênh: agent 1 viết bài, agent 2 chỉnh SEO, agent 3 đăng bài. Thay vì LLM lớn chọn agent tiếp theo và kiểm tra mỗi bản thảo, dùng Jev nhỏ để route bài từ agent 1 sang agent 2 chỉ khi bài đạt tiêu chí, và chỉ gọi LLM lớn review khi Jev đánh giá bài cần sửa.

## Gotchas
- Nếu bỏ semantic feedback khi REVISE, accuracy giảm mạnh (từ 75.33% xuống 57.33% trên IDRBench I3).
- Khi tỷ lệ artifact cần sửa cao, hiệu quả tiết kiệm token giảm theo.
