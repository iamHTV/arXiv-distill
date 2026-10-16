# Skill: agentic-retrieval-react-loop
Source: 2610.05750v1
Type: workflow

## Khi nào dùng skill này
- Hệ thống tìm kiếm cần xử lý các truy vấn phức tạp đòi hỏi suy luận đa bước.
- Standard retrieval (dense retrieval dựa trên semantic similarity) không đủ chính xác cho ứng dụng của bạn.
- Có thể chấp nhận chi phí cao hơn (thời gian, token) để có độ chính xác tốt hơn.

## Tình huống KHÔNG nên dùng
- Tìm kiếm đơn giản, chỉ cần semantic similarity cơ bản.
- Không chấp nhận chi phí 107s và 764K tokens cho mỗi truy vấn.

## Input cần có
- Hệ thống retriever đã có sẵn (dense retrieval).
- Mô hình LLM có khả năng reasoning (suy luận).
- Bộ dữ liệu không cấu trúc cần tìm kiếm.

## Các bước thực hiện
1. Xây dựng ReAct agentic loop: LLM đưa ra reasoning (suy luận) về truy vấn cần làm, retriever tìm kiếm, LLM kiểm tra kết quả, quyết định tiếp tục hay dừng.
2. Lặp lại vòng lặp này cho đến khi agent có đủ thông tin để trả lời.
3. Chỉ bật agentic retrieval cho các truy vấn phức tạp, dùng standard retrieval cho truy vấn đơn giản (để tiết kiệm chi phí).
4. Đánh giá trên nDCG@10 và các metric liên quan để xác nhận hiệu quả.

## Output mong đợi
- Cải thiện nDCG@10 khoảng 8.7 điểm so với standard retrieval.
- Tổng quát hóa tốt trên nhiều domain (ViDoRe, BRIGHT).
- Chi phí: ~107 giây và 764K input tokens + 5.8K output tokens cho mỗi truy vấn phức tạp.

## Ví dụ áp dụng
Solopreneur làm hệ thống tìm kiếm tài liệu pháp lý: truy vấn đơn giản ("mã thuế 2026") dùng standard retrieval; truy vấn phức tạp ("so sánh quy định thuế giữa năm 2025 và 2026 cho doanh nghiệp nhỏ") dùng agentic retrieval với ReAct loop để LLM suy luận multi-step và tìm kiếm nhiều nguồn.

## Gotchas
- Chi phí rất cao: 107.4 giây vs 0.67 giây cho standard retrieval; 764.1K input tokens mỗi truy vấn.
- Chỉ nên dùng cho truy vấn thực sự phức tạp, không dùng cho mọi truy vấn.
- Cần LLM có khả năng reasoning tốt để agentic retrieval hoạt động hiệu quả.
