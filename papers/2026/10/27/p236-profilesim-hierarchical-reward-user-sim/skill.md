# Skill: Build profile-conditioned user simulator cho sales agent (ProfileSim recipe)
Source: 2610.32435
Type: framework (data-synthesis + training recipe)

## Khi nào dùng skill này
- Bạn cần data hội thoại domain-specific để train intent recognition (nhận diện intent — mục đích khách hàng) hoặc eval sales agent, nhưng không có dữ liệu thật đủ lớn (privacy, cost, expert).
- Bạn muốn stress-test chatbot/call bot trước khi deploy bằng simulated user (user giả) đa dạng persona.
- Bạn cần cold-start (khởi đầu nhanh) cho agent mới mà không có history interaction.

## Khi NÊN DÙNG
- Bạn có real call log/chat log domain riêng (≥10K sessions) để extract profile + reverse-engineer intent.
- Bạn cần user voice style (khẩu ngữ điện thoại), không phải written text.

## Khi KHÔNG nên dùng
- Không có log thật nào → profile/intent đều phải bịa → simulator học theo bịa.
- Domain thay đổi liên tục mà không rebuild được intent taxonomy (bảng phân loại intent).
- Cần emotion dynamics (cảm xúc biến đổi theo lượt) — skill này profile static, chưa support.

## Input cần có
- Real dialogue corpus (voice/telephony hoặc chat) domain riêng, đã desensitize (ẩn danh).
- Product information structured (thuộc tính sản phẩm/dịch vụ bán).
- SOP (standard operating procedure — quy trình chuẩn) gồm stages + allowed transitions.
- Knowledge base cho RAG: product docs, FAQ, policy.
- GPU: 2×A100-class cho SFT (~14 h), 8×H200-class cho GRPO (~20 h).

## Các bước thực hiện
1. **Clean + extract user profile**: desensitize, sửa transcription error, filter quality; annotate 10,000 dialogue–profile pairs bằng LLM mạnh (paper dùng GPT-5); profile gồm objective features (gender, age range, occupation, income status, language style) + subjective features (Big Five 5 chiều). LoRA fine-tune Qwen3.5-9B 3 epochs thành profile extractor; manual validate 1,000 pairs (target ≥95% valid).
2. **Reverse-engineer business profile**: map mỗi utterance → intent label (73 fine-grained intents paper), nhóm thành 9 intent groups; viết lại intent thành natural-language business profile prompt (vd "Next, you may ask about loan application process..."). Ước lượng transition matrix 9×9 từ cặp (intent group t, t+1) trong log; thêm stay probability pstay = 0,1; sample group theo matrix rồi sample uniform profile trong group.
3. **SFT user simulator**: quintuple (product; history; user profile; business profile; target utterance); LoRA trên backbone ~9B-class, 3 epochs, lr 2e-4, max output 1,024 tokens; mục tiêu: colloquial (khẩu ngữ) generation + conditional profile generation.
4. **SOP + RAG agent (environment)**: SOP = directed graph stages; mỗi turn retrieve 3 loại (intent nhận diện, candidate stages, stage templates) → filter theo SOP state hiện tại; prompt CoT optional; output JSON {next_stage, response}; agent Freeze cố định khi train simulator.
5. **GRPO hierarchical rewards**: G=8 dialogues rollout/context; user simulator = policy trainable, agent = environment fixed; full-dialogue rollout (vì reward profile cần cumulative responses); dialogue-level reward = cosine similarity(p_user_target, p_user_implied_from_cumulative) ∈ [0,1]; utterance-level = 0,30·coherence + 0,15·nonrepetition (cos vs utterance trước >0,8 → reward 0) + 0,25·naturalness + 0,30·business-consistency (judge 1–5 → (s−1)/4 cho coherence/naturalness; nonrep/biz binary); turn reward = 0,5·dialogue + 0,5·utterance; advantage A_i,t = (r_i,t − μG)/(σG+ε) với μ,σ computes từ dialogue mean rewards → turn-level credit assignment.
6. **Sinh dataset closed-loop**: agent mở cuộc bằng opening template; simulator respond condition profile; business profile evolve theo transition mechanism; terminate khi max turns hoặc user intent kết thúc. Paper: 3,000 sessions, ~20,000 pairs, avg 7 turns, 58% scenario-specific intents.
7. **Evaluate**: (a) PPL trên real test set (alignment distribution); (b) colloquial naturalness judge score (target ~4.9/5); (c) utterance length (target ≈11 chars telephony); (d) profile adherence cosine (target ≥92%); (e) agent score trên long-tail intent bottom 20% — thấp hơn = simulator stress agent tốt hơn (target < baseline LLMs 4.18–4.45); (f) human spot-check 500 samples/metric, Cohen's κ ≥ 0,72.
8. **Dùng downstream**: train intent recognition model trên synthetic corpus; eval agent robustness; cold-start deploy agent mới.

## Output mong đợi
- User simulator 9B-class đạt colloquial 4.97/5, length 11.14 chars, profile adherence 92.55%, agent stress score 3.49 (thấp nhất các generator); PPL 17.49 gần Full SFT 17.52 (GRPO không degrade distribution alignment); dataset 3,000 sessions tư vấn intent recognition training + agent eval.

## Ví dụ áp dụng
- Solopreneur bán khóa học online: lấy 5,000 call log tư vấn đã ẩn danh → personas (Big Five + thu nhập) + intent taxonomy (giá, lịch học, hoàn tiền, chương trình học) + transition matrix; SFT+GRPO Qwen3.5-9B; agent SOP graph (chào→khám nhu cầu→giới thiệu khóa học→xử lý phản đối→đóng). Sinh 3,000 cuộc gọi giả → phát hiện agent trả lời tệ intent "chính sách hoàn tiền" (long-tail) → train intent classifier + patch script trước khi launch.

## Gotchas
- **User profile dominant**: conditioning user profile giảm PPL 36.24 vs business profile 15.44 — đừng bỏ qua persona chỉ vì "context business là đủ".
- **Full-dialogue rollout bắt buộc**: reward profile consistency tính từ cumulative responses → không thể evaluate từng utterance độc lập; đừng rút ngắn rollout.
- **Freeze agent khi GRPO**: agent là environment fixed; nếu đồng thời train cả 2 → reward không stable.
- **Compliance ≠ realism**: GPT-5 compliance 62% nhưng utterance 44.54 chars verbose — score compliance cao có thể chỉ do explicit verbalization intent; đánh giá realism bằng colloquial + length + agent stress, không riêng compliance.
- **PPL insensitive**: PPL đo token likelihood, không đo long-range coherence/persona consistency → GRPO gain behavioral không hiện trong PPL (17.52→17.49 nhỏ); đừng kết luận GRPO vô dụng vì PPL gần như không đổi.
- **Static profile**: simulator không mô tả shift attitude/emotion giữa cuộc gọi → scenario cần empathy dynamics (đồng cảm biến đổi) phải extend riêng.
- **pstay=0,1 hard-coded**: tuning theo domain (topic-switch-heavy domain có thể cần thấp hơn).
- Transcript noise: real voice logs cần transcription-error correction step nghiêm túc — profile quality phụ thuộc transcript quality (95.4% valid chỉ sau khi.clean).
