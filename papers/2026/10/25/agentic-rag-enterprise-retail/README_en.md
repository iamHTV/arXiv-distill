# [2610.25096v1] Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources

## Core Value (1 sentence)

RetailRAG (retail-aware agentic RAG framework) beats all 6 RAG baselines on RetailBridge (1,680 multi-source queries, 3 complexity levels), achieving 0.429 LLM-judge average accuracy vs 0.336 for the best baseline (HetaRAG) with 3x fewer API calls (7.45 vs 25.21).

## Problem

Prior work has not solved evaluating agentic RAG for enterprise retail workflows, because existing agentic RAG systems operate on a single homogeneous corpus, while real retail queries span heterogeneous sources combining structured tables and unstructured text, requiring agents to route across sources, bridge isolated evidence, and synthesize a final answer.

## Contribution

(i) RetailBridge: the first multi-source retail QA benchmark, built by mapping persona-driven seller-buyer simulations into a heterogeneous enterprise database without privacy constraints.
(ii) A compositional QA synthesis pipeline: entity-linked and answer-linked operators recursively yield multi-source, multi-hop retail queries across three levels of compositional depth (Level-1 to Level-3).
(iii) Multi-stage validation of benchmark quality and practical relevance through human review, retail domain-expert assessment, and comparison with a real retail dataset.
(iv) RetailRAG: the first retail-aware agentic RAG framework, integrating auto-schema briefing, source-routed plan chaining, and diagnostic plan revision.
(v) Comprehensive benchmark of diverse agentic RAG baselines and LLM backbones, exposing multi-source chaining as the fundamental bottleneck of current retail LLM agents.

## Method

RetailBridge construction has 2 steps: (Step 1) Generate atomic QAs answerable from a single source: select evidence from one source, generate question and search query with LLM, validate via 2 filters (executable verification: query must execute on source; LLM verification: 2 judges GPT-5.5 and Claude Opus 4.7 independently confirm correctness). (Step 2) Recursively compose atomic QAs via 2 operators: entity-linked composition (Oent) hides a single entity behind a referring expression, and answer-linked composition (Oans) hides a set or scalar value behind a referring expression. Recursion stops at maximum level L=3. Every query carries reasoning level, source diversity, and evidence modality, stratifying RetailBridge along 3 diagnostic axes: reasoning capability, multi-source chaining, evidence modality.

RetailRAG has 3 components: (i) Auto-schema briefing: deterministic inspection profiles each column as numeric/categorical/free-text, LLM organizes into 4 sections (schema & metadata summary, categorical value constraints, entity alignment keys, derived analytical metrics) and injects into planner's prompt. (ii) Source-routed plan chaining: adaptive router assesses query complexity and routes simple ones directly to a single tool call, reserving planning loop for multi-source ones; planner produces full chain in a single pass specifying each step's source and search query, with later steps referencing earlier results as variables. (iii) Diagnostic plan revision: when a step fails mid-chain, repair only the failed step via 2 stages (diagnose: LLM detects failures from execution signals and assigns typed cause; revision: LLM rewrites only the failed step guided by diagnosed cause).

## KNOWLEDGE — Data & Concepts

