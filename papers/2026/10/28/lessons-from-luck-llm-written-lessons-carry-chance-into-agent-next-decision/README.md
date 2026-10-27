# 2610.33029v1 Lessons from Luck: Do LLM-Written Lessons Carry Chance into an Agent's Next Decision?

## Giá trị cốt lõi (1 câu)
Bài học tự viết từ kết quả chạy trước của agent có thể mang ngẫu nhiên (luck) vào quyết định sau — sau sự cố ngẫu nhiên của công cụ tốt hơn, người đọc bài học chọn công cụ kém hơn ở 11.6% lần chạy, hơn gấp 29 lần so với 0.4% khi đọc bài học từ thành công hoặc item không liên quan.

## Problem
Prior work (các nghiên cứu trước) về agent tự cải tiến (self-improving agents) viết bài học (lessons) từ các lần chạy trước và đọc chúng trước các lần chạy sau. Tuy nhiên, kết quả (outcome) có tiếng ồn (noisy): một quyết định đúng có thể thất bại do ngẫu nhiên, và một quyết định sai có thể thành công do may mắn. Nếu bước viết bài học biến một kết quả thành một quy tắc bền vững (durable rule), nó có thể mang ngẫu nhiên về phía trước: bài học viết sau sự cố ngẫu nhiên của một quyết định đúng có thể bảo các lần chạy sau bỏ lệnh đó. Chưa có nghiên cứu nào đo lường việc kết quả do ngẫu nhiên, khi chất lượng quyết định được giữ cố định, có được viết vào bài học và di chuyển quyết định của một phiên (session) mới của cùng một model hay không.

## Contribution
1. Thiết lập một nghiên cứu đăng ký (registered study) với 256 thế giới giả lập (synthetic worlds), mỗi thế giới là một tác vụ vận hành lặp lại (recurring operational task) với hai công cụ hoán đổi được (interchangeable tools) có độ tin cậy đã ghi nhận.
2. Đo một liên kết (link) trong chuỗi: một model viết bài học từ một lần chạy scripted; một phiên mới của cùng model đọc bài học và chọn công cụ cho lần chạy tiếp theo. 11 endpoint LLM đưa 90.084 câu trả lời.
3. Tìm ra: sau sự cố ngẫu nhiên của công cụ tốt hơn, bài học mang ngẫu nhiên (luck-carrying; interaction +0.112 [+0.097, +0.126]); người đọc chọn công cụ kém hơn ở 11.6% lần chạy với bài học viết từ sự cố đó, vs 0.4% với item không liên quan và 0.4% với bài học từ thành công.
4. Đánh giá hai biện pháp khắc phục (remedies): ghi chú chất lượng quyết định (three-sentence decision-quality note) giảm tỷ lệ xuống 7.5%; hướng dẫn duy nhất cho cả hai kết quả với tùy chọn không thay đổi (no-change option) giảm xuống 3.1%; không biện pháp nào thỏa mãn quy tắc giảm hại (harm-reduction rule) ở mọi endpoint.

## Method
Pipeline (dòng xử lý) có các bước chính:
1. Mỗi thế giới (world) cung cấp 4 lần chạy scripted (scripted previous runs): quyết định tốt (good decision) hoặc quyết định xấu (bad decision), chéo với thành công (success) hoặc sự cố (failure). Hai công cụ hoán đổi được khác chỉ ở độ tin cậy đã ghi nhận (tỷ lệ thành công 0.80–0.93 cho công cụ tốt, 0.50–0.70 cho công cụ kém).
3. Một model viết bài học từ lần chạy với một trong 3 hướng dẫn viết (lesson-writing instructions): RB (ReasoningBank deployed), RBD (RB + biện pháp khắc phục 3 câu), N (một hướng dẫn cho cả hai kết quả).
4. Một phiên mới (fresh session) của cùng model, giữ log quyền thẩm quyền (authoritative log) và kết quả lần chạy trước, chọn công cụ cho lần chạy tiếp theo với một mục ký úcu (memory item): bài học đó, bài học từ kết quả khác, item không liên quan (irrelevant item), hoặc chỉ thị không suy luận (unreasoned directive / PLANTED).
5. Đối số chính (primary contrasts) là P2 (quyết định tốt) và P3m (quyết định xấu) — sự tương tác giữa kết quả và mục ký úcu.
6. Giao thức được đóng băng (frozen), nộp công khai (Zenodo) và đóng dấu thời gian (Bitcoin block) trước bất kỳ lời gọi xác nhận nào.

