# [2610.23480v1] MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups

## Core value (1 sentence)
Not the model but the agent harness makes a literature assistant useful: a retrieve–read-full-text–verify–abstain loop running on self-hosted open-weight models doubles accuracy from 0.387 to 0.874 and produces zero fabricated local citations across 100 fabricated references × 3 backbones.

## Problem
Prior work forces research groups into one of three choices: (a) hosted services that receive unpublished work as input; (b) self-hosted chat frontends that keep data local but give the model no way to retrieve, read, or verify answers against its own corpus; (c) building a full retrieval-and-verification stack in-house from components with no standard interface. No prior work combines measuring abstention AND confabulation in a single benchmark for a paper-search agent.

## Contribution
- Munin: open-source (Apache-2.0, github.com/elgetilab/munin) self-hosted framework that indexes a group's corpus plus its citation graph and wraps whichever open-weight model the group can serve in an agent harness with specialized reading, search, and computation tools.
- Claim + measurement: the harness, not the model, is what makes the system useful on domain literature — an evaluation suite that runs as a single command ships with the software so any adopting group can re-run it on its own corpus and model.
- New benchmark: pairs an abstention test (withholding real source papers from a live retrieval stack, with the ingested version as positive control) with a confabulation test (papers that do not exist, scored by checking emitted DOIs against corpus membership — no LLM judge needed).

## Method
- Deployment topology: backend (harness, knowledge base = vector store + citation graph + PDF parser + ingestion pipeline, inference endpoint) runs entirely inside the institution; frontend (auth, upload, chat) is decoupled and connects via a reverse SSH tunnel initiated by the backend — no inbound port is opened into the research network.
- Per-turn routing: before the first model call, the query is embedded with BGE-base-en-v1.5 (768-dim) and a distance-weighted kNN vote over 244 labelled queries (k=8, margin 0.10, OOD cosine threshold 0.45, pin prior 0.5); slash commands (/research, /code, /chat) force a profile; fail-safe falls back to the pinned profile or chat.
- Harness: 3 profiles (chat/research/code), 4 sub-agents (source, search, deep_research, computer) with isolated interior context plus ~45 single-shot tools; sub-agents return compact results tagged with outcomes (resolved/not_found/thin_evidence) so a 15k–35k-token paper never enters the outer window.
- source agent: 4 modes (summary, QA, extraction, comparison); each call = resolve reference (DOI, arXiv ID, internal ID, URL, or title + authors + year) → extract full text → answer in a single LM call (chunk only if the document exceeds the context window). Replacing summarise-then-reason with single-call full-text reading moved accuracy from 0.497 to 0.864 (Appendix B.2).
- Outcome taxonomy (5 values): not_found (read successfully, answer absent — informative negative), extraction_failed (log for re-ingestion), ambiguous (top-hit auto-selection prohibited; requires disambiguation), out_of_scope (tell the user widening scope would resolve it), resolution miss (log as corpus gap).
- Egress gate per request: off / oa_only / full. Post-turn citation audit attaches a warning to the stored answer if any cited reference cannot be verified.
- DOI fabrication pressure removal: accepting titles as references removes the pressure to fabricate DOIs (a fabricated DOI is indistinguishable from a real one; Rao & Callison-Burch measured the DOI as the least accurate field in generated bibliographies across 931 papers). A DOI-tagged reference appearing in neither the user input nor any earlier tool output is a candidate fabrication, logged as a countable rate.

## KNOWLEDGE — Data & concepts
- 3-arm ablation on 199 paired LitQA2 questions (concurrency 1, 16,384-token output budget):
  - Qwen3.8-27B (production backbone, dense 27B, 2×RTX 5090 32GB tensor-parallel): bare 0.387 → agentic 0.874 (+0.487, 95% CI [0.407, 0.568], p<0.001); egress=off 0.704; naive RAG top-5: 0.211.
  - Qwen3.6-35B-A3B (MoE 35B total/3B active, AWQ 4-bit): bare 0.337 → 0.869 (+0.533 [0.452, 0.613]); egress=off 0.663; RAG 0.126.
  - gpt-oss-20b (MoE 21B/3.6B active, native MXFP4, single 24GB GPU): bare 0.407 → 0.563 (+0.156 [0.075, 0.241], p=0.004); egress=off 0.482; RAG 0.101 (162/199 turns ended with no final message).
- Naive RAG (prepend top-5 retrieved docs, single completion) scores BELOW the bare model on every backbone: RAG−bare = −0.176 (Qwen3.8), −0.211 (Qwen3.6), −0.306 (gpt-oss), all p<0.001. Agentic−RAG: +0.663 / +0.744 / +0.462.
- Faithfulness (fraction of claims supported by passages the model itself read): Qwen3.6 RAG 0.290 → agentic 0.627 (+0.336); Qwen3.8 0.282 → 0.540 (+0.258); gpt-oss 0.351 → 0.392 (+0.253, p=0.056, n=21). Zero-supported answers: 38%→3% (Qwen3.6), 27%→7% (Qwen3.8). Evidence set: 26–38 passages vs 5 abstracts.
- Egress decomposition (corpus-only / external tiers): 69/31 (Qwen3.6), 57/43 (Qwen3.8), 48/52 (gpt-oss); external tier worth +0.166/+0.211/+0.080 accuracy.
- Abstention C1 (100 frozen items: 80 nonexistent DOIs verified against Crossref + 20 title/claim descriptions, egress=full): refusal rate Qwen3.6 0.980 [0.950, 1.000], Qwen3.8 1.000 [0.963, 1.000], gpt-oss 0.720 (floor — 24 undecided, 20 empty turn-ends); 0 confabulated local citations on every backbone.
- Abstention C2b (50 single-source questions, production vs shadow corpus with the 49 source papers and 2,247 chunks removed, egress=off): accuracy present→absent: Qwen3.6 0.640→0.040, Qwen3.8 0.540→0.040, gpt-oss 0.400→0.040; abstention 0.300→0.860 / 0.420→0.920 / 0.340→0.800 (~9/10 Qwen, ~8/10 gpt-oss).
- Vs published baselines: PaperQA2 66.0% (trained on LitQA2); both Qwen backbones still exceed it with egress off (0.704, 0.663); human expert mean over 9 experts, SD 0.119.
- Cost: agentic 67.0s/query (Qwen3.6), 157.3s (Qwen3.8), 29.3s (gpt-oss) at egress=full; bare 15.7/8.0/2.4s; tool calls/query 7.33/6.93/8.75; recovery rate 1.000 (0.965 gpt-oss egress-off) — a failed tool call never aborts the query.
- Web search usage: gpt-oss only 17/199 questions; Qwen3.8 331, Qwen3.6 362 web searches.
- Routing anchor suite: 18 hand-written cases, trajectory pass rate >0.95; router correct on 7/10 queries with a known expected profile.
- Code: github.com/elgetilab/munin (Apache-2.0, v1.0.0, Zenodo 10.5281/zenodo.23191404), 54 scorecards with per-question verdicts.

