# [2610.21424v1] Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents

## Problem
Scientific agents must connect research problems, methods, and findings dispersed through narrative articles. Conventional articles express this structure through narrative text, tables, and figures; agents must reconstruct research roles and dependencies from passages. Passage-based retrieval supplies relevant source text but agents still need to connect findings to methods, conditions, and comparisons. Repeated full-paper inputs incur token-based API charges and occupy context needed for additional papers and task history.

## Contribution
- Introduces SPRA (Structured Paper Representation for Agents), a paper-level representation of persistent research objects and typed relations.
- The empirical-AI profile organizes Problems, Contributions, Components, ExperimentSetups, Measures, and Findings for querying, traversal, and reuse.
- Paper-level citation relations record dependencies, component use, and comparisons with prior work; source locations support verification.
- Instantiates SPRA across more than one million AI papers, with 19.95 million research units and 24.07 million internal relations.
- Evaluations access SPRA through Schema-RAG with task evidence fixed before inference.

## Method
- SPRA stores research objects independently of a particular query. Structured JSON encodes each instance; a versioned profile specifies scientific roles, relation signatures, cardinalities, and source-linking rules.
- The representation follows the paper's scientific argument: a Problem motivates a Contribution; Components and ExperimentSetups describe what is built and tested; Measures define evaluation targets; and Findings record reported observations.
- Six roles organize the empirical-AI profile: Problem, Contribution, Component, ExperimentSetup, Measure, Finding.
- Internal relations (Table 1): part_of, co_contribution, compares_to, evaluates, about, supports, motivates, resolves with admissible endpoint signatures.
- Citation relations: builds_on, uses_component, compares_with connect the focal research argument to prior work.
- Publicly accessible via Paper Schema API on the SciVerse scholarly-data platform.

## Key Findings
- SPRA declared across more than 1 million AI papers (1965–2026), 19.95 million research units, 24.07 million internal relations.
- Across seven subfields: SPRA improves source-conditioned scientific QA by 0.381/5 over passage retrieval while remaining close to Full Compact (0.078/5 lower on average).
- Directed cross-paper reasoning: qualification improves by 0.184/5 over passage retrieval; Top-5 synthesis shows mixed quality effects.
- Across all paired RQ2 tasks including Top-5: input+output tokens decrease by 28.5% relative to passage retrieval and 95.3% relative to Full Compact.
- In idea generation: 0.067-point lower Overall score than Full Compact accompanies 93.7% fewer input+output tokens.

## Actionable Insights
1. Build structured paper representation for agents to query and reuse. Apply: when building AI research systems, extract papers into structured objects (problem, contribution, component, experiment setup, measure, finding) instead of storing raw text only. First step: Set up a JSON schema for papers with research roles and typed relations between them.
2. Use Schema-RAG instead of passage retrieval to reduce tokens and improve quality. Apply: when building scientific QA systems, retrieve structured research objects instead of raw passages. First step: Build a retrieval system that can query research objects by role and relation.
3. Reduce input+output tokens by using structured representation. Apply: when building AI research workflows, use structured representation to reduce API costs compared to feeding full papers. First step: Compare token cost between passage retrieval and structured object retrieval on your task.

## Assumptions & Limitations
- Evaluated on AI literature (1965–2026); may differ on domains outside AI.
- Only evaluated on 7 AI subfields; does not generalize to all scientific fields.
- Evaluation sample of 9,849 source-aligned papers may not represent the full 1 million-paper corpus.
- Idea generation tasks show slightly lower Overall score than Full Compact (0.067/5), trading quality for token efficiency.

## Metadata
- Year: 2026, Authors: Yutong Leng, Haojiong Chen, Xiaoyang Wang, Mindong Liu, Runyuan Ma, Fukai Shang, Jiantao Qiu (Shanghai AI Laboratory; Shanghai Jiao Tong University), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2610.21424v1