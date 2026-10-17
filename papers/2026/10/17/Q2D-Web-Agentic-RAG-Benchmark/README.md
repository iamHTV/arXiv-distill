# [2609.08887v2] Q2D-Web: A Large-Scale Benchmark for Retrieval in Agentic RAG Systems

## Problem
- Đánh giá bộ tìm kiếm đầu tiên (first-stage retriever) trong RAG sản xuất quy mô lớn cần một chuẩn mốc (benchmark) ghép một tập hợp tài liệu lớn (large-scale corpus) với một tập lớn các truy vấn tìm kiếm do agent định dạng lại (agent-reformulated search queries) dựa trên các truy vấn của người dùng thực và các chuỗi hội thoại (conversation threads), và gắn nhãn nhiều tài liệu liên quan (relevant documents) cho mỗi truy vấn. Prior work chưa giải quyết được khoảng trống đánh giá này: các bộ sưu tập quy mô lớn thường chỉ cung cấp một số ít truy vấn đánh giá, trong khi các chuẩn mốc có nhiều truy vấn thường chỉ chứa hàng triệu tài liệu. Hơn nữa, phần lớn các chuẩn mốc đánh giá các truy vấn do con người viết (human-written queries), trong khi các bộ tìm kiếm đầu tiên trong ống dẫn RAG do agent điều khiển (agentic RAG pipelines) phục vụ các truy vấn do máy định dạng lại (machine-written reformulations) mà phân phối (distribution) khác với hành vi tìm kiếm của con người.

## Contribution
- Q2D-Web (Query2Doc-Web) — một chuẩn mốc tìm kiếm agentic (agentic retrieval benchmark) lớn bao gồm một tập hợp tài liệu web khoảng 190 triệu tài liệu (~190M-document web corpus) và khoảng 70 nghìn truy vấn tìm kiếm agentic (~70k agentic search queries) trong mười ngôn ngữ (ten languages), được định dạng lại từ các truy vấn của người dùng thực thế trong các hệ thống sản xuất (production systems).
- Q2D-Web cung cấp ba tập hợp phán xét liên quan (relevance judgments) cố định: trích dẫn của agent (agent citations), xếp hạng sản xuất (production rankings), và một tập hợp kết hợp (combined set) hợp nhất cả hai tín hiệu và thêm phán xét dựa trên LLM (LLM-based judgments) của các tài liệu pooled chưa gắn nhãn để giảm sai sót âm (false negatives).
- Chấm điểm 13 bộ tìm retriever (retrievers) bao gồm từ vựng (lexical), dicht estructura (dense), và tương tác muộn (late-interaction) và tìm thấy rằng thứ tự tương đối (relative ordering) của chúng hầu như không phụ thuộc vào lựa chọn tập hợp phán xét (judgment set), trong khi khác biệt đáng kể giữa các miền chủ đề (topical domains), ngôn ngữ truy vấn (query languages), và loại truy vấn (query types).
- Để cho phép đánh giá nhanh (fast evaluation), cũng nghiên cứu lấy mẫu một phần của tập hợp tài liệu (subcorpus sampling) làm xấp xỉ cho đánh giá toàn bộ tập hợp tài liệu (full-corpus evaluations). Giữ lại một phần ba của tập hợp tài liệu (a third of the corpus), được chọn bằng fusión xếp hạng tương lai (reciprocal rank fusion — RRF) qua các lần chạy retriever đã pooled (pooled retriever runs), bảo toàn thứ hạng mô hình của toàn bộ tập hợp tài liệu (full-corpus model ranking) dưới các phán xét kết hợp (combined judgments) trong khi nâng độ chính xác Recall@1000 tuyệt đối chỉ 4–7 điểm.

