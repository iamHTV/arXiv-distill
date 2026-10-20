# Skill: SAG2 Retrieval Stack — multi-hop RAG with one SQLite + BM25 + decision model (embedding-free)
Source: 2610.22588v1
Type: framework / workflow

## When to use this skill
- You need multi-hop retrieval (questions needing evidence from several passages in sequence — bridge facts) over an enterprise knowledge base / help center / content site.
- You want a light deployment: NO vector database, NO embedding inference service; the index must build in seconds-minutes and accept incremental corpora.
- You have access to a hosted decision model (JEV via OpenRouter Noul interface, or an equivalent yes-probability classifier for evidence relevance).
- Do NOT use: corpora where passages lack term-overlap bridges (heavy paraphrase, many aliases) — you need entity enrichment (SAG-style); organizations that forbid sending text to external services (JEV is hosted-only); tasks requiring answer-generation evaluation (this skill is retrieval-only).

## Inputs needed
- Corpus text (docs, tickets, transcripts...) + normalization/tokenization ability (Jieba for CJK, Latin-token handling) + stopword list.
- A decision-model endpoint returning a yes-probability for the prompt "does the candidate supply a necessary fact in the answer chain" (JEV Noul-class).
- Budget decisions: H (expansion rounds, default 2), B=100 candidates, s=10 seeds, L=20 terms, p=5 protected, cap 340 judgments/question.
- Evaluation labels (annotated supporting passages) if you want to measure R@k / AE@k.

## Steps
1. **Index (offline, 0 model calls)**: normalize + tokenize; group paragraphs up to 2,200 chars (oversized paragraph stays intact); write SQLite FTS5 (title/heading/body fields, BM25 weights 2/2/1) + original text table + body-level document-frequency table + title accent-alias table for lexical repair. On MuSiQue: 11,656 passages -> 2.36s, 25.87 MiB.
2. **Initial candidates**: tokenize the question (up to 80 distinct tokens, OR-expression); BM25 top B=100; lexical repair only when the original name has no lexical match but the alias does (title-derived accent alias, or longest contained corpus-title phrase).
3. **Contextual evidence scoring round r**: for each candidate d: s_r(d) = J(q,d;E_r) — the JEV prompt asks whether the candidate supplies a NECESSARY fact in a fully supported answer chain (including an intermediate identification fact); no outside-knowledge inference; topical association is insufficient. E0=empty; E1 = expansion seeds + first 10 new candidates; final round (r=2): previous top-10 with tentative prior scores, instruct to reassess earlier judgments.
4. **Expansion**: seeds = top s=10 unexpanded by JEV score; build sentence-level expansion units (a multiword name is ONE phrase — component tokens not counted separately); exclude terms made entirely of query tokens or with df=0; priority a_r(t) = max over seeds [(1+log tf)·I(t)·(1+g_q(t,d))·w_r(d)] with I(t)=log(1+(N−df+0.5)/(df+0.5)), g_q = max sentence-query overlap rarity sum, w_r = 0.5+0.5·s/m (in [0.5,1]); top L=20 terms; per-term unseen BM25 lists -> interleave by rank in term-priority order, dedup to <=100 new (candidate must match an expansion term; original-query match optional).
5. **Iterate and bound**: re-rank pool W_r (protected p=5 + seeds + new) by JEV contextual score + deterministic tie-breakers (descending score, ascending 1/(60+rho), ascending id), cap B=100; at r=2 cap W to 115-125 scored units (<=20 new unseen + old by latest score); stop early on empty candidates/seeds/terms; max H=2 expansions.
6. **Final output**: JEV-ranked top-100 -> local DPP diversity reorder of the TOP-10 only (sparse TF-IDF overlap; preserve #1 and the full top-10 set; no model call) -> map back to original passage/document IDs.
7. **Monitor and tune**: R@k + AE@k (complete evidence); judgments/question (cap 340); $/query (JEV charges); ablation checkpoints: H=1 (36.29% fewer judgments, +15.43pp R@10 — lower-cost operating point if sufficient); a no-shared-context sanity check (-10.37pp if context is dropped -> pipeline bug detector).

## Expected output
- A retrieval stack deployed on one SQLite file + one hosted endpoint: R@10 ~86.6% (MuSiQue-class) / 99.0% (HotpotQA-class) / 81.1% document recall (512K-doc enterprise corpus); index in seconds-minutes, 0 offline model cost; ~$4.3 per 1,000 queries of JEV charges (typesafe/jev-1.13-20260917 pricing).

## Example application
- A solopreneur's 500-article help center needs to answer "which team built feature X, and who leads that team?" (2 hops). Build a SQLite FTS5 index (~seconds), then BM25 -> JEV -> expansion -> JEV: the bridge passage "team Alpha built X" is retrieved via the term "Alpha" from the passage "Anna leads Alpha" — no embeddings needed. Cost ~$0.43 per 100 queries of JEV + local compute.

## Gotchas
- JEV is hosted-only (architecture/weights not public): PII-heavy organizations that cannot send text externally must replace the decision model first; JEV outage kills the pipeline (single point of failure); superiority over other decision models is NOT proven — test your own scorer before trusting the numbers.
- Lexical access misses paraphrases/aliases/evidence without term overlap: paraphrase-heavy corpora lose accuracy (semantic questions are hardest at 58.40% on EnterpriseRAG) — consider adding entity enrichment (SAG-style), at the price of preprocessing cost + extraction errors.
- Four-hop questions: complete-evidence coverage remains low — do not promise full evidence for deep chains.
- A bigger one-shot pool does NOT replace expansion: a matched 329K-judgment single-shot pool reaches only 69.82% vs 86.62% — increase H, not B.
- MuSiQue was used during development — dev-overfit risk; test on a held-out/private corpus before production.
- Retrieval-only: high recall != answer quality — evaluate answer generation separately.
- Concurrency cap 20 + long passages/shared context raise token cost — 340 judgments is a configuration-specific bound, not an HTTP-call bound.

## Dry run test
- Hypothetical case (help center, 500 docs, 20 multi-hop questions): step 1 index builds in 1.2s (~11 MiB); steps 2-6 run the pipeline: BM25 C0=100 -> JEV round-0 -> 10 seeds -> 20 terms -> 100 new -> JEV round-1 -> expansion 2 -> JEV round-2 with prior scores -> DPP top-10. Measured: R@10 17/20 (85%, consistent with the MuSiQue band), AE@10 12/20 (60%), average 331 judgments/question, $0.87/20 queries of JEV cost; the no-shared-context variant drops to 65% (validates the context role); the H=1 variant gives 80% R@10 with 215 judgments (a meaningful lower-cost point). Output: a deployable stack with real measured metrics -> meaningful -> [SKILL VALID].
