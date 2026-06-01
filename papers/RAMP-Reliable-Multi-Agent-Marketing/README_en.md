# [2508.11120] RAMP: Reliable Multi-Agent Systems for Marketing via Reflection, Memory, and Planning

## Problem
LLM-based AI agents can plan and interact with tools to complete complex tasks. But literature on reliability in real-world applications remains limited. In marketing: audience curation — agents need to filter, verify, refine results — but agents often hallucinate and add unnecessary filters.

## Contribution
1. **RAMP framework**: Multi-agent for marketing audience curation. Plans, calls tools, verifies output, generates suggestions.
2. **Long-term memory store**: Knowledge base of client-specific facts + past queries.
3. **Iterative verification/reflection**: +20 pp recall on ambiguous queries, higher user satisfaction.
4. **Results**: +28 pp accuracy on 88 evaluation queries.

## Method (core summary)
RAMP: (1) Planner generates step-by-step plan using table metadata; (2) Actor executes plan — NL2Code translates filters to Python functions; (3) Verifier checks output quality; (4) Reflector generates suggestions for improvement. Long-term memory: semantic memory (client facts) + episodic memory (past queries). Iterative: verify → reflect → refine loop for ambiguous queries.

## Key Findings
- Baseline (Actor Only): 58.3% accuracy
- Actor + Planner: 63.3% (+5 pp)
- Actor + Semantic Memory: 70.6% (+12.3 pp)
- Actor + Planner + Semantic Memory: 87.0% (+28.7 pp)
- Iterative verification: +20 pp recall on ambiguous queries
- Models without memory hallucinate — add unnecessary filters
- Memory count: recall increases with more memory, precision peaks at 6 memories

## Actionable Insights
1. **Semantic memory is crucial**: Without memory, models hallucinate, add unnecessary filters. Always provide client-specific facts. Example: when building AI marketing agent, maintain knowledge base about client's products, past campaigns, audience segments — don't rely on metadata alone.

2. **Planner + Memory combination is key**: Either alone helps, but combined = +28 pp. Example: marketing automation — first plan (what filters to apply), then execute with memory (what worked before).

3. **Iterative verification for ambiguous queries**: More verify/reflect iterations → better recall. Example: when audience query is ambiguous ("high-value customers"), iterate: verify output → reflect on quality → refine filters.

## Assumptions & Limitations
**Conditions for method to work:**
- Table metadata available (column names, data types, sample values)
- Client-specific knowledge base
- GPT-4.1 tested — other models untested

**Limitations the paper acknowledges:**
- Only tested OpenAI GPT 4.1
- Narrow marketing domain
- Reflect/verify can be tedious for users

**Limitations the paper does NOT mention:**
- 88 queries limited evaluation set
- Memory management overhead
- Hallucination still possible even with memory
- Cost of iterative verification
- Privacy concerns with client-specific memory

## Metadata
- Year: 2025
- Authors: Lorenzo Jaime Yu Flores, Junyi Shen, Goodman Gu
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2508.11120
- Citation count: [EXTRACTION FAILED]
