# 2609.28007 Đánh giá mô hình LLM trọng số mở cho tài liệu bằng tiếng Turkce dưới ràng buộc truy xuất và phần cứng

## Problem
Hầu hết các mô hình LLM có khả năng tiếng Turkce được đánh giá bằng các tiêu chí dùng chung thay vì các tài liệu lĩnh vực dài, cấu trúc phức tạp. Cần đánh giá các mô hình trọng số mở (open-weight — trọng số mô hình được công khai) cho câu hỏi-đáp tài liệu bằng tiếng Turkce trong cài đặt triển khai cục bộ có hạn chế tài nguyên.

## Contribution
- Đánh giá năm mô hình trọng số mở 7B–8B cho câu hỏi-đáp tài liệu bằng tiếng Turkce trong cài đặt triển khai cục bộ trên GPU laptop NVIDIA RTX 3050 với 6 GB VRAM, định lượng 4-bit (4-bit quantisation), cửa sổ ngữ cảnh 4.096 token.
- Tiêu chí chính chứa 100 câu hỏi được kiểm chứng hệ thống rút ra từ báo cáo công nghiệp R&D 109 trang bằng tiếng Turkce; giao thức đánh giá được sao chép trên báo cáo lĩnh vực công 112 trang và tập 100 câu hỏi độc lập thứ hai.
- Đóng góp phương pháp chính: giao thức đánh giá gắn chú ý bằng chứng (evidence-annotated evaluation protocol) tách biệt thất bại truy xuất (retrieval failure) khỏi thất bại suy luận mô hình (downstream model reasoning failure) mà không cần cuộc gọi mô hình bổ sung.
- Kết quả: độ chính xác end-to-end từ 49% đến 75%. Bảy cấu hình truy xuất (từ điển ký tự TF-IDF, từ điển từ BM25, truy xuất đặc trưng dense, kết hợp hybrid) được so sánh bằng khoảng tin cậy Wilson 95% và kiểm định McNemar đôi chính xác; không có cấu hình nào vượt trội đáng kể so với gốc từ điển ký tự TF-IDF trên cả hai tài liệu. Sự nhớ lại bằng chứng (evidence recall) bão hòa khác nhau trên hai báo cáo, cho thấy truy xuất và dung lượng ngữ cảnh hiệu quả (effective context capacity) có thể là ràng buộc buộc đối với một số tài liệu nhưng không phải tất cả.

## Method
Năm mô hình: Trendyol-LLM-8B-T1 (8.2B, Turkce–Anh lý trí, xây trên Qwen3-8B), Qwen2.5-7B (7.6B, đa ngôn ngữ), Cosmos Turkish-Llama-8B-Instruct (8.0B, Turkce-adapted Llama), Mistral-7B (7.2B, đa ngôn ngữ), Kocdigital-LLM-8B (8.0B, Turkce-adapted Llama). Tất cả dùng định lượng Q4_K_M, température 0, seed cố định, phục vụ cục bộ qua Ollama.

Tiêu chí chính: báo cáo công nghiệp R&D 109 trang (PDF, văn bản chạy, bảng nhân sự và tài chính, bản quyền sáng chế, hợp tác, mô tả dự án) chuyển sang văn bản giữ bố cục (layout-preserving text) trước khi chia đoạn và truy xuất. 452 đoạn cho báo cáo chính, 348 đoạn cho báo cáo thứ cấp. 100 câu hỏi chia thành bốn dải khả năng: 30 câu dễ (truy xuất sự thật), 30 câu trung bình (suy lý số), 20 câu khó (suy lý nhiều bước), 20 câu khinh bác (abstention — thông tin không có trong báo cáo). Mỗi câu ghi câu trả lời mong đợi, bằng chứng hỗ trợ, và quy tắc chấm điểm.

Giao thức đánh giá: Truy xuất chạy một lần, ngữ cảnh lấy được giữ cố định trên năm mô hình. Cửa sổ ngữ cảnh 3.500 ký tự. Chấm điểm theo loại câu trả lời (số, thực thể, từ khóa, đúng/sai, chọn nhiều, ngày, khinh bác). Đánh giá bằng chứng (evidence recall) tính độc lập so với chấm điểm câu trả lời.

## KNOWLEDGE — Số liệu & khái niệm
- Độ chính xác tổng thể: Trendyol-8B 75%, Qwen2.5-7B 65%, Cosmos-8B 54%, Mistral-7B 51%, Kocdigital-8B 49% (phát tán 26 điểm).
- Báo cáo thứ cấp: Trendyol 82%, Qwen2.5 65%, Cosmos 60%, Kocdigital 58%, Mistral 51%.
- Khinh bác: Qwen2.5 19/20 (cao nhất), Cosmos/Trendyol 18/20, Kocdigital 9/20 (thấp nhất, không phù hợp cho tìm kiếm báo cáo factuel khi câu trả lời không được onderste là tốn kém).
- Độ trễ: Qwen2.5 trung bình 1.69 giây/câu (nhanh nhất), Trendyol 23.86 giây/câu (chậm nhất, khoảng 14 lần chậm hơn). Trendyol trả lời dài hơn (207 ký tự sau khi xóa scratchpad vs 44 ký tự Qwen2.5).
- Nhớ lại bằng chứng: báo cáo chính 57% (31/54; Dễ 74%, Trung bình 43%, Khó 58%), báo cáo thứ cấp 91% (70/77; Dễ 96%, Trung bình 93%, Khó 79%).
- Ngân sách chẩn đoán 7.000/9.000 ký tự tăng nhớ lại báo cáo chính lên 72%/76%, báo cáo thứ cấp lên 94%/95%.
- Truy xuất: gốc từ điển ký tự TF-IDF 57% (báo cáo chính), 91% (báo cáo thứ cấp); không cấu hình nào vượt trội đáng kể so với gốc TF-IDF (tất cả p > 0.05).

