# [2608.30255v1] CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval

## Problem
- Item-to-item (I2I) retrieval is a core primitive in large-scale recommendation and advertising systems. In production Snap Dynamic Product Ads (DPA), I2I retrieval faces two challenges: separate visual, textual, and multimodal encoders fragment the retrieval stack, and content-only training does not align embeddings with the co-engagement behavior that drives downstream conversions.

## Contribution
- CAMIE — a co-engagement-aware multimodal item embedding framework for Snap DPA retrieval.
- CAMIE builds on LLM/MLLM backbones, using their native multimodal interfaces to represent item images and metadata in a shared embedding space.
- Fine-tunes the backbone on co-engaged item pairs mined from user journeys with a symmetric in-batch InfoNCE objective.
- Offline: CAMIE outperforms the strongest commercial multimodal embedding model on Recall@10 and serves text-only retrieval from the same checkpoint with minimal quality loss.
- Online: CAMIE serves as a drop-in replacement for two deployed content-based I2I encoders, delivering +0.390% CTR / +10.832% CVR over the multimodal control, +18.958% CTR / +13.12% CVR over the text control, and +0.211% CTR / +1.911% CVR on overall DPA traffic.
- CAMIE is deployed in production.

## Method (core summary)
- Builds on LLM/MLLM backbones, using native multimodal interfaces to represent item images and metadata in a shared embedding space.
- Fine-tunes on co-engaged item pairs from user journeys with symmetric in-batch InfoNCE objective.
- Serves both multimodal and text-only retrieval from the same checkpoint.

## Key Findings
- 12 authors from Snap Inc., arXiv category: cs.IR.
- Offline: CAMIE outperforms strongest commercial multimodal embedding model on Recall@10.
- Online: +0.390% CTR / +10.832% CVR over multimodal control; +18.958% CTR / +13.12% CVR over text control; +0.211% CTR / +1.911% CVR on overall DPA traffic.
- CAMIE deployed in production.

## Actionable Insights
1. Use co-engagement tuning to align embeddings with actual conversion behavior. Application: when building recommendation/ad systems, fine-tune embeddings on co-engaged item pairs from user journeys instead of content-only.
2. Use a single multimodal backbone to serve both multimodal and text-only retrieval. Application: use one LLM/MLLM backbone for both cases instead of maintaining separate retrieval stacks.

## Assumptions & Limitations
- Evaluated on Snap DPA system; results may not transfer to other recommendation/ad systems.
- No detailed information about training time and computational cost.

## Metadata
- Year: 2026, authors: Xiaodong Liu, Xiao Bai, Yunzhi Zhou, Siman Wang, Congfei Zhang, Wen Zhang, Yajun Wang, Jingxiao Ma, Jinchao Li, Hsiang-wei Chao, Zhe Liu, Yu Zhang (Snap Inc.), arXiv category: cs.IR, PDF link: https://arxiv.org/pdf/2608.30255v1
