# [2610.22588v1] SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV

## Problem
- Multi-hop retrieval (truy xuất nhiều bước — câu hỏi cần facts từ nhiều passage, passage A đặt tên birthplace, passage B mới dùng được sau khi biết birthplace) yêu cầu retrieval infrastructure đắt đỏ: dense retrieval (truy xuất vector) cần precompute embedding toàn corpus + vector database; structure-augmented (SAG tiền nhiệm) cần LLM extraction event–entity + MySQL + Elasticsearch + embedding. Prior work chưa chứng minh multi-hop accuracy mạnh với infrastructure tối thiểu.

## Contribution
- SAG2: embedding-free (không cần embedding model) multi-hop retrieval architecture = 1 SQLite database duy nhất + BM25 + contextual evidence decisions từ JEV (decision model chuyên biệt qua Noul interface — nhận natural-language context, trả yes-probability per decision, KHÔNG sinh reasoning text trung gian).
- Thay thành phần SAG: event–entity records + dense indexes → lexical index over original passages; associations online qua passage-to-term-to-passage expansion (passage chọn → terms → passage mới); moved semantic evidence selection to query time → loại bỏ offline embedding computation, LLM event–entity extraction, dedicated database servers.
- passage-to-term-to-passage procedure với contextual evidence scores guide expansion + newly retrieved passages update context cho decisions sau.

