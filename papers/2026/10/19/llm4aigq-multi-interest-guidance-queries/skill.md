# Skill: Multi-Interest Guidance Query Generation (SFT-RL-DPO)
Source: 2609.03674v1
Type: framework / workflow

## Khi nào dùng skill này
- Cần sinh personalized guidance queries (truy vấn gợi ý cá nhân hóa) hoặc content gợi ý cho user có nhiều sở thích (multi-interest users) trong e-commerce, content recommendation, marketing automation.
- Cần LLM nhỏ (30B MoE) đạt quality gần teacher model lớn mà latency thấp cho online serving.
- KHÔNG nên dùng: user chỉ có 1 interest rõ ràng (đơn giản hơn); không có behavior sequence history (thiếu input); không có teacher model cho supervision.

## Input cần có
- User profile P_u (consume patterns + basic personal info, summarized bởi Qwen model)
- User historical sequence S_u: recent ≤50 behaviors, format "<idx><time><type><content>", type ∈ {like, favorite, add-to-cart, purchase, search}, content = item title (đã compress thành short title) hoặc search query
- Item short titles (compress từ original titles qua Qwen3-30B-A3B fine-tuned bởi DeepSeek-V4 Pro outputs)
- Teacher model (DeepSeek-V4 Pro hoặc tương đương) cho interest segmentation + reference queries
- Manually annotated data cho judge model (rating S/A/B)
- Infra: mapping table (user_id → guidance queries), vector retrieval, nearline compute

## Các bước thực hiện
1. **Context compression:** Truncate history to 50 recent behaviors; format "<idx><time><type><content>" cách nhau bằng "|". Compress item titles thành short titles (bỏ marketing keywords, flagship store words) — giảm 26.8% input tokens, 10.7% RT.
2. **SFT (single-interest style learning):** Dùng teacher model segment user interests + sinh reference guidance query per sub-interest; fine-tune student trên single-interest subsequences only (KHÔNG dùng mixed-interest sequences — gây autonomous extrapolation, focus vào 1 main interest). Instructions chỉ ra application scenarios (single item consultation, comparative decision-making, category selection) + yêu cầu guidance value, content compliance, concise expression.
3. **RL (multi-interest segmentation + generation):** Prompt model reason 3 steps: Step 1 — segment thành ≤3 interest subsequences (temporal proximity + semantic relevance + profile preferences), label I_k; Step 2 — infer consumption intent M_k + predict next item i_k; Step 3 — sinh 3 guidance queries + confidence score c. Optimize bằng GRPO (group size 8) với 4-level rewards:
   - Think-level: R_match (Optimal Ordered Matching DP giữa reference và model subsequences, score = 2·|Ŝ∩S|/(|Ŝ|+|S|)·log(|Ŝ|+|S|), primary interests earlier) + R_think_format (detect Step1/2/3 + JSON completeness).
   - Query-level: R_length (≤15 Chinese chars) + R_value (judge model rating S=1/A=0.5/B=0).
   - Interest-level: R_sem (weighted cosine similarity với reference query, weights = normalized confidence) + R_style (Type-Token Ratio) + R_format (số queries = 3 đúng).
   - Global-level: R_content (1 − mean pairwise cosine similarity giữa mean-pooled cluster representations).
   - Reward weights: ω_think_format 0.5, ω_match 2.0, ω_length 0.2, ω_value 0.8, ω_sem 0.5, ω_style 0.3, ω_format 0.2, ω_content 0.5.
4. **DPO (distill think → non-think):** Positive = final answers của RL checkpoint think-mode (discard reasoning traces); negative = non-thinking-mode responses (70% RL checkpoints + 30% base model). Lọc preference pairs: remove top 30% most semantically similar pairs. DPO fine-tune (LoRA, 500 steps, gradient accumulation 4).
5. **Nearline deployment:** Invoke model sau mỗi N accumulated user interactions (clicks/favorites), non-thinking mode output interest labels + guidance queries → write vào mapping table (user_id → queries).
6. **Online serving:** User vào shopping-guide interface → vector retrieval locate index trong mapping table → retrieve personalized candidates real-time.

## Output mong đợi
- Per user: ≤3 interest labels, mỗi label kèm 3 guidance queries (≤15 Chinese characters) + confidence scores, JSON format {"interest_tag": [query1, query2, query3], ...}.
- Quality: S ratio ~0.86 (top-rated queries), B ratio ~0.03; win rate vs teacher ~55–58%; Recall@10 ~0.24 (ONESFT+RL+DPO).
- Online: +2.5–4.5% uCTR (user click-through rate) trong A/B test.

## Ví dụ áp dụng
- Solopreneur bán hàng trên Shopee/TikTok Shop: sinh gợi ý search query cho customer segmentation — customer có history trộn (máy ảnh + cà phê) → segment 2 clusters: "máy ảnh du lịch nhẹ dưới 500 USD" (interest 1) + "cà phê specialty hạt single-origin" (interest 2) → hiển thị guidance queries riêng per cluster trên homepage, thay vì 1 query chung chung.

## Gotchas
- KHÔNG fine-tune trên mixed-interest sequences — model sẽ focus vào 1 main interest và extrapolate autonomous (low-frequency trigger words bị mất).
- DPO làm win rate giảm nhẹ (57.53%→54.95%) — trade-off reasoning quality vs latency; chỉ dùng DPO khi online latency quan trọng.
- Preference-pair filtering quan trọng: KHÔNG lọc → "ineffective learning", outputs templated/homogeneous (−8.9% Recall@10).
- Larger teacher model KHÔNG tốt hơn cho relevance — DeepSeek-V4-Pro tốt vì high-frequency contextual terms; models lớn hơn generate novel queries → hallucination trong e-commerce.
- Judge model rating S/A/B cần manually annotated data — annotation quality quyết định R_value; tiêu chí B bao gồm unsafe content (politics, pornography) — cần moderation.
- Query ≤15 Chinese characters — constraint ngôn ngữ-specific; với tiếng Việt/Anh cần adjust threshold.
- RL chỉ 100 steps — early stage; cần monitor underfitting trên domain mới.
