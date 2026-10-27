# 2610.32415v1 Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge

## Core Value (1 sentence)
ANT-OR, a multi-agent annotation framework, improves agreement@≥2 accuracy by 4.5 points over the strongest baseline and achieves the highest alignment with human annotator distributions (measured by Fleiss' κ) within 2 points — by distilling contrastive decision rules from positive and negative feedback.

## Problem
LLM-based annotation has advanced rapidly, but existing benchmarks remain misaligned with real-world practice. Actual annotation often involves lengthy, task-specific guidelines, and different annotators may produce divergent but reasonable judgments, especially on boundary cases, where single-labeled datasets fail to reflect this disagreement. This gap also limits existing single-agent and workflow-based annotation systems, which often lack adaptability to complex, evolving guidelines. Existing LLM annotation benchmarks often lack the guideline documents used in real-world tasks and provide only a single gold-standard label per sample. Single-label benchmarks collapse this uncertainty and cannot determine whether LLM annotators achieve human-level consistency.

## Contribution
1. Identifies two critical bottlenecks to reliable automated annotation: inadequate benchmarks that fail to capture inter-annotator disagreement and complexity from detailed annotation guidelines, and limitations of current annotation agents, particularly those based on single-agent or static multi-agent designs.
2. Constructs and releases ANT-A (Aggregated N-annotator Task Annotations), a multi-annotator benchmark comprising 7 datasets with detailed guidelines and 5 independent human annotations per sample, enabling a distribution-aware evaluation using Fleiss' κ to assess how closely model annotations align with human labeling distributions.
3. Proposes ANT-OR (automated ANnotation framework Through multi-agent Optimization with agent-level contRastive knowledge), an adaptive multi-agent framework that can transform collective prediction successes and failures into reusable structured decision knowledge, enabling more robust collaboration on complex annotation tasks involving nuanced decision boundaries.
4. Extensive experiments show ANT-OR substantially improves annotation performance across diverse tasks, outperforming the strongest baseline by 4.5 points in accuracy and achieves the highest agreement with human annotator distributions as measured by Fleiss' κ within 2 points on average.
5. ANT-A spans 7 datasets across domains (medical, e-commerce, general) and modalities (text, vision-language), 1,500 samples per dataset, 5 independent human annotations per sample.

## Method
The ANT-OR pipeline has these main steps:
1. Dataset Preparation: collect domain-relevant query samples, anonymize identifiable information, filter duplicates and low-quality instances to obtain 1,500 samples with clear-cut and boundary cases.
2. Guideline Document Design: derive annotation guidelines from real-world requirements, refine by clarifying ambiguous definitions, adding decision rules for boundary cases.
3. Human Annotation Process: 10 annotators in pool, each sample independently labeled by 5 annotators, three-phase protocol (pre-annotation, rule clarification, batch annotation), total cost USD $4,078.
4. Contrastive Knowledge Mining: each agent maintains positive and negative sample pools. When an agent makes a wrong prediction, construct contrastive tuple (s+1, s+2, s−) and use LLM to mine discriminative dimension d. Maintain support count per dimension; retain only dimensions with support ≥ 2.
5. Knowledge-Augmented Reasoning: annotator–verifier architecture (3 annotators + 1 verifier). Quality-aware sample retrieval: Score(q, si) = sim(E(q), E(si)) · wi. Dimension–Sample Coupled Injection: inject both instance-level and rule-level into prompts.
6. Attribution-Guided Optimization: attribute each error to responsible agents, refine their prompts using LLMOpt(pa; {(q−, r)}, s+, d). Roll back if batch-level performance doesn't improve.
7. Iterative Knowledge Base Expansion: over multiple epochs, add verified prediction outcomes to contrastive sample pools for subsequent retrieval and contrastive mining.

## KNOWLEDGE — Data & Concepts
- Agreement@≥2: an annotation is counted as correct if it matches at least 2 of 5 human annotators.
- Fleiss' κ: measures inter-annotator consistency.
- Contrastive decision rules: decision rules distilled from contrastive samples (positive and negative).
- Discriminative dimension: structured textual unit containing category-specific decision criteria distilled from contrastive cases.
- Contrastive sample pool: verified positive and negative samples for each agent.
- Contrastive tuple: (s+1, s+2, s−) used to mine discriminative dimensions.
- Support count: number of times a dimension has been involved in fusion; retain only dimensions with support ≥ 2.
- Annotator–Verifier Architecture: 3 independent annotators + 1 verifier who compares justifications to determine final label.
- Quality-Aware Sample Retrieval: retrieval score combines semantic similarity and historical reliability.
- Dimension–Sample Coupled Injection: inject both instance-level and rule-level into prompts.
- 7 datasets: Disease Privacy Assessment, Billing Scenario Classification, E-commerce Medical Entity Extraction, Social Text Classification, Image Attribution Recognition, Image Classification, Image Text Relevance.
- 1,500 samples per dataset, 5 independent human annotations per sample.
- Human average Fleiss' κ: 63.60.
- ANT-OR: agreement@≥2 average 71.75%, Fleiss' κ average 61.37.
- ANT-OR improves 4.5 points over strongest baseline (SPO at 67.08%).
- ANT-OR achieves Fleiss' κ within 2 points of human inter-annotator agreement.
- Optimization cost: $101.43 (ANT-OR) vs $65.94 (SPO), accuracy improvement 4.7 points (71.75% vs 67.08%).
- ANT-OR generalizes 3.7 percentage points better on test sets than SPO (which overfits training data).
- 3 LLM-based annotators + 1 verifier, temperature = 0.1.
- 200 training samples per task, batch size 20, 3 iterations per batch over 6 epochs.
- Evaluation on 1,000 test samples; 300 samples unused.

## INSIGHT — Mechanism & Why
- [Single-label benchmarks collapse uncertainty] occurs because real annotation tasks have detailed guidelines that can be ambiguous, and annotator disagreement may reflect valid alternative interpretations rather than annotation errors. Single-label evaluation cannot determine whether LLM annotators achieve human-level consistency.
- [Static agent systems lack adaptability] occurs because single-agent or static multi-agent systems depend on hand-crafted prompts and static workflows, failing on complex tasks with detailed guidelines and boundary cases. Need systems that adapt to complex, evolving guidelines.
- [Contrastive knowledge drives improvement] occurs because mining discriminative dimensions from contrastive samples (positive and negative) provides richer optimization signals than error cases alone. Structured decision knowledge is the key driver of improvement.

## IDEA — Actionable Applications
1. Apply ANT-A Benchmark to evaluate your company's LLM annotation system: collect 5 independent human labels per sample, use Fleiss' κ to assess how closely model annotations align with human labeling distributions. First step: build a small annotation dataset with detailed guidelines and 5 independent annotators per sample.
2. Apply annotator–verifier architecture to your multi-agent annotation system: 3 independent annotators produce labels and rationales with separately optimized prompts, then a verifier compares justifications to determine final label. First step: implement 3 annotator + 1 verifier system with different prompts per annotator.
3. Apply contrastive knowledge mining: when an agent makes a wrong prediction, retrieve two semantically similar correct samples to form a contrastive tuple, then use an LLM to summarize a discriminative dimension from confusing cases. First step: set up storage for correct and incorrect samples; after each wrong prediction, extract discriminative dimensions and store in knowledge base.

## WISDOM — General Principle
- Principle: LLM annotation should be evaluated by distribution-aware agreement with human judgments (not just matching a single gold label) — annotator disagreement on boundary cases reflects real-world ambiguity, not errors to eliminate.
- When to use: When building automated data annotation systems for tasks with detailed guidelines and many boundary cases (text classification, medical entity extraction, image classification...).
- When NOT to use: When annotation tasks have clear, unambiguous answers (e.g., spam/not-spam with clear rules) — no need for complex multi-agent systems.

## Assumptions & Limitations
- Required condition: Need professional human annotators to create reference labels and detailed task guidelines.
- Paper-acknowledged limitations: Benchmark still represents only a subset of real-world annotation settings; can be extended to cover long-document annotation, open-ended judgment, and specialized expert workflows. Optimization cost is higher due to multi-agent design and iteration.
- Limitations the paper does NOT state: Does not explain how to automatically create detailed task guidelines without human intervention.

## Metadata
- Year: 2026
- Authors: Xiaopeng Ke, Zhixin Wang, Xuebo Liu, Xinyu Ma, Xing Zheng, Bowen Song, Weiqiang Wang, Min Zhang
- arXiv category: cs.CL
- PDF link: https://arxiv.org/pdf/2610.32415v1
- Classification: [applied]