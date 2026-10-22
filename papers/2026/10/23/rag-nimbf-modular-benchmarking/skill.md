# Skill: Phân tích cấu hình RAG không xâm lấn (RAG-NIMBF)
Source: 2610.27816
Type: framework

## Khi nào dùng skill này
- Cần đánh giá hệ thống RAG sản xuất hiện có mà không muốn sửa đổi pipeline.
- Muốn quét không gian cấu hình (kích thước đoạn, chiến lược truy xuất, mẫu nhắc, mô hình sinh) một cách có hệ thống.
- KHÔNG dùng khi chỉ cần chấm điểm một pipeline đã cho mà không muốn quét không gian cấu hình.

## Input cần có
- Pipeline RAG hiện có (hoặc các thành phần RAG có thể đóng gói).
- Quy định khai báo cho phạm vi tham số của từng thành phần.
- Bộ dữ liệu đánh giá (ví dụ SQuAD hoặc tập câu hỏi-đáp của riêng bạn).
- Điểm cuối mô hình (Ollama, OpenAI-compatible, vLLM, TGI).
- MLflow để theo dõi thí nghiệm.

## Các bước thực hiện
1. Gắn RAG-NIMBF vào pipeline RAG hiện có như một lớp đánh giá không xâm lấn (không sửa đổi nội bộ mô hình hay bộ truy xuất).
2. Định nghĩa phạm vi tham số quét cho từng thành phần (chiến lược chia đoạn, kích thước đoạn, mức chồng lấp, phương pháp truy xuất, mẫu nhắc, mô hình sinh).
3. Chạy tích phân Cartes của tất cả tổ hợp và đánh giá mỗi lần chạy bằng bộ chỉ số lai (faithfulness, nDCG@5, Recall@k, TTFT, TPS).
4. Lưu tất cả tham số và chỉ số vào MLflow để tái lập kết quả.
5. Phân tích tương tác giữa các giai đoạn pipeline (ví dụ kích thước đoạn × chiến lược truy xuất, mẫu nhắc × kích thước mô hình).

## Output mong đợi
- MMR tăng nDCG@5 +4 đến +11 điểm so với tìm kiếm tương tự.
- Nhắc chi tiết tăng faithfulness +10 đến +13 điểm trên các mô hình giỏi/suy lý, nhưng không đáng kể trên mô hình nhỏ (20B).
- Không gian cấu hình RAG chuyển thành các thí nghiệm có thể tái lập và so sánh được.

## Ví dụ áp dụng
- Hệ thống RAG doanh nghiệp đối với tài liệu nội bộ: gắn RAG-NIMBF, quét kích thước đoạn 500/1000 và mẫu nhắc ngắn/chi tiết, chọn cấu hình có faithfulness cao nhất ở thời gian chạy chấp nhận được.

## Gotchas
- Chỉ đánh giá trên SQuAD (câu hỏi ngắn, một đoạn) — có thể không chuyển giao sang tập doanh nghiệp.
- Tất cả đánh giá chất lượng tự động, tương đối với critic RAGAS.
- Reranking, HyDE, so sánh mô hình nhúng bị bỏ qua; top-k và λ của MMR giữ cố định.