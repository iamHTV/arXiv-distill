# [2503.05212] Knowledge Updating? No More Model Editing! Just Selective Contextual Reasoning

## Problem
Real-world knowledge evolves → information in LLMs becomes outdated, inadequate, erroneous. Model editing emerged as approach for updating LLMs with minimal computational costs. But existing methods underestimate adverse effects of parameter modifications on broadly distributed knowledge. Post-edit LLMs struggle with multi-hop reasoning and continuous updates.

## Contribution
1. **Evaluation of 10 model editing methods**: Along 4 dimensions: reliability, generalization, locality, portability. All show significant shortcomings.
2. **SCR (Selective Contextual Reasoning)**: Does not modify parameters. Harnesses LLM's inherent contextual reasoning with updated knowledge pieces.
3. **Outperforms 10 model editing methods**: On counterfactual datasets with 3 backbone LLMs.

## Method (core summary)
SCR: (1) LLM assesses whether incoming query falls within scope of external knowledge base; (2) If yes → contextualize relevant external knowledge texts to enhance reasoning; (3) If no → answer directly. No parameter modification. Uses LLM's inherent contextual reasoning capabilities.

## Key Findings
- All 10 model editing methods show significant shortcomings across reliability, generalization, locality, portability
- SCR outperforms all 10 methods on counterfactual datasets
- No parameter modification needed
- Training-free, parameter-free, interpretable
- Works with 3 backbone LLMs

## Actionable Insights
1. **Don't edit model parameters**: Model editing has significant shortcomings. Use external knowledge base + contextual reasoning instead. Example: when needing to update LLM knowledge, don't fine-tune — provide updated knowledge via context.

2. **Selective contextual reasoning**: LLM assesses query scope first, then contextualizes relevant knowledge. Example: when building knowledge-aware chatbot, check if query relates to updated knowledge → if yes, inject relevant context → if no, answer directly.

3. **External knowledge > parameter editing**: Maintain external knowledge base, update it independently. LLM reasons over it. Example: company knowledge base updates frequently → don't retrain LLM → update external KB → LLM reasons over it via SCR.

## Assumptions & Limitations
**Conditions for method to work:**
- External knowledge base available
- LLM has contextual reasoning capabilities
- Query scope assessment accurate

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- External KB maintenance overhead
- Context window limits
- Scope assessment accuracy
- Latency of external retrieval
- Multi-hop reasoning quality

## Metadata
- Year: 2025
- Authors: Guoxiu He, Xin Song, Aixin Sun
- Category: cs.CL
- PDF: https://arxiv.org/pdf/2503.05212
- Citation count: [EXTRACTION FAILED]