## KNOWLEDGE — Số liệu & khái niệm
- Luck-carrying (mang ngẫu nhiên): bài học viết từ kết quả do ngẫu nhiên làm thay đổi công cụ một phiên mới chọn, vượt quá mức kết quả thô một mình làm được.
- Outcome bias (sự thiên vị về kết quả): phán quyết một quyết định theo kết quả thay vì theo thông tin có sẵn khi quyết định được đưa ra.
- Hindsight bias (sự thiên vị ngược thời gian): biết kết quả làm cho nó có vẻ dễ dự đoán hơn thực tế.
- ReasoningBank (RB): hướng dẫn viết bài học định tuyến theo kết quả (outcome-routed writing instruction) — hướng dẫn thành công sau thành công, hướng dẫn thất bại sau thất bại.
- RBD (RB plus remedy): RB thêm một dòng gạch đầu dòng 3 câu: "Trước khi viết, phán đoán xem quyết định của agent có đúng không chỉ dựa vào những gì được biết trước kết quả. Một kết quả đơn lẻ không phải là bằng chứng quyết định đúng hoặc sai. Khuyến nghị một hành động khác chỉ nếu quyết định không đúng dựa trên thông tin đó."
- N (neutral): một hướng dẫn dùng cho cả hai kết quả (các cụm từ cụ thể đến kết quả được làm trung tính) với câu thêm "Nếu không có gì về cách thực hiện tác vụ cần thay đổi, hãy nói vậy."
- 256 thế giới giả lập (synthetic worlds), 16 miền (domains) với 16 thế giới mỗi miền.
- 11 endpoint LLM qua OpenRouter: Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5, GPT-6.1 Sol, GPT-6 Luna, Gemini 3.8 Flash, Grok 4.7, Qwen 3.8 Max, DeepSeek V4 Pro, Mistral Large 4, Kimi K3.
- 90.084 câu trả lời hợp lệ từ reader stage; 33.789 bài học từ writer stage.
- P2 (good decision): +0.112 [+0.097, +0.126] — phát hiện luck-carrying.
- P3m (bad decision): +0.002 [−0.001, +0.005] — bounded below 0.10 (không phát hiện).
- Worse-tool rate sau sự cố ngẫu nhiên của công cụ tốt: 11.6% với bài học từ sự cố, 0.4% với item không liên quan, 0.4% với bài học từ thành công.
- Sự tách biệt (descriptive split): +0.042 trong thế giới ghi rõ sự cố độc lập vs +0.181 trong thế giới không ghi rõ.
- 6 endpoint mang ngẫu nhiên (Qwen 3.8 Max +0.352, DeepSeek V4 Pro +0.277, v.v.); 5 endpoint bounded below 0.10.
- Biện pháp RBD: P2 giảm −0.039, worse-tool rate 7.5%; Biện pháp N: P2 giảm −0.085, worse-tool rate 3.1%.

## INSIGHT — Cơ chế & tại sao
- [Bài học overwrites ghi chép (record)] xảy ra VÌ mọi người đọc đều giữ log quyền thẩm quyền (authoritative log) cho biết công cụ tốt vẫn tốt hơn, và được biết kết quả lần chạy trước. Khi log và dòng chạy trước là bằng chứng, một bài học khớp (matched lesson) không thêm quan sát nào người đọc thiếu, nên cho một người đọc biết nguồn bài học thì các đối số khớp có giá trị định chuẩn (normative value) bằng 0. Tuy nhiên, bài học cùng với sự cố báo cáo đã làm tăng tỷ lệ chọn công cụ kém từ 0.4% lên 11.6%. Nghĩa là bài học có thể làm Barlow ghi chép (outweigh the record).
- [Hầu hết hiệu ứng ở nơi ghi chép để chỗ cho nghi ngờ] xảy ra VÌ tương tác là +0.181 trong các thế giới mà log không nói sự cố độc lập (independent) và +0.042 trong các thế giới ghi rõ nó. Khi độc lập không được ghi rõ, một sự cố gần đây có thể được đọc như dấu hiệu của một lỗi hiện tại, nên lựa chọn công cụ kém là một sự lệch so với tiêu chuẩn dựa trên log thay vì một lỗi rõ ràng. Nghĩa là việc ghi rõ trong log rằng sự cố là sự kiện độc lập giảm bớt hiệu ứng (mô tả, không phải kiểm tra).
- [Hướng dẫn viết định tuyến theo kết quả (outcome-routed writing) cần kiểm tra] xảy ra VÌ hướng dẫn thất bại của ReasoningBank yêu cầu viết "suy nghĩ tại sao trajector thất bại", đề xuất "các chiến lược để ngăn chặn thất bại" và ưu tiên "các thủ tục khôi phục cụ thể, có thể hành động", điều này cho rằng có gì đó về lần chạy có lỗi và mời gọi thay đổi hành động. Sau thành công, log bản thân chống lại công cụ kém. Nghĩa là các pipeline viết memory cần được kiểm tra với kết quả do ngẫu nhiên trước khi triển khai.

