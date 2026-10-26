# 2610.31709 — Mining the Design Space of Multi-Agent Workflows

## Giá trị cốt lẽ (1 câu)

Thiết kế workflow multi-agent LLM không nên bắt đầu bằng Star fan-out (các worker độc lập giải quyết rồi tổng hợp một lần), mà nên dùng SharedMemory (tài liệu liên tục chia sẻ) thay vì Debate (truyền tin nhiều vòng), và viết prompt template cụ thể có named placeholder (tên ô trống định hướng ngữ cảnh) — hiệu quả không kém việc chọn cấu trúc liên lạc.

## Problem

Thiết kế hệ thống multi-agent LLM (hệ thống nhiều agent LLM làm việc cùng nhau) vẫn dựa trên tentative and error (thử và sai) và "folk wisdom" (kinh nghiệm dân gian phi hệ thống). Các nghiên cứu thủ công chỉ kiểm tra ít cấu trúc liên lạc (topology) cố định, trong khi các bộ tối ưu tự động loại bỏ các quỹ traversal (search trajectory) trung gian sau khi chọn workflow phù hợp với tâche — việc này làm mất đi các compara­sion (so sánh) trung gian cần thiết để giải thích tại sao thiết kế này thành công và thiết kế kia thất bại.

## Contribution

1. Xây dựng pipeline hai giai đoạn để khai thác các nguyên tắc thiết kế workflow có thể tái lập từ mã nguồn workflow và các dấu vết thực thi (execution trace).
2. Sử dụng lại bộ tối ưu MCTS (tìm kiếm cây Monte Carlo) của AFlow trên 6 toán tử có thể ghép (composable operators) và 26 nhiệm vụ Enigmata đã được xác định định mức (deterministically verified), giữ lại tất cả các vòng trung gian để xây dựng bộ sưu tập 28.568 workflow có thể thực thi.
3. Sử dụng vòng AutoResearch (nghiên cứu tự động hóa) trong sandbox (môi trường kín) để khai thác mã điều phối (orchestration code) và mẫu prompt (prompt template) dưới mục tiêu xác thực bị phạt L0 (L0-penalized validation objective), sau đó kiểm tra các nguyên tắc ứng viên trên các vòng tìm kiếm riêng lẻ (held-out searches).
4. Khai thác được 3 nguyên tắc thiết kế ở 3 cấp độ: Star-first làm giảm hiệu quả, SharedMemory vượt trội hơn Debate, và cấu trúc prompt cụ thể (specificity) có lợi tương đương việc chọn cấu trúc liên lạc (communication structure).

## Method

Pipeline hai giai đoạn:

**Giai đoạn 1 (Sampling - Lấy mẫu):** Sử dụng lại AFlow MCTS để tìm kiếm workflow qua N = 20 vòng (rounds), K = 5 chạy độc lập trên mỗi điều kiện. Mỗi workflow W được biểu thị bằng lớp Python có thể thực thi trong graph.py kèm theo mẫu prompt văn bản cứng (hard text prompt templates) trong prompt.py (không có soft prompt hay cập nhật gradient). Lấy mẫu cha từ top-k (k = 4) workflow đã đánh giá theo phân phối hỗn hợp uniform/softmax (λ = 0.2 trọng số uniform, nhiệt độ α = 0.4).

**Giai đoạn 2 (Analysis - Phân tích):** Dùng AutoResearch trong sandbox để khai thác tính năng từ graph.py và prompt.py, fit hồi quy (regressor) từ tính năng (phi(W)) và mô tả nhiệm vụ (psi(T)) đến điểm số (m), tính điểm trên tập xác thực riêng lẻ (held-out validation) bằng mục tiêu F = R² − λ||phi||₀ (phạt số lượng tính năng đang hoạt động).

## KNOWLEDGE — Số liệu & khái niệm

- Bộ sưu tập: 28.568 workflow có thể thực thi qua 26 nhiệm vụ Enigmata (nhiệm vụ lý luận xác định định mức), 1.701 chuỗi tìm kiếm MCTS hoàn thành từ 1.740 ô lưới (grid cells).
- 6 toán tử: Sequential (47.2%), Star (44.5%), Debate (22.3%), SharedMemory (20.8%), DebateWithModerator (11.8%), StarWithCoordinator (8.8%).
- R² chỉ dùng graph.py = 0.521; cùng lúc khai thác prompt.py nâng R² lên 0.638 (27 tính năng).
- Chi phí: ~$0,0064 mỗi ví dụ nhiệm vụ, tổng ~$4.454 chi phí tính toán.
- Original agent backbone: GPT-5.4 làm MCTS optimizer; {GPT-5.4-mini, GPT-5.4-nano} làm worker và aggregator.

