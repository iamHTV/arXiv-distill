# Skill: Phân bổ compute inference cho Multi-Agent Coding Team

Source: 2610.17471v1
Type: framework

## Khi nào dùng skill này
- Bạn đang xây dựng multi-agent team để giải quyết tác vụ code dài hạn và muốn biết phân bổ compute inference vào đâu để đạt reward-cost Pareto frontier.
- Bạn có một lead agent mạnh và muốn biết khi nào nên thêm workers, với model gì, và vào giai đoạn nào của workflow.
- Bạn cần tối ưu chi phí inference khi mở rộng agent team.

## Tình huống KHÔNG nên dùng
- Nhiệm vụ đơn giản, một agent đơn là đủ — không cần multi-agent team.
- Bạn không có sự khác biệt về khả năng giữa các model (không có model mạnh và model rẻ để ghép heterogeneous team).

## Input cần có
- Task mục tiêu rõ ràng (ví dụ: tái hiện repository, triển khai tính năng, sửa lỗi).
- Lead agent model mạnh (ví dụ: Sol).
- Worker agent model (có thể mạnh hoặc rẻ, ví dụ: Luna).
- Giai đoạn workflow: lập kế hoạch (P), triển khai (I), xác thực (V).

## Các bước thực hiện
1. Ủy quyền chỉ giai đoạn lập kế hoạch (P) cho workers, để lead tự triển khai và xác thực code — lập kế hoạch mang hiệu quả reward-cost cao nhất (ηP = 3.8 vs ≤2.4 cho giai đoạn khác).
2. Dùng model mạnh cho lead, model rẻ cho workers lập kế hoạch — lead mạnh với planner rẻ khôi phục 47.5% reward gain của team toàn mạnh với chỉ 13.9% chi phí bổ sung.
3. Giới hạn số implementer và verifier ở mức tối đa 4 workers — thêm nhiều hơn không cải thiện reward (bế tắc sau 4 workers).
4. Tăng số lượng planner khi nhóm lớn — lập kế hoạch tiếp tục cải thiện reward khi nhóm lớn hơn.
5. Chọn chế độ blocking (lead chờ workers hoàn thành) nếu cần độ chính xác cao, hoặc async (lead làm việc song song) nếu cần tốc độ nhưng chấp nhận mất ~6 điểm reward dưới hướng dẫn tối thiểu.

## Output mong đợi
- Một heterogeneous multi-agent team với lead mạnh, planners rẻ, số lượng implementer/verifier giới hạn.
- Compute inference được phân bổ ưu tiên vào lập kế hoạch, không lãng phí vào triển khai/xác thực thừa.
- Chi phí thấp hơn đáng kể so với team đồng nhất toàn mạnh mà vẫn đạt gần cùng mức reward.

## Ví dụ áp dụng
Bạn xây dựng agent tự viết code cho ứng dụng doanh nghiệp. Lead (GPT-5.6 Sol) nhận nhiệm vụ, ủy quyền lập kế hoạch cho 3 workers (GPT-5.6 Luna) khám phá repository và lập kế hoạch thiết kế. Lead sau đó tự viết code và xác thực. Nếu cần thêm worker, chỉ tăng planner, không tăng implementer vượt quá 4. Chi phí inference giảm 70% so với team toàn model mạnh trong khi reward chỉ kém 1.4 điểm.

## Gotchas
- Model rẻ làm triển khai (implementer) làm giảm reward — chỉ dùng model rẻ cho lập kế hoạch.
- Thêm implementer và verifier vượt quá 4 workers không cải thiện reward, chỉ làm phân mảnh code và tốn chi phí.
- Mở chung chế độ async (không chờ workers) tiết kiệm thời gian nhưng làm giảm khoảng 6 điểm reward so với blocking trong điều hướng tối thiểu.