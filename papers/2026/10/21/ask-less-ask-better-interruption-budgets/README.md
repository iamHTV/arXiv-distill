# [2610.24411v1] Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets

## Giá trị cốt lõi (1 câu)
Một giao thức đánh giá tách biệt bao nhiêu lần agent hỏi (interruption budget) từ chất lượng câu hỏi (user-attention cost): giới hạn 1–3 câu hỏi cắt chi phí chú ý người dùng 36–73% còn giữ 86–94% phần thưởng tác vụ, và memory-guided review cắt thêm 13% chi phí với mất phần thưởng tối thiểu.

## Problem
Các đánh giá agent LLM chủ động hiện tại thường đo gánh nặng người dùng bằng cách đếm số câu hỏi, coi các câu hỏi cần thiết và có thể tránh đều nhau. Nhưng trả lời mỗi câu hỏi đòi hỏi thời gian và nỗ lực của người dùng, và chú ý là hiếm có — lợi ích của việc hỏi phải được cân đối với chi phí gián đoạn.

## Contribution
1. Một giao thức đánh giá phân biệt tần suất hỏi (interruption budget) từ chất lượng hỏi (user-attention cost), với ngân sách giới hạn số câu hỏi và chi phí chú ý người dùng tính thêm cho câu hỏi khó đọc hoặc không đáng hỏi.
2. Một chỉ số chi phí chú ý người dùng (user-attention cost) được xác thực bởi con người: trên các cặp cuộc trò chuyện có cùng số câu hỏi, thẩm phán người dùng đồng ý với chi phí về cuộc trò chuyện nào tốn công hơn 75% thời gian.
3. Một agent memory-guided review (MGR) kiểm tra mỗi câu hỏi được đề xuất đối với bộ nhớ持久 của câu trả lời trước của người dùng và bằng chứng tác vụ, cắt chi phí chú ý thêm 13% tại cùng ngân sách với mất phần thưởng tối thiểu.
4. Đánh giá trên 8 LLM và 4 miền dịch vụ khách hàng, cho thấy các mô hình khác nhau mạnh mẽ về hiệu quả hỏi: tại cùng chi phí chú ý, các mô hình hiệu quả nhất đạt gấp hơn hai lần phần thưởng từ câu hỏi của các mô hình khác.

## Method
Giao thức đánh giá dùng interruption budget để giới hạn số câu hỏi mỗi tác vụ, và user-attention cost để đo mức độ đòi hỏi và sự hợp lý của mỗi yêu cầu. Một câu hỏi là discretionary request sau yêu cầu ban đầu (làm rõ, xác nhận, yêu cầu đáp lại gợi ý); các giao dịch bắt buộc bởi chính sách môi trường (xác thực, xác nhận bắt buộc) được miễn trừ. Chi phí chú ý người dùng: Afull(τ) = Σ(1 + κeff·e(q) + κval·w(q)), với κeff = κval = 1, mỗi yêu cầu tốn 1–3 đơn vị. Reading effort: thẩm phán LLM đánh giá trên 5 chiều (mục tiêu rõ ràng, yêu cầu đơn lẻ, nỗ lực trả lời, khả năng hành động, tính súc tích), điểm r(q) ∈ [0,20], e(q) = 1 − r(q)/20. Question value: v(q) ∈ [0,10] theo 4 tiêu chí (câu trả lời không có trong nhật ký, không thể tìm bằng công cụ, cần cho tác vụ, do người dùng cung cấp), w(q) = 1 − v(q)/10. Tiện ích: Uλ(τ) = R(τ) − λAfull(τ), λ = 0.03. Agent memory-guided review (MGR): backbone LLM đề xuất bước, LLM classifier định tuyến, self-review kiểm tra câu hỏi đối với bộ nhớ持久 M = (P, s, I) và trả về APPROVE/SUBSTITUTE/BLOCK. Bộ nhớ持久 lưu bản ghi người dùng lời giải văn bản, tóm tắt tác vụ s và liên kết bằng chứng I.

