# 2610.36915 Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG

## Giá trị cốt lõi (1 câu)
Decision model (mô hình quyết định có type — trả về xác suất các lựa chọn cố định trong một forward pass, không sinh văn bản) phân loại loại xung đột kiến thức (knowledge-conflict typing) trong RAG đúng gần như LLM nhưng tốn 4–39× ít chi phí và nhanh 2.6–6.0 lần, và niềm tin (confidence) của nó xếp hạng được lỗi nên có thể gửi chỉ phần không tự tin lên LLM cao cấp (cascade).

## Problem
Các mô hình ngôn ngữ được bổ sung tìm kiếm (search-augmented language models) trả lời từ các trang web truy xuất, và những trang này thường mâu thuẫn nhau. Xung đột có nhiều nguyên nhân rất khác nhau: câu hỏi thiếu thông tin có nhiều đáp án hợp lệ, chủ đề chính bị tranh cãi, thông tin đã cũ, hoặc nguồn sai. Mỗi trường hợp đòi hỏi phản hồi khác nhau: kết hợp các đáp án, trình bày các quan điểm trung lập, ưu tiên thông tin mới nhất, hoặc bỏ qua nguồn không đáng tin cậy. Cattan et al. (2025) formal hóa như một phân loại năm loại, công bố CONFLICTS — một benchmark 458 câu truy xuất được chuyên gia gán loại xung đột — và thấy việc cho máy sinh biết loại chuẩn (gold type) làm tăng tỷ lệ câu trả lời đúng hành vi mong đợi khoảng 24 điểm. Nhưng việc dự đoán loại rất khó ngay cả với LLM hiện đại (Gemini 2.5 Flash đạt 65.3%). Gap: chưa có nghiên cứu so sánh hệ thống các typed decision model — một lớp model mới trả về xác suất các đáp án được phép trong một forward pass thay vì sinh văn bản — làm nhiệm vụ này nhanh và rẻ thế nào so với LLM.

## Contribution
- Một điều tra toàn bộ (census) các decision model về conflict typing: đánh giá mọi decision model mà một cổng suy luận thương mại (gateway) phục vụ (11 model từ 7 nhà cung cấp) trên CONFLICTS dưới giao thức của paper gốc: cùng biểu diễn đầu vào, cùng định nghĩa và ví dụ thể loại sao chép nguyên văn từ nguồn của paper, và Gemini chạy lại trên cùng các đầu vào để mọi so sánh đều ghép đôi (paired). 10 trong 11 model đạt ngang hoặc vượt LLM của paper với một phần chi phí và độ trễ của nó; Gemini 3.8 Flash hiện tại chính xác đáng kể hơn 8 trong số chúng.
- Một nghiên cứu định dạng (formulation study): phân giải phân loại thành các câu hỏi yes/no làm giảm accuracy cho mọi model 11, và một bản sửa (repair) fit trên một model không giúp model nào khác, làm cho câu hỏi trực tiếp là định dạng đáng tin cậy.
- Các cascades chi phí-chất lượng: niềm tin (confidence) của decision model xếp hạng được lỗi của nó, nên gửi các truy vấn không chắc chắn nhất của nó đến LLM là hiệu quả: với một phần tư truy vấn được thăng hạng (escalated) lên Gemini 3.8 Flash, 8 trong 11 cascade ngang nhau với LLM đơn tại 25–37% chi phí của nó.
- Chẩn đoán đã quy định trước (pre-specified diagnostics): kiểm tra decision model có phụ thuộc vào ngày xuất bản, có nhạy cảm với thứ tự nguồn, hay bỏ lỡ một nguồn sai duy nhất trong những nguồn đồng ý. Ngày không đóng vai trò nào có thể đo, độ nhạy cảm thứ tự nguồn thay đổi giữa các model, và một nguồn sai được gieo (planted) hiện rõ trong xác suất hơn trong đáp án hàng đầu.
- Một thử nghiệm cuối đến cuối (end-to-end): cho vào máy sinh (generator), các loại của 10 trong 11 decision model tạo ra các câu trả lời tuân theo hành vi mong đợi đúng thường xuyên như với các loại của LLM, dưới cả hai judge đã chỉ định.

