# Skill: rag-retrieval-strategy-comparison
Source: 2609.38473v1
Type: framework

## Khi nào dùng skill này
- Xây hệ thống RAG cho tra cứu tài liệu chuyên ngành (scientific/technical documents).
- Muốn chọn chiến lược retrieval phù hợp (top-k, re-ranking, ColBERT, agentic tool-call).
- Có corpus tài liệu và câu hỏi tham chiếu để đánh giá.

## Tình huống KHÔNG nên dùng
- Không có corpus tài liệu để truy xuất.
- Chỉ cần tìm kiếm đơn giản, không cần so sánh nhiều chiến lược.

## Input cần có
- Corpus tài liệu (ví dụ 463K paper arXiv hoặc tài liệu doanh nghiệp).
- Bộ câu hỏi tham chiếu với đáp án chuẩn (gold papers).
- Các chiến lược retrieval đã triển khai (top-k, rewriting, re-ranking, ColBERT, etc.).

## Các bước thực hiện
1. Triển khai 6 chiến lược retrieval: classic top-k dense, query rewriting, re-ranking, RRF, agentic tool-call, ColBERTv2 late interaction.
2. Chạy trên cùng corpus và dataset câu hỏi.
3. Đo answer rate, Hit@3, mean paired delta versus Classic baseline với 95% CI.
4. Chọn chiến lược có answer rate cao nhất và Hit@3 cao nhất (ColBERTv2 thường là tốt nhất).
5. Không dùng query rewriting đơn lẻ không kèm re-ranking.

## Output mong đợi
- ColBERTv2: answer rate 99.9%, top-3 gold paper 92.8–94.8%.
- Rephrased & Reranked: pooled +0.18 delta vs Classic.
- Tool Call: thấp nhất (96.9–98.3% answer rate).

## Ví dụ áp dụng
Solopreneur xây hệ thống tra cứu tài liệu pháp lý: triển khai ColBERTv2 late interaction cho retrieval, kết hợp re-ranking sau khi rewrite truy vấn. Đánh giá trên corpus văn bản pháp lý và câu hỏi tham chí, chọn chiến lược có answer rate cao nhất.

## Gotchas
- Rewriting alone làm giảm chất lượng retrieval (Hit@3 39.7% vs 46.3% Classic) — luôn kèm re-ranking.
- Tool Call agentic model có answer rate thấp nhất — không nên dùng làm chiến lược chính.
- Cần corpus và câu hỏi tham chiếu để đánh giá đúng chiến lược.
