# [2610.00758v1] Scalable Multi-Task Inverse Reinforcement Learning

## Problem
- Nghịch-Smith verstär học (inverse reinforcement learning) nhằm khôi phục phần thưởng mà các agent dùng để suy đoán hành vi (revealed preferences), cho phép học tập sao chép (imitation learning) và hỗ trợ sự căn chỉnh từ phản hồi con người (alignment from human feedback). Nhiều trường hợp có nhiều tác vụ khác nhau — mỗi tác vụ tương ứng một hàm phần thưởng (reward function) riêng của agent. Việc tắt một tuyến cung (shutting down a train line) dẫn các khách hàng di động có sở thích riêng về tốc độ, chi phí và độ dồn dập phải định tuyến lại. Vì vậy, một nhà lập kế hoạch phải dự đoán việc ré-optim hóa dù chỉ có mức độ bao phủ (coverage) hạn chế của mỗi khách hàng. Chúng tôi xem xét N nhiệm vụ độc lập, tức là N hàm phần thưởng riêng của agent, trong đó mỗi tác vụ cho chúng ta thấy hành vi mềm-sát-ối tương tự (soft-optimal behavior) được điều khiển trong môi trường nguồn (source environment). Chúng ta sau đó tìm cách học những phần thưởng này để dự đoán cách hành vi của các agent sẽ chuyển tiếp đến môi trường đích (target environment).
- Thử nghiệm đơn-task thường tập trung trên một vùng nhỏ của không gian trạng thái, nên sự phủ thất (partial coverage) làm suy yếu việc xác định phần thưởng (reward identification). Cụ thể, trong khung học cố định nhiệt độ (maximum-entropy RL framework), điều này thể hiện qua nhiệt độ (temperature): nhiệt độ cao giúp coverage cao hơn nhưng làm phẳng xác suất lựa chọn (choice probabilities), trong khi nhiệt độ thấp làm sắc nét tín hiệu phần thưởng (reward signal) nhưng làm hẹp coverage. Việc sắp xếp (fitting) mỗi nhiệm vụ một cách độc lập kế thừa vấn đề hỗ trợ đơn-task (single-task support problem).

## Method (tóm tắt cốt lõi)
- Phương pháp học ngữ cảnh sinh động đa nhiệm (multi-task inverse reinforcement learning) gộp dữ liệu từ nhiều agent với phần thưởng khác nhau trong cùng một môi trường dưới giả định thấp-rank (low-rank assumption).
- Học tập phương diện chung-cross-task của đầu vào của nhiệm vụ (trong ngữ cảnh này, sở thích của agent) dưới giả định thấp-rank (low-rank assumption).

## Key Findings
- 4 tác giả từ Netflix, Cornell Tech, MIT, category arXiv: cs.LG.
- Phân tích phương pháp trên nhiều tác vụ trong môi trường mới.
- Phương pháp mạnh mẽ với sự phủ thất (limited coverage).
- Khôi phục phần thưởng trên và ngoài hỗ trợ của mỗi nhiệm vụ (each task's support).
- Chuyển giao (transfer) đến môi trường đích với sự hối hận (regret) thấp hơn các phương pháp cơ sở (baselines).
- Lợi thế tính toán (computational advantage) so với các phương pháp cho từng tác vụ (per-task methods) mở rộng hơn khi số tác vụ tăng.

## Actionable Insights
1. Dùng multi-task inverse reinforcement learning để học hỏi từ nhiều tác vụ liên quan với cùng một môi trường dưới giả định thấp-rank. Áp dụng: khi có nhiều tác vụ liên quan với cùng một môi trường, dùng multi-task inverse reinforcement learning để học cách tính toán phần thưởng cho từng tác vụ.
2. Dùng hình thức thấp-rank để học cách đại diện chung-cross-task của đầu vào của nhiệm vụ (trong bối cảnh này, sở thích của agent). Áp dụng: dùng hình thức thấp-rank để học cách đại diện chung-cross-task của đầu vào của nhiệm vụ khi có nhiều tác vụ liên quan.

## Assumptions & Limitations
- Đánh giá trên các tác vụ liên quan với cùng một môi trường dưới giả định thấp-rank.
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).

## Metadata
- Năm: 2026, tác giả: Allen Tran, Jia Wan, Nathan Kallus, Aurélien Bibaut (Netflix, Cornell Tech, MIT), category arXiv: cs.LG, link PDF: https://arxiv.org/pdf/2610.00758v1