## Method (tóm tắt cốt lõi)
Ý tưởng cốt lõi: dùng typed decision model — trả về xác suất các đáp án được phép trong một forward pass, không sinh văn bản — làm bộ phân loại loại xung đột (knowledge-conflict typing) trước khi máy sinh viết câu trả lời. Pipeline:
1. Một truy vấn và khoảng 10 kết quả tìm kiếm được đánh số và truyền vào decision model dưới dạng "state".
2. Decision model trả lời một câu hỏi lựa chọn (flat question) với năm tùy chọn là năm thể loại xung đột (No conflict, Complementary information, Conflicting opinions, Outdated information, Misinformation). Nhiệm vụ, định nghĩa thể loại và ví dụ sao chép nguyên văn từ prompt của Cattan et al. (2025). Loại dự đoán là tùy chọn có xác suất cao nhất, và xác suất đó là niềm tin (confidence) của model.
3. Máy sinh viết câu trả lời dựa trên loại được dự đoán.
4. Tùy chọn: cascade (thác) — gửi một phần tư truy vấn có niềm tin thấp nhất đến LLM cao cấp, đáp án của LLM thay thế đáp án của decision model. Ngưỡng là một phân vị của niềm tin decision model, không dùng nhãn, nên toàn bộ đường cong accuracy–chi phí có thể tính trên tập test mà không sọt dữ liệu (leakage).

Hai định dạng được nghiên cứu: Flat (một câu hỏi lựa chọn năm tùy chọn) và Tree (phân giải thành các câu hỏi yes/no). Kết quả: Flat thắng Tree với mọi model.

## KNOWLEDGE — Số liệu & khái niệm
- 11 decision models từ 7 nhà cung cấp, phục vụ bởi một cổng suy luận thương mại (Vercel AI Gateway): Jev 1.13, Jev 1.14, Decider v1.2, Decider Flash v1.2, GPT-6 Luna Decisions, d1, d1 Ultra, Decision-1, Elephant-1, Mammoth-1, Classify-1.
- Được hỏi trực tiếp, 11 decision model phân loại đúng 50.0–67.0% truy vấn test (trung vị 62.6%). Gemini 2.5 Flash với prompt của paper đạt 61.3% trên cùng các truy vấn.
- So với Gemini 2.5 Flash: 8 decision model ngang nhau (statistically tied), 2 chính xác hơn đáng kể (Liquid d1 Ultra +5.7 điểm, p=0.027; Perplexity Decider v1.2 +5.4, p=0.049), 1 kém hơn đáng kể (ScaleDown Classify-1, −11.3, p<0.001).
- Chi phí: $0.04–$0.41 trên mỗi 1000 truy vấn (2 model miễn phí vào lúc chạy) so với $1.66; độ trễ 0.26–0.72 giây so với 1.55 giây. Trong 10 model đạt ngang hoặc vượt LLM của paper, những model được tính phí rẻ 4–39×, và tất cả nhanh 2.6–6.0 lần.
- Gemini 3.8 Flash hiện tại mạnh hơn: ở mức suy nghĩ thấp nhất đạt 70.0%, +8.6 điểm so với Gemini 2.5 Flash (p<0.001), với 2.2× chi phí. Nó chính xác hơn đáng kể 8 trong số decision model; 3 model khác kém hơn 3.0 đến 3.7 điểm nhưng không khác biệt đáng kể.
- Suy nghĩ thêm không giúp cả hai Gemini: Gemini 3.8 Flash ở mức mặc định đạt 66.7% (−3.2 điểm so với mức thấp, p=0.019); Gemini 2.5 Flash với suy nghĩ 57.9% (p=0.19).
- CONFLICTS (Cattan et al., 2025): 458 truy vấn, 5 thể loại (No conflict 161, Complementary 115, Conflicting opinions 115, Outdated 62, Misinformation 5); tập test đóng băng 406 truy vấn, tập phát triển 52.
- Chuẩn đoán theo lớp: các model khác nhau nhất trên Outdated information (F1 từ 27.5 đến 72.7; Gemini 3.8 Flash: 66.1). Misinformation chỉ có 4 mẫu test, làm bại mọi hệ thống: không có decision model nào vượt F1 11.8 (Gemini 3.8 Flash: 25.0).
- Độ chuẩn đoán (calibration): sai số chuẩn đoán dự kiến (expected calibration error — ECE, sai số giữa xác suất đáp án hàng đầu và độ chính xác) của câu hỏi flat dao động từ 0.031 đến 0.188, và 7 trong 11 model tự tin quá mức trung bình (xác suất đáp án hàng đầu cao hơn accuracy).
- Niềm tin xếp hạng lỗi: AUROC từ 0.64 đến 0.76.
- Cascade: thăng hạng phần tư truy vấn không chắc chắn nhất lên Gemini 3.8 Flash tạo ra các cascade ngang nhau với LLM đơn đối với 8 trong 11 model, tại 25–37% chi phí của LLM. Thăng hạng theo niềm tin thắng thăng hạng ngẫu nhiên cùng số truy vấn đối với 10 trong 11 model, lên đến 4.9 điểm; ngoại lệ là GPT-6 Luna Decisions, niềm tin của nó gần như xếp hạng ngẫu nhiên lỗi (AUROC 0.65).
- Ngày xuất bản không đóng vai trò nào có thể đo (loại bỏ mọi ngày, hoặc thêm hạng mức mới nhất tính bằng mã, không thay đổi accuracy đáng kể trong 22/22 kiểm tra).
- Thứ tự nguồn: xáo trộn kết quả thay đổi loại dự đoán trên 5.4–42.1% truy vấn (gộp hai hạt giống), trên ngưỡng tiếng ồn cho mọi model 11; Gemini 3.8 Flash lật trên 9.4%.
- Nguồn sai được gieo: trong 96 truy vấn No conflict, viết lại một kết quả để nêu đáp án sai hợp lý. Các decision model gọi 7.3–66.7% bản sao gieo là Misinformation (Gemini 3.8 Flash: 52.1%). Xác suất của Misinformation tách bản sao gieo từ bản sạch với AUROC 0.66–0.86, ít nhất 0.75 đối với 10 trong 11.
- End-to-end: với judge chính, Vanilla 87.9%, Pipeline 91.6% (+3.7 điểm, p=0.032), Oracle 95.3% (+7.4, p<0.001). Thay Gemini 2.5 Flash làm nhà dự đoán thay đổi ít: 10 trong 11 decision model ngang nhau với nó (−3.9 đến +0.7 điểm), chỉ Classify-1 kém hơn đáng kể (−3.9, p=0.011). Với một phần tư truy vấn thăng hạng lên Gemini 3.8 Flash, 11 trong 11 cascade ngang nhau với nó (−1.0 đến +0.7).