## INSIGHT — Mechanisms & why
[Harness doubles accuracy] BECAUSE [the model can pull additional papers into context, re-read specific passages, and cross-check a value against a second source before committing; when no source exists in the corpus, the loop routes to an explicit not-in-corpus path instead of letting the model fabricate from memory]. This means [the accuracy gain is a property of the reading-and-verification process, not a change in response threshold — abstention does not increase (0.075 vs 0.040 bare on Qwen3.8), so the gain does not come from skipping hard questions].
[Naive RAG is worse than bare] BECAUSE [a fixed top-5 of prepended abstracts occupies context without giving the model a way to verify or dig deeper — the model trusts the retrieval surface instead of reading full text]. This means [retrieval without a verification loop is net-harmful; do not default to "add RAG" to a product].
[Zero fabricated citations] BECAUSE [the interface accepts 5 reference forms (titles allowed, DOI not required) removing fabrication pressure; the outcome taxonomy separates informative negatives from system failures; an unknown DOI not present in the input or prior tool output is logged as a countable signal]. This means [confabulation is not inevitable — it is a design problem, measurable with a test that needs no judge].

## IDEA — What to apply
Apply "harness before model" to a solopreneur's content RAG system: first step — instead of upgrading to a more expensive model, add a full-text-reading + two-source-cross-check + explicit-refusal loop to the current agent, then measure accuracy before/after on 50 questions with known answers.
Apply abstention certification to every retrieval-backed assistant: first step — build a 20–50 question single-source test set, run it twice (with and without the source document in the index), and count how often the system says "not in corpus" instead of fabricating — target ≥80% abstention when the source is absent, 0 fabricated citations.
Use the 5-value outcome taxonomy instead of a boolean found/not-found in tool returns: first step — log extraction_failed (needs re-ingestion) and ambiguous (needs disambiguation) separately to distinguish system breakage from corpus gaps.

## WISDOM — General principle
Principle: the unit of improvement in applied AI is the harness (tool + verify + abstain loop), not the model — evaluate a system with paired-question ablation + shadow corpus + fabricated-reference tests before swapping models. NOT when: the task needs no retrieval/verification, or there is no private corpus to run the evaluation suite on.

## Assumptions & Limitations
- Conditions required: a private corpus to ingest; an open-weight model servable on the group's hardware (down to 24GB VRAM for a 20B MXFP4); a test set whose source papers are in the corpus.
- Limitations acknowledged by the paper: no new model/embedding/retrieval algorithm; 3 models from 2 developers, effect size model-dependent (gpt-oss ~1/3 of Qwen); small per-family adjustments still needed (3 Qwen clarification-handling fixes, 2 routing gates for Qwen3.6, 1 tool-name mismatch fix for gpt-oss); this harness ≠ the class of all agentic systems; certification thresholds are regression gates, not per-answer predictors; not tested on 16GB GPUs; bare/RAG sample at temperature 0.7 vs agentic research-profile settings (asymmetry in every run); run-to-run noise ±0.035, so paired differences below ~3 points are within the measurement floor; C2b abstention rates computed on subsets of 20–32 answerable questions; faithfulness judge is single-passage (multi-passage claims get no credit — all faithfulness figures are lower bounds), validated on RAGTruth without in-domain validation; abstention detected by a text marker — 13/100 Qwen3.8 correct refusals also cited a real corpus document (wrong-paper retrieval is invisible to the scorer); gpt-oss empty turn-ends (25 bare, 162 RAG, 20 C1) make bare/RAG/C1 rates floors; binary abstain with no confidence score, so no risk-coverage curve; corpus not published; chat traffic transits a rented web host; egress=full sends queries to a commercial search API.
- Limitations the paper does NOT mention: true GPU-second cost (only wall-clock + tokens, because the cluster has no job accounting); behavior when the corpus contains documents with wrong information (not merely missing documents); maintenance cost of the citation graph at scale; latency budget for real-time use cases (67–157s/query).

## Metadata
- Year: 2026
- Authors: Markus Fischer, Jens Meiler, Matthias Elgeti (Leipzig University Medical School, ScaDS.AI, SECAI)
- arXiv category: cs.CL
- PDF: https://arxiv.org/pdf/2610.23480v1
- arXiv ID: 2610.23480v1
- Citation count: none yet (paper published 2026-10-16)
- Label: [applied]
- Skill: munin-self-hosted-agent-harness | Test: [SKILL VALID]
