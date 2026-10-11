# [2605.10555] Agent-First Tool API: A Semantic Interface Paradigm for Enterprise AI Agent Systems

## Problem
AI agents transition from research prototypes to enterprise production systems, but tool interfaces remain rooted in human-oriented CRUD paradigms. Five architectural mismatches: exact-identifier dependence, rendering-oriented responses, single-shot interaction assumptions, user-equivalent authorization, opaque error semantics.

## Contribution
1. **Six-Verb Semantic Protocol**: Decomposes tool interactions into search, resolve, preview, execute, verify, recover.
2. **Normalized Tool Contract (NTC)**: Structured decision-support metadata — confidence scores, evidence chains, suggested next actions.
3. **Dual-layer governance**: Static capability policies + dynamic risk escalation.

## Method (core summary)
Agent-First Tool API: (1) Six-Verb Protocol: search → resolve → preview → execute → verify → recover; (2) NTC: each tool response contains structured metadata — confidence, evidence, next actions; (3) Governance: static policies (what tools can do) + dynamic risk (real-time escalation). Validated on production SaaS: 85 tools, 6 business domains.

## Key Findings
- 88% end-to-end task success rate vs 64% CRUD baselines (+37.5%)
- 72.7% reduction in human interventions
- 5.8x improvement in autonomous error recovery
- 85 registered tools across 6 business domains
- Production multi-tenant SaaS platform validated

## Actionable Insights
1. **Six-Verb Protocol for tool interactions**: When designing APIs for AI agents, use structured protocol: search → resolve → preview → execute → verify → recover. Example: when building AI assistant that calls APIs, structure each interaction with 6 verbs — agents know exactly what to expect.

2. **NTC: structured metadata in responses**: Tool responses must contain confidence scores, evidence chains, suggested next actions. Example: when API returns data, include: confidence: 0.85, evidence: [source1, source2], next_actions: ["verify_with_user", "execute"].

3. **Dual-layer governance**: Static policies (what tools can do) + dynamic risk (real-time escalation). Example: when deploying AI agent in enterprise, define static policies (agent can read but not write financial data) + dynamic risk (if agent tries to delete >10 records → escalate to human).

## Assumptions & Limitations
**Conditions for paradigm to work:**
- Enterprise APIs can be adapted to Agent-First protocol
- Production SaaS platform available
- Tool registration system

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- Migration cost from CRUD to Agent-First
- Tool developer adoption challenges
- Performance overhead of six-verb protocol
- Legacy system compatibility

## Metadata
- Year: 2026
- Author: Kai Pan
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.10555
- Citation count: [EXTRACTION FAILED]