## INSIGHT — Cơ chế & tại sao
- [Decision model phân loại đúng gần như LLM trên typing xung đột] xảy ra VÌ [typing xung đột là bài toán phân loại năm nhãn trong một forward pass, không cần sinh văn bản — decision model được huấn luyện để chuẩn đoán (calibrated) chứ không phải để sinh]. Điều này nghĩa là [có thể thay LLM bằng decision model cho bước typing trong pipeline RAG để giảm 4–39× chi phí và 2.6–6.0× độ trễ].
- [Niềm tin của decision model xếp hạng được lỗi của nó] xảy ra VÌ [xác suất đáp án hàng đầu phản hồi mức chuẩn đoán của model]. Điều này nghĩa là [gửi phần truy vấn không chắc chắn nhất đến LLM cao cấp (cascade) khôi phục phần lớn khoảng cách accuracy với chi phí chỉ 25–37% của LLM].
- [Phân giải taxonomy thành các câu hỏi yes/no làm giảm accuracy cho mọi model] xảy ra VÌ [yes/no bias (khả năng phân tipo "có" cao) và các câu hỏi phụ không tách được các lớp — ví dụ câu hỏi "compatible" trả lời yes cho chủ đề quan triển gần như dễ như cho thông tin bổ sung]. Điều này nghĩa là [dùng câu hỏi lựa chọn trực tiếp (flat), không phân giải taxonomy thành yes/no].
- Điều kiện: insight cascade chỉ có ích khi niềm tin xếp hạng được lỗi (AUROC 0.64–0.76). Một model (GPT-6 Luna) có niềm tin gần như ngẫu nhiên nên cascade không giúp nó.
- Một bản sửa (repair) fit trên lỗi của một model không chuyển giao (transfer) sang model khác.

