# Skill: Pre-Route RAG vs Long-Context Routing
Source: 2605.10235
Type: framework

## When to use this skill

- When building RAG systems with long documents (10K+ tokens) and needing to decide which queries should use RAG (retrieve snippets) vs Long Context (full document) — especially when cost is a concern
- When Self-Route (failure-driven fallback) isn't effective — model outputs "unanswerable" too conservatively or too confidently
- When routing decisions need to be interpretable and cost-efficient

- Do NOT use when: documents are short (<4K tokens, always use full context); using only 1 strategy (always-RAG or always-LC); no access to LLM for routing reasoning

## Input needed

- Document corpus with varying lengths (10K-128K+ tokens)
- LLM capable of structured reasoning (GPT-4-class for prompt-only; can distill to 1.7B)
- Evaluation queries with ground-truth answers
- Cost model: per-token pricing for RAG retrieval vs full context processing

## Steps

1. **Collect Lightweight Metadata** — For each document/query pair, gather: (a) document type (report, novel, manual, email); (b) document length; (c) head snippet (first 200 tokens). No expensive metadata extraction needed — Head-only metadata (length + head) nearly matches Full-Meta.

2. **Structured Routing Prompt** — Design prompt template: "Given document type: {type}, length: {length} tokens, opening: {snippet}. Question: {query}. Analyze: (1) Task type — is this comparison, fact-retrieval, or synthesis? (2) Information distribution — is the answer concentrated in specific sections or scattered? (3) Coverage estimate — can retrieved snippets cover the answer? (4) Recommendation: RAG or Long-Context, with reasoning." LLM outputs routing decision + explanation.

3. **Execute Routing Decision** — If RAG: run retrieval pipeline, concatenate top-k snippets with query, generate answer. If LC: feed full document + query to LLM. Track routing decisions to analyze patterns (which queries consistently need LC?).

4. **Distill to Small Model** — If lightweight deployment needed: (a) Run large model (235B) as teacher on training set, collect routing decisions + reasoning chains; (b) Fine-tune small model (1.7B) with reasoning-chain supervision; (c) Small model inherits routing logic, deploy on edge.

5. **Evaluate Cost-Effectiveness** — Compute: accuracy per token cost, route accuracy (% routing decisions matching oracle), LC usage rate (% queries routed to LC). Compare with Self-Route, Always-RAG, Always-LC baselines.

## Expected output

- Route accuracy >80% (routing decisions match oracle)
- LC usage reduction vs Self-Route (fewer unnecessary LC calls)
- Higher QA score vs Always-RAG (better quality when LC needed)
- Distilled 1.7B model achieves ~90% routing accuracy of large teacher

## Example application

Scenario: Legal tech company builds contract analysis tool. Documents: 50-200 page contracts. Pre-Route deployment: (1) User uploads contract → system collects metadata (type: contract, length: 85K tokens, head: "This Agreement dated..."); (2) User asks: "What are the termination conditions?" → routing prompt: "Fact-retrieval question, answer concentrated in specific clause → RAG"; (3) User asks: "Compare indemnification obligations across all sections" → routing prompt: "Comparison task, information scattered → LC"; (4) Result: 70% queries routed to RAG (cheaper), 30% to LC (higher quality when needed). Cost: 40% reduction vs always-LC. Accuracy: +3% vs always-RAG.

## Gotchas

- Routing prompt quality matters: vague prompts → inconsistent routing. Template must include specific analysis dimensions (task type, information distribution, coverage).
- 74.3% of small model errors tilt toward LC (safer option) — distillation helps but small models still biased. Need to calibrate LC threshold.
- Metadata can be misleading: short documents might need LC if comparison-heavy; long documents might work with RAG if question is localized. Routing prompt must consider task type, not just length.
- Binary routing limitation: some queries benefit from hybrid approach (RAG first, then targeted LC on specific sections). Pre-Route doesn't capture this nuance.
