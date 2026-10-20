# [2610.25111v1] Explore or Confirm? LLM Agents Misallocate Measurements Under Noise

## Giá trị cốt lõi (1 câu)
Các agent LLM phân bổ sai ngân sách đo lẫn giữa khám phá ứng cử viên mới và xác nhận ứng cử viên hứa hẹn bằng cách kiểm tra lại: trên lưới Wellocate, ba mô hình over-confirm (75-94% slot kiểm tra lại), một mô hình under-confirm (14%), và mọi model đều chọn ứng viên cuối kém hơn quy trình scripted đơn giản nhất.

## Problem
Khi chi phí suy luận mô hình giảm dần, thí nghiệm vật lý trở thành bước chậm và đắt đỏ nhất trong khám phá khoa học. Mỗi thí nghiệm trả về một giá trị đọc ồn ào: giá trị cao có thể là ứng viên tốt hoặc một lượt gezogen may mắn. Với ngân sách cố định, agent AI phải liên tục chọn giữa khám phá ứng cử viên mới và xác nhận ứng cử viên hứa hẹn bằng cách kiểm tra lại.

## Contribution
1. Xây dựng Wellocate, một chiến dịch thí nghiệm mô phỏng với giá trị thực Known: dựa trên lưới được tạo (NK landscape) và hai bộ dữ liệu protein thực (GB1, PhoQ), được xáo trộn tên amino axit để không model nào trả lời từ ký ức.
2. Đo lường sự phân bổ sai của 5 mô hình ngôn ngữ như agent tối thiểu (không công cụ, không bộ nhớ ngoài lịch sử trong mỗi prompt): chúng phân bổ sai ở cả hai hướng (over-confirm và under-confirm).
3. Thử nghiệm 3 hỗ trợ đơn giản (ledger, landscape note, Menu danh sách ứng viên chưa thử): Menu cắt kiểm tra lại mạnh mẽ ở 3 mô hình over-confirm; ledger và landscape note thay đổi kiểm tra lại tối đa 5 điểm phần trăm.
4. Phát hành Wellocate làm benchmark và môi trường RL với chia sẻ cố định và cơ sở scripted, cho phép bất kỳ ai đo lường agent phân bổ ngân sách như thế nào trước khi giao thí nghiệm thực.

## Method
Wellocate biến chiến dịch thí nghiệm thành một tập avuto với điểm số. Ứng viên là xâu 4 chữ cái, một chữ cái mỗi vị trí, từ bảng chữ cái 20 chữ (một chữ cho mỗi axit amino), không gian chứa 160,000 ứng viên. Mỗi ứng viên có giá trị thực ẩn, chất lượng, mà agent không bao giờ thấy. Giá trị thực đến từ một landscape (bảng cố định cho mỗi ứng viên giá trị của nó). Ba landscape: một tổng hợp (NK landscape gọi là "grid"), hai thực tế (GB1 và PhoQ深度 đột biến quét). Tên axit amino được xáo trộn bằng ánh xạ ngẫu nhiên tại mỗi vị trí từ A đến T. Mỗi biến thể giữ giá trị đo được của nó dưới tên mới. Mỗi landscape có ứng viên tốt nhất riêng (IOJO trên grid). Mọi giá trị trong một landscape được nhân bằng hằng số واحدة để ứng viên tốt nhất đạt 8.762 (đọc số cao nhất trong dữ liệu GB1), đặt tất cả trên một thang đo và không thay đổi xếp hạng. Ứng viên khả thi nếu giá trị thực nằm trong top 7% của landscape (11,199 trên grid). Mỗi chiến dịch có 15 vòng của 4 slot, một slot mỗi puits thí nghiệm, 60 đo l량 tổng thể. Mỗi chiến dịch bắt đầu từ cùng ứng viên, ứng viên khả thi trung vị (GDIF trên grid, 6.87). Mỗi vòng agent orders 4 ứng viên, môi trường xử lý mỗi lệnh. Nó từ chối lệnh cho ứng viên không khả thi trước khi lệnh sử dụng một slot và hỏi agent thay thế. Nếu 3 thay thế liên tiếp cũng bị từ chối, slot bị mất. Nó thất bại khoảng 15% lệnh cho ứng viên khả thi ngẫu nhiên, bất kể giá trị: không có gì quay lại, và slot vẫn bị chi bỏ. Mọi lệnh khác trả về một đọc: giá trị thực của ứng viên cộng với ồn ào có độ lệch chuẩn 7.3% của giá trị đó. Môi trường giữ bản ghi của mọi lệnh, sự từ chối, sự thất bại và đọc, và hiển thị agent toàn bộ bản ghi trước mỗi vòng. Agent có thể order một ứng viên đã đo trước đó. Cuối cùng nó nominate một ứng viên, được chấm trên giá trị thực của nó. Điểm số chia sự thiếu hụt của ứng viên cuối từ ứng viên tốt nhất trong landscape thành 2 phần: exploration loss (quanto xa ứng viên tốt nhất agent đã đo từ ứng viên tốt nhất của landscape) và selection loss (quanto xa ứng viên nominated từ ứng viên tốt nhất agent đã đo).

