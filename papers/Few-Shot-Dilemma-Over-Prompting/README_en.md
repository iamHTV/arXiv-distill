# [2509.13196] The Few-shot Dilemma: Over-prompting Large Language Models

## Problem
Over-prompting — a phenomenon where excessive examples in prompts lead to diminished performance — challenges conventional wisdom about in-context few-shot learning. Prior empirical conclusion that "more relevant few-shot examples universally benefit LLMs" is NOT TRUE for all models.

## Contribution
1. **Few-shot dilemma identified**: Excessive domain-specific examples can paradoxically degrade performance in certain LLMs.
2. **TF-IDF selection outperforms**: TF-IDF vectors > random sampling > semantic embedding for software requirement classification.
3. **Optimal quantity per LLM**: Each LLM has optimal number of examples. TF-IDF + stratified → superior performance with fewer examples.

## Method (core summary)
3 few-shot selection methods: random sampling, semantic embedding, TF-IDF vectors. Tests on 7 LLMs (GPT-4o, GPT-3.5-turbo, DeepSeek-V3, Gemma-3, LLaMA-3.1, LLaMA-3.2, Mistral). Gradually increases number of TF-IDF-selected examples → identifies optimal quantity per LLM. Dataset: software requirement classification (functional vs non-functional).

## Key Findings
- Over-prompting: excessive examples → diminished performance on certain LLMs
- TF-IDF outperforms random sampling and semantic embedding
- LLaMA-3.1-8B surpasses SOTA fine-tuned PRC-BERT by 1% with 10-20 selected examples
- Large models (DeepSeek-V3, GPT-4o): more consistent with lengthy contexts
- 8B parameters may be threshold for effective few-shot comprehension
- Gemma-3-4B: declining performance with more examples

## Actionable Insights
1. **Less is more for few-shot**: Not more examples = better. Find optimal quantity for your LLM. Example: when prompting LLM for classification task, start with 5-10 examples, test performance, gradually increase until performance drops.

2. **TF-IDF selection > random**: Select examples by TF-IDF similarity instead of random. Better relevance, fewer examples needed. Example: when building few-shot prompt, use TF-IDF to find most relevant examples from training set.

3. **Model size matters**: Models <8B parameters have over-prompting problem. Larger models handle more examples. Example: when using small model (3-4B), limit examples to 10-20. Large model (70B+) → more examples OK.

## Assumptions & Limitations
**Conditions for findings to work:**
- Software requirement classification tasks
- TF-IDF selection applicable
- Model-specific optimal quantity

**Limitations the paper acknowledges:**
- Computational overhead of processing numerous examples
- Limited to specific tasks

**Limitations the paper does NOT mention:**
- Task-specific optimal quantity may vary
- Domain dependency
- Prompt format effects
- Temperature/sampling effects

## Metadata
- Year: 2025
- Authors: Yongjian Tang, Doruk Tuncel, Christian Koerner, Thomas Runkler
- Category: cs.CL
- PDF: https://arxiv.org/pdf/2509.13196
- Citation count: [EXTRACTION FAILED]
