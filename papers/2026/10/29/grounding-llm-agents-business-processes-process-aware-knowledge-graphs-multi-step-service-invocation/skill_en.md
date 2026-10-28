# Skill: enterprise-api-process-aware-retrieval
Source: 2610.37242
Type: workflow

## When to use this skill
- You are building an LLM agent that calls multiple enterprise APIs in sequence (e.g. create a purchase order, then post goods receipt) and want to reduce wrong codes, missing keys, and out-of-order calls.
- The enterprise publishes OData metadata and/or has BPMN reference processes (or you can write them).
- You accept the manual effort of authoring activity-to-EntitySet mappings, about 20 minutes per activity.

## When NOT to use this skill
- Free-form APIs with no process structure (chunk-RAG is a better fit).
- You do not have structured service metadata (OData/OpenAPI) to ingest into the graph.

## Input needed
- OData $metadata documents for the target services (EntitySet, EntityType, Property, NavigationProperty, ValueHelp).
- BPMN 2.0 reference process files (or an ordered list of activities for each business process).
- A manual activity-to-EntitySet mapping (USES ENTITY SET edges) — which documents each activity reads or writes.
- An embedding model (e.g. qwen3-embedding:8b) and a Cypher-capable graph database (e.g. FalkorDB).
- A ReAct agent with hybrid retrieval, GET, and POST tools, plus a payload validator (mock or real).

## Steps to perform
1. Build the typed property graph: run the OData parser to create EntityType/EntitySet/Property/Navigation/ValueHelp nodes and HAS PROPERTY, NAVIGATE FROM, NAVIGATE TO, HAS VALUE HELP edges (store cardinality on Navigation nodes). Run the BPMN parser to create Process/Activity nodes and HAS NEXT edges from sequence flows.
2. Write the activity-to-EntitySet mapping: link each BPMN activity to the EntitySets it reads or writes (e.g. create purchase order → PurchaseOrder, PurchaseOrderItem). Keep it small (~45 edges) so it can be reviewed in full.
3. Index EntitySet summaries with FAISS for dense retrieval seeds.
4. Implement hybrid retrieval: for each query, run top-k dense retrieval over EntitySet summaries; for each seed, run a bounded Cypher query along HAS NEXT edges to fetch downstream EntitySets in the process chain; merge, deduplicate, keep dense order, and return each endpoint with its schema context (required keys, cardinalities, valid code lists, process-chain info).
5. Configure the ReAct agent: hybrid retrieval returns all typed context in one call; the agent uses GET/POST validated by a validator layer. The agent picks the endpoint, builds the payload with required keys and codes from ValueHelp, and follows process order.
6. Evaluate: Recall@k, MRR, nDCG@10 for retrieval; Completion rate and Invalid calls per run for the agent. Run the construction-fidelity audit (coverage and exactness of the graph vs sources).

## Expected output
- A typed property graph containing OData metadata and BPMN processes, linking activities to EntitySets.
- For each query: a list of proposed endpoints with schema context (required keys, cardinality, valid codes, process-chain info).
- Metrics: Recall@3, Completion rate, Invalid call rate, tool calls per run, latency.

## Example application
You build an enterprise purchasing agent. Query: "create a purchase order with a valid type code for supplier 4711, then post the goods receipt." Steps 1–3 build the graph from OData $metadata and the BPMN process "create purchase order → post goods receipt." Step 4 finds PurchaseOrder via dense search, expands to MaterialDocumentHeader via process edges, and returns the valid order-type codes (NB/UB/FO) and the 1:N item cardinality. Step 5: the agent picks PurchaseOrderType=NB from the value list, POSTs the purchase order, then POSTs the goods receipt with the purchase document reference.

## Gotchas
- The gain appears only on queries with a process signal (low lexical overlap). No improvement on OpenAPI services without a process layer.
- A wrong activity-to-EntitySet mapping degrades performance — performance depends on a correct mapping. Validate via provenance split and construction-fidelity audit.
- The mock validator shares the same metadata as the graph, so low invalid-call rates show grounding closes this failure mode by construction but do not measure performance against an independent backend.
- Mapping effort is the main practical bottleneck: ~20 minutes per activity, ~2 working days for 41 activities. Can be semi-automated with an LLM proposing edges (precision 0.79, recall 0.93, F1 0.86) and a human checking.
- Completion remains low for both methods (0.387 vs 0.103); the system is not yet ready for production deployment.
