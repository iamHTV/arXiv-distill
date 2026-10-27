# Skill: agentorch-global-orchestration-improvement
Source: 2610.33375v1
Type: optimization-method

## Khi nào dùng skill này
- Cần giảm số lượng LLM calls trong hệ thống workflow doanh nghiệp mà vẫn duy trì độ chính xác cao.
- Muốn so sánh global orchestration với step-by-step interaction trên cùng các workflow, công cụ, môi trường thực thi.
- Muốn áp dụng các kỹ thuật hẹp khoảng cách giữa global và step-by-step orchestration.

## Tình huống KHÔNG nên dùng
- Workflow có quá nhiều nhánh điều khiển phụ thuộc vào kết quả runtime không thể dự đoán trước.
- Không cần giảm số lượng LLM calls (chi phí suy luận không phải vấn đề).

## Input cần có
- 650 enterprise SOPs (hoặc tập workflow doanh nghiệp của riêng bạn) với reference workflow cho mỗi SOP.
- Danh mục tool interfaces (ví dụ: 64 tool spans Slack, Jira, Salesforce, Google Sheets, Google Drive, Snowflake, Workato).
- Môi trường thực thi có thể mô phỏng (simulated backend) cho đánh giá tái tạo được.
- Runtime variants cho mỗi SOP (đầu vào khác nhau, điều kiện thực thi khác nhau).

## Các bước thực hiện
1. Xây dựng AgentOrch benchmark từ các thực thể doanh nghiệp có thể thực thi: mỗi SOP có reference workflow và nhiều runtime variants.
2. Chạy Global orchestration: model sinh workflow hoàn chỉnh trước khi thực thi, không quan sát đầu vào runtime cụ thể.
3. Chạy Step-by-Step interaction: vòng lặp hành động–quan sát, model gọi LLM sau mỗi hành động để quyết định bước tiếp theo.
4. Áp dụng Local (xây dựng workflow tăng dần): xây dựng workflow qua trình chỉnh sửa chỉ thêm, sau mỗi chỉnh sửa validator kiểm tra và chấp nhận hoặc từ chối. Không cần đầu vào runtime hay kết quả thực thi.
5. Áp dụng Replan (sửa bằng phản hồi thực thi): thực thi workflow Global trên một vài runtime variants, cung cấp phản hồi thực thi cho model, yêu cầu model sửa đổi workflow hoàn chỉnh.
6. Đánh giá Orchestration Accuracy: trung bình của Execution Trace Accuracy và Side-Effect Accuracy.
7. (Tùy chọn) Đào tạo mục tiêu: đào tạo model trên 3,000 source recipes, mỗi mẫu kết hợp thông số tác vụ với workflow tham chiếu hoàn chỉnh. Lấy cái tốt hơn của SFT và RL.

## Output mong đợi
- Khoảng cách Orchestration Accuracy giữa Global và Step-by-Step.
- Số lượng LLM calls và completion tokens cho mỗi giao thức.
- Workflow đã được cải thiện qua Local, Replan, hoặc đào tạo mục tiêu.

## Ví dụ áp dụng
Công ty có hệ thống onboarding nhân viên đa bước (tạo tài khoản Slack, tạo record Salesforce, gửi email chào mừng, thêm vào Google Sheet). Hiện tại dùng Step-by-Step, mỗi lần onboarding tốn 23.2 lần LLM calls. Áp dụng Global orchestration: sinh toàn bộ workflow onboarding trước khi thực thi, thực thi mà không cần thêm LLM calls. Nếu độ chính xác chưa đủ, áp dụng Local (xây dựng tăng dần với validator) và Replan (sửa bằng phản hồi thực thi từ 2 variants mẫu). Kết quả: giảm 23.2 lần LLM calls, khoảng cách chính xác coết xuống ~8.5 pp.

## Gotchas
- Global orchestration vẫn kém chính xác hơn Step-by-Step trên mọi model được đánh giá (khoảng cách còn ~8.5 pp với model mới nhất).
- Model quy mô lớn không nhất quán hẹp khoảng cách — không nhất quán đơn thuần dùng model lớn hơn.
- Reasoning không cung cấp lợi ích nhất quán tuyệt đối cho Global cũng không nhất quán hẹp khoảng cách.
- Cần reference workflow cho mỗi SOP để đánh giá — không áp dụng được cho workflow hoàn toàn mới chưa từng thực thi.
- Cần môi trường thực thi có thể mô phỏng để đánh giá tái tạo được.