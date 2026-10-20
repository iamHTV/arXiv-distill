# [2610.24873v1] The One-Pixel of Reasoning: One Truthful Relation Is Enough to Mislead LLM Agents

## Giá trị cốt lõi (1 câu)
Một câu chân nguyên duy nhất, đích đến một liên kết ngầm (implicit warrant) giữa bằng chứng và kết luận, có thể lật ngược niềm tin của agent: tấn công one-relation (ORA) đạt ASR 54.9% (proprietary) và 80.0% (open-weight) trên 18 mô hình, và tranh luận đa agent làm tăng lỗi nhóm từ 50.0% lên 59.5%.

## Problem
Prior work tấn công LLM qua hướng dẫn (prompt injection, jailbreak, indirect injection) hoặc nhiễm training data, để mặt phẳng suy luận (inferential relation) — liên kết ngầm giữa bằng chứng và kết luận — không được phòng vệ. Agent phán đoán xem một khai bố có thật và xem nó có enough để thay đổi kết luận, nhưng chỉ để ý đến cái thứ nhất.

## Contribution
1. Trình bày one-relation attack (ORA), một tấn công nhận thức mới đích đến liên kết suy luận ngầm (implicit warrant) giữa bằng chứng và kết luận, dùng một câu chân nguyên duy nhất để định hướng agent sang niềm tin sai.
2. Xây dựng ORA theo năm giai đoạn: xây dựng đồ thị đối số, định vị liên kết quan trọng, sinh undercutter chân nguyên, kiểm tra ứng viên, chọn và phát hành một câu.
3. Thử nghiệm rộng trên 18 mục tiêu trong hai miền thực tế (phân tích y khoa PubMedQA, phát hiện lỗ hổng PrimeVul), cho thấy kháng appointed cao, lỗi tự tin, tấn công qua kiểm tra nguồn hỗ trợ và tránh được xác định, và tranh luận đa agent làm tăng lỗi nhóm.
4. Điều khiển qua matched controls tách biệt vai trò của việc định vị (targeting) và định vị (qualification).

## Method
ORA hoạt động trên hai giả định: (i) victim nhận câu hỏi q và bằng chứng E, trả lời niềm tin fv(q, E; ξ) và mức tin cậy pv; (ii) attacker thêm câu δ vào E, giữ nguyên bằng chứng gốc. Một liên kết suy luận ngầm được tái cấu trúc thành warrant w: g(w) ⇒ c(w) (căn cứ g(w) ⇒ 주장 c(w)). Attacker sinh câu δ điều chỉnh tính áp dụng hoặc đủ của liên kết này (undercutter), không khẳng định主張 đối lập. Năm giai đoạn: (1) xây dựng đồ thị đối số từ (q, E), ghi lại 주장, căn cứ, sức mạnh lưu lự, bại relevant Def(w), và chỉ số mang câu trả lời a(w); (2) định vị liên kết quan trọng bằng RS(w) = L(w){λUinst + (1−λ)D(w)}, trong đó L(w) là trọng số mang câu trả lời, D(w) là điểm bại relevant; (3) sinh undercutter chân nguyên C = (δ1…δnc), nc ≤ K, điều kiện trên w⋆, căn cứ, toàn bộ nguồn, và y⋆; (4) kiểm tra ứng viên bằng kiểm tra từ vựng (cánh cảnh thực thể/số/lạ, mã token) và kiểm tra hỗ trợ ngữ nghĩa sau khi phát hành; (5) chọn và phát hành: query mode dùng phản hồi victim để phát hành ứng viên đầu tiên tạo BLv = 1 trong ngân sách, zero-query mode dùng attacker để đánh giá hỗ trợ nguồn, sự khéo léo, và mức gây lừa dự kiến, chọn một câu mà không cần phản hồi victim.

## KNOWLEDGE — Số liệu & khái niệm
- 18 mục tiêu: GPT-4.1 (nano/mini/full), GPT-5.4 (nano/mini/full), GPT-5.6 (luna/terra), Qwen2.5 (7B/14B/32B), DeepSeek-R1 (7B/14B/32B), Phi-4 (mini/mini-R/full/R)
- 1000 inputs mỗi miền: PubMedQA (y khoa), PrimeVul (phát hiện lỗ hổng, cân bằng lỗ hổng/an toàn)
- Attacker: GPT-5.6-LUNA (Luna)
- ASR (best-of-10): proprietary 54.9%, open-weight 80.0% trung bình trên hai miền
- Medical ASR: GPT-5.6-terra 47.6% (gần nửa câu trả lời đúng ban đầu bị lật ngược)
- Cyber ASR: DeepSeek-R1 92.5%/98.9%/99.3%, Qwen2.5 92.4%/90.0%/97.2%, Phi-4-R 91.7%/89.1%/93.1%
- Mô hình lý trí (reasoning-oriented) dễ bị tấn công hơn: DeepSeek-R1 cao hơn Qwen2.5 20.8–28.0 điểm phần trăm; Phi reasoning variants cải thiện độ chính xác sạch nhưng dễ bị tấn công hơn
- Transfer không phản hồi victim: zero-query attacks vẫn hiệu quả trên cả hai nhóm trong cả hai miền
- Kiểm tra nguồn hỗ trợ: 83.1% tấn công y khoa query thành công qua kiểm tra hỗ trợ KHÔNG xác định được; 90.9% Cyber
- Multi-agent debate: lỗi nhóm tăng từ 50.0% lên 59.5%; chuyển tiếp đúng→sai xảy ra 5 lần thường xuyên hơn là phục hồi sai→đúng
- Ablation (Table 5): ORA 55.0% Medical / 37.0% Cyber / 46.0% Combined; Random warrant 27.0/21.0/24.0; Random content 11.0/28.0/19.5 (độ tin cậy belief: ORA +0.076/+0.256/+0.424, Random warrant +0.439/+0.541/+0.424)
- Ngân sách truy vấn K=10: ASR proprietary y khoa tăng 39.2 điểm phần trăm so với K=1
- Ngưỡng đảo ngược đơn liên kết (Proposition 1): Cw = ηw max[dyw]+/γy > 1 là điều kiện cần và đủ để đảo ngược
- Mức tin cậy: HC-Conf (tỷ lệ lật ngược với p ≥ 0.8) phân biệt sự ngần ngại từ lỗi quyết định

