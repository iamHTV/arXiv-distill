# [2609.37454v1] Governing the Edge: Automating Commercial Property and Casualty Insurance Underwriting via a Hybrid Local-Cloud Multi-Agent Framework

## Problem
Underwriters in commercial Property and Casualty (P&C) insurance spend most of their day on paperwork rather than on judgment. Industry studies estimate that 30–40% of an underwriter's time goes into administrative work such as reading documents, looking up data, and rekeying, and a single submission can take about 40 minutes to process by hand. Current AI approaches only cover part of this: a single large prompt cannot enforce compliance, cannot call out to authoritative data, and usually ships raw sensitive data to a cloud API. Agent pipelines such as CrewAI split the work into separate agents, but they coordinate on task dependencies rather than on compliance, and neither keeps data private.

## Contribution
- Presents Governing the Edge, a multi-agent framework that takes over the administrative layer of commercial P&C underwriting.
- Uses 13 nodes (11 specialized agents and 2 deterministic control nodes, one of them a human-escalation interrupt) arranged as a directed workflow graph in LangGraph, split across two tiers: agents touching sensitive data run locally on Gemma 2, agents that only need to reason over anonymized scores run on Claude Sonnet via LiteLLM.
- Compliance is built into the structure of the graph — rules act as conditions on edges between agents, so a non-compliant submission cannot reach pricing in the first place instead of being caught after the fact.
- Walk-through of one full scenario end-to-end (commercial auto submission whose principal driver carries serious violations), showing every agent call, every tool invocation, and the routing decision that results.

## Method
- LangGraph StateGraph with 13 nodes and 3 branch points. Two tiers: local tier runs Gemma 2 (ollama/gemma2, temperature=0) for anything touching sensitive data; cloud tier runs Claude Sonnet 4.6 via LiteLLM for heavier reasoning over anonymized data.
- Flow: Document Parser (1) → Intake Agent (2) extracts ACORD 125 fields → 3 parallel risk sub-agents (3a Property/Fleet, 3b Geo/Driver, 3c Business/Ops) each invoking their bound tool → Risk Aggregator (3d), first cloud agent, merges scores → Compliance Agent (4) runs 10 P&C rules → if PASS, Coverage Gap (5) and Pricing (6) run in parallel → Explainability Agent (7) assembles audit trace → Human Escalation (8) is a plain interrupt firing when confidence < 0.80 or compliance fails.
- Governance: Compliance Agent runs 10 rules (5 STOP, 5 WARN). STOP rules send submission straight to human regardless of confidence. WARN rules lower confidence score and write to audit trail. Edge from Compliance Agent to Coverage Gap and Pricing only opens when check returns PASS.
- Privacy boundary: sensitive fields (raw_document, parsed_fields) omitted from state object sent to cloud agents, which see only anonymized risk_profile, compliance_result, coverage_gaps.

## Key Findings
- Framework processes a submission needing about 40 minutes of manual work in a few minutes on a single edge device (268.8 seconds end-to-end average over 20 scenarios).
- Overall compliance accuracy 70% across the 20-scenario benchmark, with the remaining gap concentrated in softer, judgment-based tiers.
- On the hard-stop violation tier — cases regulators care about most — the framework enforces every rule correctly and reproducibly (6/6), because hard stops are deterministic predicates over fields extracted at temperature 0.
- Latency trade-off: on-device inference makes the framework slower per submission than a single cloud prompt.
- Keeps a complete audit trail and respects the privacy boundary throughout, with per-agent error-tracking infrastructure across eight failure categories for operational monitoring.

## Actionable Insights
1. Build compliance into the graph structure of the workflow, not as a post-hoc check. Apply: when building multi-agent for business processes with compliance requirements, put compliance rules as edge conditions between agents — a non-compliant submission cannot proceed to the next step. First step: Design a LangGraph state graph with edge conditions checking compliance before allowing state transition.
2. Separate sensitive data layer from anonymized data layer. Apply: agents touching sensitive data run locally, agents processing only anonymized scores run on cloud. First step: Identify sensitive fields in state and exclude them from state sent to cloud agents.
3. Use deterministic rules for hard-stops, not LLM judgment. Apply: hard-stop rules (e.g., reject application with too many violations) should be Python functions, not dependent on LLM output. First step: Write Python functions that check hard-stop conditions before calling LLM agents.

## Assumptions & Limitations
- External tools are synthetic stubs returning synthetic randomized data, not connected to live APIs; results not bit-for-bit reproducible between runs.
- Scenarios are synthetic; ground-truth decisions set by a single expert; limits generalization.
- Manual times come from a published benchmark [9], not the authors' own measurements.
- Only evaluated on Gemma 2 (local) and Claude Sonnet 4.6 (cloud); does not generalize to all LLMs.

## Metadata
- Year: 2026, Authors: Vivek Kumar Singh, Gautam Bhowmick (Independent Researchers), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.37454v1