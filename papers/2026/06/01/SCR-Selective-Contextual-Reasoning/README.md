# [2503.05212] Cập nhật Tri thức? Không cần Sửa đổi Mô hình! Chỉ cần Suy luận Ngữ cảnh Có chọn lọc

## Vấn đề
Real-world knowledge evolves → information trong LLMs trở nên outdated (lỗi thời), inadequate (không đủ), erroneous (sai). Model editing (sửa đổi mô hình) emerged như approach cho updating LLMs với minimal computational costs. Nhưng existing methods underestimate adverse effects (tác động bất lợi) của parameter modifications (sửa đổi tham số) lên broadly distributed knowledge (tri thức phân phối rộng). Post-edit LLMs struggle với multi-hop reasoning và continuous updates.

## Đóng góp
1. **Evaluation 10 model editing methods**: Along 4 dimensions: reliability, generalization, locality, portability. All show significant shortcomings
2. **SCR (Selective Contextual Reasoning)**: Không modify parameters. Harnesses LLM's inherent contextual reasoning với updated knowledge pieces
3. **Outperforms 10 model editing methods**: On counterfactual datasets với 3 backbone LLMs

## Phương pháp (tóm tắt cốt lõi)
SCR: (1) LLM assesses whether incoming query falls within scope of external knowledge base; (2) If yes → contextualize relevant external knowledge texts to enhance reasoning; (3) If no → answer directly. No parameter modification. Uses LLM's inherent contextual reasoning capabilities.

## Kết quả chính
- All 10 model editing methods show significant shortcomings across reliability, generalization, locality, portability
- SCR outperforms all 10 methods on counterfactual datasets
- No parameter modification needed
- Training-free, parameter-free, interpretable
- Works với 3 backbone LLMs

## Insight có thể áp dụng ngay
1. **Don't edit model parameters**: Model editing has significant shortcomings. Use external knowledge base + contextual reasoning instead. Ví dụ: khi cần update LLM knowledge, don't fine-tune — provide updated knowledge via context.

2. **Selective contextual reasoning**: LLM assesses query scope first, then contextualizes relevant knowledge. Ví dụ: khi build knowledge-aware chatbot, check if query relates to updated knowledge → if yes, inject relevant context → if no, answer directly.

3. **External knowledge > parameter editing**: Maintain external knowledge base, update it independently. LLM reasons over it. Ví dụ: company knowledge base updates frequently → don't retrain LLM → update external KB → LLM reasons over it via SCR.

## Giả định & Hạn chế
**Điều kiện để method work:**
- External knowledge base available
- LLM có contextual reasoning capabilities
- Query scope assessment accurate

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- External KB maintenance overhead
- Context window limits
- Scope assessment accuracy
- Latency of external retrieval
- Multi-hop reasoning quality

## Metadata
- Năm: 2025
- Tác giả: Guoxiu He, Xin Song, Aixin Sun
- Category: cs.CL
- Link PDF: https://arxiv.org/pdf/2503.05212
- Citation count: [EXTRACTION FAILED]
