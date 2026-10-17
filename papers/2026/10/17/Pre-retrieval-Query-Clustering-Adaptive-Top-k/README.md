# [2609.13489v2] Pre-retrieval Query Clustering for Adaptive Top-k Document Retrieval in RAG Systems

## Problem
- Hệ thống RAG thường lấy số liệu cố định (top-k) để căn chỉnh sinh văn bản, nhưng cách tiếp cận tĩnh này dễ gãy: truy vấn đơn giản bị lấy quá nhiều (over-retrieval — thêm tiếng ồn và chi phí) trong khi truy vấn phức tạp bị lấy quá ít (under-retrieved), gây lỗi quá trình (recall failures) lan sai vào câu trả lời sai. Prior work chưa giải quyết được câu hỏi: cần lấy bao nhiêu tài liệu để trả lời một truy vấn tùy ý một cách đáng tin cậy?

## Contribution
- QCAR (Query-Clustering Adaptive Retrieval) — khung làm việc lấy văn bản thích ứng trước khi lấy (pre-retrieval), tập trung vào truy vấn (query-centric).
- Ngoại tuyến (offline): ước tính độ khó lấy của mỗi truy vấn bằng cách đo NDCG dưới trình lấy mặc định (default retriever) và lấy điểm “bão hòa” (saturation) k* riêng cho mỗi truy vấn từ đường cong NDCG–k; nhóm một tập lớn truy vấn trong không gian nhúng (embedding space) và tóm tắt mỗi cụm bằng độ sâu lấy khuyến nghị màurat độ bao phủ cao (ví dụ: ~95%) sử dụng quy tắc trung bình cộng phương sai (mean-plus-variance rule).
- Thời gian chạy (runtime): gán truy vấn đến vào cụm và chọn top-k tương ứng trong thời gian hằng (constant time).
- Tiền khi lấy (pre-retrieval) và tập trung vào truy vấn (query-centric), mạnh mẽ trong bộ dữ liệu khách quán, kiểu vụ án (case-like corpus) và có thể áp dụng trên các miền như pháp lý, y tế, tài chính và tìm kiếm doanh nghiệp.

## Method (tóm tắt cốt lõi)
- Ngoại tuyến 3 bước: (1) Khám phá cụm ý định (intent clusters): nhúng truy vấn lịch sử bằng bộ mã hóa nhúng (dense encoder) và nhóm theo độ tương tự ngữ nghĩa (semantic similarity); truy vấn trong cùng cụm chia sẻ yêu cầu lấy tương tự. (2) Đo độ khó lấy: cho mẫu truy vấn từ mỗi cụm, đánh giá chất lượng lấy bằng NDCG — điều này lượng hóa trình lấy phải lấy bao nhiêu tài liệu để đạt nhớ lại (recall) chấp nhận được. (3) Gán khuyến nghị độ sâu cấp cụm: tập hợp ước tính độ khó mỗi truy vấn thành một độ sâu khuyến nghị k* đơn cho mỗi cụm, nhắm độ bao phủ cao (ví dụ: ~95%) dùng quy tắc trung bình cộng phương sai. Đầu ra là Cơ sở Truy vấn-Cụm (Query-Cluster Database D_qc) chứa: (i) mô hình ánh xạ đã fit (fitted projection model), (ii) vị trí tâm cụm (cluster centroid locations), (iii) ánh xách từ ID cụm đến độ sâu lấy khuyến nghị.
- Thời gian chạy: (1) Kiểm tra từ vựng (lexical check): quét truy vấn cho các dấu hiệu phạm vi (scope markers), nếu tìm được gán k* = k_max và tiến hành lấy. (2) Gán cụm (cluster assignment): nếu không, nhúng truy vấn, chiếu vào không gian đã học, gán vào tâm cụm gần nhất, tra k* tương ứng từ D_qc. (3) Lấy và sinh (retrieval and generation): thực thi RAG chuẩn với k* thích ứng.
- Chi phí thêm nhỏ: khớp từ vựng <1ms, một lời gọi nhúng (embedding call) 30–50ms (đã cần cho lấy), phép chiếu (projection transform) 1ms, tìm điểm láng giềng gần nhất qua K tâm cụm (<1ms với K ~100), và tra cụm O(1).

## Key Findings
- 6.820 câu hỏi từ 20.000 truy vấn thô (sau khi làm sạch, lọc PII).
- Đối với baseline k=50: truy vấn đơn giản — giảm 35,95% lượng token, cải thiện F1 +0,37; truy vấn phức tạp — cải thiện F1 +0,37 với chi phí tăng 85,95% lượng token.
- Thử nghiệm A/B trên lưu lượng đầy đủ (full-traffic): F1 cải thiện hơn 36% trong khi giảm lượng token 14% trên cụm độ phức tạp thấp mà không mất độ chính xác.
- Phân tích cuối cùng đến cuối (end-to-end): cơ chế động giảm lượng token tới 23% khi duy trì sự khớp khái niệm (conceptual parity) với baseline cho truy vấn đơn giản; cải thiện nhớ lại sự thật (factual recall) 9–17% cho truy vấn phức tạp.
- UMAP + k-means tốt nhất: n_components=190, n_neighbors=200, min_dist=0.0, k=80 cụm (SS=0,6, DBI=0,46).

## Actionable Insights
1. Ước tính độ khó truy vấn trước khi lấy văn bản (pre-retrieval query difficulty estimation) để chọn độ sâu lấy thích ứng (adaptive top-k) thay vì dùng số liệu cố định. Áp dụng: xây dựng Query-Cluster Database từ log truy vấn lịch sử, gán truy vấn mới vào cụm gần nhất và chọn top-k tương ứng, giảm token cho truy vấn đơn giản mà không tổn thất độ chính xác.
2. Nhóm truy vấn trước khi lấy (pre-retrieval query clustering) mạnh mẽ hơn phương pháp tin cậy sau khi lấy (post-retrieval confidence) đối với bộ dữ liệu kiểu vụ án (case-like corpus). Áp dụng: dùng UMAP + k-means để nhóm truy vấn lịch sử, tính đường cong NDCG–k cho mỗi cụm, xác định điểm bão hòa k* bằng quy tắc trung bình cộng phương sai.

## Assumptions & Limitations
- Thiết kế cho hệ thống RAG miền bị giới hạn (bounded-domain) với phân phối truy vấn ổn định, lặp lại và có sẵn truy vấn lịch sử.
- Văn bản được lấy từ miền nhất quán (hồ sơ vụ án, hồ sơ y tế, wiki doanh nghiệp) thay vì web mở.
- Cài đặt miền mở (open-domain) là môi trường riêng biệt vì đa dạng truy vấn không có giới hạn.
- Thử nghiệm tập trung vào luật chấn thương cá nhân (personal injury law); chuyển sang ngành mới cần log truy vấn lịch sử, cơ chế gán điểm liên quan (LLM-as-a-Judge hay gán điểm con người), và mẫu từ vựng theo miền.
- Không nói rõ: độ trễ thêm từ nhúng truy vấn và tìm điểm gần nhất có thể tích lũy ở mức lưu lượng cao.

## Metadata
- Năm: 2026, tác giả: Ye Xia (Portland State University), Emre Yamangil, Haixun Wang (EvenUp), category arXiv: cs.IR, link PDF: https://arxiv.org/pdf/2609.13489v2, hội thảo: CIKM ’26, Rome, Ý
