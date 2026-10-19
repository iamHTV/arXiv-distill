# [2609.05110v1] Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval

## Core value (1 sentence)
Embedding surgery is a lightweight approach for adaptive ranking correction in dense retrieval: apply localized, minimal updates to retrieved document embeddings at query time, guided by editorial feedback, user interactions, or LLM pseudo-labels, formulated as a convex optimization problem enforcing ranking constraints while minimizing modifications to affected document representations.

## Problem
Prior work failed to solve the rigidity of dense retrieval systems (core components of search engines, recommendation platforms, and RAG pipelines): document embeddings are computed offline and stored in static indexes, making it difficult to adapt to user feedback or evolving search intent. Prior approaches (fine-tuning encoders + re-indexing) are computationally expensive and unsuitable for timely correction of specific ranking errors.

## Contribution
- Introduces embedding surgery, a lightweight approach for adaptive ranking correction in dense retrieval via localized, minimal updates to document embeddings at query time.
- Formulates embedding surgery as a constrained convex optimization problem (quadratic program) that enforces ranking constraints derived from feedback while minimizing modifications to affected document representations; closed-form solution for a single pairwise constraint; efficient QP solvers for batches of constraints.
- A unified framework integrating embedding surgery with editorial, click-based, and LLM-derived feedback in dense retrieval pipelines.
- Extensive evaluation across four dense retrieval models (Contriever, TAS-B, E5 multilingual, Snowflake-Arctic Embed) and seven IR benchmarks (TREC DL 2019/2020, DL-Hard, TREC Robust '04, TREC CAsT 2019, MS MARCO, QSharedRel).
- Large-scale analysis over 56k queries on ANN index structures (IVF, HNSW), showing updates remain localized, preserve retrieval effectiveness, and can be applied safely and efficiently via in-place overwriting without costly index reconstruction.

## Method
Dense retrieval: vector-based IR paradigm where queries and documents are independently encoded into a shared latent space using a bi-encoder architecture, trained jointly with contrastive learning; similarity computed via inner product or cosine similarity. Document embeddings are precomputed offline and indexed using ANN systems (FAISS, Falcon, ScaNN, HNSW, MRNG). Formally, let q ∈ R^d be the query embedding and di ∈ R^d the document embedding; score(q, di) = ⟨q, di⟩; top-k documents π = [d1, ..., dk] are returned. Embedding surgery applies small, localized modifications to document embeddings so the resulting ranking better reflects feedback signals while preserving global structure of the embedding space. Given query q with embedding q and ranked list π = [d1, ..., dk], assume feedback signals R specifying desired corrections. Each element of R is a pairwise preference (dr, dn) where both belong to π, indicating dr should be ranked above dn for query q. Embedding surgery computes updates Δdi to embeddings of retrieved documents that enforce these constraints while minimizing overall perturbation. Optimization: minimize Σ∥Δdi∥2^2 subject to ⟨q, dr + Δdr⟩ ≥ ⟨q, dn + Δdn⟩ + ε, ∀(dr, dn) ∈ R. Δdi is the correction applied to original embedding di; ∥·∥2 is L2 norm penalizing large deviations; ε > 0 defines margin enforcing separation between relevance scores. Objective encourages minimal movement in embedding space; constraints guarantee resulting ranking consistent with feedback. Problem is convex and quadratic, admits unique global optimum, solvable efficiently with standard solvers (e.g., CVXPY). Corrected embeddings: d'i = di + Δdi. Variants: symmetric (default, both embeddings adjust — balanced correction minimizing total movement while satisfying feedback); demotion (Δdr = 0, only less relevant modified — demotes less relevant document); promotion (Δdn = 0, only more relevant modified — promotes more relevant document upward). Feedback models: editorial (human relevance judgments, gold standard), click-based (counterfactual models: Perfect P, Noisy N, Near-Random R user models with selection bias, position bias, relevance bias; pc(q,d,i) = p̂r(q,d) · p̂e(i), k′=20, p̂e(i)=1), LLM-based (BGE, Qwen rerankers providing pseudo-labels). For each query, retrieve top-20 results and apply embedding surgery. Use FAISS Flat indexes for RQ1/RQ2/RQ4; IVF and HNSW for RQ3. Optimization solved with cvxpy library on single CPU core (AMD Rome 7742, 2.25 GHz). Margin ε set to minimum between score difference within each constrained pair and fixed threshold 0.01. Embeddings not re-normalized after applying Δdi; scores computed as raw inner products; relative norm change bounded by small update magnitudes. Optimization performed independently per query; updates applied immediately to index. Only embeddings of documents involved in constraints are modified; all other document embeddings remain unchanged.

## KNOWLEDGE — Data & figures
- Dense retrieval: vector-based IR paradigm; bi-encoder; contrastive learning; inner product/cosine similarity.
- ANN: Approximate Nearest Neighbor — FAISS, Falcon, ScaNN, HNSW, MRNG.
- Embedding surgery: localized, minimal updates to document embeddings at query time for ranking correction.
- Convex optimization (quadratic program): enforces ranking constraints while minimizing embedding changes.
- Kendall Tau distance (KD): counts pairwise inversions between pre-surgery and target rankings.
- Swap Accuracy: percentage of document pairs correctly ordered after surgery.
- nDCG@k: Normalized Discounted Cumulative Gain — quality of top-k retrieved documents accounting for graded relevance and ranking position.
- RR/MRR: Reciprocal Rank / Mean Reciprocal Rank — for datasets with single relevant item per query.
- 4 models: Contriever, TAS-B, E5 (multilingual), Snowflake-Arctic Embed — all zero-shot, no task-specific fine-tuning.
- 7 benchmarks: TREC DL 2019 (43 queries), DL 2020 (54 queries), DL-Hard (challenging subset), TREC Robust '04 (249 queries, zero-shot out-of-domain since models fine-tuned on MS MARCO), TREC CAsT 2019 (20 conversational sessions, ~10 turns each), QSharedRel (346 queries from MS MARCO Dev, query pairs sharing at least one relevant passage; 169 focal queries), MS MARCO Dev (~56k judged queries for large-scale analysis).
- 3 feedback sources: editorial (expert assessors, high quality), click-based (counterfactual user models P/N/R), LLM-derived (BGE, Qwen rerankers as pseudo-labels).
- Results: consistent improvements, up to +60.64% relative nDCG@10 (TAS-B on DL-Hard under editorial feedback).
- Symmetric variant best across all datasets except Robust '04 (close to demotion).
- Contriever, editorial feedback: nDCG@10 0.674→0.845 (DL '19), 0.672→0.878 (DL '20), 0.377→0.591 (DL-Hard), 0.466→0.687 (Robust '04).
- Click-based perfect user (P) after 1,000 clicks: 0.702, 0.700, 0.454, 0.486 for DL '19, DL '20, DL-Hard, Robust '04.
- Robust to noisy feedback; Near-random (R) yields limited gains but does not degrade original retrieval effectiveness (except marginal, statistically nonsignificant decrease on Robust '04).
- LLM-based: BGE reranking; stable gains, smallest +3.59% (Snowflake, DL '19), largest +24.56% (E5, Robust '04).
- Ranking corrections propagate to semantically related queries (QSharedRel).
- Complements query adaptation methods such as CoRocchio, yielding additional gains while being more robust to noisy feedback.
- Large-scale: 56k queries on ANN indexes (IVF, HNSW); updates remain localized, preserve retrieval effectiveness, applied safely via in-place overwriting without costly index reconstruction.
- Computational cost: low; optimization solved with cvxpy on single CPU core.
- Code: https://github.com/maddalena-amendola/Embedding-Surgery
- arXiv category: cs.IR
- Venue: ACM CIKM 2026

## INSIGHT — Mechanism & why
[Dense retrieval becomes rigid after training] BECAUSE [document embeddings are computed offline and stored in static indexes, making it difficult to incorporate user feedback or adapt to evolving search intent]. This means [a lightweight, query-time update method is needed without retraining or re-indexing].
[Embedding surgery effectively corrects ranking errors] BECAUSE [it is formulated as a convex optimization problem (quadratic program) enforcing ranking constraints while minimizing modifications to affected document representations]. This means [localized, minimal updates preserve the global structure of the embedding space].
[The symmetric variant is most effective] BECAUSE [both embeddings are adjusted, creating a balanced correction that minimizes total movement while satisfying the feedback constraint]. This means [adjusting both directions (promoting the more relevant document and demoting the less relevant one) works better than changing only one side].

## IDEA — What to apply
Apply embedding surgery to an enterprise dense retrieval system: step 1 is to identify ranking errors via editorial feedback or user interactions, then apply localized updates to the embeddings of retrieved documents at query time.
Combine embedding surgery with CoRocchio (query adaptation): step 1 is to apply both — surgery adjusts document embeddings, CoRocchio adjusts query embeddings — for additional gains.

## WISDOM — General principle
Principle: Correct dense retrieval ranking errors with localized, minimal updates to document embeddings at query time (no retraining/re-indexing); corrections can propagate to semantically related queries and complement query adaptation methods such as CoRocchio.

## Assumptions & Limitations
- Conditions for validity: dense retrieval system; access to feedback signals (editorial/user interactions/LLM); query-specific ranking errors to correct.
- Limitations acknowledged by the paper: using LLM as assessor should be approached with caution (LLM-generated labels exhibit systematic weaknesses limiting their ability to fully replace human relevance assessments); Near-random click behavior yields limited gains and can marginally degrade original retrieval effectiveness (Robust '04, statistically nonsignificant).
- Limitations the paper does NOT mention: operational cost of solving the optimization problem per query at scale; stability of embedding updates across repeated applications; latency impact of running surgery at query time.

## Metadata
- Year: 2026
- Authors: Maddalena Amendola (IIT-CNR, Pisa, Italy), Antonio Mallia (Seltz, San Francisco, USA), Raffaele Perego (ISTI-CNR, Pisa, Italy)
- arXiv category: cs.IR
- PDF link: https://arxiv.org/pdf/2609.05110v1
- arXiv ID: 2609.05110v1
- Label: [applied]
- Skill: embedding-surgery | Test: [SKILL VALID]
