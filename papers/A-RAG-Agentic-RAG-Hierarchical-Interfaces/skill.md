# Skill: A-RAG — Agentic RAG với Giao diện Phân cấp
Nguồn: 2602.03442
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) RAG systems cần agent-driven retrieval
- Khi multi-hop QA tasks cần multiple retrieval granularities
- Khi muốn leverage LLM tool-use capabilities cho retrieval

## KHÔNG nên dùng khi
- Simple single-hop retrieval sufficient
- LLM lacks tool-use capabilities
- Corpus không indexed cho search

## Input cần có
- Corpus indexed cho keyword và semantic search
- LLM with tool-use capabilities
- Multi-hop questions cần answer

## Các bước thực hiện

### Bước 1 — Setup Retrieval Tools (thiết lập công cụ)
1. Keyword search: exact match retrieval
2. Semantic search: embedding-based retrieval
3. Chunk read: detailed paragraph reading
4. Output: 3 tools available for agent

### Bước 2 — Agent-Driven Retrieval (truy xuất do tác nhân)
1. Agent receives question
2. Decides which tool to use based on question type
3. Adaptively searches across granularities
4. Output: retrieved information

### Bước 3 — Answer with Retrieved Context (trả lời với ngữ cảnh)
1. Agent uses retrieved information
2. Reasons through multi-hop connections
3. Generates answer
4. Output: answer with citations

## Output mong đợi
- Better multi-hop QA performance
- Efficient token usage
- Scalable with model improvements

## Ví dụ áp dụng
**Tình huống**: Build knowledge base QA system.

**Áp dụng**:
1. Setup: keyword search, semantic search, chunk read tools
2. Question: "What company acquired the startup that won TechCrunch Disrupt 2024?"
3. Agent: keyword search "TechCrunch Disrupt 2024" → finds startup name → semantic search for acquisition → chunk read for details
4. Answer: correct with multi-hop reasoning

## Lưu ý quan trọng
1. **Agent-friendly interfaces**: Design tools for agent, not complex algorithms
2. **Hierarchical retrieval**: Keyword → semantic → chunk for coverage
3. **Model-driven scales**: Better model = better retrieval automatically
4. **Multi-hop only**: Best for questions requiring multiple retrieval steps
5. **Token efficiency**: Comparable or lower tokens than single-shot