## INSIGHT — Cơ chế & tại sao

[Star-first làm giảm hiệu quả] xảy ra VÌ [các worker giải quyết độc lập mà không giao tiếp bên ngoài (lateral communication), lỗi lan truyền và trình tổng hợp (aggregator) phải hòa giải mà không có kiểm chứng từ đồng輩 (peer verification)]. Điều này nghĩa là [fan-out độc lập vào đầuולה làm tăng sai số mà không có cơ chế sửa lỗi giữa các nhánh].

[SharedMemory vượt trội hơn Debate] xảy ra VÌ [trạng thái liên tục trong tài liệu chia sẻ (persistent shared document / blackboard) tránh mất thông tin so với luồng hội thoại nhiều vòng (multi-round conversational dialogue)]. Điều này nghĩa là [các agent viết tuần tự vào một tài liệu duy nhất giữ bối cảnh tốt hơn việc mỗi agent đọc toàn bộ đề xuất của nhau rồi sửa lại].

[Cấu trúc prompt cụ thể (specificity) và định tuyến ngữ cảnh dựa trên placeholder (placeholder-based context routing) quan trọng bằng việc chọn cấu trúc liên lạc] xảy ra VÌ [cấu trúc dưới cấp (sub-topological) trong prompt.py giải thích thêm độ biến thiên của workflow mà chỉ nhìn cấu trúc宏觀 (macro-topology) trong graph.py không bắt được (R² tăng từ 0.521 lên 0.638)].

## IDEA — Áp dụng được gì

1. Không bắt đầu workflow multi-agent bằng Star fan-out: Thay vì để các agent làm việc độc lập rồi tổng hợp một lần, hãy bắt đầu bằng Sequential (chuỗi các agent tuần tự) hoặc SharedMemory. Bước đầu: thiết kế entry point là một agent điều phối tuần tự thay vì quạt độc lập ra nhiều worker.

2. Dùng SharedMemory thay vì Debate cho tác vụ lý luận phức tạp: Thay vì để các agent đọc toàn bộ đề xuất của nhau rồi sửa trong nhiều vòng, hãy tạo một tài liệu chia sẻ liên tục (blackboard) mà các agent lần lượt đọc và ghi thêm. Bước đầu: xây dựng một shared document mà các agent cập nhật tuần tự thay vì luồng chat nhiều vòng.

3. Viết prompt template cụ thể có named placeholder: Thay vì prompt chung chung, hãy viết mẫu prompt chi tiết với các ô trống được đặt tên (named placeholders) như {problem}, {worker_outputs} để định tuyến ngữ cảnh. Bước đầu: kiểm tra lại mẫu prompt hiện tại, thêm named placeholders và specificity cao hơn cho mỗi vai trò agent.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Thiết kế workflow multi-agent nên bắt đầu bằng trạng thái chia sẻ liên tục, không phải fan-out độc lập; cấu trúc prompt quan trọng bằng cấu trúc liên lạc.
- Khi nào dùng: Khi xây dựng hệ thống multi-agent cho tác vụ lý luận phức tạp đòi hỏi phối hợp giữa các agent.
- Khi nào KHÔNG dùng: Tác vụ đơn giản không cần phối hợp (single-agent đủ).
- Ví dụ áp dụng ngoài domain gốc: Trong đội content (nhóm tạo nội dung), làm việc cùng một Google Doc (shared memory) hiệu quả hơn mỗi thành viên viết bản nháp riêng rồi người trưởng nhóm hợp nhất một lần.

## Assumptions & Limitations

- Điều kiện phải đúng: tác vụ lý luận xác định định mức (deterministically verified) không cần công cụ bên ngoài (tool-free); duy nhất một họ mô hình (GPT-5.4 làm optimizer, mini/nano làm worker).
- Limitation paper thừa nhận: tập trung vào tác vụ lý luận trừuát từ Enigmata, đơn họ mô hình, thiết bị kiểm soát loại bỏ tiếng ngõ grading và sai số API nhưng giới hạn khả năng áp dụng thực tế.
- Limitation paper KHÔNG nói: hiệu quả trên tác vụ có công cụ (tool-using), tác vụ thực tế ngoài lý luận trừuát, chi phí thu con người để đánh giá quy mô lớn.

## Metadata

- Năm: 2026
- Tác giả: Xavier Cadet, Junyan Cheng, Peter Chin, Kyle Richardson
- Category arXiv: cs.SE
- Link PDF: https://arxiv.org/pdf/2610.31709
- Citation count: chưa có (paper mới, Oct 2026)