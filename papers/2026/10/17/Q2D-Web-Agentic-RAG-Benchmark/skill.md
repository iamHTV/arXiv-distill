# Skill: q2d-web-retriever-evaluation
Source: 2609.08887v2
Type: evaluation-method

## Khi nào dùng skill này
- Xây dựng hoặc đánh giá bộ tìm kiếm đầu tiên (first-stage retriever) trong hệ thống RAG sản xuất (production RAG).
- Cần đánh giá trên corpus lớn và truy vấn do agent định dạng lại (agent-reformulated queries), không chỉ truy vấn do con người viết.
- Muốn giảm chi phí đánh giá bằng cách lấy mẫu một phần của corpus (subcorpus sampling) mà vẫn giữ thứ hạng mô hình.

## Tình huống KHÔNG nên dùng
- Đánh giá trên corpus nhỏ (ít hơn hàng triệu tài liệu).
- Chỉ có truy vấn do con người viết, không có truy vấn do agent định dạng lại.
- Không cần đánh giá bộ tìm kiếm đầu tiên, chỉ đánh giá bộ xếp hạng lại (reranker) thứ hai.

## Input cần có
- Tập hợp tài liệu lớn (large-scale corpus), ví dụ: ~190M tài liệu web.
- Tập truy vấn do agent định dạng lại (agent-reformulated queries) dựa trên truy vấn của người dùng thực.
- Ba tập hợp phán xét liên quan (relevance-judgment sets): trích dẫn của agent (agent citations), xếp hạng sản xuất (production rankings), và tập kết hợp (combined set).
- 13 bộ retriever để đánh giá (lexical, dense, late-interaction).

## Các bước thực hiện
1. Xây dựng chuẩn mốc Q2D-Web: lấy mẫu truy vấn từ các cuộc gọi tìm kiếm của agent, lắp ráp và loại bỏ trùng lặp tập hợp tài liệu, xây dựng ba tập hợp phán xét liên quan.
2. Lấy mẫu một tập hợp đánh giá con (evaluation subcorpus) trong khi giữ lại tất cả các mẫu dương đã gắn nhãn (labeled positives).
3. Chấm điểm 13 bộ retriever (lexical, dense, late-interaction) trên ba tập hợp phán xét.
4. So sánh thứ tự tương đối của các retriever qua các miền chủ đề (topical domains), ngôn ngữ truy vấn (query languages), và loại truy vấn (query types).
5. Để giảm chi phí đánh giá, lấy mẫu một phần của corpus bằng reciprocal rank fusion (RRF) qua các lần chạy retriever đã pooled (pooled retriever runs) — giữ lại 1/3 corpus bảo toàn thứ hạng mô hình của corpus đầy đủ.
6. Đánh giá Recall@1000, Recall@100, và nDCG@10 trên cả corpus đầy đủ và corpus đã lấy mẫu.

## Output mong đợi
- Thứ hạng mô hình (model ranking) của 13 retriever trên ba tập phán xét.
- Xác nhận rằng lấy mẫu 1/3 corpus bằng RRF bảo toàn thứ hạng mô hình của corpus đầy đủ trong khi nâng Recall@1000 chỉ 4–7 điểm.

## Ví dụ áp dụng
- Xây dựng hệ thống RAG sản xuất: đánh giá bộ tìm kiếm đầu tiên trên corpus lớn (~190M tài liệu) với truy vấn do agent định dạng lại, dùng RRF để lấy mẫu 1/3 corpus để đánh giá nhanh mà vẫn giữ thứ hạng mô hình.

## Gotchas
- Đánh giá tập trung trên tập dữ liệu cố định (fixed-corpus); sự chuẩn hoá sang corpus khác và tìm kiếm trên web trực tiếp chưa được nghiên cứu.
- Thứ tự tương đối của các retriever hầu như không phụ thuộc vào lựa chọn tập hợp phán xét, nhưng khác biệt đáng kể giữa các miền chủ đề, ngôn ngữ truy vấn, và loại truy vấn.
- pplx-embed-v1-4b thắng tất cả ba tập phán xét trên Recall@1000; Nemotron-3-Embed-8B mạnh nhất trên Recall@100 và nDCG@10 dưới Combined.
