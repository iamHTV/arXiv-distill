# [2610.25461v1] Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations

## Giá trị cốt lõi (1 câu)
Một sales agent được fine-tuned trên 4,6 triệu cuộc hội thoại thương mại thật tăng revenue per visitor +10.0% so với không có agent, và vượt mô hình frontier cùng scaffolding +21.6% engaged conversion, với chi phí chỉ 1.8% so với nhân viên bán hàng người.

## Problem
Prior work chưa kiểm tra xem một sales agent trained trên cuộc hội thoại thương mại thật có tăng doanh số trên live traffic hay không — các benchmark hiện tại dùng khách giả tạo (simulator) có thể reorder leaderboard (correlation chỉ r=0.24 giữa hai simulator trên SalesLLM), và các thí nghiệm field trước đây predates current models hoặc chỉ đo lường hỗ trợ nhân viên, không phải bán hàng độc lập.

## Contribution
1. Một giao thức đánh giá 4 nghiên cứu liên kết điểm benchmark offline với kết quả revenue ngẫu nhiên trên live traffic.
2. Một dozen 100 trang web đồng ý tham gia trong 14 ngành, mỗi ngành có metric chính xác định trước.
3. So sánh cách ly mô hình: Javo vs mô hình frontier bên trong cùng một scaffolding (giao diện, retrieval, catalog tools, system prompt, guardrails), nên bất kỳ chênh lệch nào đều gán cho trọng số mô hình.
4. So sánh ngẫu nhiên với mỗi trang web's nhân viên chatlive, kèm chi phí, độ trễ và CSAT bên cạnh conversion.

## Method
Javo là mô hình mở trọng số (Qwen3-32B) được fine-tuned trên toàn bộ cuộc hội thoại thương mại: SFT trên 1,65 triệu ví dụ (2 epochs) để họcelicitation, recommendation, objection handling, next-step proposals trong ngữ cảnh; sau đó preference optimization trên 190,000 cặp lượt bán tại cùng trạng thái hội thoại, với lượt ưu tiên dẫn đến tiến độ (ý định mua, đặt hàng, lead) và lượt không ưu tiên dẫn đến stall hoặc exit. Một phần dữ liệu thứ dạy ràng buộc: không giảm giá hoặc điều khoản ngoài chính sách trang web, không yêu cầu ngoài catalog, khai báo AI khi được hỏi, chuyển giao người khi được yêu cầu. Tất cả các agent arm chạy trong cùng một scaffold (widget, retrieval catalog, tools, prompt, guardrails, ngân sách trễ 8 giây), chỉ khác trọng số mô hình. Ba nghiên cứu field dùng ngẫu nhiên hóa khách trên 100 trang web (1 tháng 5 đến 30 tháng 9 2026, 14,8 triệu khách duy nhất), mỗi khách được gán cố định cho một arm trong suốt nghiên cứu.

## KNOWLEDGE — Số liệu & khái niệm
- Corpus đào tạo: 4,6 triệu cuộc hội thoại (sau khi lọc), 58,4 triệu lượt (median 10 lượt/cuộc hội thoại), tiếng Anh 68%, Pháp 16%, Tây Ban Nha 8%, khác 8%, thu thập tháng 2/2024 đến tháng 3/2026, kết thúc trước ngày 1 tháng 5 2026; 17,4% có nhãn kết quả đã присоединя؛ tỷ lệ PII còn lại trên mẫu kiểm tra 2,500: 0.16%
- Training settings: base model Qwen3-32B; SFT 1,65 triệu ví dụ / 2 epochs; preference pairs 190,000; constraint examples 34,000; 32 H100 GPUs, 2,240 GPU-hours; phiên bản đồng hồ javo-v1, đóng băng ngày 24 tháng 4 2026
- Study 1 (SalesLLM-EN, CustomerLM): Javo 7.01 (95% CI 6.87–7.15), best frontier 6.21, S1a ngưỡng 6.33; Javo base model 5.73; Javo SFT only 6.51; Javo không dữ liệu ràng buộc 7.13; người bán 1–3 năm kinh nghiệm 6.13; người bán 5+ năm 6.88
- SmartSalesBench: Javo 0.79 vs best frontier 0.69
- τ-bench retail pass1: Javo 73.0%, best frontier 73.0% (guardrail held)
- Study 2 (vs không agent): RPV +10.0% (95% CI +5.1 đến +14.9); conversion +8.0% (+4.1 đến +11.9); engagement-scaled RPV illustration +123.9%
- Study 3 (vs agent frontier GPT-5.2, cùng scaffolding): engaged conversion +21.6% (+16.9 đến +26.3); ITT RPV +16.9% (+11.2 đến +22.6)
- Study 4 (vs nhân viên live chat): engaged conversion +0.5% (−5.0 đến +6.0), non-inferior (margin −7%, one-sided p=0.004), không có sự vượt trội đáng kể; CSAT Javo 4.42 vs người 4.43
- Chi phí mỗi cuộc trò chuyện tham gia: Javo $0.06, frontier $0.14, người $3.40 (Javo = 1.8% chi phí của người)
- Guardrails (tất cả held): tỷ lệ trả hàng 4.0% vs không agent 4.1% (ngưỡng ≤ +0.5 pp); tỷ lệ hủy 11.9% vs 12.2%; phàn nàn mỗi 1.000 khách 0.18 vs 0.20; yêu cầu không đượcSupported 0.15% vs frontier 0.56% (ngưỡng ≤ 1.0%); 제안 không được phép 0 vs frontier 3 (không dung nhận); chiến thuật áp lực cấm 0.01% vs frontier 0.05% (ngưỡng ≤ 0.1%)
- Sales behaviors (chia tỷ lệ cuộc trò chuyện tham gia): needs elicited trước recommendation đầu tiên Javo 82% vs frontier 61% vs người 81%; recommendation gắn với nhu cầu đã nêu Javo 78% vs 58% vs 72%; objection được giải quyết Javo 60% vs 39% vs 57%; next step cụ thể Javo 88% vs 68% vs 78%; median số tin nhắn mỗi cuộc trò chuyện Javo 8 vs frontier 6 vs người 9