## Method (tóm tắt cốt lõi)
- Indexing (offline, 0 model call): normalize + tokenize (Jieba cho CJK + handling Latin), stopwords, group paragraphs ≤2,200 chars, SQLite FTS5 (fields title/heading/body, BM25 weights 2/2/1) + original text + body-level document frequencies.
- Retrieval (online): C0 = BM25 top B=100 (OR ≤80 query tokens); scoring s_r(d) = J(q,d;E_r) ∈ [0,1] — JEV prompt hỏi candidate có supplies necessary fact trong fully supported answer chain (kể cả intermediate identification fact), topical association insufficient, no outside-knowledge inference; E0=∅, E1 = seeds + first 10 new, final round reconsider previous top-10 với tentative prior scores.
- Expansion: seeds S_r = top s=10 unexpanded; term priority a_r(t) = max_d [(1+log tf)·I(t)·(1+g_q(t,d))·w_r(d)], I(t)=log(1+(N−df+0.5)/(df+0.5)), w_r∈[0.5,1] (downweight low-score seeds); top L=20 terms; per-term unseen BM25 lists interleaved by priority order, dedup ≤100 new candidates (phải match expansion term; original-query term optional → bridge term possible); H=2 expansions (≤3 scoring rounds), max 340 passage judgments/question; local DPP diversity reorder TOP-10 only (sparse TF-IDF overlap, preserve #1 + set, no model call).

## Key Findings
- Recall@10 hàng đầu cả 3 benchmarks (1,000-question subsets): MuSiQue 86.62%, 2WikiMultiHopQA 97.43%, HotpotQA 99.00% — beat SAG +3.25/+3.86/+1.30pp; beat BM25 +32.21/+25.93/+12.10pp. MuSiQue complete-evidence coverage (AllEvidence@10) 17.40% (BM25) → 69.50%.
- Baselines MuSiQue R@10: BM25 54.41, Contriever 53.58, BGE-Large 64.08, GTE-Qwen2-7B 70.80, GritLM-7B 75.19, NV-Embed-v2 77.27, HippoRAG2 73.76, SAG 83.37 → SAG2 86.62 (beat mọi 7B embedding model + structure-augmented). SAG retains R@1/R@2 lead on MuSiQue (advantage strong hơn khi reader có nhiều passages).
- EnterpriseRAG-Bench (511,962 documents, chunks ~1,000 chars): document Recall@10 SAG2 81.10% overall vs BM25 68.4 / Vector 46.0 / Bash Agent 55.8; project-related 83.58%, completeness 76.24%, intra-document 100.00%, constrained 96.67%, conflicting 92.50%, basic 86.86%, semantic 58.40% (hardest).
- Ablations (MuSiQue, paired 95% bootstrap 2,000 resamples): expansion 1 → R@10 67.93→83.36 (+15.43 [14.09,16.81]), 2 → 86.62 (+3.26 [2.52,4.02]); 1 expansion dùng 36.29% fewer judgments (lower-cost operating point); expansion recovers passages absent from initial top-100 trên 389/1,000 questions.
- Budget control: one-shot BM25+JEV pool with matched judgments (329,194 vs 331,325, 0.64% shortfall) → R@10 69.82 / AE@10 39.60 vs SAG2 86.62/69.50 (+16.80 [15.28,18.33]) — bigger one-shot pool KHÔNG thay được contextual expansion.
- Context ablation: removing shared scoring context → R@10 76.25 (−10.37 [9.11,11.64]), AE@10 52.20 — retrieved context drives evidence selection + expansion.
- Cost: index 11,656 passages in 2.36 giây, 25.87 MiB SQLite, 0 offline model calls/$0; JEV charges $0.433769/100 queries, $4.326379/1,000 queries (exclude machine rental + answer generation); model typesafe/jev-1.13-20260917 qua OpenRouter; concurrency cap 20.
- MuSiQue subset composition: 518 two-hop, 316 three-hop, 166 four-hop questions.

## Actionable Insights
- Build knowledge-base retrieval với 1 SQLite FTS5 + hosted decision model — KHÔNG cần vector DB, embedding service, hay MySQL/Elasticsearch stack: index minutes-thousands of passages trong vài giây, deploy trên 1 file. Ví dụ: solopreneur có 500 help-center articles → SQLite FTS5 index trong ~1s, multi-hop questions answered via BM25+JEV pipeline với cost ~$4.3/1,000 queries (JEV charges).
- Đừng giải multi-hop bằng cách nhét candidate pool lớn hơn (one-shot): +judgment budget 329K một lượt R@10 chỉ 69.82% vs 86.62% của contextual expansion — budget cho expansion 2 rounds (H=2) thay vì pool B=100→200. Ví dụ: RAG pipeline doanh nghiệp mở rộng depth không breadth.
- Dùng tổ hợp local BM25 + contextual decision model riêng biệt (JEV-class) thay vì embed-model monoculture: lexical blocks paraphrase fail nhưng expansion bridging terms rescue 389/1,000 questions; và decision model đánh evidence-IN-context không theo similarity standalone. Ví dụ: dùng JEV/Noul-style yes-probability scorer cho pipeline evidence selection.

## Assumptions & Limitations
- Điều kiện: access được hosted JEV decision service (qua OpenRouter); corpus text có lexical term connections giữa các passage (bridge terms); question distribution tương tự multi-hop QA benchmarks.
- Paper thừa nhận: JEV architecture/params/weights KHÔNG public → system không thể fully on-prem với public artifacts; phụ thuộc provider availability/throughput, questions+candidate text phải gửi service → không dùng where external processing prohibited; không isolate term-weight factors hoặc prove JEV superior to other decision models; fixed dev subsets, MuSiQue used during development (overfit risk); EnterpriseRAG-Bench corpus synthetic; lexical access misses paraphrases/aliases/evidence without term overlap; four-hop complete-evidence coverage still low; cost study 1 corpus — scaling + incremental updates unmeasured; online latency not reported.
- Limitation paper KHÔNG nói: retrieval-only metrics — answer generation NOT evaluated (recall cao ≠ answer quality); JEV $4.33/1,000 queries vs self-hosted embedding model cost comparison unfair (hosted pricing); JEV service outage = hệ thống chết (single point of failure); concurrency cap 20 giới hạn throughput; DPP diversity local heuristic chưa ablation riêng; candidate B=100 cap với corpus lớn có thể miss rare passages.

## Metadata
- Năm: 2026 | Tác giả: Yuchao Wu (Zleap AI) | Category: cs.CL | PDF: https://arxiv.org/pdf/2610.22588v1 | Citation: [NO DATA — published 15 Oct 2026] | Code: https://github.com/Zleap-AI/SAG-Benchmark
