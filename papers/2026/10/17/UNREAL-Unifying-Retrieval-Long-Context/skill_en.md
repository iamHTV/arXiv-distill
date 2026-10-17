# Skill: unreal-internal-evidence-selection
Source: 2610.08463v1
Type: framework

## When to use this skill
- Building retrieval and long-context inference systems using a single model instead of two separate models (retriever + LLM).
- Need evidence selection at both corpus scale (millions of chunks) and long-context scale (long prompts).
- Can add fewer than 500K trainable parameters on top of a frozen LLM backbone.

## When NOT to use this skill
- Need full fine-tuning of the model instead of adding a small number of parameters.
- No access to the model's internal states/residual stream.
- Task is not about evidence selection (e.g., pure text generation).

## Input needed
- Frozen LLM with access to internal states/residual stream.
- Candidate chunks to encode.
- Retrieval query.
- Contrastive loss function to train soft prompt and layer weights.

## Steps to execute
1. Encode candidate chunks from the internal states of the frozen LLM.
2. Derive retrieval queries directly from the internal states of the frozen LLM.
3. Add a soft prompt to elicit retrieval mode and layer weights combining internal states for evidence ranking.
4. Train with contrastive loss on the frozen backbone.
5. At corpus scale: retrieve from a 21M-chunk Wikipedia index (3B tokens).
6. At long-context scale: rank chunks within a long prompt and return only selected text to the same frozen LLM for answering.

## Expected output
- Single model for evidence selection across corpus retrieval and long-context inference.
- Recall improvements: HotpotQA 49.1%→73.2%, 2WikiMultiHopQA 31.7%→60.1%, MuSiQue 8.8%→14.4%.
- Long-context accuracy improvements: NoLiMa 1.0%→24.83% (128K tokens), LV-Eval F1 49.97%→54.66% (256K words).
- Reduced FLOPs and time-to-first-token from ~32K tokens onward.

## Application example
- Build a QA system on long documents: use UNREAL to rank chunks within a long prompt and return only relevant chunks to the LLM for answering, instead of feeding the entire long prompt to the model.

## Gotchas
- Evaluated on 4 backbone models.
- Corpus is Wikipedia (3B tokens, 21M chunks).
- Long-context tasks: NoLiMa, LV-Eval, HELMET.
- Adds fewer than 500K trainable parameters — not a zero-parameter solution.
