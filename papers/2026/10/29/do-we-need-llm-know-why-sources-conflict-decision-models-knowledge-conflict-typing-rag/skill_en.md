# Skill: rag-conflict-typing-decision-model
Source: 2610.36915
Type: workflow

## When to use this skill
- You are building a RAG (search-augmented generation) system and need to classify the type of knowledge conflict among retrieved sources before generating the answer.
- You want to reduce the cost and latency of this classification step versus calling a high-end LLM.
- You have a small labeled conflict dataset (or can label a small portion) to choose the model and set the cascade threshold.

## When NOT to use this skill
- Your task requires long text generation or open-ended reasoning, not fixed-label classification.
- You do not have an API supporting structured output (probabilities over allowed answers) from a decision model.

## Input needed
- Query and numbered list of search results (URL, title, snippet, publication date if available, most relevant 512-token segment).
- List of decision models available via your gateway and their price/latency.
- A small labeled dev set of conflict types to choose question format and set the cascade threshold (if using cascade).
- A generator and a high-end LLM for the cascade step (if using cascade).

## Steps to perform
1. Build the input for each query: concatenate URL, title, snippet, publication date (if available), and the most relevant 512-token segment of each search result; keep dataset order and number them.
2. Send one direct choice question (flat question) with five options (No conflict, Complementary information, Conflicting opinions, Outdated information, Misinformation) to each candidate decision model. Copy task, category definitions, and examples verbatim from Cattan et al. (2025)'s prompt. The predicted type is the most probable option; its probability is the model's confidence.
3. Choose the best decision model on the dev set: measure accuracy, macro-F1, and expected calibration error (ECE). Do not choose on accuracy alone — also check how well confidence ranks errors (AUROC) if you plan to use cascade.
4. Decide whether to use cascade: if confidence ranks errors well (high AUROC), escalate the least confident fraction of queries (e.g. 25% lowest) to a high-end LLM, keep the rest with the decision model. The threshold is a quantile of confidence, uses no labels.
5. Feed the predicted type into the generator, with the definition and expected behavior of that type; the generator writes the final answer.
6. (Optional) End-to-end evaluation: use an LLM judge to check whether the answer follows the expected behavior of the gold type.

## Expected output
- Predicted conflict type for each query, with confidence (top probability).
- If using cascade: the fraction of queries escalated to the high-end LLM and the fraction handled by the decision model.
- A report of accuracy, cost, and latency of the classification step versus using only the high-end LLM.

## Example application
You operate a web-question-answering system. Before generating the answer, you run steps 1–3 and find a cheap decision model (e.g. $0.04/1,000 queries) matches LLM accuracy ($1.66/1,000 queries) but is 5× faster. You run step 4 and escalate the 25% least confident queries to Gemini 3.8 Flash, keeping 75% with the decision model — cost drops to 25–37% of LLM-only cost, accuracy ties the LLM. You run step 5 and generate the answer given the predicted type.

## Gotchas
- Decomposing the taxonomy into yes/no questions lowers accuracy for all 11 models — use the direct choice question (flat), not a yes/no split.
- A repair fitted on one model's errors does not transfer to other models — use the same question format for all models.
- Some models' confidence (e.g. GPT-6 Luna, AUROC 0.65) barely ranks errors — cascade does not help them; measure AUROC before deciding on cascade.
- Hosted models change without notice (unversioned identifiers) — re-measure periodically on your own deployment data, not on a single accuracy figure.
- The primary LLM judge is the generator's own model, which may favor its own answers — use an independent judge if possible.