## INSIGHT — Cơ chế & tại sao
[Mô hình Turkce chuyên biệt không nhất thiết mạnh hơn đa ngôn ngữ] xảy ra VÌ Qwen2.5 (đa ngôn ngữ) vượt qua Cosmos và Kocdigital (được điều chỉnh Turkce), cho thấy sự điều chỉnh Turkce đơn lẻ không đảm bảo hiệu năng tài liệu-grounded mạnh hơn. Điều này nghĩa là [lựa chọn mô hình cần được đánh giá riêng trên tác vụ tài liệu bằng tiếng Turkce thực tế chứ không chỉ dựa trên nhãn điều chỉnh ngôn ngữ].
[Thất bại truy xuất và thất bại suy luận mô hình cần được tách biệt] xảy ra VÌ khi mô hình trả lời sai, hoặc mô hình không suy luận đúng trên bằng chứng đã cung cấp, hoặc hệ thống truy xuất không cung cấp bằng chứng cần thiết. Ghi chỉ độ chính xác cuối cùng (end-to-end accuracy) dưới dạng độ chính xác mô hình sẽ trách modèles cho những bostə (lỗi misses) của hệ thống truy xuất, mặc dù hai chế độ thất bại cần biện pháp khác nhau. Điều này nghĩa là [cần ghi lại bằng chứng cụ thể mà mỗi câu hỏi phụ thuộc để đo nhớ lại bằng chứng độc lập so với đầu ra mô hình và gán lỗi cho mô hình hay cho hệ thống truy xuất].

## IDEA — Áp dụng được gì
1. Áp dụng giao thức đánh giá gắn chú ý bằng chứng vào hệ thống câu hỏi-đáp tài liệu doanh nghiệp: bước đầu là ghi lại bằng chứng cụ thể hỗ trợ mỗi câu hỏi và đo nhớ lại bằng chứng độc lập so với chấm điểm câu trả lời, tách biệt lỗi truy xuất khỏi lỗi suy luận.
2. Áp dụng nguyên tắc lựa chọn mô hình dựa trên kết quả thực nghiệm chứ không chỉ nhãn ngôn ngữ: bước đầu là chạy thử nghiệm nhỏ trên tập tài liệu bằng ngôn ngữ mục tiêu với các mô hình ứng viên và chọn mô hình đạt kết quả tốt nhất.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Việc triển khai LLM cục bộ cho tài liệu lĩnh vực bằng ngôn ngữ không phải tiếng Anh cần đánh giá riêng lựa chọn mô hình, hành vi truy xuất, và giới hạn phần cứng; sự điều chỉnh ngôn ngữ đơn lẻ không đảm bảo hiệu năng, và truy xuất có thể là ràng buộc buộc đối với một số tài liệu nhưng không phải tất cả. Khi nào dùng: khi triển khai hệ thống câu hỏi-đáp tài liệu cục bộ có hạn chế phần cứng và dữ liệu nhạy cảm. Khi nào KHÔNG: khi cần xử lý trên đám mây hoặc khi không có tài liệu lĩnh vực bằng ngôn ngữ mục tiêu để đánh giá.

## Assumptions & Limitations
- Tiêu chí chính dựa trên một báo cáo công nghiệp R&D duy nhất; báo cáo lĩnh vực công là kiểm tra độ bền chéo chứ không phải tiêu chí đa lĩnh vực toàn diện. Cần triển khai lại trên tài liệu pháp lý, y tế, và các lĩnh vực khác trước khi rút ra kết luận rộng hơn.
- Chỉ đánh giá năm mô hình 7B–8B trên một cài đặt phần cứng cụ thể (RTX 3050, 6 GB VRAM).
- Cửa sổ ngữ cảnh 4.096-token và ngân sách 3.500 ký tự có thể bị ràng buộc đối với một số tài liệu.

## Metadata
- Năm 2026; tác giả: Imtiaz Ul Hassan, Ardhendu Behera, Swagat Kumar, Peter Matthew, Yonghuai Liu (Edge Hill University, Vương quốc Anh), Öykü Akbulut, Onur Kaya (Ermetal Otomotiv ve Eşya San. Tic. A.Ş., Türkiye); category: cs.CL; PDF: https://arxiv.org/pdf/2609.28007v1; citation count: [NO DATA — paper 2026-09-23]