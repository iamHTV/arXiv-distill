# 2609.24152 — Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search at Scale

## Core Value (1 sentence)

Grad-CIR is a methodology for training composed image retrieval (CIR) retrievers on graded relevance rather than binary — using VLM to auto-curate training data and 4-level relevance labels, an iterative relevance-feedback loop mining hard negatives, and a hierarchy-aware angular objective — achieving 4.9%–5.9% NDCG@10 lift over binary labels, deployed in production at Walmart serving live visual-search traffic.

## Problem

Visual search on large e-commerce catalogs must serve both "similarity" queries asking for items resembling an uploaded image and "modifier" queries comprising an image and text describing a desired modification (e.g., a color change or style swap). The latter is known as composed image retrieval (CIR). Existing CIR methods treat relevance as binary and train on triplets with a single positive target — a poor fit for real catalogs where many candidates partially satisfy a user query and ranking across that partial-match spectrum drives customer experience.

## Contribution

1. **Grad-CIR**: A methodology for training CIR retrievers on graded relevance, comprising 3 components: (i) VLM to curate training data, generating queries (object detection + modifier synthesis) and 4-level relevance labels without manual annotation, (ii) an iterative relevance-feedback loop expanding the training set by mining hard negatives from the in-training retriever, (iii) a hierarchy-aware angular objective to train the retriever directly on graded labels rather than collapsing them to binary.

2. **Implementation on PaliGemma2**: Instantiated on a PaliGemma2 bi-encoder trained on 3.5M graded pairs curated from raw Walmart catalog data.

3. **Experimental results**: Controlled graded-vs-binary ablation shows lift of 4.9%–5.9% in NDCG@10. The same recipe applied to other multimodal encoders lifts early-fusion backbones by up to 8.5% NDCG@10. On the public FashionIQ benchmark, GradCIR (applied to PaliGemma2) reaches 0.6703 average recall when fine-tuned, slightly ahead of the strongest peer-reviewed supervised baseline, and matching or exceeding all published CLIP-L-class zero-shot CIR methods.

4. **Production deployment**: The system is deployed in production at Walmart, serving live visual-search user traffic.

## Method

Grad-CIR comprises 3 main components:

1. **VLM curates training data**: Uses VLM to generate queries (object detection + modifier synthesis) and 4-level relevance labels without manual annotation.

2. **Iterative relevance-feedback loop**: Expands the training set by mining hard negatives from the in-training retriever.

3. **Hierarchy-aware angular objective**: Trains the retriever directly on graded relevance labels rather than collapsing them to binary.

**Process:** Collect raw catalog data → VLM generates queries and graded relevance labels → Train retriever with hierarchy-aware angular objective → Iterative relevance feedback mines hard negatives → Expand training set → Repeat.

## KNOWLEDGE — Data & Concepts

- 3.5M graded pairs curated from raw Walmart catalog data.
- Model: PaliGemma2 bi-encoder.
- 4.9%–5.9% NDCG@10 lift over binary labels (controlled ablation).
- Up to 8.5% NDCG@10 lift for early-fusion backbones when applied to other multimodal encoders.
- FashionIQ benchmark: 0.6703 average recall when GradCIR (PaliGemma2) is fine-tuned.
- Surpasses strongest peer-reviewed supervised baseline; matches or exceeds all published CLIP-L-class zero-shot CIR methods.
- Deployed in production at Walmart serving live visual-search user traffic.

## INSIGHT — Mechanism & Why

[Graded relevance better than binary relevance] occurs BECAUSE [in real catalogs, many candidates partially satisfy a user query and ranking across that partial-match spectrum drives customer experience; binary labels ignore this gradation]. This means [training on graded relevance labels helps the retriever rank partial-match candidates better].

[VLM auto-curates training data] occurs BECAUSE [VLM can generate queries and 4-level relevance labels without manual annotation, reducing data curation cost]. This means [CIR training data can be scaled without large manual annotation cost].

[Iterative relevance feedback mines hard negatives] occurs BECAUSE [the in-training retriever can identify hard negative examples to expand the training set]. This means [training continuously improves the retriever by focusing on difficult cases].

## IDEA — Actionable Applications

1. Apply graded relevance to product search systems: Instead of only match/no-match labels, create 4-level relevance labels (fully match, mostly match, partially match, no match) for query-product pairs. First step: use VLM to auto-assign graded relevance labels to existing query-product pairs.

2. Use relevance feedback loop to improve retriever: During retriever training, mine hard negatives from retriever outputs to expand the training set. First step: after each training epoch, take examples the retriever ranks incorrectly and add them to the training set.

3. Apply hierarchy-aware angular objective to multimodal retrieval models: Instead of training on binary labels, use hierarchy-aware angular loss to train directly on graded relevance labels. First step: modify the retrieval model's loss function from binary contrastive loss to hierarchy-aware angular loss.

## WISDOM — General Principle

- Principle: In multimodal retrieval systems, graded relevance labels help models rank partial-match candidates better than binary labels — partial match still has value for customers.
- When to use: When building search or retrieval systems where many candidates can partially satisfy a query.
- When NOT to use: When queries have one clearly correct answer and no concept of partial match.
- Example outside original domain: In a movie recommendation system, instead of only "watched/didn't watch" labels, use graded relevance labels (watched fully, watched half, watched a bit, didn't watch) so the system can recommend movies the customer is partially interested in.

## Assumptions & Limitations

- Conditions that must hold: large catalog data available for VLM curation; NDCG@10 measurable as metric.
- Paper's acknowledged limitations: experiments on Walmart data and FashionIQ; may not represent all e-commerce catalog types.
- Limitations paper does NOT state: cost of running VLM for data curation at scale; effectiveness on non-image+text queries; generalizability across domains beyond e-commerce.

## Metadata

- Year: 2026
- Authors: Hrushikesh Mohapatra, Anubhav Gupta, Prijith Chandra, Asish Mohapatra, Sudip Datta, Anuj Garg, Venkat Bulusu, Arvind Maan, Sitesh Kumar Jalan
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2609.24152
- Citation count: not yet (new paper, Oct 2026)