# Skill: Deploy a self-hosted agent harness with abstention certification (Munin-style)
Source: 2610.23480v1
Type: framework / evaluation-method

## When to use this skill
- Building an assistant that reads a private corpus (internal docs, unpublished work) without sending data to an external service.
- Improving a RAG system's answer quality without switching to a more expensive model.
- Measuring and certifying that the system abstains when the corpus lacks the source, instead of fabricating citations.
- NOT for: tasks needing no retrieval/verification (plain chat); no private corpus to ingest; hardware below 1 GPU with 24GB VRAM.

## Inputs required
- The group's corpus (PDFs/URLs/DOIs), at least a few dozen documents.
- 1 GPU ≥24GB VRAM (e.g. RTX 5090 32GB) for a 20B–27B model (gpt-oss-20b MXFP4 or Qwen3.8-27B AWQ/INT4).
- Munin (github.com/elgetilab/munin, Apache-2.0, release v1.0.0).
- Evaluation test set: ≥100 questions with known answers (drawn from the corpus itself), plus 50–100 "fabricated document" items (nonexistent DOIs verified against Crossref, or titles/claims of papers that do not exist).
- 244 sample queries labelled with profiles (chat/research/code) for the router; 18 hand-written anchor cases.

## Steps
1. Ingest the corpus: run Munin's ingestion pipeline — parse PDFs, chunk (only documents exceeding the context window), build the vector store + citation graph. Verify every document resolves in the index.
2. Configure per-turn routing: embed queries with BGE-base-en-v1.5 (768-dim), kNN vote k=8 over 244 labelled queries, margin 0.10, OOD cosine threshold 0.45, pin prior 0.5. Slash commands /research, /code, /chat force a profile. Write 18 anchor cases (disjoint from the example set) — deploy a harness change only when trajectory pass rate >0.95.
3. Configure the harness: 3 profiles (chat/research/code); 4 sub-agents (source, search, deep_research, computer) with isolated interior context; ~45 tools reachable via core tools + tool_search. Every sub-agent MUST return a compact result tagged with an outcome (resolved/not_found/thin_evidence) — never stuff full paper text into the outer window.
4. Configure the source agent: accept references in 5 forms (DOI, arXiv ID, internal ID, URL, title + authors + year) — do NOT require a DOI (requiring DOIs invites fabrication). Each call: resolve → extract full text → answer in a single LM call. Return the 5-value outcome taxonomy (not_found / extraction_failed / ambiguous / out_of_scope / resolution miss), each with its caller contract.
5. Configure the per-request egress gate: off (no network), oa_only (scholarly APIs only), full (+ web search/fetch). Enable the post-turn citation audit — attach a warning to the stored answer whenever a cited reference cannot be verified.
6. Run the evaluation suite (single command) — 3 arms on the same test set: (a) bare model, (b) naive RAG top-5, (c) agentic full harness. Pass criteria: agentic − bare ≥ +0.30 accuracy; RAG − bare ≤ 0 (if RAG beats bare, re-examine retrieval quality before trusting results). Compare paired differences with bootstrap 95% CI; ignore differences below 3 points (run-to-run noise ±0.035).
7. Certify abstention: (a) Test C1 — run 100 fabricated-document items at egress=full; require refusal rate ≥0.95 and 0 confabulated local citations; (b) Test C2b — build a shadow corpus (remove 49–50 source papers and their chunks), run 50 single-source questions twice (production vs shadow) at egress=off; require abstention ≥0.80 when the source is absent.
8. Set certification thresholds as regression gates: store the scorecards (per-question verdicts + faithfulness) of the passing run. On every backbone swap or harness fix — re-run the suite; deploy only if accuracy drops ≤3 points, refusal ≥0.95, abstention ≥0.80.

## Expected output
- 54+ scorecard files with per-question verdicts and faithfulness scores per arm/backbone.
- Decision-grade metrics: 3-arm accuracy (bare/RAG/agentic), faithfulness, refusal rate, abstention rate, recovery rate, tool calls/query, wall-clock/query.
- A deploy / no-go decision for a new backbone or harness change, based on thresholds rather than vibes.

## Example application
A Vietnamese content freelancer installs Munin over a corpus of 200 blog posts + client documents, running Qwen3.8-27B on 1 GPU. Before swapping in a new model: run the suite — ablation shows bare 0.35 → agentic 0.82; C1: 96/100 refusal, 0 fabricated citations; C2b: 0.84 abstention when the source is removed. Thresholds met → deploy the new model, store the scorecard as the baseline for the next swap.

## Gotchas
- Requiring DOIs in the interface → the model fabricates DOIs (a fake DOI is indistinguishable from a real one). Always allow title + authors + year.
- Naive RAG (prepend top-5 docs, single completion) can score BELOW the bare model (−0.18 to −0.31 accuracy) — never enable RAG by default without a verification loop.
- Abstention detected by a text marker → wrong-paper retrieval (correct format, wrong source) is invisible to the scorer. Manually spot-check the ~13/100 refusals that also cite a real document.
- Isolated sub-agent context is the core design: stuffing full papers into the outer window loses both accuracy and grounding.
- Bare/RAG arms sample at temperature 0.7, different from the agentic research profile — mind this asymmetry when comparing arms.
- At egress=off the model still "calls" web tools (calls are intercepted at the guard) — this is normal; the log still records the full tool-call sequence.
- Run-to-run noise ±0.035: differences below 3 points are noise; do not conclude one model is better.