## KNOWLEDGE — Số liệu & khái niệm
- Không gian ứng viên: 160,000 (20^4), ứng viên khả thi top 7% (11,199)
- Chiến dịch: 15 vòng × 4 slot = 60 đo l量
- Ứng viên khởi đầu: GDIF (trung vị khả thi, 6.87 trên grid), ứng viên tốt nhất: IOJO (8.762)
- Ứng viên khả thi: giá trị thực trong top 7% landscape (7.2% biến thể GBI giữ ít nhất một phần mười sức khỏe wild type)
- Ứng viên khả thi tương xúc: 25.8% hàng xóm khả thi trên grid (trung bình), 45.9% GB1, 37.6% PhoQ
- ồn ào: độ lệch chuẩn 7.3% của giá trị đọc (sai số đếm của GB1 deep mutational scan)
- 15% lệnh cho ứng viên khả thi thất bại ngẫu nhiên
- 5 mô hình: Opus 4.7, Gemini 2.5 Flash, DeepSeek V3.1, GPT-6.1 Sol, Gemini 3.1 Pro
- Quy tắc scripted: guessing rule (kiểm tra lại tốt nhất cố định số lần mỗi vòng), model-guided rule (học từ các đọc của bản thân), informed rule (biết ứng viên nào khả thi)
- Grid: guessing rule kiểm tra lại 23.8%, model-guided 37.6% (scripted band); informed rule 23.3% (biết khả thi)
- Grid picks: Opus 4.7 7.62, Gemini 2.5 Flash 7.70, DeepSeek V3.1 7.76, GPT-6.1 Sol 7.67, Gemini 3.1 Pro 7.69; guessing rule 7.87; informed rule 8.00
- Grid re-testing share: Opus 4.7 74.9%, Gemini 2.5 Flash 94.0%, DeepSeek V3.1 91.0%, GPT-6.1 Sol 44.1%, Gemini 3.1 Pro 14.0%
- GB1: best scripted rule kiểm tra lại 0.9% slot; models kiểm tra lại 19.4% (Sol) đến 96.0% (DeepSeek V3.1)
- GB1 picks: Opus 4.7 4.78, Gemini 2.5 Flash 1.12, DeepSeek V3.1 0.84, GPT-6.1 Sol 6.36, Gemini 3.1 Pro 4.90
- PhoQ: best scripted rule kiểm tra lại 0% slot
- PhoQ picks: Opus 4.7 1.89, Gemini 2.5 Flash 2.13, DeepSeek V3.1 0.83, GPT-6.1 Sol 2.37, Gemini 3.1 Pro 1.72
- Ba nhóm: over-confirmers (Opus 4.7, Gemini 2.5 Flash, DeepSeek V3.1, 75-94% grid re-test), under-confirmer (Gemini 3.1 Pro, 14%), GPT-6.1 Sol (44%, nằm justo trên băng)
- Exploration loss (grid): over-confirmers 0.94-1.04 điểm thiếu so với tốt nhất landscape, guessing rule 0.67
- Selection loss (grid): Gemini 3.1 Pro 0.38, guessing rule 0.23
- Hỗ trợ: ledger (tóm tắt các đọc), landscape note (mô tả cách landscape xây dựng), Menu (danh sách 10 ứng viên chưa thử)
- Ledger và landscape note thay đổi kiểm tra lại tối đa 5 điểm phần trăm
- Menu cắt kiểm tra lại mạnh ở 3 over-confirmers; trên GB1 không Menu: Gemini 2.5 Flash thử 3.9 ứng viên khác, DeepSeek V3.1 thử 2.4 ứng viên khác trong chiến dịch 60 đo l量; có Menu: picks tăng hơn 3 đơn vị giá trị thực
- Gemini 3.1 Pro replay: thay thế vòng cuối bằng kiểm tra lại các ứng viên hàng đầu, tại m=3 hồi phục khoảng 23% selection loss
- Mức ồn ào: grid đạt cao nhất ở 1 kiểm tra lại/vòng ở ồn ào thí nghiệm thực; GB1 và PhoQ đạt cao nhất ở 0; kiểm tra lại trả tiền trên PhoQ ở khoảng 4× ồn ào thí nghiệm và GB1 chỉ khoảng 8×