## IDEA — Áp dụng được gì
1. Áp dụng kiểm tra luck-carrying vào pipeline viết memory (ghi nhớ) của agent tự cải tiến: trước khi triển khai hướng dẫn viết bài học, chạy một thử nghiệm với kết quả do ngẫu nhiên (chất lượng quyết định cố định) để xem bài học có di chuyển quyết định của phiên sau hay không. Bước đầu: tạo một bộ kiểm tra với hai công cụ có độ tin cậy khác nhau, scripted một lần chạy với quyết định đúng và sự cố ngẫu nhiên, sau đó xem bài học viết từ sự cố đó có làm phiên mới chọn công cụ kém hơn hay không.
2. Thêm ghi chú chất lượng quyết định (three-sentence decision-quality note) vào hướng dẫn viết bài học: trước khi viết, yêu cầu agent phán đoán quyết định có đúng không chỉ dựa vào thông tin có trước kết quả, và chỉ khuyến nghị hành động khác nếu quyết định không đúng dựa trên thông tin đó. Bước đầu: chèn đoạn 3 câu vào hướng dẫn viết memory của agent, đặt ngay trước câu hỏi viết bài học.
3. Sử dụng một hướng dẫn duy nhất cho cả thành công và thất bại với tùy chọn không thay đổi (no-change option): hướng dẫn viết không phụ thuộc vào kết quả và có câu "Nếu không có gì về cách thực hiện tác vụ cần thay đổi, hãy nói vậy." Bước đầu: thay thế hướng dẫn viết phân tách theo thành công/thất bại bằng một hướng dẫn thống nhất có tùy chọn không thay đổi.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: Bài học tự viết từ kết quả do ngẫu nhiên có thể làm đè lên ghi chép quyền thẩm quyền — trước khi lưu bài học vào memory, hãy kiểm tra xem quyết định có đúng dựa trên thông tin trước kết quả hay không.
- Khi nào dùng: Khi thiết kế hệ thống agent tự viết bài học từ các lần chạy trước và đọc chúng trước các lần sau (self-improving agents với memory).
- Khi nào KHÔNG dùng: Không áp dụng cho hệ thống không ghi memory từ các lần chạy trước (read-only agent, agent không tự cải tiến).

## Assumptions & Limitations
- Điều kiện phải đúng: Mỗi thế giới phải có hai công cụ hoán đổi được với độ tin cậy đã ghi nhận; log phải cho thấy tỷ lệ thành công của mỗi công cụ qua 180–365 lần chạy trước.
- Limitation paper thừa nhận: Chỉ đo một liên kết của chuỗi (một bài học lưu trữ, được đọc một lần, sau một lần chạy scripted); không thực thi tự cải tiến, truy xuất hoặc memory tích luỹ; không ước lượng tần suất agent thực tế gặp tình huống như vậy; kiểm tra biện pháp khắc phục chỉ với kết quả không báo hiệu sự thay đổi trong độ tin cậy của công cụ.
- Limitation paper KHÔNG nói: Không phân cách được lời khuyên của bài học từ một báo cáo lần thứ hai về sự cố — không có người đọc nào thấy bài học mà không có dòng chạy trước, và không có mục ký úcu nào gọi lại sự cố mà không có bài học.

## Metadata
- Năm: 2026
- Tác giả: Kazuki Nakayashiki
- Category arXiv: cs.LG
- Link PDF: https://arxiv.org/pdf/2610.33029v1
- Classification: [applied]