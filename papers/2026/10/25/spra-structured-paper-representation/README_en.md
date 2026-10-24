# [2610.21424v2] Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents

## Core Value (1 sentence)

SPRA (Structured Paper Representation for Agents) turns scientific research into persistent, queryable objects and typed relations so AI agents can look up, traverse, and reuse paper content efficiently — reducing tokens by 28.5% vs passage retrieval and 95.3% vs Full Compact.

## Problem

Prior work has not solved connecting research problems, methods, and findings dispersed across narrative articles for scientific agents. Scientific agents must read full articles or rely on passage retrieval, which costs tokens and loses the structural relationships between research objects (problem, contribution, component, experiment setup, measure, finding).

## Contribution

(i) SPRA (Structured Paper Representation for Agents): a paper-level representation of persistent research objects and typed relations, with an empirical-AI profile organizing Problems, Contributions, Components, ExperimentSetups, Measures, and Findings for querying, traversal, and reuse.
(ii) Selected paper-level citation relations record dependencies, component use, and comparisons with prior work; source locations support verification.
(iii) SPRA instantiated across more than 1 million AI papers, with 19.95 million research units and 24.07 million internal relations.
(iv) Evaluation of SPRA through Schema-RAG with task evidence fixed before inference.

## Method

SPRA construction has 5 stages: (1) Input is a source article parsed into section-aware Markdown with source markers. (2) A shared unit census precedes relation planning and role-specific filling. (3) Assembly joins source-linked records and stores external citations separately; schema validity checks the relation contract, and source resolution checks whether a recorded address reaches a source item. (4) Five core LLM calls establish a shared unit census, predict relations, and fill Problem, Method, and Evidence content. Two citation passes join roles and verbatim signals to bibliographic metadata by citation key. (5) The assembly code resolves source markers, captures tables verbatim, reconciles identifiers, and checks types, endpoints, provenance, and census coverage.

The representation follows the paper's scientific argument: a Problem motivates a Contribution; Components and ExperimentSetups describe what is built and tested; Measures define evaluation targets; Findings record reported observations. These six roles organize the empirical-AI profile. Table 1 specifies the relations connecting these objects and their admissible endpoints; citation roles express external dependencies in a separate layer.

## KNOWLEDGE — Data & Concepts

- SPRA corpus (September 2026 snapshot): 1,059,112 structured paper records spanning 1965–2026, drawn from AI conference literature and preprints including arXiv.
- 19,949,289 research units, 24,073,381 internal typed relations.
- 6 research roles: Problem, Contribution, Component, ExperimentSetup, Measure, Finding.
- 7 relation types: part_of, co_contribution, compares_to, evaluates, about, supports, motivates, resolves.
- Evaluation sample: 9,849 eligible papers across 7 AI subfields, 2025 publications, 1,407 eligible papers per subfield.
- RQ1 (source-conditioned scientific QA): Schema-RAG 2.342/5 on G-U1 (semantic answer quality), beats Text-RAG 1.961/5 (+0.381/5), below Full Compact 2.420/5 (−0.078/5). G-U3 (Problem + Contribution): Schema-RAG 3.216/5, highest vs Full Compact 3.201/5.
- RQ2 (cross-paper reasoning, 3,070 paired tasks): Schema-RAG uses 9.51M input+output tokens, 28.5% fewer than Text-RAG (13.30M) and 95.3% fewer than Full Compact (203.26M). Directed judgment vs Text-RAG: qualification +0.184/5, correctness +0.026/5, grounding +0.045/5.
- RQ3 (idea generation, 1,001 variants): SPRA-Full Compact Overall −0.067 points, SPRA-Text-RAG Overall +0.011 points. SPRA uses 93.7% fewer tokens than Full Compact and 17.7% fewer than Text-RAG.
- Citation expansion: adding up to 2 resolved citation neighbors improves cross-paper integration by +0.253/5.
- Structural validity: 203,628/214,239 core units (95.0%) have source pointers; 106,439/109,591 relations (97.1%) join both endpoints.
- Semantic alignment: 84.49/100 contribution-level score from GPT-4.1; information-unit alignment 4.436/5.

## INSIGHT — Mechanism & Why

[Structured representation with typed relations] lets agents access research structure directly instead of reading full text → Schema-RAG beats Text-RAG by +0.381/5 on G-U1 and reduces tokens by 28.5% on RQ2. This means decomposing articles into clearly-typed objects and relations reduces cognitive load for agents.

[Source bindings and citation relations] let agents trace and verify findings → qualification improves +0.184/5 on RQ2 directed judgment. This means connecting Findings to conditions and qualifications helps agents assess how reliable a finding is.

[Full Compact is not always optimal] for all tasks: on RQ3 Top-5 synthesis, SPRA trails Full Compact by −0.067/5 on Overall, and grounding/qualification decrease on Top-5. This means compact structure must be assessed against each task's information needs — full text is not always better.

[Schema-RAG near Full Compact on G-U3] (3.216 vs 3.201/5) shows identifying a paper's problem and contribution doesn't require full text, just structured extraction. This means agents can quickly grasp article essence without reading everything.

## IDEA — Actionable Applications

Apply [structured paper representation] to building a knowledge base for research agents in business: instead of storing full articles, extract the 6 roles (problem, contribution, component, experiment setup, measure, finding) and relations between them so agents can look up quickly.

Apply [Schema-RAG] to enterprise scientific QA systems: instead of passage retrieval, retrieve structured objects and typed relations to reduce token cost and improve source-conditioned answer accuracy.

Apply [citation expansion] to expanding evidence for research: start from seed objects, then add up to 2 resolved citation neighbors to gather additional evidence under a shared context ceiling.

## WISDOM — General Principle

Principle: Structured research representation with typed relations and source bindings is usually more effective than raw text for AI agents when the goal is to query, traverse, and reuse scientific content, because structure reduces cognitive load and enables verification.

When to use: When building knowledge base query systems for research or technical content, especially when fast lookup and source verification are needed.

When NOT to use: When tasks require understanding full article context (e.g., Top-5 synthesis needs full text), or when source verification isn't needed and only quick summary is required.

Example outside original domain: Building a legal knowledge base — extract the 6 roles (legal problem, contribution, component, setup, measure, finding) and relations between legal clauses so an AI lawyer can look up and verify.

## Assumptions & Limitations

- Conditions for success: Source articles can be parsed into section-aware Markdown; access to Sciverse platform or local Paper Schema API installation; agents can call LLMs to extract structure.
- Paper's acknowledged limitations: Evaluations cover only the empirical-AI profile and specified task workflows; transfer to other domains, successive-task reuse, and stability under meaning-preserving rewrites remain future evaluation directions. Comparisons do not isolate contribution of individual role or predicate labels.
- Limitations paper does NOT mention: No evaluation on domains outside AI (e.g., medicine, physics); no evaluation of storage, retrieval, and maintenance costs provided by Sciverse; no evaluation of hosted service stability under updates.

## Metadata

- Year: 2026
- Authors: Yutong Leng, Haojiong Chen, Xiaoyang Wang, Mindong Liu, Runyuan Ma, Fukai Shang, Jiantao Qiu
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.21424v2
- Citation count: no information available