## KNOWLEDGE — Số liệu & khái niệm
- 4 miền dịch vụ khách hàng (retail, airline, telecom từ τ-bench/τ²-bench; Ambiguous WebShop), 382 tác vụ kiểm tra dịch vụ khách hàng, 559 tác vụ nghiên cứu tương tác
- 8 mô hình: GPT-6-Astra, GPT-5.4, GPT-4.1, Grok-4.6, Grok-4.3, GPT-OSS-120B, Llama-4-Maverick, Llama-3.3-70B
- 3 lần thử mỗi mô hình
- Không giới hạn (Unrestricted): hỏi 2.84 câu/phiên, chi phí 49.4, phần thưởng 29.5
- Budgeted (N=1–3): chi phí 44.7, phần thưởng 30.7, giá trị câu hỏi 69.4
- Budgeted + MGR: chi phí 43.9, phần thưởng 30.7, giá trị câu hỏi 71.7
- Ngân sách 1–3 câu hỏi cắt chi phí chú ý 36–73% so với không giới hạn, giữ 86–94% phần thưởng tác vụ
- Chỉ giữ 49–80% phần thưởng thêm từ việc hỏi
- Tại cùng ngân sách, MGR cắt chi phí chú ý thêm 13% với mất phần thưởng tối thiểu
- GPT-6-Astra và Grok-4.6 là các mô hình hỏi hiệu quả nhất: 7.3–7.8 điểm phần thưởng mỗi đơn vị chi phí (gấp hơn hai lần bất kỳ mô hình khác, tối đa 3.3)
- Tần suất hỏi không dự báo hiệu quả: trên Telecom không giới hạn, GPT-4.1 hỏi 5.7 câu cho 5.5 điểm phần thưởng, GPT-6-Astra hỏi 1.6 cho 31.9 điểm
- MGR cắt chi phí cho 7/8 mô hình và nâng giá trị câu hỏi cho 6, nhưng tăng phần thưởng tại cùng chi phí chỉ được hỗ trợ cho Grok-4.6 và Llama-3.3
- Nghiên cứu tương tác (5 mô hình, N=1–8): ngân sách cắt chỉ 15.6% chi phí với mất 3.1 điểm phần thưởng, MGR cắt thêm 5.4% với mất thêm 0.9 điểm
- Nghiên cứu con người: tại cùng số câu hỏi, thẩm phán phán cuộc trò chuyện chi phí cao hơn mệt mỏi hơn trong 75% câu trả lời không hòa; chi phí đồng ý với thẩm phán trên 90% so sánh giữ vữ
- Giá trị ngưỡng đá vỡ λ∗ ≈ 0.02: người dùng hy sinh hơn 2 điểm phần thưởng để tránh 1 đơn vị chi phí thì ngân sách tốt hơn
- Self-review và bảo trì bộ nhớ thêm trung bình 1.8 cuộc gọi mô hình và khoảng 15k token/phiên

## INSIGHT — Cơ chế & tại sao
[Hỏi ít và hỏi tốt là hai mục tiêu khác nhau] VÌ [ngân sách kiểm soát tần suất hỏi nhưng không kiểm soát câu hỏi nào được hỏi; một agent có thể hỏi ít nhưng hỏi các câu không đáng hỏi, hoặc hỏi nhiều nhưng hỏi các câu có giá trị cao]. Điều này nghĩa là [đánh giá agent chủ động phải đo cả hai].
[Chi phí chú ý người dùng bắt nửa nỗ lực cảm nhận mà số câu hỏi bỏ lỡ] VÌ [tại cùng số câu hỏi, các cuộc trò chuyện có câu hỏi không đáng hỏi cảm thấy mệt mỏi hơn; thẩm phán đồng ý chi phí cao hơn = cuộc trò chuyện tốn công hơn 75%]. Điều này nghĩa là [độ dài câu hỏi không phải là chỉ số tốt cho gánh nặng tổng thể — câu hỏi không đáng hỏi, không phải câu hỏi dài, khiến cuộc trò chuyện mệt mỏi].
[Bộ nhớ持久 là yếu tố then chốt để review chọn lọc] VÌ [không có bộ nhớ, review降低 cả phần thưởng và giá trị câu hỏi ở cùng chi phí; với bộ nhớ, chi phí giảm 6.2% và tăng 2.9 điểm giá trị tại cùng N]. Điều này nghĩa là [agent cần biết người dùng đã nói gì trước đó để tránh hỏi lại].
[Ngân sách cao nhất tuân theo hiệu quả hỏi] VÌ [các mô hình hỏi hiệu quả nhất nên được phép hỏi nhiều câu hơn; tại λ=0.03, 3 mô hình hỏi hiệu quả nhất đạt tốt nhất với 2–3 câu, 5 mô hình còn lại với 1 câu]. Điều này nghĩa là [ngân sách nên được tùy chỉnh theo mô hình, không phải một mức dùng chung].

