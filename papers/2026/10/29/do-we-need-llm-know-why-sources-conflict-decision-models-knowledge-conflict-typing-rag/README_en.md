# 2610.36915 Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG

## Core value (1 sentence)
A typed decision model (returns probabilities over fixed options in one forward pass, no text generation) classifies knowledge-conflict types in RAG nearly as accurately as an LLM, at 4–39× lower cost and 2.6–6.0× lower latency, and its confidence ranks its own errors so only the uncertain fraction needs escalation to a high-end LLM (cascade).

## Problem
Search-augmented language models answer from retrieved web pages, and those pages often disagree. Disagreement has very different causes: a question may be underspecified with several valid answers; it may touch a contested topic on which reasonable sources differ; the answer may have changed over time, so some pages are stale; or a page may simply be wrong. Each case calls for a different response: combine the answers, present the viewpoints neutrally, prefer the most recent information, or ignore the unreliable source. Cattan et al. (2025) formalized this as a five-way taxonomy, released CONFLICTS — a benchmark of 458 search queries annotated by experts with their conflict type — and showed that giving a generator the gold type raises the share of responses with the expected behavior by about 24 points. But predicting the type is hard: the best LLM they tested, Gemini 2.5 Flash, reached 65.3% accuracy. The gap: no prior work compares typed decision models — a new class of models that return probabilities over allowed answers in a single forward pass instead of generating text — on this task of typing the conflict among many retrieved sources, fast and cheap.

## Contribution
- A census of decision models on conflict typing: evaluate every decision model served by one commercial inference gateway (11 models from 7 providers) on CONFLICTS under the original paper's protocol: same input representation, same category definitions and examples taken verbatim from the paper's source, and Gemini rerun on identical inputs so every comparison is paired. 10 of the 11 models match or exceed the paper's LLM at a fraction of its cost and latency; the current Gemini 3.8 Flash is significantly more accurate than 8 of them.
- A formulation study: decomposing the taxonomy into yes/no questions lowers accuracy for all 11 models, and a repair fitted on one model helps none, leaving the direct question as the reliable format.
- Cost-quality cascades: decision models' confidence ranks their own errors, so sending their least certain queries to an LLM is effective: with a quarter of queries escalated to Gemini 3.8 Flash, 8 of the 11 cascades are statistically tied with the LLM alone at 25–37% of its cost.
- Pre-specified diagnostics: test whether decision models depend on publication dates, are sensitive to source order, or miss a single false source among agreeing ones. Dates play no measurable role, order sensitivity varies from model to model, and a planted false source shows up in the probabilities more than in the top answer.
- An end-to-end test: given to a generator, the types of 10 of the 11 decision models yield answers that follow the expected behavior as often as with the LLM's types, under both judges specified.

## Method (core summary)
The core idea: use a typed decision model — returning probabilities over allowed answers in a single forward pass, without generating text — as the knowledge-conflict-type classifier before the generator writes the answer. Pipeline:
1. A query and about 10 numbered search results are passed to the decision model as the "state".
2. The decision model answers one direct choice question (flat question) with five options being the five conflict types (No conflict, Complementary information, Conflicting opinions, Outdated information, Misinformation). The task, category definitions, and examples are copied verbatim from Cattan et al. (2025)'s prompt. The predicted type is the most probable option, and its probability is the model's confidence.
3. The generator writes the answer based on the predicted type.
4. Optionally: a confidence-gated cascade — the fraction f of queries with the lowest confidence is sent to a high-end LLM (Gemini 3.8 Flash), whose answer replaces the decision model's. The threshold is a quantile of the decision model's confidences and uses no labels, so the full accuracy–cost curve can be computed on the test split without leakage.

Two formats are studied: Flat (one choice question with five options) and Tree (decomposed into yes/no questions). Result: Flat beats Tree for all 11 models.

