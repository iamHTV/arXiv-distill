# Skill: Multi-Interest Guidance Query Generation (SFT-RL-DPO)
Source: 2609.03674v1
Type: framework / workflow

## When to use this skill
- You need to generate personalized guidance queries or suggestion content for users with multiple interests (multi-interest users) in e-commerce, content recommendation, or marketing automation.
- You need a small LLM (30B MoE) to reach near-teacher quality with low latency for online serving.
- Do NOT use: when the user has a single clear interest (simpler approaches suffice); when there is no behavior sequence history (missing input); when no teacher model is available for supervision.

## Required inputs
- User profile P_u (consumption patterns + basic personal info, summarized by a Qwen model)
- User historical sequence S_u: recent ≤50 behaviors, format "<idx><time><type><content>", type ∈ {like, favorite, add-to-cart, purchase, search}, content = item title (compressed to a short title) or search query
- Item short titles (compressed from original titles via Qwen3-30B-A3B fine-tuned on DeepSeek-V4 Pro outputs)
- Teacher model (DeepSeek-V4 Pro or equivalent) for interest segmentation + reference queries
- Manually annotated data for the judge model (S/A/B rating)
- Infra: mapping table (user_id → guidance queries), vector retrieval, nearline compute

## Steps
1. **Context compression:** Truncate history to the 50 most recent behaviors; format "<idx><time><type><content>" separated by "|". Compress item titles into short titles (drop marketing keywords, flagship-store words) — reduces input tokens 26.8% and RT 10.7%.
2. **SFT (single-interest style learning):** Use the teacher model to segment user interests and generate a reference guidance query per sub-interest; fine-tune the student on single-interest subsequences only (NOT mixed-interest sequences — causes autonomous extrapolation and focus on a single main interest). Instructions indicate application scenarios (single item consultation, comparative decision-making, category selection) and require guidance value, content compliance, concise expression.
3. **RL (multi-interest segmentation + generation):** Prompt the model to reason in 3 steps: Step 1 — segment into ≤3 interest subsequences (temporal proximity + semantic relevance + profile preferences), label I_k; Step 2 — infer consumption intent M_k + predict the next item i_k; Step 3 — generate 3 guidance queries + a confidence score c. Optimize with GRPO (group size 8) using 4-level rewards:
   - Think-level: R_match (Optimal Ordered Matching DP between reference and model subsequences, score = 2·|Ŝ∩S|/(|Ŝ|+|S|)·log(|Ŝ|+|S|), primary interests earlier) + R_think_format (detect Step1/2/3 + JSON completeness).
   - Query-level: R_length (≤15 Chinese characters) + R_value (judge model rating S=1/A=0.5/B=0).
   - Interest-level: R_sem (weighted cosine similarity with the reference query, weights = normalized confidence) + R_style (Type-Token Ratio) + R_format (exactly 3 queries).
   - Global-level: R_content (1 − mean pairwise cosine similarity between mean-pooled cluster representations).
   - Reward weights: ω_think_format 0.5, ω_match 2.0, ω_length 0.2, ω_value 0.8, ω_sem 0.5, ω_style 0.3, ω_format 0.2, ω_content 0.5.
4. **DPO (distill think → non-think):** Positives = final answers from the RL checkpoint's think-mode (discard reasoning traces); negatives = non-thinking-mode responses (70% RL checkpoints + 30% base model). Filter preference pairs: remove the top 30% most semantically similar pairs. DPO fine-tune (LoRA, 500 steps, gradient accumulation 4).
5. **Nearline deployment:** Invoke the model after every N accumulated user interactions (clicks/favorites); non-thinking mode outputs interest labels + guidance queries → write into the mapping table (user_id → queries).
6. **Online serving:** When a user enters the shopping-guide interface, vector retrieval locates the index in the mapping table → retrieves personalized candidates in real time.

## Expected output
- Per user: ≤3 interest labels, each with 3 guidance queries (≤15 Chinese characters) + confidence scores, JSON format {"interest_tag": [query1, query2, query3], ...}.
- Quality: S ratio ~0.86 (top-rated queries), B ratio ~0.03; win rate vs teacher ~55–58%; Recall@10 ~0.24 (ONESFT+RL+DPO).
- Online: +2.5–4.5% uCTR (user click-through rate) in A/B tests.

## Example application
- A solopreneur selling on Shopee/TikTok Shop: generate search-query suggestions for customer segmentation — a customer with mixed history (cameras + coffee) → segment into 2 clusters: "light travel camera under $500" (interest 1) + "specialty single-origin coffee beans" (interest 2) → show per-cluster guidance queries on the homepage instead of one generic query.

## Gotchas
- Do NOT fine-tune on mixed-interest sequences — the model will focus on a single main interest and extrapolate autonomously (low-frequency trigger words are lost).
- DPO slightly reduces win rate (57.53%→54.95%) — a trade-off between reasoning quality and latency; use DPO only when online latency matters.
- Preference-pair filtering matters: without filtering → "ineffective learning", templated/homogeneous outputs (−8.9% Recall@10).
- A larger teacher model is NOT better for relevance — DeepSeek-V4-Pro works well because of high-frequency contextual terms; larger models generate novel queries → hallucination in e-commerce.
- The judge model's S/A/B rating needs manually annotated data — annotation quality determines R_value; the B criteria include unsafe content (politics, pornography) — moderation required.
- Query ≤15 Chinese characters — a language-specific constraint; adjust the threshold for Vietnamese/English.
- RL only 100 steps — early stage; monitor for underfitting on new domains.
