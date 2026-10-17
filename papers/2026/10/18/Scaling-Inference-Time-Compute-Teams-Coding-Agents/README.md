# [2610.17471v1] Scaling Inference-Time Compute with Teams of Coding Agents

## Problem
Hệ thống multi-agent hứa hẹn một trục mở rộng mới cho inference-time compute: thay vì để một agent suy nghĩ lâu hơn hoặc lấy mẫu nhiều lần, một nhiệm vụ được chia cho nhiều agent làm song song và phối hợp. Tuy nhiên, trong thực tế, thêm nhiều agent dễ dàng tạo ra công việc trùng lặp, thất bại phối hợp, và chi phí cao hơn. Việc thiết kế nhóm agent như một bài toán phân bổ compute: bắt đầu từ một agent đơn (solo agent), compute bổ sung nên đi vào đâu để đến reward-cost Pareto frontier?

## Contribution
- Đặt thiết kế nhóm agent làm bài toán phân bổ compute (compute allocation problem): bắt đầu từ solo agent, compute bổ sung nên được phân bổ vào đâu để đạt reward-cost Pareto frontier.
- Xây dựng một multi-agent harness tối thiểu từ đầu và تتبع frontier bằng cách thay đổi, lần lượt, giai đoạn workflow mà lead ủy quyền cho workers (lập kế hoạch, triển khai, xác thực), các model tạo thành nhóm, và số lượng workers.
- Nhận ra 3 phát hiện cốt lõi: (1) lập kế hoạch làخدام compute hiệu quả nhất; (2) model rẻ hiệu quả khi làm lập kế hoạch nhưng không khi làm triển khai; (3) lập kế hoạch tiếp tục cải thiện reward khi nhóm lớn, trong khi triển khai và xác thực bế tắc sau 4 workers.

## Method
- Harness phân cấp: lead agent phân rã nhiệm vụ, ủy quyền sub-task cho workers, và tổng hợp kết quả. Workers chạy trong shared sandbox. Lead dùng công cụ delegate_agent(task, agent_id=None) để tạo worker mới hoặc phục hồi worker cũ.
- Mô hình: 3 cấp GPT-5.6 (Sol, Terra, Luna), medium reasoning effort. Homogeneous team dùng cùng model cho lead và workers. Heterogeneous team ghép lead Sol/Terra với workers Luna.
- Dataset: ProgramBench (200 tác vụ tái hiện repository từ đầu), Commit0-Lite (16 thư viện Python).
- 4 cấu hình delegation stage: P (lập kế hoạch), I (triển khai), V (xác thực), PIV (tất cả 3 giai đoạn). Chế độ blocking (lead chờ) và async (lead tiếp tục làm việc).

## Key Findings
- Nhóm vượt qua agent đơn nhưng tốn 3–7 lần chi phí inference hơn.
- Nhóm 17 agents heterogeneous đạt trong 1.4 điểm reward của nhóm 5 agents mạnh mẽ đồng nhất, với chi phí thấp hơn 70%.
- ηP = 3.8 (reward pts / $100) vs tối đa 2.4 cho bất kỳ giai đoạn nào khác — mỗi dollar chi vào lập kế hoạch mua ~1.6× nhiều reward hơn cùng dollar chi vào triển khai, xác thực, hoặc toàn bộ workflow.
- Lập kế hoạch đơn lẻ khớp reward của PIV hướng dẫn nghiêm ngặt với nửa chi phí.
- Lead mạnh với lập kế hoạch bằng model rẻ khôi phục 47.5% của reward gain của nhóm toàn mạnh với chỉ 13.9% chi phí bổ sung; model rẻ làm triển khai giảm reward.
- Lập kế hoạch tiếp tục cải thiện reward khi nhóm lớn, trong khi triển khai và xác thực bế tắc sau 4 workers.

## Actionable Insights
1. Đầu tư compute vào giai đoạn lập kế hoạch trước khi viết code — lập kế hoạch mang hiệu quả reward-cost cao nhất. Áp dụng: khi xây dựng multi-agent coding, hãy để workers chuyên làm lập kế hoạch và khám phá repository, còn lead tự viết và xác thực code. Bước đầu: Thay đổi prompt của lead để chỉ ủy quyền giai đoạn lập kế hoạch cho workers, giữ triển khai và xác thực cho chính lead.
2. Dùng model rẻ cho lập kế hoạch, model mạnh cho triển khai. Áp dụng: trong heterogeneous team, dùng model mạnh (Sol) cho lead, model rẻ (Luna) cho workers lập kế hoạch. Bước đầu: Thiết lập team với lead model cao cấp và workers model thấp cấp chỉ cho giai đoạn lập kế hoạch.
3. Giới hạn số lượng implementer và verifier ở mức 4 workers trở xuống — thêm nhiều hơn không cải thiện reward. Áp dụng: khi mở rộng team, chỉ tăng số lượng planner, không tăng implementer/verifier vượt quá 4. Bước đầu: Đặt giới hạn tối đa 4 workers cho giai đoạn triển khai và xác thực.

## Assumptions & Limitations
- Đánh giá trên ProgramBench (tác vụ tái hiện repository từ đầu), kết quả có thể khác trên Commit0 hoặc các domain ngoài phần mềm.
- Chỉ dùng 3 model GPT-5.6 (Sol, Terra, Luna), không generalize sang Claude, Gemini, hoặc các model opensource.
- Số workers tối đa 16, chưa xét đội ngũ hàng trăm nghìn agent.
- 84% tin nhắn gửi đến lead, chỉ 4% giữa các workers — thấy chưa rõ cách phối hợp giữa workers khi dự án quá lớn để một agent nắm toàn bộ.

## Metadata
- Năm: 2026, tác giả: Keenan Samway, Marzieh Fadaee, Daniel D'souza, Tan Yi-Chern, Omar Darwiche Domingues, Nouha Dziri (Cohere Labs), category arXiv: cs.MA, link PDF: https://arxiv.org/pdf/2610.17471v1