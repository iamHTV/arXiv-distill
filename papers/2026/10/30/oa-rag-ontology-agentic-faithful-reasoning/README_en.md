# 2610.36335 OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning

## Problem
- Current RAG (retrieval-augmented generation) mainly retrieves text chunks and lets the LLM reason over them. Gap: logical relationships between concepts are ignored, conclusions rely heavily on the LLM's parametric knowledge, so answer faithfulness (agreement with the knowledge source) is not controlled and hallucination risk remains.
- Prior work has not addressed: (1) ontologies contain BOTH formal axioms (Description Logic under OWL) and informal annotations (definitions, synonyms, comments), but existing systems exploit only one of the two; (2) the required reasoning pattern is unknown in advance, so no system adaptively selects among formal reasoning, ontology-grounded LLM reasoning, and ontology-assisted LLM reasoning, nor reports the grounding level of each answer.

## Contribution
- OA-RAG: the first agentic framework combining formal OWL reasoning with LLM reasoning. For each answer it reports the ontology observations used as evidence plus a 4-level grounding level: entailed, supported, related, unrelated.
- Formulates 3 reasoning patterns ordered by faithfulness, and automatically constructs QA benchmarks from 3 large-scale ontologies (GO, FoodOn, SNOMED CT) for the first two patterns.
- Core numbers: beats the strongest baseline by 10–15 percentage points on average on Tests 1–2 (44.3% vs 28.9% with Llama-3-8B-Instruct; 59.7% vs 49.7% with Qwen3.5-9B); competitive on Test 3 while using 10× fewer tokens than the strongest baseline (9.7k vs 96.7k tokens per question with Qwen3.5-9B).

## Method (core summary)
- Stage 1 — pre-tool reasoning: the LLM reasons only from the input context and parametric knowledge, producing a preliminary answer (draft) when the context suffices.
- Stage 2 — ReAct loop: an agent prompt introduces the ontology tool; each action is a SPARQL query against the ontology service: DESCRIBE "A" (fetch a concept card: name, definition, parents, children, stated relations, annotations); ASK {"A" "r" "B"} (check whether subsumption O |= A ⊑ ∃r.B is entailed by the reasoner; under the open-world assumption, Not Entailed does not mean false); SELECT (retrieve concepts/relations satisfying conditions). Query fallback: empty SELECT → BM25 comparison against concept cards returns top-k candidates. Name linking: exact match → ambiguous (candidates returned for disambiguation) → unknown-name fallback (BM25 pool of 200 names, reranked by string similarity, top-5 suggestions to repair the query).
- Stage 3 — answering, 2 steps: (1) filter failed/empty observations into an evidence digest E; answer y-hat = M(P_fin, q, E, y-tilde) if E is non-empty, else M(P_own, q) from parametric knowledge; (2) attribution turn: prompt P_att extracts cited evidence C-hat ⊆ E and the grounding level g-hat. Entailed/supported/related map to the three patterns of Figure 1.

## Key Findings
- Datasets: 3 ontologies (GO, FoodOn, SNOMED CT), each with 300 MCQs + 200 open questions (OQs). Test 1 (formal reasoning): 1,500 questions on source ontologies; Test 2 (ontology-grounded LLM reasoning): 1,477 questions on revised ontologies; Test 3 (ontology-assisted): 6,781 questions from MedQA, USMLE Step 1/2/3, MedMCQA, PubMedQA with SNOMED CT as the underlying ontology, following OntoTune's setup.
- OA-RAG achieves the best average accuracy with both backbones: 50.5% (Llama-3-8B-Instruct) and 68.1% (Qwen3.5-9B) across all 5 test settings.
- Tests 1–2 average: 44.3% vs 28.9% strongest baseline (+15.4 points, Llama); 59.7% vs 49.7% (+10.0 points, Qwen). OntoTune-sft/sft+dpo (ontology fine-tuning) only slightly improves OQs (7.8%→11.2% on Test 1); MedRAGdoc and i-MedRAGdoc fall below the base model on OQs with both backbones.
- Test 3: OA-RAG (Qwen) reaches 84.9% with an 8,192-token context window; i-MedRAGdoc(262k) needs 22 vs 5.8 LLM calls, 96.7k vs 9.7k tokens per question (10×), ~66× more retrieved text, ~5× more generated tokens; under the same 8,192-token window i-MedRAGdoc drops to 66.7% vs 84.9% for OA-RAG. RAGont(text) beats RAGdoc(text) with both backbones — ontologies are a more compact retrieval source than textbooks.
- Grounding level as a reliability signal: entailed+supported account for 70.0% (Llama) / 53.2% (Qwen) of questions, unrelated only 0.2% / 7.8%. Qwen Test 3: 94.9% of entailed and 82.1% of supported answers are correct (together 39.7% of questions) vs 72.1% of the remaining answers — stronger grounding correlates with higher accuracy.
- Evidence retrieval is the primary bottleneck: fully retrieved gold evidence 61.7% for MCQs vs 23.6% for OQs; once retrieved, gold evidence is cited in 95.1–98.4% of MCQs and ≥77.8% of OQs; Qwen retrieves markedly better than Llama.
- Ablation, Qwen average: full OA-RAG 68.1% → without ReAct loop 52.6% (−15.5) → without answering step 65.2% (−2.9) → without query fallback 67.7% (−0.4). Llama: 50.5% → 36.7% (−13.8) → 44.7% (−5.8) → 48.7% (−1.8%).
- Case study: plausible-but-wrong pre-tool answers corrected by explicit ontology relations — Halothane hepatitis causative agent = halothane (E→A); blind staggers = altLabel of Selenium poisoning (D→C).

## Actionable Insights
- "Draft first, verify later with a structured source" pattern: generate a draft from internal knowledge, then verify against a product graph/ontology before publishing. Apply: an FAQ bot drafts with an LLM, then runs DESCRIBE/ASK-style checks on a structured product catalogue before replying.
- Attach a 4-level grounding level to every answer for UI display of reliability; auto-publish only entailed/supported answers, route related/unrelated ones to human review. Apply: a content fact-check pipeline labels the grounding level of each claim in an article.
- Ontologies as retrieval sources are ~10× more token-efficient than textbook chunks → cost optimization for domain Q&A with a structured schema. Apply: replace RAG doc chunks with concept cards for a product/service catalogue, cutting tokens per question ~10×.

## Assumptions & Limitations
- Conditions for the method to work: a high-quality OWL ontology plus a runtime reasoner are required; domains lacking a standard ontology cannot use it — evaluation is biomedical/healthcare only.
- Acknowledged by the paper: the grounding level is the model's self-assessment — "no formal guarantee of correctness"; open-world assumption: ASK returning Not Entailed does not mean false because the ontology may be incomplete (the prompt explicitly instructs the model about this).
- Only 8–9B backbones tested (Llama-3-8B, Qwen3.5-9B), context capped at 8,192 tokens; no frontier closed-model comparison.
- Not stated but visible: retrieval bottleneck on OQs (23.6% fully retrieved) because definition-heavy information is less retrievable; single ontology per system — the agentic web across multiple ontologies is left to future work; the BM25 concept-card fallback can inject noise on small ontologies.

## Metadata
- Year: 2026 (submitted 26 Oct 2026). Authors: Hui Yang; Jiaoyan Chen; Yongsheng Gao. arXiv category: cs.AI. PDF link: https://arxiv.org/pdf/2610.36335v1. Citation count: [NO CITATION DATA — paper too new].
