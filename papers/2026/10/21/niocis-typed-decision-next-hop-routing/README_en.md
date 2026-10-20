# [2610.25985v1] NIOCIS: Typed-Decision Next-Hop Routing with Node-Conditioned Option Spaces for Tool-Use Agents

## Core Value (1 sentence)
NIOCIS is a routing layer that replaces per-hop LLM deliberation with a typed-decision readout from a single forward pass, generating no text, achieving 32.8% agreement with the deployed agent fleet's actions (35.6% within declared options) in 10 ms versus 2.2 s per LLM hop.

## Problem
Tool-use agents pay per decision: at each hop, an LLM re-reads the state and thinks for seconds, though its actions are finite and its decisions recur. Execution logs already contain the answer thousands of times over, but agents recompute from scratch every time.

## Contribution
1. Loop-collapsed action graph: folds execution logs into a directed graph of forward action transitions (E+) plus explicit recovery back-edges (E−) carrying rollbacks, backtracks, and task redirects.
2. Typed-decision routing: next-hop selection as a typed decision over a node-conditioned declared option space (current node's outgoing edges plus stop), implemented with one-pass feature-MLP readouts reaching 32.8% agreement with the deployed fleet's choices (35.6% within declared space).
3. Gated self-evolution loop: each real episode becomes training data; an update is committed only if held-out validation performance does not regress beyond δ = 0.005; otherwise rolled back.
4. Route-level measurement: strict survival (episode fidelity to realized reference trace) and wrong-hop gap (accumulated cost of diverging hops).

## Method
NIOCIS comprises: (i) folding logs into a loop-collapsed action graph — directed forward transitions with recovery back-edges for rollback/backtrack/task redirect; (ii) routing with a typed-decision router whose option set is exactly the current node's outgoing edges (plus stop), whose output is a calibrated distribution the caller can threshold, with uncertain cases escalating to the LLM; (iii) self-evolution: each real episode becomes training data, updates pass a rollback gate and survive only with evidence, any update regressing beyond gate tolerance (δ) is rolled back. Full design has step budget B and per-node revisit cap R. Router reads from a single forward pass, generating no text; options structurally identified (stable edge identifiers, not surface names). Laya 0.3.21 backbone (non-autoregressive typed-decision engine on ModernBERT-large encoder) with marker-position decision head. Training via behavior cloning (cross-entropy) on (state, goal, context, next-hop) tuples from held-in logged transitions; out-of-space targets stay in objective, option masking enters only at decode.

## KNOWLEDGE — Data & Concepts
- Real SOC corpus: 22,328 records (22,192 tool calls + 136 generation records) over 1,656 traces from production SOC agent fleet (September 2026), 1,615 episodes, 154-name tool catalog, 4 domain slices (detection 1,174; response 245; protection 139; recognition 54; 3 minor agent episodes pooled)
- Decision steps: 15,704 advances + 2,364 kept recovery returns = 18,068 decision states
- Loop events: 4,124 retries (63.6% of loop events, in 2,164 bursts) + 2,364 back returns (36.4%, 146 per 100 episodes) = 29.2% of executed steps
- Node vocabulary saturation: 77 labels at 50-episode subsamples → 124 at 400 → 154 at full 1,615
- Transition pair discovery: 336 at 50 → 1,267 at 400 → 2,027 at 1,000 → 2,536 at 1,615 (702 pairs at recovery returns)
- 23 capability families; 58 arcs (50 heaviest + 8 so no family isolated) carry 64.2% of cross-family mass
- 3,709 of 14,089 advance transitions (26.3%) never leave their own family
- Two-directional hunting loops (SIEM alerts ↔ event lists 550/465; identity ↔ threat-intel 178/170; host ↔ threat-intel 171/142)
- Results (Table 2, 3,875 held-out test decisions): majority arm 26.8%; logistic regression 32.3%; feature MLP CE 32.8% (35.6% in-space); feature MLP CE+Brier 32.7% (35.5%); edge-ID CE 31.4% (34.1%); edge-ID CE+Brier 31.6% (34.3%); hidden-state probe CE 30.3% (32.9%); hidden-state probe CE+Brier 30.7% (33.3%); hidden-state probe edge-ID CE+Brier 28.9%; Laya zero-shot typed choice 26.6% (9.3% in-space)
- Paired tests (Table 3): feature MLP CE+Brier − majority = +5.70 pts, CI [+4.60, +6.90] (separates); edge-ID − class space (probe) = −3.79 pts, CI [−5.01, −2.62] (separates)
- Branch factor buckets: ≤3 (263 states, 6.8%, MLP 93.9%/99.2% in-space); 4–10 (139 states, 3.6%, MLP 38.9%/54.0%); 11+ (3,473 states, 89.6%, MLP 27.6%/29.8% in-space)
- Latency: typed decode 10–19.5 ms p50 (batch-1 GPU); MIMO Pro V2.6 LLM 2.2 s p50 (7.4 s p90); jpt-4b fine-tuned 244 ms/decision vs 10 ms
- E3 (Table 5): MIMO Pro V2.6 every hop 9.6% match, 100% LLM calls/decision; hidden-state probe 30.7% match, 0% LLM calls; typed+esc τ=0.55: 20.9% match, 74.1% LLM calls; τ=0.75: 19.1%, 80.2%; τ=0.9: 16.5%, 85.0%
- Confidence band: most confident 15% holds 91.9% accuracy; realized hop outside declared options for 7.9% of decisions; outside model top-20 for 9.3%
- E4: gate refuses 13/40 candidate updates over 10 seeded chains; δ = 0.005 (half an accuracy point)
- E5 (public process logs): BPIC'12 (13,087 cases, 262,200 events, 24 labels, loop mass 59.2%); BPIC'17 (31,509 cases, 1,202,267 events, 26 labels, 59.3%); helpdesk (4,580 cases, 21,348 events, 14 labels, 8.9%); receipt (1,434 cases, 8,577 events, 27 labels, 2.9%); roadtraffic (10,002 cases, 37,255 events, 11 labels, 1.4%); statechart (1 case, 17,912 events, 106 labels, 99.4%)

## INSIGHT — Mechanism & Why
[Typed-decision layer replaces per-hop LLM deliberation] BECAUSE [actions are finite and decisions recur; execution logs already contain the answer thousands of times over; a one-pass readout reads a calibrated distribution with no generated text and decides in milliseconds]. This means [inference cost can be reduced by orders of magnitude for recurring routing decisions].
[Node-conditioned option space beats flat catalog] BECAUSE [node-conditioned space beats a flat 155-class catalog by 3.5 points and a size-matched global-frequency space by 1.4 points, but is statistically indistinguishable from node-conditioned space built without graph traversal — the gain comes from per-node candidate restriction, not graph traversal]. This means [restricting candidates by current state matters more than graph structure].
[Gated self-evolution absorbs label corruption] BECAUSE [the gate refuses updates that regress beyond δ = 0.005 on held-out validation, and the loop absorbs 12% label-corruption stress]. This means [self-evolution can be safe with a well-defined rollback gate].
[Confidence band holds high accuracy] BECAUSE [the calibrated distribution allows thresholding; the most confident 15% holds 91.9% accuracy, and three different confidence rules trace alike]. This means [cheap computation for easy decisions, LLM only when genuinely uncertain].

## IDEA — Actionable Applications
1. Apply [typed-decision routing layer] to [reduce inference cost for tool-calling AI agents]: first step is to collect agent execution logs, fold them into a loop-collapsed action graph, then train a small readout to select next-hop from the current node's declared options, calling LLM only when confidence is low.
2. Apply [gated self-evolution loop] to [improve agents over time without regression]: first step is to set up an evaluation-gated update with δ = 0.005 tolerance, only committing router updates that don't regress held-out validation performance.
3. Apply [accept/escalate confidence gating] to [tiered decision cost]: first step is to deploy a two-tier stack where a cheap readout handles control decisions and an LLM is escalated only for uncertain states (max distribution < τ).

## WISDOM — General Principles
1. Principle: For recurring routing decisions, a cheap readout over a constrained option space can replace most LLM calls, keeping LLM only for uncertain cases. Apply when: building tool-calling agents with finite actions and recurring decisions. Do not apply when: no execution log history or infinite open-vocabulary action space.
2. Principle: Per-node candidate restriction (node-conditioned option space) matters more than graph traversal structure. Apply when: designing routing layers for agents. Do not apply when: no action graph can be induced from logs.

## Assumptions & Limitations
- Conditions that must hold: agent execution log history available, finite action set, node-conditioned option space can be induced from state.
- Limitations acknowledged by paper: reference behavior is a realized fleet policy, not a planner oracle; exported data strips tool result payloads and agent chat bodies; outcome labels are convention-derived (weak), not independently annotated; no token/currency cost measured (only latency and LLM calls per decision).
- Limitations paper does NOT mention: no evaluation on non-security-operations tasks; no direct comparison with existing model/tool routing systems beyond MIMO Pro V2.6 stand-in; no real deployment cost of maintaining the action graph.

## Metadata
- Year: 2026
- Authors: Jin Han, Mingfeng Xin, Feng Liang, Jingtao Yu (Independent Researcher)
- arXiv Category: cs.CR
- PDF Link: https://arxiv.org/pdf/2610.25985
- arXiv ID: 2610.25985v1
- Label: [applied]
- Citation count: [not found]