# Skill: pilot-proactive-insight-learner-experiments
Source: 2608.18637v2
Type: framework

## Khi nào dùng skill này
- Tối ưu hóa hệ thống khuyến nghị (recommendation system) với LLM agent.
- Muốn agent tự thiết kế thí nghiệm A/B và cá nhân hóa chiến lược theo phân khúc người dùng.
- Cần ranh giới an toàn (guardrails) deterministik cho agent.

## Tình huống KHÔNG nên dùng
- Không có hệ thống khuyến nghị hoặc dữ liệu giao dịch thật.
- Chỉ cần tối ưu hóa tham số đơn giản, không cần agent thiết kế thí nghiệm.

## Input cần có
- Hệ thống khuyến nghị và dữ liệu giao dịch thật.
- Các deterministic services để thực thi ranh giới an toàn, thống kê, và quyền hạn.
- Mô hình LLM có khả năng lập kế hoạch thí nghiệm.

## Các bước thực hiện
1. Thiết lập Experiment Manager agent để quản lý vòng đời thí nghiệm (thiết kế, chạy, phân tích, kết luận).
2. Thiết lập Insight Learner agent để học phần định từ các thí nghiệm trước và áp dụng vào thí nghiệm mới.
3. Đặt deterministic guardrails: exposure PV, transaction count, ad PVR, GMV guardrail, v.v. để agent không vượt quá ranh giới an toàn.
4. Chạy thí nghiệm liên tục, agent tự cá nhân hóa chiến lược theo phân khúc người dùng (ví dụ visit_frequency ≥ 5/t tuần).
5. Tích lũy phương pháp luận thí nghiệm (reusable experimental methodology) để áp dụng cho các tác vụ sau.

## Output mong đợi
- Cải thiện IPV lên đến +1.40%, Core IPV +1.60%, transaction count +0.96%, transaction amount +1.50%.
- Nâng cao search efficiency từ 53.3% lên 93.3%.
- Không cần can thiệp của con người trong suốt quá trình thí nghiệm.

## Ví dụ áp dụng
Solopreneur chạy hệ thống khuyến nghị sản phẩm: dùng PILOT để agent tự thiết kế thí nghiệm A/B cho từng phân khúc người dùng (ví dụ người dùng ghé thăm ≥ 5 lần/tuần), đặt guardrails cho GMV không giảm quá 0.5%, và tích lũy phương pháp luận thí nghiệm để áp dụng vào các Campaign sau.

## Gotchas
- So sánh trong paper là before/after, không randomized — kết quả có thể có bias.
- Cần deterministic services để thực thi guardrails; nếu không có, agent có thể vượt quá ranh giới an toàn.
- Chưa đánh giá trên nhiều domen ngoài khuyến nghị.
