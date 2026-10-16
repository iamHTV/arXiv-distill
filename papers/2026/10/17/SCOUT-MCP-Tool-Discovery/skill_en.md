# Skill: SCOUT MCP Meta-Tool Gateway
Source: 2608.23992
Type: framework / architecture-pattern

## When to use this skill
- An enterprise agent has >100 tools across many MCP servers — tool schemas consume >50% of the context window before the user speaks
- You need natural-language discoverability over a large catalog (200+ servers) without touching clients
- You need per-user access control at the retrieval layer, not as a post-filter

Do NOT use: catalog <50 tools (full injection is fine); retrieval infrastructure without an SLA (fallback full injection burns context); you need feedback-loop learning (this skill has none).

## Input required
- A proxy MCP server (FastAPI or equivalent) aggregating multiple backend MCP servers
- A vector DB with native BM25 + dense HNSW in one query interface (paper uses Milvus with built-in RRFRanker)
- An embedding API (paper uses OpenAI text-embedding-3-large, 3,072-dim) + three-tier cache (memory → Redis → MySQL, 24h TTL)
- Per-user server permission mapping (User ↔ Proxy Server ↔ MCP Server)

## Steps
1. Define 2 synthetic MCP meta-tools: tool_search (params: query string required, top_k int default 5 clamped [1,20], scope enum my_servers|all_servers) and execute_tool (params: tool_name, server_name, arguments — both name fields carry a "Do not guess" guardrail and must come verbatim from tool_search).
2. Write tool descriptions as behavioral spec: tool_search labeled "REQUIRED FIRST STEP" + domain category list + guardrail "Never guess a tool_name. Always get it from tool_search first."; execute_tool labeled "REQUIRED SECOND STEP"; add "After calling tool_search you can immediately call execute_tool — you already have its full schema above."
3. Ingestion pipeline (triggers: server becomes ACTIVE, admin manual refresh, catalog change detected): load schemas from the three-tier cache → chunk into a structured NL document (Tool + Category + Server Description + Description + Parameters with type/enum/required-optional) → embed in batches of 16 → upsert insert-before-delete (zero search downtime). Chunk ID deterministic {server}_{tool}; entity_source = {server}.tool.
4. Retrieval pipeline: resolve session + three-way injection gate (client config, proxy config, index non-empty) → translate scope into a Milvus metadata filter (enforced INSIDE the DB) → two-branch search: dense HNSW COSINE top_k×3 + BM25 top_k×3 → fuse with RRF k=60 → top_k → hydrate full schemas from cache.
5. Lifecycle: five states (PENDING/ACTIVE/DEGRADED/INACTIVE/REJECTED) add/remove chunks in Milvus; scheduled job probes DEGRADED servers past cooldown; 15-minute cron polls the catalog for changes.
6. Tiered fallback: embedding API failure → BM25-only; index absent → full tool injection (preserves MCP protocol compatibility). Instrument log events (tools_list_tool_search, tool_search_completed with results_count/latency_ms, tool_search_fallback at WARNING, execute_tool_failed) for observability.
7. Dual connector (prod/dev): each connector surfaces its own tool_search/execute_tool pair with an environment label embedded in the description text ("production environment"/"development") — the LLM routes by natural-language intent alone, no extra config.

## Expected output
- tools/list returns 2 tools instead of N; tool-token consumption drops ~99% (140.2k → 1.3k tokens); retrieval Hit@5 ≥95% on your query benchmark; authorization enforced at the retrieval layer; graceful degradation when infrastructure fails.

## Example application
- PayPal MCP Hub: 2,000+ tools, 100+ servers. After SCOUT: 1,300 tokens (0.8% of context), Hit@1 84.8% / Hit@5 95.6% / MRR 0.821 on a 49-query benchmark; production 24h: 31,701 sessions, 0.0% fallback rate, search-to-execution 1:4.5, latency median 440ms (P95 936ms — above the 500ms target, monitor it).

## Gotchas
- P95 latency can exceed the <500ms target (observed 936ms) — the 3× over-fetch plus the embedding API call sit on the critical path; monitor p50/p95/p99.
- Over-fetching top_k×3 per branch is MANDATORY: a document ranked 10th dense / 2nd BM25 is lost if each branch fetches only top_k.
- BM25-only fails the vocabulary-gap class (Q5 "Slack" → 0 matches); dense-only fails exact-API-name queries — never run single-modality.
- Poorly written tool descriptions are under-retrieved regardless of modality — audit descriptions before trusting retrieval metrics.
- The 15-minute sync cron means new schemas lag up to 15 minutes; time-sensitive changes need a manual force-refresh.
- Intra-domain ranking fails on lexical overlap (respond_to_meeting beat create_event) — if a domain has many same-verb tools, consider an intent-classification pre-filter.
