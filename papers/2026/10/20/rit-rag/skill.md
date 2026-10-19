# Skill: rit-rag
Source: 2610.11370v2
Type: framework

## Khi nào dùng skill này
- Hệ thống RAG doanh nghiệp với kho tài liệu kỹ thuật lớn (triệu trang), cần cân bằng độ thu hồi và độ chính xác.
- Muốn tránh việc agentic RAG đọc mỗi đoạn riêng lẻ không có cấu trúc, hay PageIndex phải cam kết sớm vào một tài liệu duy nhất.
- Có sẵn cấu trúc phân cấp của tài liệu (ToC, sitemap, breadcrumb) hoặc có thể gây ra cấu trúc.

## Tình huống KHÔNG nên dùng
- Kho tài liệu nhỏ, không cần điều hướng cấu trúc (RAG đơn giản đã đủ).
- Tài liệu không có cấu trúc phân cấp và không thể gây ra cấu trúc đáng tin cậy.

## Input cần có
- Corpus tài liệu với cấu trúc phân cấp (ToC/sitemap/breadcrumb) hoặc khả năng gây ra cấu trúc.
- Hệ thống tra cứu lai (BM25 + dense) với chunk đã lập chỉ mục và liên kết với nút cấu trúc (node ID, tiêu đề, ID tổ tiên).
- LLM agent có thể gọi công cụ GetToC (lấy chuỗi cấu trúc cây con) và Read (đọc nội dung nút).
- Ngân sách công cụ B (tổng) và Bs (cuộc gọi GetToC).

## Các bước thực hiện
1. Xây dựng cây cấu trúc cho mỗi tài liệu từ ToC/sitemap; mỗi nút sở hữu văn bản dưới nó, metadata gồm tiêu đề/tóm tắt/từ khóa.
2. Lập chỉ mục tra cứu lai trên các đoạn văn; mỗi đoạn gắn metadata cấu trúc (ID nút, tiêu đề, ID tổ tiên và tiêu đề tổ tiên).
3. Tại thời điểm truy vấn: lấy top-k′ đoạn (k′ > k, ví dụ 200); mỗi đoạn thuộc đúng một nút.
4. Tính điểm số nút s(v, q~) = max sim(q~, c) qua các đoạn của nút; chọn n nút cao điểm (ví dụ n=50).
5. Mở rộng với tổ tiên của các nút đã chọn để tạo câu con phụ Fq~ (một cây con cho mỗi tài liệu có nút trong tập đã chọn).
6. Trình bày S(Fq~) cho agent (chuỗi JSON của các cây con, sắp xếp giảm điểm số cao nhất trong cây).
7. Agent điều hướng cây con: chọn nút St hứa hẹn, đọc văn bản cv qua công cụ Read; dựa trên nội dung, agent trả lời, đọc thêm nút cùng câu con, hoặc đổi câu truy vấn cho vòng sau.
8. Agent dừng khi trả lời hoặc đạt ngân sách B công cụ (tối đa Bs cuộc gọi GetToC).

## Output mong đợi
- Hệ thống RAG đạt độ chính xác cao nhất, cân bằng độ thu hồi (từ retrieval khắp kho) và độ chính xác (từ đọc chọn lọc qua cấu trúc), không cam kết sớm vào tài liệu sai.

## Ví dụ áp dụng
- Hệ thống hỗ trợ khách hàng doanh nghiệp với 6.000 trang tài liệu: khi khách hỏi về tính năng cụ thể, hệ thống truy xuất rộng các đoạn liên quan, gây ra cây con cấu trúc xung quanh các đoạn đó, agent đọc chọn lọc các mục hợp lý và trả lời — tránh bị chìm trong hàng trăm đoạn không liên quan.

## Gotchas
- Không cam kết vào một tài liệu duy nhất trước khi xem nội dung (tránh early-commitment problem của PageIndex).
- Không đọc toàn bộ đoạn đã truy xuất như agentic RAG truyền thống (gây quá tải ngữ cảnh, thấp độ chính xác).
- Không bỏ qua chi phí tiền xử lý (gây ra ToC, sinh metadata) — nhưng chi phí này chỉ phát sinh một lần.
- Phương pháp phụ thuộc vào cấu trúc phân cấp khả dụng; tiêu đề yếu hoặc phân tích kém có thể hạn chế chất lượng bản đồ cấu trúc.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 8 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 4-5 (tính điểm nút và mở rộng tổ tiên) cần triển khai cụ thể liên kết đoạn-nút-cây.
- Input section có đủ không? [YES] — corpus cấu trúc, hệ thống tra cứu lai, LLM agent với GetToC/Read, ngân sách công cụ.

## Dry run (tình huống giả)
- Tình huống: Doanh nghiệp có kho tài liệu kỹ thuật 2,8 triệu trang; nhân viên hỏi về cách cấu hình một tính năng.
- Chạy skill: (1) Xây dựng cây cấu trúc từ sitemap của mỗi trang; (2) lập chỉ mục tra cứu lai trên đoạn văn gắn metadata cấu trúc; (3) truy vấn lấy top-200 đoạn liên quan; (4) tính điểm nút, chọn top-50 nút, mở rộng tổ tiên tạo cây con phụ; (5) trình bày cây con phụ cho agent; (6) agent chọn đọc các nút hợp lý, đổi truy vấn nếu cần; (7) agent trả lời sau khi thu thập đủ bằng chứng.

## Verdict: [SKILL VALID]