## INSIGHT — Cơ chế & tại sao
[Over-confirmers kiểm tra lại quá nhiều] VÌ [họ cạn kiệt các ứng viên mới đáng thử — agent phải đặt tên mọi ứng viên mới bản thân, và hầu hết tên mới nó thử bị từ chối vì không khả thi]. Điều này nghĩa là [cung cấp danh sách ứng viên chưa thử (Menu) cắt kiểm tra lại và cải thiện chọn cuối].
[Under-confirmer chọn Sieger trên một đọc đơn] VÌ [nó tin tưởng vào các đọc đơn lẻ, không kiểm tra lại đủ, nên thường chọn ứng viên đo được chỉ một lần có đọc may mắn cao]. Điều này nghĩa là [xác nhận phải chạy qua toàn bộ chiến dịch, không chỉ vòng cuối].
[Kiểm tra lại không tự động tốt hơn] VÌ [mỗi kiểm tra lại cũng lấy một slot từ ứng viên mới, có thể tăng exploration loss; trên GB1 và PhoQ quy tắc scripted tốt nhất kiểm tra lại gần 0 slot, và mọi model kiểm tra lại nhiều hơn quy tắc đó]. Điều này nghĩa là [mức ồn ào quyết định liệu kiểm tra lại có trả tiền không — trên protein 1 đọc hiếm khi đặt ứng viên trong sai thứ tự].
[Mọi mô hình đều chọn ứng viên cuối kém hơn quy trình scripted đơn giản nhất] VÌ [không có công cụ, không bộ nhớ ngoài lịch sử prompt, agent hoàn toàn phụ thuộc vào khả năng phân bổ của bản thân]. Điều này nghĩa là [cần đo lường cách agent chia ngân sách trước khi giao thí nghiệm thực].

## IDEA — Áp dụng được gì
1. Áp dụng [Wellocate benchmark] vào [đo lường cách agent LLM phân bổ ngân sách thí nghiệm]: bước đầu là chạy agent trên Wellocate với các landscape khác nhau và mức ồn ào khác nhau, theo dõi tỷ lệ kiểm tra lại và giá trị ứng viên cuối.
2. Áp dụng [Menu danh sách ứng viên chưa thử] vào [giúp agent khám phá không cạn kiệt ứng viên]: bước đầu là cung cấp agent danh sách ứng viên chưa thử được xếp hạng bởi mô hình đơn giản fit từ các đọc của bản thân.
3. Áp dụng [xác nhận chạy qua toàn bộ chiến dịch] vào [tránh chọn sai do đọc may mắn]: bước đầu là thiết lập vòng kiểm tra lại ứng viên hàng đầu ở cuối chiến dịch, không chỉ kiểm tra lại khi agent tự quyết định.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Phân bổ ngân sách đo lẫn giữa khám phá và xác nhận phải đọc landscape và mức ồn ào — không có quy tắc cố định nào tốt ở mọi nơi. Áp dụng khi: thiết kế agent cho thí nghiệm khoa học hoặc đo lường costly. Không áp dụng khi: chỉ cần một quy tắc cố định cho mọi tình huống.
2. Nguyên tắc: Agent cần nguồn ứng viên bên ngoài để không cạn kiệt không gian tìm kiếm. Áp dụng khi: xây dựng agent khám phá không gian ứng viên lớn với tỷ lệ khả thi thấp. Không áp dụng khi: không gian ứng viên nhỏ và dễ liệt kê toàn bộ.

## Assumptions & Limitations
- Điều kiện phải đúng: có landscape với giá trị thực Known, có mô hình ồn ào mô phỏng sai số thí nghiệm thực, có ngân sách đo l량 cố định.
- Limitation paper thừa nhận: agent tối thiểu không có công cụ và không bộ nhớ ngoài lịch sử prompt; kết quả trên 3 landscape (1 tổng hợp, 2 protein) có thể không general hoá sang mọi loại thí nghiệm; chỉ đánh giá 5 mô hình ngôn ngữ.
- Limitation paper KHÔNG nói: không có chi phí inference thực tế của agent; không đánh giá agent có công cụ hoặc bộ nhớ ngoài; không so sánh với các phương pháp thiết kế thí nghiệm cổ điển ngoài 3 quy tắc scripted.

## Metadata
- Năm: 2026
- Tác giả: Abdul Karim, Matt Keon (Xstendyl)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.25111
- arXiv ID: 2610.25111v1
- Nhãn: [applied]
- Citation count: [không tìm được]