## Method (tóm tắt cốt lõi)
- Ống dẫn xây dựng Q2D-Web (Q2D-Web construction pipeline): lấy mẫu truy vấn từ các cuộc gọi tìm kiếm của agent (agent search calls), lắp ráp và loại bỏ trùng lặp (deduplicate) tập hợp tài liệu, xây dựng ba tập hợp phán xét liên quan (relevance-judgment sets), và lấy mẫu một tập hợp tài liệu đánh giá con (evaluation subcorpus) trong khi giữ lại tất cả các mẫu dương đã gắn nhãn (labeled positives).
- Ba tập hợp phán xét liên quan: trích dẫn của agent (agent citations), xếp hạng sản xuất (production rankings), và tập hợp kết hợp (combined set) hợp nhất cả hai tín hiệu và thêm phán xét dựa trên LLM của các tài liệu pooled chưa gắn nhãn.
- 13 bộ retriever bao gồm lexical, dense, và late-interaction models.
- Lấy mẫu một phần của tập hợp tài liệu (subcorpus sampling): giữ lại một phần ba của corpus, chọn bằng reciprocal rank fusion (RRF) qua các lần chạy retriever đã pooled, bảo toàn thứ hạng mô hình của toàn bộ corpus dưới các phán xét kết hợp.

## Key Findings
- 7 tác giả từ Perplexity AI, category arXiv: cs.IR.
- ~190 triệu tài liệu web, ~70 nghìn truy vấn, 10 ngôn ngữ.
- Thứ tự tương đối của các retriever hầu như không phụ thuộc vào lựa chọn tập hợp phán xét, nhưng khác biệt đáng kể giữa các miền chủ đề, ngôn ngữ truy vấn, và loại truy vấn.
- Lấy mẫu 1/3 corpus bằng RRF bảo toàn thứ hạng mô hình của corpus đầy đủ trong khi nâng Recall@1000 chỉ 4–7 điểm.
- pplx-embed-v1-4b thắng tất cả ba tập phán xét (Citation, Web Ranking, và Comb.) trên Recall@1000.
- Nemotron-3-Embed-8B mạnh nhất trên Recall@100 và nDCG@10 dưới Combined.
- Mô hình tương tác muộn (late-interaction) kém hơn mã hóa dicht (dense encoders) cùng kích thước trên Recall@1000 3–5 điểm nhưng khoảng cách thu hẹp xuống tối đa 1 điểm trên nDCG@10.
- Họ Qwen3-Embedding: Recall@1000 cải thiện đơn điệu theo kích thước mô hình (0.6B→4B→8B: 58.68→62.78→65.32 trên Comb.).

## Actionable Insights
1. Đánh giá bộ tìm kiếm đầu tiên (first-stage retriever) trong RAG cần benchmark với corpus lớn và truy vấn do agent định dạng lại, không chỉ truy vấn do con người viết. Áp dụng: khi xây dựng hệ thống RAG sản xuất, đánh giá bộ tìm kiếm trên corpus lớn (~190M tài liệu) với truy vấn do agent tạo ra, không chỉ truy vấn thủ công.
2. Lấy mẫu một phần của corpus bằng reciprocal rank fusion (RRF) có thể giữ nguyên thứ hạng mô hình của corpus đầy đủ mà chỉ cần 1/3 corpus. Áp dụng: khi đánh giá bộ tìm kiếm trên corpus lớn, dùng RRF để lấy mẫu 1/3 corpus để giảm chi phí đánh giá mà vẫn giữ thứ hạng mô hình.

## Assumptions & Limitations
- Đánh giá tập trung trên tập dữ liệu cố định (fixed-corpus); sự chuẩn hoá sang corpus khác và tìm kiếm trên web trực tiếp cần được nghiên cứu thêm.
- Đánh giá 13 bộ retriever (lexical, dense, late-interaction).

## Metadata
- Năm: 2026, tác giả: Maximilian Schall, Sedigheh Eslami, Markus Krimmel, Antoine Chaffin, Louis Milliken, Bo Wang, Denis Bykov (Perplexity AI), category arXiv: cs.IR, link PDF: https://arxiv.org/pdf/2609.08887v2
