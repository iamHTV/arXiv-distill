# Skill: qcar-adaptive-top-k-retrieval
Source: 2609.13489v2
Type: framework

## Khi nào dùng skill này
- Hệ thống RAG dùng top-k cố định, gây lấy quá nhiều (over-retrieval) trên truy vấn đơn giản và lấy quá ít (under-retrieval) trên truy vấn phức tạp.
- Có sẵn log truy vấn lịch sử (historical query log) trong một miền bị giới hạn (bounded-domain).
- Có thể đo NDCG của trình lấy mặc định (default retriever) trên mẫu truy vấn.

## Tình huống KHÔNG nên dùng
- Hệ thống tìm kiếm trên web mở (open-domain) với đa dạng truy vấn không có giới hạn.
- Không có log truy vấn lịch sử hoặc không thể gán điểm liên quan (relevance labeling).
- Cần phản hồi tức thì mà không thể chấp nhận chi phí thêm từ bước nhúng truy vấn (embedding call).

## Input cần có
- Log truy vấn lịch sử (sau khi làm sạch, lọc PII).
- Bộ tài liệu để lấy (case files, hồ sơ y tế, wiki doanh nghiệp, v.v.).
- Trình lấy văn bản (retriever) có thể tính NDCG.
- Bộ mã hóa nhúng (dense encoder, ví dụ: text-embedding-ada-002).
- Cơ chế gán điểm liên quan (LLM-as-a-Judge hoặc gán điểm con người).

## Các bước thực hiện
1. Nhúng truy vấn lịch sử bằng bộ mã hóa nhúng (ví dụ: text-embedding-ada-002, chiều 1536) và nhóm theo độ tương tự ngữ nghĩa (UMAP + k-means) để khám phá các cụm ý định (intent clusters).
2. Cho mỗi cụm, lấy mẫu truy vấn và đánh giá chất lượng lấy bằng NDCG để đo độ khó lấy (retrieval difficulty) — lượng hóa số tài liệu cần lấy để đạt nhớ lại (recall) chấp nhận được.
3. Tổng hợp ước tính độ khó mỗi truy vấn thành một độ sâu khuyến nghị k* đơn cho mỗi cụm, nhắm độ bao phủ cao (~95%) dùng quy tắc trung bình cộng phương sai (mean-plus-variance rule).
4. Xây dựng Cơ sở Truy vấn-Cụm (Query-Cluster Database D_qc) chứa: mô hình ánh xạ đã fit, vị trí tâm cụm, ánh xách từ ID cụm đến k*.
5. Tại thời gian chạy: quét truy vấn cho dấu hiệu phạm vi (scope markers); nếu tìm được, gán k* = k_max.
6. Nếu không, nhúng truy vấn, chiếu vào không gian đã học, gán vào tâm cụm gần nhất, tra k* từ D_qc.
7. Thực thi RAG chuẩn với k* thích ứng.
8. Định kỳ tái xây dựng D_qc hoặc cập nhật khi phát hiện dịch chuyển phân phối (distribution shift).

## Output mong đợi
- Hệ thống lấy văn bản thích ứng (adaptive retrieval depth) giảm token cho truy vấn đơn giản mà không mất độ chính xác.
- Cơ sở dữ liệu truy vấn-cụm có thể tra cứu k* trong thời gian hằng (O(1)).

## Ví dụ áp dụng
- Trợ lý pháp lý RAG: truy vấn "Hành시다 thiệt hại thân thể tại California là bao lâu?" (tìm kiếm đơn giản) gán k* nhỏ (ví dụ: k=10), giảm token 35,95% so với k=50 cố định và cải thiện F1 +0,37; truy vấn "Giải thích negligence hòa hợp ảnh hưởng đến thiệt hại như thế nào khi vादी có phần lỗi, và dẫn dottes luật liên quan." (phức tạp) gán k* lớn, cải thiện F1 +0,37 với nhiều token hơn.

## Gotchas
- Thiết kế cho miền bị giới hạn (bounded-domain) với phân phối truy vấn ổn định, lặp lại.
- Văn bản từ miền nhất quán (hồ sơ vụ án, hồ sơ y tế, wiki doanh nghiệp) chứ không phải web mở.
- Thử nghiệm tập trung luật chấn thương cá nhân; chuyển ngành mới cần log truy vấn lịch sử, cơ chế gán điểm liên quan, mẫu từ vựng theo miền.
- Không nói rõ: độ trễ thêm từ nhúng truy vấn và tìm điểm gần nhất có thể tích lũy ở mức lưu lượng cao.
