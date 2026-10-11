# [2602.03442] A-RAG: Mở rộng Agentic RAG qua Giao diện Truy xuất Phân cấp

## Vấn đề
Frontier language models có strong reasoning và long-horizon tool-use capabilities. Nhưng existing RAG systems fail to leverage (tận dụng) these capabilities. Hai paradigms cũ: (1) single-shot retrieval + concatenate; (2) predefined workflow. Neither paradigm allows model to participate trong retrieval decisions — preventing efficient scaling với model improvements.

## Đóng góp
1. **A-RAG framework**: Agentic RAG exposes hierarchical retrieval interfaces (giao diện truy xuất phân cấp) trực tiếp cho model
2. **3 retrieval tools**: Keyword search, semantic search, chunk read — agent adaptively searches across multiple granularities (độ chi tiết)
3. **Outperforms existing approaches**: Comparable hoặc lower retrieved tokens trên multi-hop QA benchmarks

## Phương pháp (tóm tắt cốt lõi)
A-RAG: expose 3 retrieval tools trực tiếp cho LLM agent: (1) Keyword search — tìm theo từ khóa; (2) Semantic search — tìm theo nghĩa; (3) Chunk read — đọc chi tiết đoạn văn. Agent tự quyết định khi nào dùng tool nào, adaptively search across granularities. Model-driven retrieval thay vì algorithm-driven.

## Kết quả chính
- Outperforms Graph-RAG và Workflow RAG trên diverse benchmarks
- Comparable hoặc lower retrieved tokens
- Scales with model size và test-time compute
- Multi-hop QA: HotpotQA, 2WikiMultiHopQA, MuSiQue, GraphRAG-Bench

## Insight có thể áp dụng ngay
1. **Agent-friendly interfaces > complex algorithms**: Khi build RAG systems, design interfaces cho agent thay vì complex retrieval algorithms. Ví dụ: expose keyword search, semantic search, chunk read làm tools — let agent decide.

2. **Hierarchical retrieval**: Multiple granularities (keyword → semantic → chunk) cho better coverage. Ví dụ: khi build knowledge base search, provide keyword search cho quick lookup, semantic search cho concept matching, chunk read cho detailed info.

3. **Model-driven retrieval scales**: Agent-driven retrieval scales với model improvements. Invest vào model quality. Ví dụ: khi upgrade LLM, retrieval automatically improves — no algorithm redesign needed.

## Giả định & Hạn chế
**Điều kiện để method work:**
- LLM with strong tool-use capabilities
- Corpus indexed cho keyword và semantic search
- Multi-hop QA tasks tested

**Hạn chế paper thừa nhận:**
- No exhaustive tool design comparison
- Not validated on larger models (GPT-5, Gemini-3)
- Multi-hop QA only — other tasks untested

**Hạn paper KHÔNG nói:**
- Computational cost of agent-driven retrieval
- Latency compared to single-shot retrieval
- Tool selection accuracy
- Scalability to very large corpora

## Metadata
- Năm: 2026
- Tác giả: Mingxuan Du, Benfeng Xu, Chiwei Zhu, et al.
- Category: cs.CL
- Link PDF: https://arxiv.org/pdf/2602.03442
- Citation count: [EXTRACTION FAILED]
