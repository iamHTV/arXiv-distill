# [2608.25937v2] Candidate supply and answer selection shape the value of LLM judging in multi-agent systems

## Giá trị cốt lõi (1 câu)
Giá trị của LLM judging trong hệ thống đa agent phụ thuộc vào cả hai bên: cung đề xuất (câu đúng có hiện thị, phổ biến hay thiểu số) và quy tắc chọn câu trả lời cuối (kết hợp tần suất bình chọn + xếp hạng judge để cứu câu đúng bị quá số).

## Problem
Prior work chưa giải quyết việc hệ thống đa agent có thể tạo ra câu trả lời đúng nhưng vẫn báo cáo câu sai, vì các nghiên cứu trước thay đổi đồng thời tạo ứng viên, giao tiếp và quy tắc chọn câu cuối — không phân bổ được đọc nào giúp, đọc nào thất bại.

## Contribution
- Khái niệm hóa đa agent tư luận như ống người tiến hóa: tạo ứng viên → giao tiếp đồng đẳng → chọn cuối; consenso không kiểm soát chất lượng có thể biểu hiện drift mimetik (sự trôi chu động theo mô mẫu).
- Nghiên cứu hai câu hỏi: (1) khi nào LLM judge cung cấp áp lực chọn hiệu quả bằng tín hiệu độ chính xác của đáp án cho các ứng viên tạo ra; (2) khi nào dùng tín hiệu đó cải thiện câu trả lời báo cáo.
- Phân tích 15.336 câu hỏi từ MMLU-Pro, GPQA, MedXpertQA, MuSR (Humanity's Last Exam phân tích riêng); replay 81.390 banco ứng viên cố định từ 16.278 câu hỏi trên năm benchmark.
- Ba phát hiện: (1) câu đúng thường đã có mặt trong ứng viên tạo ra nhưng hệ thống vẫn hội tụ và báo cáo câu sai; (2) độ tin cậy của judge không phải tính chất cố định của model, mà thay đổi theo tác đơn, generator và mức độ hiếm của câu trả lời đúng; (3) kết hợp tần suất câu trả lời với xếp hạng judge chỉ thay đổi quy tắc chọn câu cuối và nâng độ chính xác từ 63.82% lên 70.82–70.95%, chủ yếu bằng cách cứu câu đúng bị过 số bởi lỗi phổ biến.

## Method
Ống người tiến hóa 3 giai đoạn: (1) tạo ứng viên: các agent độc lập tạo đáp án ứng viên đa dạng và lý thuyết hỗ trợ; (2) tiến hóa thông tin: giao tiếp đồng đẳng cho phép agent lặp, chấp nhận, sửa đổi hoặc kết hợp lời khai; (3) chọn cuối: hệ thống tổng hợp hoặc lọc ứng viên để tạo đầu ra cuối. Thí nghiệm y khoa trên 7.350 trường hợp chạy mỗi giao thức qua 2.450 câu hỏi tư duy y khoa MedXpertQA dưới 4 giao thức tạo ứng viên và tương tác được kiểm soát. Benchmark xếp hạng ngoài đoạn: mỗi câu hỏi, gọi lại generator nhiều lần tạo banco ứng viên đầy đủ; pgen = tỉ lệ thực nghiệm của ứng viên đúng trong tất cả ứng viên hợp lệ thu thập cho câu hỏi đó. LLM judge xếp hạng ẩn danh các lý thuyết ứng viên (không thấy đáp án hoặc nhãn đúng/sai); đo độ tin cậy xếp hạng bằng rank AUC (xác suất ứng viên đúng được xếp hạng trên ứng viên sai ngẫu nhiên từ cùng banco; 0.5 = ngẫu nhiên). Đánh giá quy tắc chọn câu cuối trên 81.390 banco ứng viên cố định (k=8) từ 16.278 câu hỏi trên năm benchmark. Kết hợp tần suất câu trả lời với xếp hạng judge qua trọng số rank (wi = (k−i)^t); ngưỡng t=2–4 cho độ chính xác 70.82–70.95%; first-ranked selection (t=5) đạt 69.04%.

## KNOWLEDGE — Số liệu & khái niệm
- Single response: 39.88% accuracy tại chi phí 1.00× token.
- Majority voting: 41.06% accuracy tại chi phí 4.96× token.
- Open committee: 42.20% accuracy tại chi phí 10.73× token (+1.14 pp so với majority vote, 95% CI 0.42–1.90).
- Evidence board: 41.89% accuracy tại chi phí 6.07× token (+0.83 pp, 95% CI −0.05–1.74, chứa không khác biệt).
- Khoảng cách tạo–giữ (generation-retention gap): 13.13–14.38 pp (ngưỡng cao vượt quá độ chính xác hệ thống thực tế).
- Khi đáp án phổ biến nhất sai và đáp án đúng ít hơn cũng có mặt: open committee chọn đáp án sai phổ biến nhất 73.25% trường hợp; evidence board 59.61%.
- 90.48–95.37% chạy kết thúc sau 1 vòng trong bốn cấu trúc giao tiếp 5 agent (star, complete, ring, hierarchical); bé buộc 6 vòng hoàn toàn tăng chi phí token lên 33×–49× mà không có tăng độ chính xác nhất quán.
- Judge rank AUC half-rise midpoint: pgen = 14.7% (95% CI 14.3–15.1%, R²=0.900) trên 15.336 câu hỏi/4 benchmark; fixed 2C/6W: 12.2% (95% CI 11.8–12.6%, R²=0.887); HLE MC: 28.6%; HLE open QA: 36.9%.
- Majority voting (t=0): 63.82% accuracy trên 81.390 banco k=8.
- Unguided single-candidate sampling: 42.53%; shuffled-rank control: 42.47%.
- Hybrid selection (t=2–4): 70.82–70.95% (+7.00–7.13 pp so với majority vote).
- First-ranked selection (t=5): 69.04% (+5.22 pp, 95% CI 4.85–5.59).
- Lợi ích first-ranked so với majority theo benchmark: MMLU-Pro +4.3, GPQA +5.9, MedXpertQA +7.9, HLE MC +4.7, MuSR +10.6.
- Theo mức độ sẵn có câu đúng pgen: hiếm (0–0.125): +6.02 pp (95% CI 5.31–6.79, n=2.407); trung bình (0.125–0.625): +7.87 pp (95% CI 7.30–8.42, n=10.269); phổ biến (>0.625): −3.22 pp (bình chọn đã đáng tin cậy).
- Mức câu hỏi: first-ranked cao hơn trong 54.5% và thấp hơn trong 24.5% câu hỏi khi đáp án đúng có mặt nhưng ít phổ biến; trong câu hỏi đa số-correct, majority vote cao hơn trong 17.6% so với 8.7% first-ranked.
- Kích thước banco k=2: first-ranked vượt majority 13.52 pp (95% CI 12.75–14.27); k=14: +0.75 pp (CI chứa không); k=16: −0.34 pp (CI −1.15–0.44).
- Chi phí đánh giá judge: US$0.10–0.39 trên 1.000 câu trả lời đúng bổ sung ở k=2–6; US$6.28 ở k=14; không xác định kinh tế ở k=16.
- Banco thiểu số đúng nhỏ (ppool < 0.25): judge vượt majority +40.1 pp ở k=6 và +20.8 pp ở k=16; banco nhiều đúng (ppool ≥ 0.25): majority vượt judge −4.0 pp ở k=6 và −8.2 pp ở k=16.
- Danh mục arXiv: cs.AI

## INSIGHT — Cơ chế & tại sao
[Hệ thống tạo câu đúng nhưng báo cáo câu sai] VÌ [drift mimetik và majority-biased cascade làm câu sai phổ biến áp đảo đáp án đúng ít phổ biến, tạo bottleneck tạo–giữ sau khi tạo]. Điều này nghĩa là [cần áp lực chọn độc lập với độ phổ biến để bảo toàn đáp án đúng thiểu số].
[Độ tin cậy judge thay đổi theo tác đơn/generator/mức hiếm câu đúng] VÌ [khi đáp án đúng hiếm, lý thuyết sai hợp lý có thể thống trị so sánh judge (rank AUC dưới 0.5 ở nhóm khả dụng thấp nhất); judge không phải tính chất cố định của model]. Điều này nghĩa là [độ tin cậy judge phải được đánh giá trong régimen cụ thể mà nó vận hành, không dùng điểm benchmark tĩnh làm bảo đảm toàn cầu].
[Kết hợp tần suất bình chọn + xếp hạng judge nâng độ chính xác 63.82% → 70.82–70.95%] VÌ [tần suất bắt lấy hỗ trợ lặp lại qua các đường đi độc lập; judge ranking có thể nâng đáp án đúng bị quá số bởi lỗi phổ biến]. Điều này nghĩa là [trọng số rank trung quy kết hợp độ ổn định thống kê của tổng hợp với sự sửa chữa nhạy với nội dung cho lỗi phổ biến].

## IDEA — Áp dụng được gì
Áp dụng kết hợp tần suất bình chọn + xếp hạng LLM judge vào hệ thống đa agent doanh nghiệp: bước đầu là dùng bình chọn đa số làm bước đầu, rồi dùng LLM judge xếp hạng các ứng viên ứng viên, kết hợp cả hai để chọn đáp án cuối (trọng số rank t=2–4).
Đánh giá độ tin cậy của judge trong régime cụ thể trước khi triển khai: bước đầu là đo rank ASEAN theo mức độ sẵn có đáp án đúng (pgen) trong banco ứng viên thực tế, không dùng điểm benchmark tĩnh.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Giá trị của việc tạo thêm ứng viên phụ thuộc vào liệu các mẫu mới làm đáp án đúng hiện diện, phổ biến đủ cho bình chọn hay để lại một thiểu số mà judge có thể nhận biết. Judge không phải luôn hữu ích: khi đáp án đúng chiếm đa số, bình chọn đã đủ tốt và judge thậm chí làm giảm độ chính xác.

## Assumptions & Limitations
- Điều kiện đúng: tác vụ suy luận có đáp án chuẩn xác định trước, banco ứng viên cố định, LLM judge có thể xếp hạng lý thuyết ẩn danh.
- Limitation paper thừa nhận: kết quả trên các hệ thống được nghiên cứu (nhiều agent, giao thức cụ thể); judge reliability thay đổi theo generator, tác đơn và نطاق khả dụng đáp án đúng; first-ranked selection làm giảm độ chính xác khi đáp án đúng chiếm đa số (>0.625).
- Limitation paper KHÔNG nói: chi phí vận hành LLM judge tại quy mô lớn hàng ngày; tính ổn định của rank AUC qua nhiều phiên bản model; tác động lên độ trễ khi gọi judge cho mỗi banco ứng viên.

## Metadata
- Năm: 2026
- Tác giả: Jia-Hao Ji, Sijie Li, Jiabei Cheng, Zixi She, Jin-Tai Yu, Zhiyuan Yuan (Fudan University)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2608.25937v2
- arXiv ID: 2608.25937v2
- Nhãn: [applied]
- Skill: candidate-supply-answer-selection | Test: [SKILL VALID]
