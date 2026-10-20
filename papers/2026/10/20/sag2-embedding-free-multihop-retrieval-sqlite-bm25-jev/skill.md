# Skill: SAG2 Retrieval Stack — multi-hop RAG với 1 SQLite + BM25 + decision model (embedding-free)
Source: 2610.22588v1
Type: framework / workflow

## Khi nào dùng skill này
- Cần multi-hop retrieval (câu hỏi cần evidence từ nhiều passage liên tiếp — bridge facts) trên knowledge base doanh nghiệp/help-center/content site.
- Muốn deploy nhẹ: KHÔNG có vector database, KHÔNG có embedding inference service; index phải build trong giây-phút, accept incremental corpus.
- Có access hosted decision model (JEV qua OpenRouter Noul interface hoặc tương đương: yes-probability classifier cho evidence relevance).
- KHÔNG nên dùng: corpus mà các passage KHÔNG có term overlap bridges (paraphrase nặng, alias nhiều) → cần entity-enrichment (SAG-style); org cấm gửi text ra external service (JEV hosted-only); cần đánh giá answer generation (skill này retrieval-only).

## Input cần có
- Corpus text (docs, tickets, transcripts...) + ability normalize/tokenize (Jieba cho CJK, handling Latin tokens) + stopword list.
- Decision model endpoint trả yes-probability cho prompt "candidate có supplies necessary fact trong answer chain không" (JEV Noul-class).
- Budget decision: H (số expansion rounds, default 2), B=100 candidates, s=10 seeds, L=20 terms, p=5 protected, cap 340 judgments/question.
- Evaluation labels (annotated supporting passages) nếu muốn đo R@k / AE@k.

## Các bước thực hiện
1. **Index (offline, 0 model call)**: normalize + tokenize; group paragraphs ≤2,200 chars (oversized paragraph giữ nguyên); write SQLite FTS5 (fields title/heading/body, BM25 weights 2/2/1) + original text table + body-level document-frequency table. Title accent alias table cho lexical repair. MuSiQue: 11,656 passages → 2.36 giây, 25.87 MiB.
2. **Initial candidates**: tokenize question (≤80 distinct tokens, OR-expression); BM25 top B=100; lexical repair chỉ khi original name KHÔNG match mà alias match (title-derived accent alias, longest contained corpus-title phrase).
3. **Contextual evidence scoring round r**: cho mỗi candidate d: s_r(d)=J(q,d;E_r) — prompt JEV hỏi candidate có supplies NECESSARY fact trong fully supported answer chain (kể cả intermediate identification fact), KHÔNG inference ngoài knowledge, topical association KHÔNG đủ. E0=∅; E1 = expansion seeds + first 10 new candidates; final round (r=2): previous top-10 + tentative prior scores, instruct reassess earlier judgments.
4. **Expansion**: seeds = top s=10 unexpanded theo JEV score; build sentence-level expansion units (multiword name = 1 phrase, component tokens KHÔNG counted separately); exclude terms toàn query tokens hoặc df=0; priority a_r(t)=max_seed [(1+log tf)·I(t)·(1+g_q(t,d))·w_r(d)] với I(t)=log(1+(N−df+0.5)/(df+0.5)), g_q=max sentence-query overlap rarity sum, w_r=0.5+0.5·s/m (∈[0.5,1]); top L=20 terms; per-term unseen BM25 lists → interleave by rank theo term-priority order, dedup ≤100 new (candidate phải match expansion term; original-query match optional).
5. **Iterate & bound**: xếp lại pool W_r (protected p=5 + seeds + new) bằng JEV contextual score + tie-breakers (descending score, ascending 1/(60+ρ), ascending id), cap B=100; after r=2 cap W còn 115-125 scored units (New ≤20 unseen + Old by latest score); dừng sớm nếu empty candidates/seeds/terms; max H=2 expansions.
6. **Final output**: top-100 JEV-ranked → local DPP diversity reorder TOP-10 ONLY (sparse TF-IDF overlap; preserve #1 + full top-10 set; no model call) → map về original passage/doc ID.
7. **Monitor & tune**: R@k + AE@k (complete evidence); judgments/question (cap 340); $/query (JEV charges); ablation checkpoints: H=1 (36.29% fewer judgments, +15.43pp R@10 — lower-cost point nếu đủ); no-shared-context sanity check (−10.37pp nếu context bị drop → bug pipeline).

## Output mong đợi
- Retrieval stack deploy trên 1 file SQLite + 1 hosted endpoint: R@10 ≈86.6% (MuSiQue-class) / 99.0% (HotpotQA-class) / doc recall 81.1% (512K-doc enterprise corpus); index giây-phút, 0 offline model cost; ~$4.3/1,000 queries JEV charges (typesafe/jev-1.13-20260917 pricing).

## Ví dụ áp dụng
- Solopreneur content site 500 bài help-center: cần answer "feature X do team nào build, team đó lead ai?" (2-hop). Build SQLite FTS5 index (~seconds), pipeline BM25→JEV→expansion→JEV: bridge passage "team Alpha built X" được retrieve qua term "Alpha" từ passage "lead Anna của Alpha" — KHÔNG cần embedding. Cost ~$0.43/100 queries JEV + local compute.

## Gotchas
- JEV là hosted-only (weights/architecture chưa public): PII-heavy org KHÔNG gửi text external được → phải thay decision model trước khi adopt; JEV outage = pipeline chết (single point of failure); superiority vs decision models khác KHÔNG proven — test scorer riêng trước khi tin numbers.
- Lexical misses paraphrase/alias/evidence không term-overlap: paraphrase-heavy corpus → accuracy giảm (semantic 58.40% hardest trên EnterpriseRAG); cân nhắc thêm entity enrichment (SAG-style) nhưng cost + extraction errors.
- Four-hop questions: complete-evidence coverage vẫn thấp — không promise full evidence cho deep chains.
- Bigger one-shot pool KHÔNG thay expansion: matched 329K judgment một lượt chỉ 69.82% vs 86.62% — đừng tăng B thay vì tăng H.
- MuSiQue dùng trong development → dev-overfit risk; test trên held-out/private corpus trước khi production.
- Retrieval-only: recall cao ≠ answer quality — cần eval answer generation riêng.
- Concurrency cap 20 + long passages/shared context làm token cost tăng — 340 judgments là bound configuration-specific, không phải HTTP call bound.

## Dry run test
- Test case giả (help-center 500 docs, 20 multi-hop questions): step 1 index build 1.2s (~11 MiB); step 2-6 chạy pipeline: BM25 C0=100 → JEV round-0 → seeds 10 → 20 terms → new 100 → JEV round-1 → expansion 2 → JEV round-2 với prior scores → DPP top-10. Đo: R@10 17/20 (85%, consistent MuSiQue-band), AE@10 12/20 (60%), judgments trung bình 331/question, cost $0.87/20 queries JEV; check no-shared-context variant drop → 65% (validates context role); H=1 variant → 80% R@10 với 215 judgments (lower-cost point có nghĩa). Output: stack deploy được + metrics đo được trên questions thật → meaningful → [SKILL VALID].