## IDEA — Áp dụng được gì
1. Áp dụng decision model làm bước typing trước máy sinh trong hệ thống RAG của bạn: bước đầu là thay prompt LLM dài bằng một typed decision model rẻ (ví dụ Jev/Decider) để phân loại loại xung đột giữa các nguồn tìm kiếm, sau đó chỉ sinh câu trả lời theo loại đó.
2. Áp dụng confidence-gated cascade: bước đầu là lấy xác suất đáp án hàng đầu từ decision model, gửi 25% truy vấn không tự tin nhất đến LLM cao cấp (ví dụ Gemini 3.8 Flash), giữ lại 75% cho decision model — giảm 63–75% chi phí LLM trong khi giữ accuracy ngang LLM.
3. Áp dụng câu hỏi lựa chọn trực tiếp (flat) thay vì phân giải thành yes/no: bước đầu là khi thiết kế prompt phân loại xung đột, dùng một câu hỏi lựa chọn năm thể loại thay vì chuỗi các câu hỏi yes/no.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: "Phân loại phân loại (classify) rẻ hơn so với sinh (generate) — hãy dùng decision model cho bước phân loại nhãn cố định trước khi gọi LLM cao cấp, và chỉ escalate phần không tự tin." Khi nào dùng: khi có bước phân loại nhãn cố định trong pipeline (ví dụ conflict typing, intent classification, routing). Khi nào KHÔNG dùng: khi cần suy luận mở hoặc sinh văn bản dài, hoặc khi niềm tin của model không xếp hạng được lỗi (AUROC thấp).
- Ví dụ áp dụng ngoài domain gốc: phân loại email khách hàng thành các chủ đề cố định (khiếu nại, hỏi giá, hỗ trợ kỹ thuật) — dùng decision model rẻ cho bước phân loại, chỉ escalate email không tự tin lên LLM cao cấp hoặc nhân viên người.

## Assumptions & Limitations
- Điều kiện phải đúng để method work: có một tập nhãn cố định và ngắn gọn để phân loại; decision model hỗ trợ structured output (xác suất các đáp án) qua API; truy vấn kèm theo ngữ cảnh đủ dài để modelReasoning (đồn lý) về mối quan hệ giữa các nguồn.
- Limitation paper thừa nhận: CONFLICTS nhỏ (406 truy vấn test, sai số khoảng ±4.8 điểm nên hiệu ứng dưới năm điểm thường không đáng kể; cascade có thể gần nhưng chưa chứng minh bằng chính thức với LLM); phân phối nhãn phản ánh cách truy vấn được chọn, không phải lưu lượng tìm kiếm thực, và chỉ có 5 mẫu Misinformation tự nhiên; biến thể gieo chỉ kiểm tra một loại thông tin sai (thực thể hoặc giá trị bị thay thế trong một nguồn); census chỉ covers các decision model mà một cổng phục vụ trong một ngày; model được lưu trữ thay đổi không báo trước (các mã định danh không phiên bản, hai model miễn phí trong các lần chạy, và rerun Gemini 2.5 Flash của họ dưới con số đã công bố); nhà cung cấp không công bố kích thước model hay dữ liệu huấn luyện nên không thể giải thích sự khác biệt giữa các model; thử nghiệm cuối đến cuối dùng một máy sinh và các judge LLM, được xác thực trên 100 câu trả lời, không thấy kết quả tìm kiếm; judge chính là model của chính máy sinh, có thể ưu ái câu trả lời của nó; kích thước lợi ích từ loại được dự đoán phụ thuộc vào judge, và họ không đo sự thật căn bản (factual grounding), chỉ số thứ ba của Cattan et al. (2025).
- Limitation paper KHÔNG nói: chưa so sánh decision model open-weight chạy cục bộ (chi phí và độ trễ phụ thuộc phần cứng cục bộ, không thể so sánh); chưa đánh giá ảnh hưởng của việc dùng nhiều judge khác nhau cùng lúc; chưa kiểm tra xem xác suất của decision model có thể định hướng máy sinh giữa các hành vi mong đợi khi loại không chắc chắn là gì.

## Metadata
- Năm: 2026 | Tác giả: Parv Khatri, Harshul Jain, Mehak Kapoor, Tanya Sah (tất cả Independent Researcher)
- Category arXiv: cs.CL (Computation and Language)
- Link PDF: https://arxiv.org/pdf/2610.36915v1
- Link abstract: https://arxiv.org/abs/2610.36915
- Code: https://github.com/Parv17k/decision-models-conflict-typing
- Citation count: [không tìm được]
