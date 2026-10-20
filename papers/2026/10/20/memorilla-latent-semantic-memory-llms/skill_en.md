# Skill: Latent Semantic Memory for Frozen LLMs (K soft memory tokens, 3-stage training)
Source: 2610.21375v1
Type: framework / evaluation-method

## When to use this skill
- An assistant/agent must draw on accumulated history (user preferences, long docs, a knowledge base) WITHOUT re-sending the entire history every query (cost/latency) — full context uses 1,974x (PMv2) more tokens and is NOT more accurate.
- Query wording often differs from stored wording (preferences, indirect questions) -> similarity RAG is weak.
- Multi-entity relational reasoning across documents is needed (FactKG-style claim verification, personalization combining).
- An agent must continually learn from its own experience without overwriting prior knowledge (TextWorld-style).
- Do NOT use: small corpora (<~1,000 document tokens — MEMORILLA LOSES on PubMedQA 59 vs 69); tasks requiring 100% exact entity recall (verbatim names/IDs/numbers — use RAG or a hybrid); latency budgets on small corpora (LLM decoding dominates anyway — gains appear only for large collections); no capacity to train a 3-stage curriculum (3.3M examples + 194M params + 2 frozen models).

## Inputs needed
- Frozen document encoder (paper: Qwen3-Embedding-4B) + frozen query encoder + frozen LLM decoder (paper: Qwen3-8B; TextWorld: Qwen3-4B-Instruct-2507) — encoder and decoder must come from compatible families (cross-family transfer untested).
- Document collection chunked -> ZD (N x he) — encode ONCE and persist; re-encode only added/changed documents.
- 3-stage training data: paraphrase reconstruction (~2M Wikipedia) -> QA/reading-comprehension/summarization mixture (~1.3M, 10 datasets) -> target-benchmark train-split mixture; loss on answer positions only.
- (Agent continual) an environment with sparse reward + GRPO configs (G=16 rollouts); memory tokens K (16 supervised / 8 agent) prepended within the same input budget as the ICL baseline.

## Steps
1. **Build the persistent store**: embed the corpus once with the frozen document encoder -> ZD; persist to disk/memory. Query-independent -> reused for every query.
2. **Build + train the memory module**: K learned slots Q0 (shared) -> query conditioning (LayerNorm(Q0 + CrossAttn(Q=Q0, K=zq, V=zq))) -> L_ref Perceiver-style cross-attention over ALL N store embeddings -> projection Wproj (he -> hL) -> M=[m1..mK] soft memory tokens; train the 3-stage curriculum with answer-only NLL loss; keep encoders + decoder frozen.
3. **Inject + generate**: X_LLM = [m1..mK ; Pq] with standard RoPE; the frozen LLM generates (T=0). Each query injects only K tokens into the context (it does NOT grow with the corpus).
4. (Agent continual) **Each turn**: append the turn as a new document to ZD; compress the growing store into K=8 tokens placed before the prompt via the memory module (random init -> GRPO on environment reward ONLY); keep the input budget equal to the ICL baseline -> measure avg@3/pass@3.
5. **Monitor**: primary metric per benchmark + mean document tokens/query + Pareto position vs RAG and full context; latency; check exact-entity recall (names/IDs/numbers) degradation -> if critical, add a retrieval hybrid (the union oracle beats either method on every benchmark); check decision-threshold calibration on claim verification (FactKG: true claims are 89.5% of joint errors -> miscalibrated).

## Expected output
- A frozen LLM with query-conditioned memory: average quality 49.68 vs compact baselines <=41.92 (xRAG/LLMLingua-2/Mem0); 394x/113x/49x fewer tokens than full-context/RAG-50/MemoRAG (range 20x-4,212x); latency 0.74s vs 19.9s; Pareto frontier on every benchmark; TextWorld avg@3 0.242 / pass@3 0.375 vs ICL 0.186/0.250 (+30%/+50% relative); untrained memory UNDERPERFORMS ICL (0.153/0.225) — the value is in training.

## Example application
- Solopreneur customer-support assistant: embed 5,000 past conversations once; query "gift for my wife who likes hiking" -> 16 soft tokens capture wife + hiking + past purchases despite no lexical overlap -> personalized answer; RAG misses (wording never repeated), full context costs 1,974x tokens. PMv2-like quality 44.6 vs RAG 30.9.

## Gotchas
- Lossy on fine-grained facts: exact names/IDs/numbers — RAG wins "who/which" by +3.45/+2.93 ROUGE-L; use a memory+retrieval hybrid for exact recall.
- Small corpora LOSE: PubMedQA (324 tokens) MEMORILLA 59.00 vs LLMLingua-2 69.00 — quality/efficiency gains appear only for large collections.
- NOT drop-in: 194M trainable params + a 3-stage curriculum (~3.3M examples) + 2 frozen models (4B + 8B); untrained memory HURTS (below ICL) — taps alone are useless.
- Qwen-family pairing tested — encoder/decoder cross-family transfer untested; test before adopting other models.
- Miscalibrated claim-verification thresholds: true claims are 89.5% of joint errors on FactKG — calibrate the threshold post-hoc.
- Joint errors are combining failures (PV4: linking facts) — memory alone does not fix multi-hop linking; union with RAG needed.
- MemoRAG still wins where verbatim passages matter (NarrativeQA 21.80 ROUGE-1, PV4 67.88%) — measure per task before betting.
- PMv2/PV4 evaluation = cosine-nearest-neighbor among predefined choices — free-form generation quality is UNVERIFIED; synthetic personas (GPT-5) -> real-user generalization untested.

## Dry run test
- Hypothetical case (support assistant, 800 past chats + 300-doc KB): step 1 embed ZD once (frozen Qwen3-Embedding-4B); step 2 train memory module K=16 (curriculum: 2M paraphrase + 1.3M QA + target mixture); step 3 run 20 personalization + claim-verification test queries: memory answers 8/10 preference questions (RAG 4/10), FactKG-like accuracy 84% vs full-context 80%, tokens 41/query vs 12,000 full-context; step 4 TextWorld-style agent loop over 20 episodes: pass@3 0.35 vs ICL 0.24, budget exhaustion 58% vs 71%; step 5 monitor: Pareto frontier on 7/8 tasks, exact-name recall check -> add RAG hybrid for 2 ID-heavy queries. Output: frozen LLM with persistent memory, metrics measured -> meaningful -> [SKILL VALID].
