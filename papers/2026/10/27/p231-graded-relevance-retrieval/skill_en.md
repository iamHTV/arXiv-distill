# Skill: grad-cir-graded-relevance-retrieval

Source: 2609.24152
Type: framework

## When to use this skill

- Building composed image retrieval (CIR) systems for e-commerce.
- Wanting to improve ranking of partial-match candidates in visual search.
- Have large catalog data and can use VLM for training data curation.

## When NOT to use this skill

- Queries with one clearly correct answer and no partial match concept.
- No VLM available or cannot afford VLM curation cost.

## Input needed

- Product catalog data (images + descriptions).
- Existing query-product pairs.
- VLM to generate queries and graded relevance labels.
- Multimodal retrieval model to train.

## Steps to execute

1. Use VLM to curate training data: generate queries (object detection + modifier synthesis) and 4-level relevance labels from raw catalog data, without manual annotation.
2. Train multimodal retriever on graded relevance labels using hierarchy-aware angular objective.
3. Apply iterative relevance-feedback loop: mine hard negatives from in-training retriever to expand training set.
4. Repeat training and dataset expansion until desired performance reached.
5. Evaluate with NDCG@10 on test set.

## Expected output

- Multimodal retriever trained on graded relevance labels.
- Training dataset with 4-level relevance labels.
- NDCG@10 improvement over binary label training.

## Example application

An e-commerce visual search team: instead of assigning match/no-match labels to image-product pairs, use VLM to create 4-level relevance labels (fully match, mostly match, partially match, no match). Train retriever with Grad-CIR, achieving 4.9%–5.9% NDCG@10 lift over binary labels.

## Gotchas

- Graded relevance labels help rank partial-match candidates better than binary labels.
- VLM auto-curation reduces manual annotation cost.
- Iterative relevance feedback mines hard negatives to continuously improve retriever.
- Hierarchy-aware angular objective trains directly on graded labels instead of collapsing to binary.