- Heterogeneous retail database: 8 sources (5 tabular TAB: 2 product catalogs/order logs tables, 3 relational metadata tables for sales scripts/reviews/customer inquiries; 3 textual TXT: sales scripts, reviews, customer inquiries text collections), built from persona-driven seller-buyer interaction simulations.
- RetailBridge: 1,680 final queries after human verification (3 NLP experts, Gwet's AC1 = 0.89), 3 levels (Level-1/2/3), stratified by Homo/Hetero (single/multiple sources) and SQL-only/Text-only/Composite.
- Domain expert verification: 90% of queries judged as questions a seller-side analyst would ask in practice (97.5% Level-1, 90.0% Level-2, 82.5% Level-3).
- RetailRAG (gpt-oss-120b backbone): LLM-judge accuracy 0.429 average, Acc 0.298, 7.45 API calls/query.
- HetaRAG (best baseline): LLM-judge 0.336, Acc 0.212, 25.21 API calls.
- MAC-SQL: 0.263 LLM-judge, 0.175 Acc. TableRAG: 0.188. ReAct: 0.200. Dense RAG: 0.050. Text-to-SQL: 0.421 (Level-1 only).
- RetailRAG Level-3 Hetero: LLM-judge 0.302 vs HetaRAG 0.212 (best baseline).
- 10 LLM backbone benchmark: Qwen3.6-Plus 0.511, GPT-5.4 0.508, Gemma-4-31B-IT (open-source) 0.498, DeepSeek-V4-Pro 0.466, GPT-oss-120B 0.429.
- Strong models convert ~70% of routing F1 into correct answers; weak models (Qwen3.6-35B-A3B) convert under 50%.
- Text retrieval is the dominant evidence modality bottleneck; models degrade more on Text-only than SQL-only.

## INSIGHT — Mechanism & Why

[Multi-source chaining is the dominant bottleneck]: most baselines drop sharply from Homo to Hetero within each level, showing that bridging evidence across sources rather than per-step retrieval is the primary failure mode. This means scaling alone doesn't solve the problem; explicit cross-source orchestration is needed.

[Auto-schema briefing and Plan Revision dominate average drops]: these two components contribute most, especially at Level-2 where transition from atomic to multi-hop reasoning is demanding. This means schema understanding and local failure recovery are more important than just planning capability.

[Plan Routing also contributes to answer quality]: removing Plan Routing lowers accuracy across levels, most visibly at Level-1, showing the routing decision itself contributes to answer quality beyond the planning loop.

[Cross-source bridging capability scales with model size]: large models narrow or reverse the Homo/Hetero gap at Level-3 regardless of model category, while smaller models stay below 0.30 on Hetero queries. This means cross-source bridging is a capability that grows with scale.

[Text retrieval is the dominant evidence modality bottleneck]: Text-only queries degrade the steepest, identifying dense text retrieval as the dominant modality bottleneck regardless of model category or scale.

## IDEA — Actionable Applications

Apply [auto-schema briefing] to building enterprise data retrieval agents for Vietnamese solopreneurs: before letting LLM plan queries, provide a data schema summary (tables, columns, categorical value constraints, entity alignment keys, derived analytical metrics) so the LLM understands data structure before planning.

Apply [diagnostic plan revision] to building multi-step function-calling agents: when a step in a chain fails, repair only the failed step instead of restarting from scratch, reducing cost and keeping the original evidence flow intact.

Apply [source-routed plan chaining] to building multi-source retrieval agents: route each planning step to the appropriate data source (SQL table or text) before execution, keeping prior steps intact and passing intermediate values as variables.

## WISDOM — General Principle

Principle: Explicit cross-source orchestration is more important than model scaling alone when building enterprise data retrieval agents across heterogeneous sources.

When to use: When building data retrieval agents for enterprises with multiple data sources (SQL tables, text, APIs).

When NOT to use: When data resides in a single source only and queries don't require bridging evidence across sources.

Example outside original domain: Building a healthcare support agent that retrieves from Electronic Health Records (structured tables) and doctor notes (unstructured text) — needs routing across both sources and bridging evidence.

## Assumptions & Limitations

- Conditions for success: Retail data can be simulated or real enterprise data available; access to heterogeneous data sources (SQL tables, text); LLM backbone can call functions and plan multi-step.
- Paper's acknowledged limitations: Evaluation covers only retail profile and specified task workflows; transfer to other domains, successive-task reuse, and stability under meaning-preserving rewrites remain future evaluation directions. Comparisons do not isolate contribution of individual design components.
- Limitations paper does NOT mention: No explicit Limitations section (paper ends at Conclusion then References); no evaluation of storage and maintenance costs; no evaluation of stability when data changes over time.

## Metadata

- Year: 2026
- Authors: Jeonghwan Choi, Jibin Hwang, Hayoon Park, Hyeonjae Cheon, Hwanjun Song
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.25096v1
- Citation count: no information available