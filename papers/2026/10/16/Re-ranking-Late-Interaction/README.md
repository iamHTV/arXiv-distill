# [2609.38473v1] Re-ranking and Late Interaction Drive Retrieval Quality: A Controlled Comparison of RAG Strategies for Scientific Question Answering

## Problem
RAG (Retrieval-Augmented Generation - sinh tăng cường truy xuất) là cách chuẩn để ground (đoce) LLM vào kiến thức bên ngoài, nhưng không gian thiết kế của các pipeline retrieval rất lớn và các trade-offs (đổi khác) giữa chúng chưa được hiểu rõ, đặc biệt trên domain-specific corpora (bộ ngữ liệu chuyên ngành) ở quy mô thực tế.

## Contribution
- So sánh kiểm soát 6 chiến lược retrieval cho scientific question answering (trả lời câu hỏi khoa học): (i) classic top-k dense retrieval, (ii) query rewriting, (iii) re-ranking, (iv) RRF (Reciprocal Rank Fusion), (v) agentic tool-call retrieval, (vi) ColBERTv2 late interaction.
- Dùng 463K paper arXiv, dataset 19.484 câu hỏi.
- ColBERT đạt highest answer rates (99.9% on both query types).
- Late-interaction strategies retrieved gold paper in top 3 for 92.8–94.8% of queries — roughly double best single-vector pipeline.

## Method (tóm cốt lõi)
6 chiến lược retrieval được so sánh trên cùng corpus 463K paper arXiv và dataset 19.484 câu hỏi khoa học. Đo answer rate (tỷ lệ trả lời), Hit@3 (vị trí trong top 3), mean paired delta versus Classic với 95% confidence intervals.

## Key Findings
- ColBERT đạt highest answer rates (99.9% trên cả hai loại câu hỏi).
- Tool Call thấp nhất (98.3% problem, 96.9% method).
- ColBERT: +0.27 problem, +0.47 method; pooled +0.37 (95% CI [+0.36, +0.38]) versus Classic.
- Rephrased & Reranked: +0.13 problem, +0.23 method; pooled +0.18 (95% CI [+0.17, +0.19]).
- Fusion và Tool Call kém hơn đáng kể so với Classic.
- Late-interaction strategies lấy gold paper trong top 3 cho 92.8–94.8% câu hỏi — khoảng gấp đôi best single-vector pipeline (Rephrased & Reranked: 47.5% và 52.8%).
- Rewriting alone làm giảm retrieval trên problem queries (Hit@3 39.7% vs. 46.3% cho Classic) — rewriting không kèm re-ranking có thể drift away (lệch khỏi mục tiêu).

## Actionable Insights
- Dùng ColBERTv2 late interaction cho retrieval chất lượng cao: answer rate 99.9%, top-3 gold paper 92.8–94.8%. Áp dụng: solopreneur xây hệ thống RAG cho tra cứu tài liệu chuyên ngành nên dùng ColBERTv2 thay vì dense retrieval đơn thuần.
- Không dùng query rewriting đơn lẻ không kèm re-ranking: làm giảm Hit@3 từ 46.3% xuống 39.7%. Áp dụng: khi viết pipeline RAG, luôn kết hợp re-ranking sau khi rewrite truy vấn.

## Assumptions & Limitations
- Điều kiện: có corpus tài liệu khoa học và câu hỏi tham chiếu; không áp dụng nếu không có ground truth.
- Paper thừa nhận: đánh giá trên corpus arXiv khoa học, có thể khác trên domain khác.
- Limitation paper không nói: chưa đánh giá chi phí token/thực tế của từng chiến lược, chưa test trên nhiều ngôn ngữ.

## Metadata
- Năm: 2026
- Tác giả: Bhagyesh Rathi, Eshan Chawla, William B. Andreopoulos (San Jose State University)
- Category arXiv: cs.IR, cs.AI
- Link PDF: https://arxiv.org/pdf/2609.38473
