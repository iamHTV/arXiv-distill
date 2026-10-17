# [2609.30547v1] REALMS: An AI-Assistant Conversational System for Real-Time Exact Audience Sizing over High-Dimensional Nested Profiles

## Problem
- Audience sizing is critical for digital marketing, but traditional approaches (skeleton audiences, sampling, predictive modeling) suffer from delays, estimation errors, and poor scalability over high-dimensional profile data. Prior work does not address exact counting on millions of profiles and thousands of attributes using natural language in real time.

## Contribution
- REALMS (Real-time Exact Audience sizing via LLM-based Multi-attribute Search) — conversational system for exact audience sizing deployed in production on an enterprise customer data platform.
- Three key components: (1) categorical attribute retrieval using embedding-based vector search to dynamically identify relevant schema attributes without manual configuration; (2) LLM-powered NL2SQL pipeline with template-based in-context learning for accurate query generation over complex nested schemas; (3) schema standardization enabling industry-agnostic deployment across diverse enterprise environments.

## Method (core summary)
- Offline pre-processing: export and flatten hierarchical profile records into a columnar representation stored in a scalable analytical database; generate embeddings and build index asynchronously.
- Schema-aware attribute retrieval: encode user query into dense embedding, match against candidate attributes via semantic retrieval rather than hand-crafted rules or schema-specific mappings.
- LLM-driven structured query generation: construct prompts using retrieved schema context and reusable query templates; LLM translates natural-language audience definitions into executable SQL queries over complex nested profile structures.
- Schema standardization: materialize data into a standardized columnar representation that abstracts away source-specific differences and exposes a consistent query surface; decouples query generation from physical data organization.
- Five-stage runtime pipeline: schema-aware attribute retrieval, KG-RAG, LLM-powered semantic parsing, scalable query execution, result interpretation.

## Key Findings
- 4 authors from Adobe Inc., arXiv categories: cs.CL, cs.IR.
- Evaluation dataset: 600 natural-language audience-sizing requests, covering 3 query intents (count, top-k, percentage) and 1–3 attributes per query.
- Table III: Schema attribute retrieval — Recall@k 94%, Exact-match rate@k 93%; Structured query correctness — Execution match 90%, LLM-as-a-judge 95%.
- Table IV ablation: REALMS (Full) — Execution Match 90%, LLM-Judge 95%; w/o KG-RAG — 68%, 72%; w/o Schema Retrieval — 57%, 63%; Random Example Retrieval — 72%, 75%.
- Table V complexity: 1 attribute — Recall 100%, Execution Match 100%, LLM-Judge 99%; 2 attributes — Recall 98%, Execution Match 94%, LLM-Judge 97%; 3 attributes — Recall 93%, Execution Match 88%, LLM-Judge 93%.
- Table VI intent: Count — Recall 96%, Execution Match 95%, LLM-Judge 97%; Top-k — Recall 95%, Execution Match 88%, LLM-Judge 90%; Percentage — Recall 93%, Execution Match 92%, LLM-Judge 93%.
- Table II load test: 10–30 RPM — no failures, median response under 9 seconds; 60 RPM with 10 concurrent users — median 10.0s, P95 14.0s, 2 failures out of 105 requests.

## Actionable Insights
1. Combine schema-aware attribute retrieval with NL2SQL to generate accurate queries over complex nested schemas. Application: use embedding to retrieve relevant schema attributes before generating SQL, reducing prompt size and improving accuracy.
2. Use template-based in-context learning instead of fine-tuning per schema to make NL2SQL portable across enterprise domains. Application: build a library of reusable query templates, combine with retrieved schema context to generate executable SQL.

## Assumptions & Limitations
- System deployed on a specific enterprise customer data platform; results may not transfer directly to other environments.
- Schema standardization is required for industry-agnostic deployment.
- Not stated: storage and update costs for embedding indexes when schemas change.

## Metadata
- Year: 2026, authors: Haixu Ma, Aditya Bansal, Shubham Lohiya, Sumit Ranjan (Adobe Inc.), arXiv categories: cs.CL, cs.IR, PDF link: https://arxiv.org/pdf/2609.30547v1
