# 2610.37242 Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation

## Core value (1 sentence)
For an LLM agent to call APIs reliably across multiple steps, it must respect sequential and parametric constraints (process order, required keys, valid code values) — not just pick the right endpoint — by combining OData metadata and BPMN reference processes into a typed property graph and using hybrid retrieval (dense embedding seeds plus bounded process-chain expansion).

## Problem
LLM agents calling enterprise APIs must select the correct endpoint, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and therefore misses process and schema constraints. An agent can pick the right booking API and still fail: it may invent a fare code, omit a required reference, or book the hotel before the flight — a call that fails just as badly as a call to the wrong API. Prior work (chunk-RAG) ranks endpoints but stops at retrieval, has no process-chain ground truth, and does not model the structural rules (fixed value lists, navigation cardinality) that decide whether a payload is valid.

## Contribution
- A typed property-graph schema combining service metadata with business processes, and an ingestion pipeline for OData $metadata and BPMN 2.0. Evaluated with a construction-fidelity audit and an ablation study.
- A hybrid retriever combining dense embedding seeds with bounded expansion along process-sequence edges. Evaluated for retrieval quality and for where it stops working.
- An execution-capable ReAct agent that uses retrieved value-help and cardinality context to build its calls. Evaluated, including a baseline that receives value lists as plain text, to separate the effect of seeing the values from the effect of the typed representation.
- OData-Proc, a public benchmark of 42 enterprise services, 14 BPMN reference processes, and 288 queries with two-annotator process-chain ground truth. To the authors' knowledge, the first benchmark that scores service discovery against business-process chains.

## Method (core summary)
The core idea: combine two open machine-readable standards — OData $metadata (describes entity collections, fields, and references of a service, but not the order in which they are used) and BPMN (describes the order of business tasks, but not the data each task uses) — into one typed property graph (a knowledge graph storing data as nodes and directed edges, both carrying type labels and key-value attributes), linking each process activity to the EntitySets it reads or writes.

The system has two stages:
1. Offline: an ingestion pipeline reads OData $metadata and BPMN 2.0 files and writes nodes and edges to a graph database (FalkorDB, running Cypher). It also writes a short text summary for each EntitySet and indexes the summaries with FAISS.
2. Online: the hybrid retriever takes top-k dense matches as seeds and expands them along the process chain with a bounded Cypher query. A ReAct agent then issues GET and POST calls, validated by a mock HTTP layer.

Two design choices matter for execution: (1) cardinality is stored on Navigation nodes (1:N vs N:1) so the agent knows how to shape payloads; (2) ValueHelp is its own node holding the list of valid codes, so the agent can get valid codes with one bounded graph lookup instead of relying on loose embedding matching.

## KNOWLEDGE — Data & concepts
- OData (Open Data Protocol — a standard for web services that read and write data over HTTP): $metadata is the machine-readable description each OData service publishes. EntitySet is a named collection of business records (e.g. PurchaseOrder). Property is a field of a record (e.g. Supplier). NavigationProperty links two EntitySets with a cardinality (e.g. one purchase order has many purchase-order items, 1:N). ValueHelp is the fixed list of valid codes for a property (e.g. purchase-order type must be NB, UB, or FO).
- BPMN (Business Process Model and Notation 2.0 — a standard for describing business processes): a flowchart of activities connected by sequence flows, stored as XML, machine-readable.
- Typed property graph: 8 node labels for OData and BPMN structure, 9 edge types connecting them.
- 42 enterprise services, 14 BPMN reference processes, 51 task activities, 45 mapping edges (activity-to-EntitySet), 132 EntitySets, 1,270 EntityTypes, 8,481 properties, 1,499 navigation edges.
- OData-Proc benchmark: 288 queries, deterministically split into 150 train and 138 test. Five query types: single entity, navigation chain, process-chain goal, multi-step workflow, value-help dependent. All 74 process-chain probes are in the test split.
- RQ1 (retrieval quality): on the process-chain probe (n=74), Hybrid improves Recall@3 (share of gold EntitySets appearing in top 3 results) by +5.7 points over Dense (0.732 vs 0.675, p=0.037). Over the full test split (n=138), Hybrid gains +2.3 points at k=3 (0.810 vs 0.787, p=1.7×10^-31). Graph-only performs poorly (Recall@3 0.617 vs Hybrid 0.810).
- RQ2 (ablation): both edge types (mapping USES ENTITY SET and sequence HAS NEXT) are needed. Mapping-only and sequence-only stay at Dense level (probe Recall@3 0.673 and 0.675). Full Hybrid beats mapping-only on the probe by +5.9 Recall@3 points (p=0.028).
- RQ3 (end-to-end agent): on 81 multi-step test queries (3 runs per query, 243 runs per condition, primary LLM qwen3-coder:30b), the agent completes 0.387 (38.7%) of tasks vs ChunkRAG 0.103 (10.3%, p<0.001). The agent is slower (11.5 vs 5.3 s per run) and makes more tool calls (2.45 vs 0.89). Oracle-retrieval test: completion stays low for both (ours 0.256, ChunkRAG 0.359) — execution by the 30B LLM, not only retrieval, limits completion.
- RQ4 (hallucination elicitation): on the 56-query probe (3 runs per query, 168 per condition), our method makes an invalid call in 3 of 101 POST runs (0.03, 95% CI [0.01, 0.08]) and invents no code. ChunkRAG makes an invalid call in 100 of 127 POST runs (0.79), 218 invalid calls total, 60 invented codes. ChunkRAG+VH (value-help lists pasted as plain text) invents no codes but has 120 invalid calls in 59 of 128 POST runs (0.46). Full typed context brings the rate to 0.03.
- RQ5 (external generalization): on SOCBench-D (OpenAPI, no BPMN layer), 110 queries, Hybrid and Tokens (token-overlap retriever) differ significantly at no k (R@3 +0.010, p=0.753). No gain without a process layer.
- Construction-fidelity audit: coverage and exactness are both 1.000 for every structural class (EntitySets, EntityTypes, Properties, Navigation edges with cardinality, ValueHelp codes, BPMN activities, activity order).
- Mapping effort: 45 hand-written edges, median 20.5 minutes per activity (range 16–25), ~840 person-minutes (~2 working days) for all 41 mapped activities. Semi-automation: an LLM proposes edges and a human checks them — precision 0.79, recall 0.93, F1 0.86 against the 45 hand-written edges.

