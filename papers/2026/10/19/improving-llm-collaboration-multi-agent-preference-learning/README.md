# [2609.32827v1] Improving LLM Collaboration via Multi-Agent Preference Learning

## Giá trị cốt lõi (1 câu)
Dùng preference learning (học từ phản hồi so sánh) thay vì scalar reward (phần thưởng vô hướng) cố định để tối ưu hợp tác multi-agent (đa tác tử), đạt gần bằng MARL (học tăng cường đa tác tử) với oracle reward (phần thưởng chuẩn) mà không cần metric (thước đo) hoàn hảo.

## Problem
- Prior work giả định đã có sẵn scalar reward (phần thưởng vô hướng) chính xác cho multi-agent collaboration (hợp tác đa tác tử); thực tế metric thường thiếu và khó tổng hợp. Chưa ai khám phá preference learning (học từ ưu tiên — tín hiệu "A hay B hơn") cho multi-agent systems (hệ thống đa tác tử).

## Contribution
- Đưa preference-based MAS (hệ thống đa tác tử) từ góc nhìn decentralized (phi tập trung) và centralized (tập trung).
- MAPL: framework (khung phương pháp) tối ưu MAS từ preference feedback (phản hồi ưu tiên), cập nhật policy (chính sách) lặp lại bằng cách so sánh solution hiện tại với solution do comparator agent (tác tử so sánh) tạo ra.
- Hiện thực MAPL bằng MARLHF (multi-agent RLHF với reward model (mô hình phần thưởng) học được) và MADPO (multi-agent direct preference optimization — tối ưu ưu tiên trực tiếp đa tác tử).
- Experiment (thí nghiệm) trên collaborative writing (viết cộng tác), coding (lập trình), tool use (dùng công cụ), travel planning (lập kế hoạch du lịch).

## Method
MAPL khởi tạo bằng thu thập joint history (lịch sử chung) và trajectory (quỹ trình) của các agents cho mỗi task (tác vụ). Với mỗi cặp trajectory, annotator (người gán nhãn) so sánh return (lợi nhuận), gán nhãn winner (người thắng) cho trajectory có return cao hơn, bỏ ties (hòa). Top-k preference pairs (cặp ưu tiên) có winning return cao nhất làm replay buffer (bộ đệm phát lại). Lặp lại: học reward model rồi optimize policy (MARLHF), hoặc tối ưu trực tiếp từ trajectory preferences (MADPO). Ba paradigm (nguyên mẫu) phối hợp: Dec-Dec (agents + comparator đều phi tập trung), Cen-Cen (đều tập trung), Dec-Cen (agents phi tập trung, comparator tập trung).

## KNOWLEDGE — Số liệu & khái niệm
- CoopHE (benchmark lập trình cộng tác) pass rate (tỷ lệ đạt): MAPL đạt 65.8%, vượt strongest single-agent baseline (đường cơ sở tác tử đơn mạnh nhất).
- Travel (lập kế hoạch du lịch) pass rate: MAPL đạt 76.4%.
- MARLHF (Dec-Dec) vs MAGRPO (MARL với oracle reward): CoopHE call rate (tỷ lệ gọi công cụ) 40.2% vs 37.9%; Travel success 13.1% vs 12.5% — MARLHF vượt oracle dưới decentralized collaboration.
- MAPL chênh MAGRPO dưới 1% ở TLDR score (điểm tóm tắt) và Travel pass rate; MARL methods (dùng oracle reward) vẫn cao nhất vì reward align (căn chỉnh) trực tiếp với objective (mục tiêu) task.
- MARLHF thường vượt MADPO ở đa số task, nhưng nhạy data coverage (độ bao phủ dữ liệu), model agents/comparator, MARL algorithm (thuật toán) bên dưới.
- Cen-Cen (tập trung cả agents lẫn comparator) thường hiệu quả nhất cho cả MARLHF và MADPO.
- Đánh giá trên 4 domains (lĩnh vực): TLDR (xử lý tài liệu), CoopHE (lập trình), BFCL (gọi hàm), Travel (lập kế hoạch du lịch), qua 5 runs (lần chạy).

## INSIGHT — Cơ chế & tại sao
- [MAPL hoạt động tốt] VÌ preference dataset (tập dữ liệu ưu tiên) có mật độ cao các mẫu chất lượng tương đồng (ví dụ code đúng với các mẫu hình hợp tác khác nhau), tạo local training signal (tín hiệu huấn luyện cục bộ) giàu để phân biệt chất lượng tương đối.
- [Comparator tập trung/lớn hơn không nhất thiết cải thiện training] VÌ information gap (khoảng trống thông tin) và realizability gap (khoảng trống khả năng hiện thực hóa) giữa agents và comparator — Dec-Cen perform poorly (hoạt động kém) ở đa số domain vì lý do này.

## IDEA — Áp dụng được gì
- Khi nhiều LLM agents (mô hình ngôn ngữ lớn tác tử) phối hợp mà không có metric cứng: để annotator (người hoặc AI judge — trọng tài AI) so sánh từng cặp output, gán nhãn winner/loser, rồi fine-tune (tinh chỉnh) reward model hoặc áp DPO (tối ưu ưu tiên trực tiếp) trực tiếp. Bước đầu: chạy 2 agents cùng 1 task, thu thập cặp trajectory, gán nhãn.
- Áp dụng cho solopreneur: khi dùng 2 AI viết 2 phiên bản caption (dòng chú thích) cho cùng sản phẩm, đừng hỏi điểm 1–10 — hãy chọn bản tốt hơn, lưu cặp (winner, loser) làm bộ dữ liệu dạy lại model phong cách bạn muốn.

## WISDOM — Nguyên tắc tổng quát
[NO WISDOM] — Paper tập trung framework (khung phương pháp) và experiment (thí nghiệm) cụ thể, chưa đủ tầm rút nguyên tắc tổng quát ngoài domain (lĩnh vực) gốc.

## Assumptions & Limitations
- Giả định có annotator (người gán nhãn) so sánh chính xác hai trajectory (quỹ trình).
- MARLHF nhạy data coverage (độ bao phủ dữ liệu), model agents/comparator, MARL algorithm (thuật toán).
- Paper thừa nhận: raw LLMs (mô hình ngôn ngữ lớn thô) không tự nhiên hợp tác → preference data (dữ liệu ưu tiên) ban đầu chứa nhiều trajectory không hợp tác.
- Paper KHÔNG nói: chi phí thu thập preference feedback (phản hồi ưu tiên) ở quy mô production (sản xuất), độ trễ khi cần annotator trực tiếp.

## Metadata
- Năm: 2026, tác giả: Shuo Liu, Xinzichen Li, Tianle Chen, Christopher Amato, category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.32827v1
