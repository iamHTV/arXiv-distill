# Skill: rag-conflict-typing-decision-model
Source: 2610.36915
Type: workflow

## Khi nào dùng skill này
- Bạn đang xây dựng hệ thống RAG (search-augmented generation — sinh ngữ được bổ sung tìm kiếm) và cần phân loại loại xung đột giữa các nguồn tìm kiếm trước khi sinh câu trả lời.
- Bạn muốn giảm chi phí và độ trễ của bước phân loại này so với việc gọi LLM cao cấp.
- Bạn có một tập dữ liệu có nhãn xung đột (hoặc có thể gán nhãn một phần nhỏ) để chọn model và đặt ngưỡng cascade.

## Tình huống KHÔNG nên dùng
- Nhiệm vụ của bạn cần sinh văn bản dài hoặc suy luận mở, không phải phân loại nhãn cố định.
- Bạn không có API hỗ trợ structured output (xác suất các đáp án) từ decision model.

## Input cần có
- Truy vấn và danh sách các kết quả tìm kiếm được đánh số (URL, tiêu đề, đoạn trích, ngày xuất bản nếu có, đoạn 512 token liên quan nhất).
- Danh sách các decision model có sẵn qua gateway của bạn và giá/độ trễ của mỗi model.
- Một tập nhỏ gán nhãn loại xung đột (dev set) để chọn định dạng câu hỏi và đặt ngưỡng cascade (nếu dùng).
- Một máy sinh (generator) và một LLM cao cấp cho bước cascade (nếu dùng).

## Các bước thực hiện
1. Xây dựng input cho mỗi truy vấn: ghép URL, tiêu đề, đoạn trích, ngày xuất bản (nếu có) và đoạn 512 token liên quan nhất của mỗi kết quả tìm kiếm, giữ thứ tự của tập dữ liệu và đánh số.
2. Gửi một câu hỏi lựa chọn trực tiếp (flat question) với năm tùy chọn (No conflict, Complementary information, Conflicting opinions, Outdated information, Misinformation) đến mỗi decision model candidate. Nhiệm vụ, định nghĩa thể loại và ví dụ sao chép nguyên văn từ prompt của Cattan et al. (2025). Loại dự đoán là tùy chọn có xác suất cao nhất; xác suất đó là niềm tin (confidence).
3. Chọn decision model tốt nhất trên tập dev: đo accuracy, macro-F1, và sai số chuẩn đoán dự kiến (ECE). Không chọn chỉ dựa trên accuracy — cũng xem niềm tin xếp hạng lỗi thế nào (AUROC) nếu bạn dự định dùng cascade.
4. Quyết định dùng cascade hay không: nếu niềm tin xếp hạng lỗi tốt (AUROC cao), hãy gửi phần truy vấn không chắc chắn nhất (ví dụ 25% thấp nhất) đến LLM cao cấp, giữ lại phần còn lại cho decision model. Ngưỡng là phân vị của niềm tin, không dùng nhãn.
5. Cho loại được dự đoán vào máy sinh, kèm định nghĩa và hành vi mong đợi của loại đó; máy sinh viết câu trả lời cuối cùng.
6. (Tùy chọn) Đánh giá cuối đến cuối: dùng một judge LLM kiểm tra câu trả lời có tuân theo hành vi mong đợi của loại vàng hay không.

## Output mong đợi
- Loại xung đột dự đoán cho mỗi truy vấn, cùng niềm tin (confidence).
- Nếu dùng cascade: phần truy vấn được escalate đến LLM cao cấp và phần được xử lý bởi decision model.
- Báo cáo accuracy, chi phí và độ trễ của bước phân loại so với việc chỉ dùng LLM cao cấp.

## Ví dụ áp dụng
Bạn vận hành hệ thống trả lời hỏi từ web. Trước khi sinh câu trả lời, bạn chạy bước 1–3 và phát hiện decision model rẻ (ví dụ $0.04/1000 truy vấn) đạt accuracy ngang LLM ($1.66/1000 truy vấn) nhưng nhanh 5 lần. Bạn chạy bước 4 và gửi 25% truy vấn không tự tin nhất đến Gemini 3.8 Flash, giữ lại 75% cho decision model — chi phí giảm xuống 25–37% của chi phí chỉ dùng LLM, accuracy dồn dập. Bạn chạy bước 5 và sinh câu trả lời theo loại được dự đoán.

## Gotchas
- Phân giải taxonomy thành các câu hỏi yes/no làm giảm accuracy với mọi model 11 — hãy dùng câu hỏi lựa chọn trực tiếp (flat), không tách thành yes/no.
- Một bản sửa fit trên lỗi của một model không chuyển giao sang model khác — hãy dùng định dạng câu hỏi không đổi cho mọi model.
- Niềm tin của một số model (ví dụ GPT-6 Luna, AUROC 0.65) gần như xếp hạng ngẫu nhiên lỗi — cascade không giúp model này; hãy đo AUROC trước khi quyết định cascade.
- Các model được lưu trữ thay đổi không báo trước (mã định danh không phiên bản) — hãy đo lại định kỳ trên dữ liệu triển khai của riêng bạn, không dựa vào accuracy duy nhất một lần.
- Judge LLM chính là model của chính máy sinh, có thể ưu ái câu trả lời của nó — hãy dùng một judge độc lập nếu có thể.