## INSIGHT — Cơ chế & tại sao
[Một câu đích đến liên kết ngầm có thể lật ngược niềm tin agent] VÌ [agent phán đoán xem một khai bố có thật và xem nó có đủ để thay đổi kết luận, nhưng ORA chỉ thao túng cái thứ hai — liên kết suy luận ngầm — bằng cách định vị một liên kết quan trọng và sinh một câu điều chỉnh tính áp dụng/đủ của nó]. Điều này nghĩa là [bằng chứng gốc vẫn nguyên vẹn, chỉ việc diễn giải nó bị thay đổi].
[Mô hình lý trí dễ bị tấn công hơn] VÌ [huấn luyện lý trí cải thiện độ chính xác tác vụ sạch nhưng không tăng khả năng chống lại việc diễn giải lại mục tiêu của bằng chứng; cả độ chính xác y khoa cao hơn và dễ bị tấn công hơn cùng tồn tại]. Điều này nghĩa là [kháng appointed không đi theo quy mô hay khả năng lý trí].
[Tấn công qua kiểm tra hỗ trợ nguồn và tránh xác định] VÌ [câu undercutter là chân nguyên (nguồn gốc hỗ trợ) và không khẳng định verdict đối lập, nên bộ kiểm tra thực sự không thể phân biệt nó từ báo cáo breaking thật]. Điều này nghĩa là [phân tích sự thật đơn lẻ không đủ — cần xác thực nguồn gốc và liên kết suy luận].
[Tranh luận đa agent làm tăng lỗi nhóm] VÌ [tất cả các agent nhìn thấy câu đã inject, sự đồng thuận đồng minh cưỡng hóa cùng một diễn giải mà không cung cấp căn cứ độc lập]. Điều này nghĩa là [thêm góc nhìn không bằng thêm bằng chứng; tranh luận đảo ngược quyết định đúng nhiều lần hơn là sửa sai].

## IDEA — Áp dụng được gì
1. Áp dụng [phân tích liên kết ngầm] vào [đánh giá rủi ro của agent sử dụng bằng chứng truy xuất]: bước đầu là xác định các liên kết suy luận ngầm quan trọng trong pipeline agent và kiểm tra xem một câu điều chỉnh có thể đảo ngược kết luận hay không.
2. Áp dụng [matched controls (random warrant / random content)] vào [kiểm tra xem tấn công đến từ việc định vị hay nội dung]: bước đầu là so sánh tấn công đích đến với hai bộ điều khiển: undercutter chuyển sang liên kết không mang câu trả lời và nội dung trung lập nghỉ ngơi tại cùng căn cứ.
3. Áp dụng [zero-query selection] vào [xây dựng tấn công truyền tải không cần phản hồi victim]: bước đầu là attacker tự đánh giá hỗ trợ nguồn, sự khéo léo, và mức gây lừa dự kiến, chọn một câu mà không cần quan sát phản hồi của victim.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Liên kết suy luận ngầm (implicit warrant) giữa bằng chứng và kết luận là một bề mặt tấn công nhận thức độc lập so với sự thật của bằng chứng. Áp dụng khi: đánh giá độ tin cậy của agent trong lĩnh vực rủi ro cao (y khoa, bảo mật, pháp lý). Không áp dụng khi: chỉ kiểm tra sự thật của các bằng chứng đầu vào.
2. Nguyên tắc: Tranh luận đa agent không tự động khắc phục lỗi — nó có thể cường hóa cùng một diễn giải sai. Áp dụng khi: thiết kế hệ thống đa agent cho quyết định quan trọng. Không áp dụng khi: coi tranh luận đa agent là defense đủ điều kiện mà không có phản hồi bên ngoài.

## Assumptions & Limitations
- Điều kiện phải đúng: attacker biết (q, E, y⋆) nhưng không biết tham số victim, gradient, hoặc suy luận ẩn; victim đánh giá trên tập đúng ban đầu Dv = {(q, E) : ˆyv,0 = y⋆}.
- Limitation paper thừa nhận: công việc tập trung vào mối quan hệ đơn liên kết; mở rộng đa liên kết ở phụ lục Q; không đánh giá trên các tác vụ ngoài phân tích y khoa và phát hiện lỗ hổng.
- Limitation paper KHÔNG nói: không có chi phí suy luận thực tế của tấn công; không so sánh với các phương pháp tấn công khác ngoài các điều khiển ngẫu nhiên; không đánh giá defense thực tế ngoài kiểm tra nguồn hỗ trợ.

## Metadata
- Năm: 2026
- Tác giả: Jinwei Hu, Youcheng Sun, Yi Dong, Xiaowei Huang (University of Liverpool, MBZUAI)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.24873
- arXiv ID: 2610.24873v1
- Nhãn: [applied]
- Citation count: [không tìm được]