# Skill: A-RAG — Agentic RAG with Hierarchical Interfaces
Source: 2602.03442
Type: workflow

## When to use this skill
- When building RAG systems needing agent-driven retrieval
- When multi-hop QA tasks need multiple retrieval granularities
- When wanting to leverage LLM tool-use capabilities for retrieval

## When NOT to use
- Simple single-hop retrieval sufficient
- LLM lacks tool-use capabilities
- Corpus not indexed for search

## Required inputs
- Corpus indexed for keyword and semantic search
- LLM with tool-use capabilities
- Multi-hop questions to answer

## Steps

### Step 1 — Setup Retrieval Tools
1. Keyword search: exact match retrieval
2. Semantic search: embedding-based retrieval
3. Chunk read: detailed paragraph reading
4. Output: 3 tools available for agent

### Step 2 — Agent-Driven Retrieval
1. Agent receives question
2. Decides which tool to use based on question type
3. Adaptively searches across granularities
4. Output: retrieved information

### Step 3 — Answer with Retrieved Context
1. Agent uses retrieved information
2. Reasons through multi-hop connections
3. Generates answer
4. Output: answer with citations

## Expected output
- Better multi-hop QA performance
- Efficient token usage
- Scalable with model improvements

## Example application
**Scenario**: Build knowledge base QA system.

**Application**:
1. Setup: keyword search, semantic search, chunk read tools
2. Question: "What company acquired the startup that won TechCrunch Disrupt 2024?"
3. Agent: keyword search "TechCrunch Disrupt 2024" → finds startup name → semantic search for acquisition → chunk read for details
4. Answer: correct with multi-hop reasoning

## Gotchas
1. **Agent-friendly interfaces**: Design tools for agent, not complex algorithms
2. **Hierarchical retrieval**: Keyword → semantic → chunk for coverage
3. **Model-driven scales**: Better model = better retrieval automatically
4. **Multi-hop only**: Best for questions requiring multiple retrieval steps
5. **Token efficiency**: Comparable or lower tokens than single-shot
