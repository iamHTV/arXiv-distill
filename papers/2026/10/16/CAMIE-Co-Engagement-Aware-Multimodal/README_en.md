# [2608.30255v1] CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval

## Problem
Snap's Dynamic Product Ads (DPA) system needs to retrieve items relevant to users based on product images and text. Existing multimodal encoders don't fully leverage co-engagement signals — when users interact with the same item across multiple contexts.

## Contribution
- Introduce CAMIE: Co-Engagement-Aware Multimodal Item Embeddings, fine-tuning an LLM/MLLM backbone on co-interacting item pairs to create multimodal embeddings for Snap's DPA retrieval.
- CAMIE is a drop-in replacement for two content-based I2I encoders, deployed in production.
- Online A/B tests: +0.390% CTR / +10.832% CVR over multimodal control, +18.958% CTR / +13.12% CVR over text control, +0.211% CTR / +1.911% CVR on overall DPA traffic.

## Method (core summary)
CAMIE fine-tunes an MLLM backbone on co-engagement pairs (items users interact with together) instead of static content labels. Content-derived labels rather than compute labels. Learns multimodal embeddings (image + text) with dimension d=512 (smaller than Gemini Embedding 2's d=3072). Fine-tuning Gemma 4 E2B reaches 108.2% R@10 with multimodal input.

## Key Findings
- Production A/B: +0.390% CTR / +10.832% CVR over multimodal control; +18.958% CTR / +13.12% CVR over text control; +0.211% CTR / +1.911% CVR on overall DPA traffic.
- Co-engagement fine-tuning adds 37.7% relative gain to MLLM.
- R@10: CAMIE 137.7% vs pretrained checkpoint 100.0%; improves ~6% relative over Gemini Embedding 2 (129.9%) while using smaller embeddings (d=512 vs d=3072).
- Measurable gain is entirely in conversion: CVR rises +10.832% while CTR change (+0.390%) is not significant, indicating co-engagement supervision makes items more clickable-relevant.

## Actionable Insights
- Use co-engagement supervision (training on items interacted together) instead of only static content labels: helps multimodal embedding learn relationships between items users actually view/buy together. Apply: solopreneur building product/content recommendation should collect pairs of items viewed/bought in the same session and fine-tune the embedding model on them.
- Replace two separate encoders (text-only, image-only) with a unified multimodal checkpoint: reduces serving cost with minimal quality loss (~1.1pp on R@10, 0.5pp on MRR). Apply: when building a retrieval system, merge encoders into a single multimodal checkpoint to save deployment cost.

## Assumptions & Limitations
- Requires sufficient co-engagement pairs data to fine-tune; doesn't apply without user interaction history.
- Paper admits: spread across backbones is 5.8% relative from best to worst, against 37.7% relative gain from co-engagement fine-tuning.
- Limitation paper doesn't mention: not evaluated on items beyond Snap ads, not tested on models smaller than Gemma 4 E2B.

## Metadata
- Year: 2026
- Authors: Xiaodong Liu, Xiao Bai, Yunzhi Zhou, Siman Wang, Congfei Zhang, Wen Zhang, Yajun Wang, Jingxiao Ma, Jinchao Li, Hsiang-wei Chao (Snap Inc.)
- arXiv category: cs.AI, cs.IR
- PDF link: https://arxiv.org/pdf/2608.30255
