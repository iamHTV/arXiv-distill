# [2609.25991v1] Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents

## Problem
RAG (Retrieval-Augmented Generation) is the dominant approach for giving LLMs access to external knowledge. However, the conventional "retrieve-concatenate-generate" pipeline makes the retrieval decision on behalf of the model: evidence is retrieved and injected whether or not the question requires it. As tool use and agent loops become more reliable, decisions about whether to retrieve, what to inspect, and when to stop can be delegated to the model. This exposes a new bottleneck: the agent does not know what knowledge is available.

## Contribution
- Propose organizing knowledge base into 3 layers (SKILL.md, index.md, frontmatter YAML) so LLM agent can autonomously decide what to query and when.
- Includes a pipeline to convert PDF/Word/web into this structure.
- Beating RAG on WixQA: Factuality 0.889, Context Recall 0.816, Hallucination Rate 4.5%, 4.015 average interaction turns.

## Method (core summary)
Knowledge-as-Skill organizes knowledge into 3 layers: SKILL.md (describes the skill/knowledge), index.md (index), frontmatter YAML (metadata). The agent autonomously decides when to query, which section to inspect, and when to stop, instead of RAG injecting evidence automatically. A pipeline converts PDF/Word/web documents into this 3-layer structure.

## Key Findings
- Knowledge-as-Skill achieves 0.889 Factuality, 0.816 Context Recall, 4.5% Hallucination Rate, 4.015 average interaction turns on WixQA.
- Beats RAG on WixQA benchmark.
- Evaluation is still preliminary.

## Actionable Insights
- Don't let RAG inject all evidence into context automatically: let the agent decide when to retrieve and which section to inspect. Apply: solopreneur building a knowledge base for agents should organize knowledge into a 3-layer structure (SKILL.md, index.md, YAML) and let the agent actively query.
- Use skill-structured knowledge base instead of raw documents: the agent knows "what this skill does, when to use it". Apply: when building content-KB for agents, each knowledge item should have a SKILL.md describing purpose and usage conditions.

## Assumptions & Limitations
- Requires the agent to have autonomous query decision capability; doesn't apply if the agent just receives context from simple RAG.
- Paper admits: evaluation is still preliminary.
- Limitation paper doesn't mention: not evaluated on many domains beyond WixQA, not tested on real token cost vs RAG.

## Metadata
- Year: 2026
- Author: Jiangxu Wu (Sun Yat-sen University)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.25991