## INSIGHT — Cơ chế & tại sao
[Đào tạo trên toàn bộ cuộc hội thoại thương mại] xảy ra VÌ [mô hình học cách xử lý nhu cầu, kháng cự và next-step trong ngữ cảnh đa lượt thay vì trả lời từ prompt đơn lẻ]. Điều này nghĩa là [dữ liệu cuộc hội thoại thật, không phải quy mô mô hình đơn độc, quyết định mức độ tốt một agent bán hàng].
[Khi scaffolding được giữ cố định, mô hình được đào tạo trên cuộc hội thoại thương mại outsell mô hình frontier] VÌ [agent frontier hành như passive question-answering bot thay vì người bán hàng chủ động, trong khi Javo được học từ các phiênところで khách bày nhu cầu, do dự, kháng cự, so sánh và sau đó mua hoặc không mua]. Điều này nghĩa là [scaffolding tốt không thay được dữ liệu domain-specific].
[Javo non-inferior so với nhân viên bán hàng tại 1.8% chi phí] VÌ [agent không mệt mỏi, không cần lương, trả lời ngay lập tức và chi phí inference thấp, trong khi vẫn đạt conversion tương đương]. Điều này nghĩa là [chi phí là lợi thế cạnh tranh chính của AI sales agent, không chỉ chất lượng cuộc trò chuyện].

## IDEA — Áp dụng được gì
1. Áp dụng [đào tạo fine-tuned trên transcript cuộc hội thoại bán hàng thật] vào [xây dựng sales agent cho trang web tienda online]: bước đầu là thu thập và de-identify 10,000+ cuộc trò chuyện chatlive cũ của trang web, gán nhãn kết quả (mua/hủy/lead), sau đó SFT mô hình mở trọng số (ví dụ Qwen3-32B) trên corpus này trước khi deploy.
2. Áp dụng [so sánh agent với mô hình frontier bên trong cùng scaffolding] vào [kiểm tra xem việc fine-tuned có giá trị hay không]: bước đầu là triển khai hai agent (mô hình đã tinh chỉnh vs mô hình frontier) với cùng widget, catalog retrieval, tools và system prompt trên 10% traffic, đo engaged conversion và RPV trong 2–4 tuần.
3. Áp dụng [chi phí 1.8% so với nhân viên bán hàng] vào [thay thế hoặc hỗ trợ live chat ngoại giờ làm việc]: bước đầu là định cấu hình agent để xử lý mọi tin nhắn ngoài giờ làm việc, chuyển giao sang người khi khách yêu cầu, theo dõi CSAT và conversion rate hàng tuần.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Dữ liệu cuộc hội thoại domain-specific quan trọng hơn quy mô mô hình cho tác vụ bán hàng có mục tiêu rõ ràng. Áp dụng khi: xây dựng agent chuyênresa (bán hàng, tư vấn, hỗ trợ) với transcript lịch sử có sẵn. Không áp dụng khi: tác vụ là general Q&A không có kết quả kinh doanh đo lường được.
2. Nguyên tắc: So sánh agent phải giữ mọi thứ khác nhau không đổi (scaffolding, prompt, tools) và chỉ thay trọng số mô hình, nếu không không thể biết sự cải thiện đến từ đâu. Áp dụng khi: đánh giá bất kỳ mô hình tinh chỉnh mới. Không áp dụng khi: chỉ muốn demo marketing nhanh.

## Assumptions & Limitations
- Điều kiện phải đúng: trang web có ít nhất 20,000 phiên/tháng, có sự kiện đặt hàng/đặt chỗ/lead có thể liên kết với ID khách, có catalog hoặc kho hàng có thể đọc được bằng máy, không có AI sales agent đang chạy, có sự đồng ý viết từ chủ sở hữu; khách ở các trang web tài chính chỉ ở chế độ chụp lead.
- Limitation paper thừa nhận: các trang web không phải mẫu ngẫu nhiên của web (nhiều trang thông qua mạng lưới khách/đại lý của tác giả); kết quả có thể nhỏ hơn đối với mua hàng ít cân nhắc xét; phiên bản frontier được đóng băng tháng 4/2026 có thể bị phiên bản sau vượt qua; Study 4 confound giữa khai báo AI và kỹ năng người bán; nhân viên là típ không phải tốt nhất; ngang 5 tháng không đo LTV, mua lại hoặc hiệu ứng thương hiệu; interference trên trang web có hạn chế tồn kho; Study 1 phụ thuộc vào khách giả tạo; kết quả có thể không chuyển sang ngôn ngữ ít được biểu diễn trong corpus; không nghiên cứu buyer-side agents.
- Limitation paper KHÔNG nói: không có đánh giá độc lập của thống kê (tác giả là Founder/CEO của AISO Boost Ltd., không có independent statistical review, study registration hoặc external ethics approval); không có dữ liệu về độ trễ trung bình thực tế của agent; không chia nhỏ kết quả theo từng trang web riêng lẻ (chỉ pooled và by-industry).

## Metadata
- Năm: 2026
- Tác giả: Benjamin Tannenbaum (Javo, AISO Boost Ltd., Israel)
- Category arXiv: cs.IR
- Link PDF: https://arxiv.org/pdf/2610.25461
- arXiv ID: 2610.25461v1
- Nhãn: [applied]
- Citation count: [không tìm được]