## IDEA — Áp dụng được gì
1. Áp dụng [interruption budget] vào [giới hạn số câu hỏi làm rõ của agent hỗ trợ khách hàng]: bước đầu là thiết lập ngân sách 1–3 câu hỏi mỗi phiên, từ chối các yêu cầu sh�� đoán thêm khi ngân sách đã hết.
2. Áp dụng [user-attention cost] vào [đánh giá chất lượng câu hỏi của agent]: bước đầu là dùng LLM judge đánh giá đọc nỗ lực và giá trị câu hỏi, tính tổng chi phí cho mỗi phiên, so sánh các agent tại cùng chi phí thay vì cùng số câu hỏi.
3. Áp dụng [memory-guided review] vào [lọc câu hỏi không đáng hỏi]: bước đầu là xây dựng bộ nhớ持久 lưu câu trả lời trước của người dùng và bằng chứng tác vụ, trước khi đưa câu hỏi ra kiểm tra xem câu trả lời đã có trong bộ nhớ hay có thể tìm bằng công cụ hay không.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Số lần hỏi không phải là척ước đo tốt cho gánh nặng người dùng — cần đo cả tần suất và chất lượng câu hỏi. Áp dụng khi: đánh giá agent主 động hỏi người dùng trong dịch vụ khách hàng. Không áp dụng khi: chỉ cần đếm số tương tác đơn giản.
2. Nguyên tắc: Bộ nhớ持久 về câu trả lời trước của người dùng là điều kiện tiên quyết để agent tránh hỏi lại và hỏi câu tốt hơn. Áp dụng khi: xây dựng agent hỏi người dùng trong nhiều lượt trò chuyện. Không áp dụng khi: tác vụ chỉ một lượt, không có ngữ cảnh trước đó.

## Assumptions & Limitations
- Điều kiện phải đúng: có mô phỏng người dùng tiết lộ sở thích chỉ khi được hỏi, có công cụ để agent tìm kiếm thông tin, có LLM judge để đánh giá đọc nỗ lực và giá trị câu hỏi.
- Limitation paper thừa nhận: nghiên cứu tương tác cắt chỉ 15.6% chi phí với mất 3.1 điểm phần thưởng, MGR cắt thêm 5.4% với mất thêm 0.9 điểm, không cải thiện tiện ích so với không giới hạn tại λ=0.03; kết quả phụ thuộc vào mức độ thẳng thắn của người dùng mô phỏng.
- Limitation paper KHÔNG nói: không có chi phí inference thực tế của self-review và bộ nhớ (trước đây ước tính 1.8 cuộc gọi mô hình + 15k token/phiên); không đánh giá trên các tác vụ ngoài dịch vụ khách hàng và nghiên cứu tương tác; không so sánh trực tiếp với các agent không hỏi.

## Metadata
- Năm: 2026
- Tác giả: Xuanming Zhang, Amir H. Rezaeian, Miguel Ballesteros, Weiyi Sun, Werner Geyer, Lydia B. Chilton, Zhou Yu, Yassine Benajiba, Dan Roth (Columbia University, Oracle AI)
- Category arXiv: cs.CL
- Link PDF: https://arxiv.org/pdf/2610.24411
- arXiv ID: 2610.24411v1
- Nhãn: [applied]
- Citation count: [không tìm được]