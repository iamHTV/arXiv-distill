# Skill: MAPL — Multi-Agent Preference Learning cho hợp tác đa tác tử
Source: 2609.32827v1
Type: framework

## Khi nào dùng skill này
- Có nhiều LLM agents (mô hình ngôn ngữ lớn tác tử) phối hợp trên cùng task (tác vụ) và cần điều phối chất lượng output (đầu ra).
- Không có scalar reward (phần thưởng vô hướng) rõ ràng, chỉ có thể so sánh hai bản output nào tốt hơn.
- Muốn cải thiện hiệu quả hợp tác multi-agent (đa tác tử) mà không định nghĩa metric (thước đo) cứng.

## Tình huống KHÔNG nên dùng
- Task đơn agents (không cần multi-agent coordination — phối hợp đa tác tử).
- Có sẵn reward function (hàm phần thưởng) hoàn hảo, đo chính xác chất lượng output.

## Input cần có
- Nhóm LLM agents làm cùng task (tối thiểu 2 agents).
- Cơ chế so sánh hai trajectory (quỹ trình)/output: annotator (người gán nhãn — người dùng hoặc AI judge — trọng tài AI).
- Dataset preference pairs (cặp ưu tiên: winner — người thắng, loser — người thua) từ các cặp so sánh.

## Các bước thực hiện
1. Thu thập joint history (lịch sử chung) và trajectory (quỹ trình) của các agents cho mỗi task.
2. Với mỗi cặp trajectory, annotator so sánh return (lợi nhuận)/chất lượng, gán nhãn winner (cao hơn) và loser, bỏ ties (hòa).
3. Lấy top-k preference pairs có winning return cao nhất làm replay buffer (bộ đệm phát lại).
4. Chọn MARLHF (học reward model (mô hình phần thưởng) từ preference (ưu tiên), rồi optimize policy (chính sách) bằng MARL — học tăng cường đa tác tử) hoặc MADPO (tối ưu trực tiếp policy từ preference).
5. Lặp lại quá trình thu thập–so sánh–huấn luyện theo nhiều iteration (lần lặp).
6. Chọn paradigm (nguyên mẫu) phối hợp: Dec-Dec (đều phi tập trung), Cen-Cen (đều tập trung), hoặc Dec-Cen (agents phi tập trung, comparator tập trung) tùy resource (tài nguyên) và nhu cầu thông tin.

## Output mong đợi
- Policies (chính sách) của agents được tối ưu từ preference feedback (phản hồi ưu tiên), chất lượng hợp tác cải thiện, gần bằng MARL với oracle reward (phần thưởng chuẩn).

## Ví dụ áp dụng
Hai agents Qwen3-1.7B cùng tóm tắt bài Reddit: agent 1 tóm tắt cao cấp, agent 2 tóm tắt chi tiết. Output ghép lại đưa cho annotator so sánh hai phiên bản, dùng preference để fine-tune (tinh chỉnh) reward model, sau đó MARLHF điều phối hai agents tóm tắt tốt hơn.

## Gotchas
- MARLHF nhạy data coverage (độ bao phủ dữ liệu), model agents/comparator, MARL algorithm (thuật toán) — không chạy mù quáng.
- Centralized comparator (bộ so sánh tập trung) lớn hơn không guaranteed (không đảm bảo) cải thiện kết quả — vì information gap (khoảng trống thông tin) và realizability gap (khoảng trống khả năng hiện thực hóa) giữa agents và comparator.
- Raw LLMs (mô hình ngôn ngữ lớn thô) không tự nhiên hợp tác → preference data (dữ liệu ưu tiên) ban đầu có thể chứa nhiều trajectory không hợp tác.