## KNOWLEDGE — Data & concepts
- 11 decision models from 7 providers, served by one commercial inference gateway (Vercel AI Gateway): Jev 1.13, Jev 1.14, Decider v1.2, Decider Flash v1.2, GPT-6 Luna Decisions, d1, d1 Ultra, Decision-1, Elephant-1, Mammoth-1, Classify-1.
- Asked directly, the 11 decision models classify 50.0–67.0% of test queries correctly (median 62.6%). Gemini 2.5 Flash with the paper's prompt reaches 61.3% on the same queries.
- Against Gemini 2.5 Flash: 8 decision models statistically tied, 2 significantly more accurate (Liquid d1 Ultra +5.7 points, p=0.027; Perplexity Decider v1.2 +5.4, p=0.049), 1 significantly less accurate (ScaleDown Classify-1, −11.3, p<0.001).
- Cost: $0.04–$0.41 per 1,000 queries (2 were free at the time of the runs) against $1.66; latency 0.26–0.72 s against 1.55 s. Among the 10 models matching or exceeding the paper's LLM, the billed ones cost 4–39× less, and all are 2.6–6.0× faster.
- Gemini 3.8 Flash current model is stronger: at lowest thinking level reaches 70.0%, +8.6 points above Gemini 2.5 Flash (p<0.001), at 2.2× its cost. Significantly more accurate than 8 decision models; the other 3 (Liquid d1 Ultra, Perplexity Decider v1.2, OpenAI GPT-6 Luna Decisions) trail by 3.0–3.7 points without significant difference. More thinking does not help either Gemini: Gemini 3.8 Flash default thinking scores 66.7% (−3.2 points vs low, p=0.019); Gemini 2.5 Flash with thinking scores 57.9% (p=0.19).
- CONFLICTS (Cattan et al., 2025): 458 queries, 5 types (No conflict 161, Complementary 115, Conflicting opinions 115, Outdated 62, Misinformation 5); frozen test split 406 queries, dev split 52.
- Per-class F1: models differ most on Outdated information (F1 27.5–72.7; Gemini 3.8 Flash 66.1). Misinformation has only 4 test instances, defeating every system: no decision model exceeds F1 11.8 (Gemini 3.8 Flash: 25.0).
- Calibration: expected calibration error (ECE) of the flat question ranges from 0.031 to 0.188, and 7 of 11 models are over-confident on average (mean top probability above accuracy).
- Confidence ranks errors: AUROC from 0.64 to 0.76.
- Cascade: escalating the least confident quarter of queries to Gemini 3.8 Flash yields cascades statistically tied with the LLM alone for 8 of 11 models, at 25–37% of its cost. Confidence-based escalation beats random escalation of the same number of queries for 10 of 11 models, by up to 4.9 points; exception is GPT-6 Luna Decisions (AUROC 0.65, confidence barely ranks errors).
- Publication dates play no measurable role (removing every date, or adding each result's recency rank computed in code, changes accuracy significantly in 0 of 22 tests).
- Source order: shuffling results changes predicted type on 5.4–42.1% of queries (pooled over two seeds), above noise floor for all 11 models; Gemini 3.8 Flash flips on 9.4%.
- Planted false source: in 96 No conflict test queries, rewrite one result to state a plausible wrong answer. Decision models call 7.3–66.7% of planted copies Misinformation (Gemini 3.8 Flash: 52.1%). Probability of Misinformation separates planted from clean copies with AUROC 0.66–0.86, at least 0.75 for 10 of 11.
- End-to-end: with primary judge, Vanilla 87.9%, Pipeline 91.6% (+3.7 points, p=0.032), Oracle 95.3% (+7.4, p<0.001). Replacing Gemini 2.5 Flash as predictor changes little: 10 of 11 decision models tied with it (−3.9 to +0.7 points), only ScaleDown Classify-1 significantly worse (−3.9, p=0.011). With a quarter of queries escalated to Gemini 3.8 Flash, 11 of 11 cascades tied with it (−1.0 to +0.7).

## INSIGHT — Mechanism & why
- [Decision models classify nearly as accurately as LLMs on conflict typing] happens BECAUSE [conflict typing is a five-label classification in a single forward pass, no text generation needed — decision models are trained to be calibrated, not to generate]. This means [an LLM can be replaced by a decision model for the typing step in a RAG pipeline, cutting cost 4–39× and latency 2.6–6.0×].
- [Decision model confidence ranks its own errors] happens BECAUSE [the top-class probability reflects the model's calibration]. This means [sending the least confident fraction to a high-end LLM (cascade) recovers most of the accuracy gap at only 25–37% of the LLM's cost].
- [Decomposing the taxonomy into yes/no questions lowers accuracy for every model] happens BECAUSE [yes/no bias and the sub-questions do not separate the classes — e.g. the "compatible" question answers yes for contested topics almost as readily as for complementary ones]. This means [use the direct choice question (flat), not a yes/no decomposition of the taxonomy].
- Condition: the cascade insight only helps when confidence ranks errors (AUROC 0.64–0.76). One model (GPT-6 Luna) has confidence near random, so cascade does not help it.
- A repair fitted on one model's errors does not transfer to any other model.

## IDEA — Actionable applications
1. Apply a decision model as the typing step before the generator in your RAG system: first step is to replace the long LLM prompt with a cheap typed decision model (e.g. Jev/Decider) to classify the conflict type among search results, then generate the answer given that type.
2. Apply a confidence-gated cascade: first step is to take the top-class probability from the decision model, escalate the 25% least confident queries to a high-end LLM (e.g. Gemini 3.8 Flash), keep the rest with the decision model — cutting 63–75% of LLM cost while keeping LLM-level accuracy.
3. Apply a direct choice question (flat) instead of a yes/no decomposition: first step is when designing a conflict-typing prompt, use one choice question over the five types instead of a chain of yes/no questions.

## WISDOM — General principle
- Principle: "Classifying is cheaper than generating — use a decision model for fixed-label classification steps before calling a high-end LLM, and escalate only the uncertain fraction." When to use: when there is a fixed-label classification step in the pipeline (e.g. conflict typing, intent classification, routing). When NOT to use: when open-ended reasoning or long text generation is needed, or when the model's confidence does not rank its errors (low AUROC).
- Example outside original domain: classify customer emails into fixed topics (complaint, pricing, technical support) — use a cheap decision model for classification, escalate only uncertain emails to a high-end LLM or human agent.

## Assumptions & Limitations
- Conditions required for the method to work: a fixed, short set of labels to classify; the decision model supports structured output (probabilities over allowed answers) via API; the query comes with enough context for the model to reason about the relationship between sources.
- Limitations the paper acknowledges: CONFLICTS is small (406 test queries, ~±4.8 point accuracy interval, so effects under ~5 points are generally not significant; cascades can be shown close to, but not formally equivalent to, the LLM); label distribution reflects how queries were selected, not real search traffic, and the dataset has only five natural Misinformation queries; the planted variant tests one kind of misinformation (an entity or value substituted in a single source); the census covers only decision models one gateway served on one day; hosted models change without notice (some identifiers are unversioned, two models were free during runs, and their rerun of Gemini 2.5 Flash scores below the published figure); providers do not disclose model sizes or training data, so differences between models cannot be explained; the end-to-end test uses one generator and LLM judges validated on 100 answers, who do not see the search results; the primary judge is the generator's own model, which may favor its own answers; the size of the gain from predicted types depends on the judge, and they do not measure factual grounding (the third metric of Cattan et al. 2025).
- Limitations the paper does NOT state: open-weight decision models run locally are not compared (cost and latency would depend on local hardware and not be comparable); no evaluation with multiple judges simultaneously; no test of whether a decision model's probabilities can steer a generator between expected behaviors when the type is uncertain.

## Metadata
- Year: 2026 | Authors: Parv Khatri, Harshul Jain, Mehak Kapoor, Tanya Sah (all Independent Researchers)
- arXiv category: cs.CL (Computation and Language)
- PDF link: https://arxiv.org/pdf/2610.36915v1
- Abstract link: https://arxiv.org/abs/2610.36915
- Code: https://github.com/Parv17k/decision-models-conflict-typing
- Citation count: [not found]
