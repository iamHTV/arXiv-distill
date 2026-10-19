# [2610.11370v2] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees

## Core value (1 sentence)
RIT-RAG combines content-based retrieval with structure-aware navigation: retrieval proposes where to look across the whole corpus, and the LLM agent decides what to read by navigating query-induced sub-trees — balancing recall (broad retrieval) and precision (selective reading) without committing to a single document upfront.

## Problem
Prior work failed to solve the tension between agentic RAG (high recall, low precision — operates at chunk level without document structure) and structure-aware RAG like PageIndex (high precision, low recall — must commit to one document before seeing its content, and the full corpus structure does not fit in the LLM context).

## Contribution
- Introduces RIT-RAG (Retrieval-Induced Tree RAG): a framework combining content retrieval with structure-aware navigation; offline builds a tree per document from its table of contents or sitemap; at query time retrieves a broad set of chunks and uses their positions to induce manageable sub-trees, potentially spanning multiple documents.
- An LLM agent navigates these sub-trees, selectively reads promising nodes, and reformulates queries when needed — retrieval proposes where to look, the agent decides what to read.
- Introduces EntQABench, a new benchmark over EntDocs — a corpus of 2.84 million webpages from a large enterprise's product documentation — to evaluate RAG systems at realistic corpus scale.
- Evaluates on three public datasets (WixQA, QASPER, FinanceBench) and EntQABench; RIT-RAG achieves the highest accuracy among vanilla, graph-based, and agentic baselines.

## Method
Offline: build a tree Ti for each document di from its table of contents or sitemap. Each node v owns text cv under it but not under its children; metadata includes title, summary, keywords. Serialization S(Ti) converts the tree into a JSON string (node ID, metadata, children list) consumable by the LLM. At query time: the retriever returns top-k′ > k chunks Rk′(q~) from a hybrid BM25+dense index. Each chunk c belongs to exactly one node node(c). Node score s(v, q~) = max sim(q~, c) over chunks of node v. Select the n highest-scoring nodes Nq~, expand with their ancestors path(v) to form Vq~, inducing a query-dependent sub-forest Fq~ (one sub-tree per document containing a node in Nq~). Represent Fq~ as string S(Fq~), listing sub-trees in decreasing order of their top node score. The LLM agent works in rounds: each round t, the agent formulates a search query q~t and calls GetToC to get S(Fq~t), reasons over it to select nodes St, and reads their text cv via the Read tool. Based on contents, the agent may generate the answer, read more nodes from the same sub-forest, or reformulate the query for the next round. The agent stops when it generates the answer or reaches budget B tool calls (at most Bs GetToC calls).

## KNOWLEDGE — Data & figures
- Datasets: WixQA (200 expert-written customer-support questions over 6,221 help-center pages), QASPER (1,372 answerable test questions over 416 NLP papers), FinanceBench (150 financial questions over 364 SEC filings in PDF), EntQABench (317 synthetically generated questions over 3 products, EntDocs corpus of 2.84 million webpages).
- Models: Claude Haiku 4.5, GPT-5-mini, GPT-5.6-Luna; structure induction uses Qwen3-32B (cost reduction) or Haiku.
- Retriever: hybrid BM25 + dense with gte-modernbert-base + FAISS, chunks up to 512 tokens.
- Hyperparameters: k′ = 200 chunks, n = 50 nodes, B = 10 tool calls, Bs = 3 GetToC calls.
- Accuracy judged by LLM (Gemini 2.5 Flash) comparing prediction to gold answer; also precision/recall/F1 of passages read vs gold evidence; preprocessing cost, API cost, per-query latency.
- Results: RIT-RAG highest accuracy on all three public datasets and all three LLMs.
- vs Agentic Search (same retriever, same LLM, same budget B=10): +10.5, +5.0, +4.5 points on WixQA; +2.4, +2.9, +3.5 points on QASPER (Haiku, GPT-5-mini, Luna).
- vs PageIndex: +2.0–5.0 points on WixQA; +12.2–13.3 points on QASPER.
- FinanceBench (induced ToC): RIT-RAG beats best baseline by +9.3, +8.0, +4.6 points; beats PageIndex by +8.7–18.6 points.
- EntQABench (2.84M webpages): RIT-RAG beats strongest baseline by +6.6, +7.9, +11.4 points.
- Retrieval analysis: RIT-RAG achieves highest F1 on all three datasets; highest precision and recall on FinanceBench; highest recall on WixQA; ranks second on both metrics on QASPER.
- Online cost: RIT-RAG 5.7–13.3 cents/question vs Agentic Search 1.3–6.3 cents; on EntDocs roughly equal (6.0 vs 6.2 cents).
- Offline preprocessing cost: $20.4 (WixQA), $17.0 (QASPER), $773 (FinanceBench, inducing ToCs of 364 long filings), $0 (EntDocs — existing structure, only node titles); graph-based methods: $86–107 (WixQA), $1.3K–$1.7K (FinanceBench), $106K–$131K (EntDocs).
- arXiv category: cs.AI

## INSIGHT — Mechanism & why
[Agentic RAG high recall / low precision; PageIndex opposite; RIT-RAG balances both] BECAUSE [RIT-RAG uses retrieval to cast a wide net across the corpus (recall) and induced sub-trees for the agent to read selectively (precision)]. This means [separating evidence discovery from content reading optimizes both metrics].
[RIT-RAG does not commit to a single document] BECAUSE [each search induces a new sub-forest that may span multiple documents; the agent is never committed to documents from an earlier round and can reformulate the query to surface different documents]. This means [avoids the early-commitment problem of PageIndex where a wrong document choice blocks recovery].
[RIT-RAG scales to million-page corpora better than PageIndex] BECAUSE [it does not need to fit the full corpus structure into the LLM context; the presented structure size is bounded by selected nodes and their ancestors, not corpus size]. This means [query-induced tree construction scales to substantially larger corpora].

## IDEA — What to apply
Apply RIT-RAG to an enterprise RAG system with a large technical documentation corpus: step 1 is to build a structure tree per document from its ToC/sitemap, use retrieval to cast a wide net, then guide the agent to query-induced sub-trees around retrieved chunks.
Use query-induced tree construction instead of single-document selection: step 1 is to link each retrieved chunk with structural metadata (node ID, title, ancestor IDs and titles) to reconstruct the sub-tree at inference time.

## WISDOM — General principle
Principle: Separate evidence discovery from content reading — retrieval ensures recall, structure-aware navigation ensures precision; do not commit to a single document before seeing its content.

## Assumptions & Limitations
- Conditions for validity: documents have a hierarchical structure (ToC, sitemap, breadcrumbs) or structure can be induced; queries require navigation over a large document collection.
- Limitations acknowledged by the paper: RIT-RAG accumulates fetched nodes until context budget is reached, with no evidence compaction or chat-history eviction; ignores cross-links between nodes at the same tree level; depends on a usable document hierarchy — weak headings or poor parsing can limit structure quality.
- Limitations the paper does NOT mention: operational cost of multiple reasoning rounds at scale; stability of accuracy across repeated runs; latency impact of multiple GetToC calls.

## Metadata
- Year: 2026
- Authors: Meghanadh Pulivarthi, Swaraj Kumar Biswal, Kushagra Bhushan, Yatin Nandwani, Sachindra Joshi, Dinesh Raghu (IBM, IIT Kharagpur)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.11370v2
- arXiv ID: 2610.11370v2
- Label: [applied]
- Skill: rit-rag | Test: [SKILL VALID]
