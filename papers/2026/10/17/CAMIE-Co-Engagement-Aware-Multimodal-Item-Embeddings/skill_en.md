# Skill: camie-co-engagement-embedding
Source: 2608.30255v1
Type: framework

## When to use this skill
- Building recommendation/ad systems using item-to-item (I2I) retrieval.
- Need to align embeddings with co-engagement behavior driving conversions.
- Have user journey data with co-engaged item pairs.

## When NOT to use this skill
- Recommendation systems not using I2I retrieval.
- No co-engagement data from user journeys available.
- Don't need to align embeddings with actual conversion behavior.

## Input needed
- Item catalog data with images and metadata.
- User journey data containing co-engaged item pairs.
- LLM/MLLM backbone with native multimodal interface.

## Steps to execute
1. Build shared embedding space from item images and metadata using LLM/MLLM native multimodal interface.
2. Mine co-engaged item pairs from user journeys.
3. Fine-tune backbone on co-engaged pairs with symmetric in-batch InfoNCE objective.
4. Serve both multimodal and text-only retrieval from same checkpoint.
5. Monitor Recall@10 (offline) and CTR/CVR (online).

## Expected output
- I2I retrieval system with Recall@10 higher than strongest commercial multimodal embedding model.
- Online CTR/CVR lift: +0.390% CTR / +10.832% CVR over multimodal control; +18.958% CTR / +13.12% CVR over text control; +0.211% CTR / +1.911% CVR on overall traffic.

## Application example
- Build Dynamic Product Ads (DPA) system for e-commerce platform. Use CAMIE to fine-tune embeddings on co-engaged pairs from user journeys, reducing retrieval stack fragmentation and improving CTR/CVR.

## Gotchas
- Evaluated on Snap DPA system; results may not transfer to other systems.
- No detailed information about training time and computational cost.
