# Skill: realms-schema-aware-nl2sql-audience-sizing
Source: 2609.30547v1
Type: framework

## When to use this skill
- Building conversational analytics on complex nested enterprise schemas.
- Need exact audience counting rather than sampling-based estimates.
- Large customer profile data (millions of profiles, thousands of attributes) with real-time response requirements (seconds, not hours).

## When NOT to use this skill
- Unstructured data without clear schema (free text, images).
- Approximate estimates are sufficient; exact counts not needed.
- No enterprise customer data source available for schema standardization.

## Input needed
- Customer profile data from multiple sources (web, transactions, offline) with different schemas.
- Natural language audience-sizing requests.
- Retriever capable of generating embeddings and vector search.
- LLM for SQL generation.
- Scalable analytical database for columnar storage.

## Steps to execute
1. Offline pre-processing: export hierarchical profile records from source data platform, flatten into columnar representation, store in scalable analytical database.
2. Generate embeddings for schema attributes and build vector index for semantic search.
3. At runtime: encode user query into dense embedding, retrieve relevant schema attributes via semantic retrieval (schema-aware attribute retrieval).
4. Build prompt using retrieved schema context and reusable query templates (template-based in-context learning).
5. Use LLM to translate natural language audience definition into executable SQL over complex nested schema structures.
6. Schema standardization: materialize data into standardized columnar representation, abstract away source-specific differences.
7. Execute SQL against analytical database, return exact audience count.
8. Generate concise natural-language explanation alongside results.

## Expected output
- Natural language audience-sizing query system with exact counts, median latency under 10 seconds.
- Recall@k 94%, Exact-match 93% for attribute retrieval; Execution match 90% for SQL generation.

## Application example
- Marketing team wants to know "How many profiles visited the mobile app within the last 6 months and are older than 30 years?": use REALMS to retrieve relevant schema attributes (app_visit, age), generate exact counting SQL, return result in seconds instead of hours via sampling.

## Gotchas
- System deployed on a specific enterprise customer data platform; results may not transfer directly to other environments.
- Schema standardization is required for industry-agnostic deployment.
- When schemas change, embedding index and query template library need updates, incurring storage and processing costs.
