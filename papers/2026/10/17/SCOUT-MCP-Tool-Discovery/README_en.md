# 2608.23992 — Hybrid Semantic Tool Discovery for Enterprise MCP Gateway (SCOUT)

## Problem
- A proxy MCP server (aggregating many backends behind one endpoint) creates two compounding problems: (1) context-engineering bottleneck — all tool schemas load at the start of every conversation: 140,200 tokens = 70.1% of the 200k window before any user query; (2) user-facing discoverability barrier — 200+ MCP servers and 2,000+ tools cannot be browsed manually. Prompt caching cuts reprocessing cost but neither frees context capacity nor improves accuracy.

## Contribution
- SCOUT (Selective Context Optimization for Universal Tooling): reframes tool exposure as a context-selection problem — inject only tools relevant to the current step. Two synthetic MCP meta-tools: tool_search (agentic RAG: BM25 + dense vector search fused by Reciprocal Rank Fusion, top-k) and execute_tool (routes invocations to backend servers).
- Six contributions: meta-tool protocol; hybrid retrieval engine; user-scoped authorization filtering at the retrieval layer (not post-filter); zero-downtime index (insert-before-delete upsert); environment-aware dual-connector routing (prod/dev by natural-language intent alone); validated across six MCP clients (Claude Code, Claude Desktop, ChatGPT Web/Desktop, GitHub Copilot VS Code, Cursor, OpenAI Codex CLI) with no client-side modifications.

## Method
- Two-phase query protocol: tools/list returns a stub list of only 2 tools. tool_search is labeled "REQUIRED FIRST STEP" with domain categories and the guardrail "Never guess a tool_name. Always get it from tool_search first." execute_tool is labeled "REQUIRED SECOND STEP." Both share domain-category semantic fingerprints, so one search returns both schemas.
- Ingestion pipeline, 4 stages: load from a three-tier cache (memory → Redis → MySQL tool_cache, 24h TTL) → chunk each schema into a structured natural-language document (tool name, server category, server description, tool description, parameter specs with type/enum/required) → embed in batches of 16 with OpenAI text-embedding-3-large (3,072-dim) → upsert insert-before-delete (zero search downtime).
- Retrieval pipeline, 4 stages: resolve session + three-way injection gate (tool_search_clients config, tool_search_proxy_ids config, index initialized and non-empty) → resolve scope (my_servers/all_servers translated into a Milvus metadata filter INSIDE the vector DB) → two-branch search (dense HNSW COSINE top_k×3; sparse BM25 top_k×3; fused by RRF k=60 → top_k) → schema hydration from cache. Fallback chain: embedding API failure → BM25-only; index absent → full injection.
- Index lifecycle: five server states (PENDING, ACTIVE, DEGRADED, INACTIVE, REJECTED) trigger corresponding Milvus actions; a scheduled job probes DEGRADED servers past cooldown; a rolling-window catalog poll re-ingests changed schemas (15-minute cron).

## Key Findings
- Context: 140,200 tokens (70.1%) → 1,300 tokens (0.8%), a 99% reduction; spot-check average ~2,500 tokens (~1.25%) at top-5.
- Retrieval quality (49-query benchmark, 9 domains, live 2,000-tool catalog, 45 evaluable): Hit@1 84.8% (38/45), Hit@5 95.6% (43/45), MRR 0.821. Original 15-Q: Hit@1 84.6%, Hit@5 100%, MRR 0.915. Expanded 35-Q (deliberately harder): Hit@1 75.6%, Hit@5 93.9%, MRR 0.784.
- By domain: analytics 11/11 Hit@1; SRE/infra 78% (7/9); productivity 75% (6/8); BI/reporting lowest at 50% (2/4) — Looker tools surface at rank 4 when queries use payment-metric vocabulary.
- Latency (1,921 requests over 24h): avg 572 ms, median 440 ms, P95 936 ms — ABOVE the paper's own stated p95 <500 ms requirement (not discussed); min 232 ms warm-cache floor.
- Production 24h: 31,701 MCP sessions, 55,314 tool calls, 1,926 tool_search invocations (43.1% invocation rate), avg 5.5 tools per search, 8,694 execute_tool completions, fallback rate 0.0%, search-to-execution ratio 1:4.5.
- Q5 "send a Slack message": pure BM25 returns zero matches ("Slack" appears in no tool description); the dense branch bridges the vocabulary gap → teams_send_message (Y*). PayPal deploys Microsoft Teams.

## Actionable Insights
- Meta-tool pattern: when an agent has >100 tools, collapse tools/list to 2 meta-tools (search + execute) — model-agnostic, zero client changes, and all orchestration lives in tool description text (labels "REQUIRED FIRST/SECOND STEP" + guardrails), no fine-tuning.
- Hybrid BM25+dense with 3× over-fetch per branch (a 30-candidate pool before RRF k=60) — BM25 catches exact API names, dense catches paraphrases; dropping one branch loses an entire query class (Q5).
- Enforce authorization inside the vector DB (metadata filter), not as a post-filter — and degrade gracefully in tiers (BM25-only → full injection) so retrieval-infrastructure failure never becomes an outage.

## Assumptions & Limitations
- Tool descriptions authored by MCP server developers vary in quality; no mechanism detects or compensates — poorly described tools are under-retrieved regardless of modality.
- No feedback-loop learning (successful invocations don't refine embeddings); 15-minute sync cron means schema changes take up to 15 minutes to propagate; top-k is tuned manually (no auto-calibration).
- Failure modes: intra-domain ranking (respond_to_meeting at rank 1 over create_event due to lexical overlap on "schedule/send"); workflow-step confusion (approve_tests at rank 1 over the entry-point generate_pr).

## Metadata
- 2026 (2026-08-25), Olympia Saha, Amy Wang, Srinivasan Manoharan (PayPal, Inc.), cs.IR + cs.AI, https://arxiv.org/pdf/2608.23992
