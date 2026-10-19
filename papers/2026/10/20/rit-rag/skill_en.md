# Skill: rit-rag
Source: 2610.11370v2
Type: framework

## When to use this skill
- Enterprise RAG system with a large technical documentation corpus (millions of pages), needing to balance recall and precision.
- Want to avoid agentic RAG reading isolated chunks without document structure, or PageIndex committing to a single document upfront.
- A document hierarchy (ToC, sitemap, breadcrumbs) is available or can be induced.

## When NOT to use this skill
- Small document corpus where simple RAG is sufficient.
- Documents without a usable hierarchical structure that cannot be induced reliably.

## Required inputs
- Document corpus with hierarchical structure (ToC/sitemap/breadcrumbs) or ability to induce structure.
- A hybrid retrieval system (BM25 + dense) with indexed chunks linked to structural nodes (node ID, title, ancestor IDs/titles).
- An LLM agent able to call GetToC (retrieve induced sub-forest string) and Read (read node content).
- Tool budget B (total) and Bs (max GetToC calls).

## Steps
1. Build a structure tree per document from its ToC/sitemap; each node owns text under it; metadata includes title, summary, keywords.
2. Index document chunks with a hybrid BM25+dense retriever; link each chunk to its structural node metadata.
3. At query time: retrieve top-k′ > k chunks (e.g., 200); each chunk belongs to exactly one node.
4. Compute node score s(v, q~) = max sim(q~, c) over chunks of node v; select the n highest-scoring nodes (e.g., n=50).
5. Expand with ancestors of selected nodes to form a query-dependent sub-forest Fq~ (one sub-tree per document containing a selected node).
6. Present S(Fq~) to the agent (JSON string of sub-trees, ordered by decreasing top-node score).
7. Agent navigates the sub-forest: selects promising nodes St, reads their text cv via Read; based on contents, the agent answers, reads more nodes from the same sub-forest, or reformulates the query for the next round.
8. Agent stops when it generates the answer or reaches budget B tool calls (max Bs GetToC calls).

## Expected output
- A RAG system with highest accuracy, balancing recall (from broad retrieval) and precision (from selective structure-guided reading), without early commitment to a wrong document.

## Example application
- Enterprise customer support with 6,000 help pages: when a customer asks about a specific feature, the system retrieves a wide set of relevant chunks, induces a structure sub-tree around them, and the agent selectively reads the relevant sections to answer — avoiding being overwhelmed by hundreds of irrelevant chunks.

## Gotchas
- Do not commit to a single document before seeing its content (avoids PageIndex's early-commitment problem).
- Do not read all retrieved chunks like traditional agentic RAG (causes context overload, low precision).
- Do not ignore the one-time preprocessing cost (building ToCs, generating metadata) — but it is amortized over many queries.
- The method depends on a usable document hierarchy — weak headings or poor parsing can limit structure quality.

## Self-check
- Can someone who has not read the original paper follow these 8 steps? [YES] — each step is a concrete action.
- Which step is most vague? Steps 4-5 (node scoring and ancestor expansion) need concrete chunk-to-node linking implementation.
- Is the Input section sufficient? [YES] — corpus structure, hybrid retrieval, LLM agent with GetToC/Read, tool budget are all covered.

## Dry run (hypothetical scenario)
- Scenario: An enterprise has a 2.8 million page technical documentation corpus; an employee asks how to configure a feature.
- Run the skill: (1) Build structure trees from each page's sitemap; (2) index chunks with hybrid retrieval linked to structural metadata; (3) query retrieves top-200 relevant chunks; (4) score nodes, select top-50, expand ancestors to build query-induced sub-forest; (5) present sub-forest to agent; (6) agent selectively reads promising nodes, reformulates query if needed; (7) agent answers once sufficient evidence is gathered.

## Verdict: [SKILL VALID]