## INSIGHT — Mechanism & why
- [Agent picks the right API but still fails] happens BECAUSE [it invents codes, omits required references, or books the hotel before the flight — violating sequential constraints (process order) and parametric constraints (which keys and code values are valid) around each call]. This means [picking the right endpoint is not enough; the agent needs both sequential and parametric constraints in its retrieval context].
- [Hybrid retrieval improves Recall@3 on process-chain queries] happens BECAUSE [process expansion from dense embedding seeds adds downstream EntitySets that dense retrieval alone cannot reach, because the query does not describe that target]. This means [the gain comes from process edges, not from generic graph structure; graphs built only from extracted entities do not have such edges].
- [Providing valid code lists as plain text stops invented codes but not invalid keys] happens BECAUSE [flat text does not constrain payload structure]. This means [full typed context (valid codes, cardinality, required keys) is needed to cut invalid calls to 3%, not just showing the value list].
- Condition: the gain appears only on queries with a process signal (low lexical overlap between query and downstream entities). There is no improvement on OpenAPI services without a process layer — this defines the scope: the method targets structured enterprise ecosystems; chunk-RAG remains a good fit for free-form APIs.
- A wrong activity-to-EntitySet mapping degrades performance — performance depends on a correct mapping.

## IDEA — Actionable applications
1. Apply the design of exposing process and schema constraints to an agent calling enterprise APIs: first step is to build a typed property graph combining service metadata (OData $metadata) and reference processes (BPMN), linking each process activity to the EntitySets it reads or writes.
2. Apply hybrid retrieval (dense embedding seeds plus bounded process-chain expansion): first step is to use FAISS dense retrieval to find the nearest EntitySets as seeds, then run a bounded Cypher query along HAS NEXT edges to fetch downstream EntitySets in the process chain.
3. Apply full typed context to the agent before it calls an API: first step is to feed all typed context (required keys, navigation cardinality, valid code lists, process-chain information) into a single retrieval call, keeping tool round-trips low for local models.

## WISDOM — General principle
- Principle: "For an LLM agent to call APIs reliably across multiple steps, provide sequential and parametric constraints (process order, required keys, valid code values) in the retrieval context, not just the endpoint." When to use: when building an enterprise automation agent that calls multiple APIs in sequence. When NOT to use: when APIs are free-form with no process structure (chunk-RAG remains a good fit).
- Example outside original domain: a corporate travel-booking system — the agent must select a flight, book it, then reserve a hotel using the booking reference, in order, with valid cabin class codes — provide the schema and process in the retrieval context, not just a list of endpoints.

## Assumptions & Limitations
- Conditions required for the method to work: the enterprise publishes OData metadata and BPMN reference processes (or one can be written); there is a validator to check keys and codes against the schema; the agent supports tool use and runs ReAct.
- Limitations the paper acknowledges: the construction-fidelity audit and mock validator use the same schema/ValueHelp nodes as the graph, so low invalid-call results show grounding closes this failure mode by construction but do not measure performance against an independent target; probe queries and the activity mapping have the same author; the probe-level retrieval effect is modest and does not survive Holm correction (main probe result p=0.037 does not meet the stricter 0.025 threshold); the second annotator is a disclosed LLM that worked from the same machine-suggested labels as the human, so near-perfect label agreement overstates label independence; the gain depends entirely on process edges, so it only transfers to ecosystems that publish a process layer or where one can be written; SAP's reference processes are unusually well documented and no second domain with a native process layer has been shown; completion remains low for both methods (0.387 vs 0.103), so the system is not yet ready for deployment; the evaluation is partly circular because the mock validator and graph share the same metadata.
- Limitations the paper does NOT state: not tested against an independent backend; not tested beyond SAP reference processes (no second domain with a native process layer); BPMN generation not automated for domains without process models; seed coverage and the agent's use of tools not improved.

## Metadata
- Year: 2026 | Authors: Saiful Khan (Science and Technology Facilities Council, RAL, UK), Afrah Farea (Department of Engineering Science, University of Oxford, UK)
- arXiv category: cs.AI (Computer Science - Artificial Intelligence)
- PDF link: https://arxiv.org/pdf/2610.37242v1
- Abstract link: https://arxiv.org/abs/2610.37242
- Citation count: [not found]
