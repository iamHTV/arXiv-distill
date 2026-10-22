# 2610.24913 A Cross-Domain Evaluation of Prompting Techniques for Large Language Models

## Problem
Existing studies evaluate prompting techniques using different LLMs, datasets, or task settings, making direct comparisons across methods and domains difficult. No controlled cross-domain evaluation using the same LLM and unified setup exists.

## Contribution
- Controlled cross-domain evaluation of four prompting techniques: Zero-Shot Prompting, Few-Shot Prompting, Retrieval-Augmented Generation (RAG), and PE2-inspired automatic prompt optimization — all using the same LLM (GPT-4o-mini) on six benchmark datasets covering arithmetic reasoning, logical reasoning, commonsense reasoning, and factual verification.
- No prompting strategy consistently outperforms others across all domains; no statistically significant differences between highest and second-highest configurations (all adjusted p-values = 1.000 after Holm correction).
- RAG: highest overall average accuracy 78.33% with 300 retrieval examples. Few-Shot: 77.83% with 200 demonstration examples. Zero-Shot: highest single result on BoolQ (90.0%). PE2: stable but not systematically superior (74.08%/74.25%/74.00% for 100/200/300 optimization examples).
- Increasing task-specific examples does not consistently improve performance — strong domain and task dependency.

## Method
Experimental setup: All experiments used GPT-4o-mini via OpenAI Chat Completions API, temperature 0.0, each benchmark instance processed through isolated API requests. Performance measured as accuracy (proportion of correctly answered instances).

Six benchmark datasets: Elementary Math QA (arithmetic), Logical Fallacy Detection (logical), Navigate (spatial/abstract logical), BoolQ (boolean QA/reading comprehension), Social IQA (social commonsense), Fact Checker (factual verification). 200 test instances per dataset used consistently across all techniques. Example pools of 100/200/300 for Few-Shot, RAG, and PE2.

Four prompting techniques:
1. Zero-Shot: task instruction only, no demonstration examples.
2. Few-Shot: adds fixed demonstration examples to prompt context (n = 100, 200, 300).
3. RAG: dynamically retrieves semantically relevant examples from task-specific example pool, k = 5 retrieved per instance, pool size 100/200/300. Uses Azure AI Search with embedding-based similarity matching. This is retrieval-based example augmentation, not knowledge-grounded RAG.
4. PE2: iterative automatic prompt optimization, uses incorrectly answered examples to generate and select revised prompt variants, limited to 3 iterations, beam-like selection based on validation accuracy. Both task and proposal roles use GPT-4o-mini.

## KNOWLEDGE — Data & Concepts
- No prompting strategy consistently outperforms others across all domains; no statistically significant differences between highest and second-highest configurations (all adjusted p-values = 1.000, 8 pairwise comparisons).
- RAG: highest overall average 78.33% (300 examples); highest on Elementary Math QA (66.0%) and Logical Fallacy Detection (85.5%).
- Few-Shot: highest average 77.83% (200 demonstration examples).
- Zero-Shot: highest single result on BoolQ (90.0%); competitive on self-contained input tasks.
- PE2: stable but not superior on average (74.08%/74.25%/74.00% for 100/200/300); highest on Social IQA (79.0%).
- Few-Shot 100→200 improves slightly (76.92%→77.83%), 300 adds no gain; RAG improves consistently (75.75%→78.33%, 100→300); PE2 stable (74.08/74.25/74.00).

## INSIGHT — Mechanism & Why
[No prompting technique consistently outperforms across all domains] happens BECAUSE the effectiveness of each technique depends on the structure and characteristics of the target task (Zero-Shot wins on BoolQ because required information is already in the instance; Few-Shot/RAG win on structured reasoning tasks). This means [prompting techniques should be selected adaptively based on task characteristics rather than treated as universally applicable optimization strategies].
[Increasing examples does not consistently improve performance] happens BECAUSE Few-Shot effectiveness depends not only on the number of examples but on their relevance and compatibility with the task; RAG scales more positively because a larger pool increases the chance of retrieving relevant examples. This means [both the choice of prompting technique and the amount of contextual information should be task-dependent design decisions, not fixed defaults].

## IDEA — Actionable Applications
1. Apply the principle of evaluating prompting techniques on the target task before choosing: first step is to run a small experiment on a representative dataset with Zero-Shot, Few-Shot, RAG, and select the best-performing technique rather than defaulting to the most complex.
2. Apply RAG with larger example pools for structured reasoning tasks: first step is to build task-specific example pools (100–300 examples) and use semantic similarity retrieval (k=5) to augment few-shot demonstrations.

## WISDOM — General Principle
Principle: Prompting effectiveness depends strongly on task structure and domain; no technique is universally optimal, so evaluate on the target task rather than choosing based on complexity. Use when: selecting a prompting technique for an LLM-based system on a specific domain. Do NOT use when: assuming more complex prompting is always better without empirical evaluation.

## Assumptions & Limitations
- Only GPT-4o-mini used; findings may not generalize to other LLM architectures/sizes.
- Only six benchmark datasets and 200 test instances per dataset; larger sets and more domains could yield more robust conclusions.
- Each configuration evaluated once per instance (no repeated generations), temperature 0.0.
- Accuracy only metric; doesn't capture class-specific error patterns or qualitative reasoning differences.
- RAG used example-based augmentation, not external knowledge retrieval.
- PE2 implementation adapted specifically for this experimental setup.

## Metadata
- Year 2026; authors: Kevin Krazius, Tim Schlippe, Paul Libbrecht (IU International University of Applied Sciences, Germany); category: cs.AI; PDF: https://arxiv.org/pdf/2610.24913v1; code: https://github.com/dieKrake/prompting-techniques; citation count: [NO DATA — paper 2026-10-17]