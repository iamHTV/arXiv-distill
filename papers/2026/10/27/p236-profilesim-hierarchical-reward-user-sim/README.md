# [2610.32435] ProfileSim: User Simulation bằng RL với Hierarchical Rewards cho Task-Oriented Dialogue

## Problem
- TOD (task-oriented dialogue — hội thoại tác vụ) cho marketing outbound (cuộc gọi chào hàng) cần dữ liệu hội thoại domain-specific khối lượng lớn, nhưng privacy regulation (quy định bảo mật), annotation cost (chi phí gán nhãn), expert labor (labor chuyên gia) làm khó obtain. Prior work (UserLM, personaLLM, USP) target general-domain written text: (1) insufficient domain constraints — thiếu modeling business process + compliance constraint (ràng buộc tuân thủ); (2) inadequate spoken-language modeling — output văn phong viết diverge khỏi disfluency/colloquial ( khẩu ngữ) của voice interaction thật.

## Contribution
- Joint modeling user profile (demographics + Big Five personality traits — 5 đặc điểm tính cách: Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Openness) và business profile (intents reverse-engineered từ real call logs — khôi phục ngược từ log cuộc gọi), làm explicit conditioning variable (biến điều kiện tường minh).
- SFT trên real voice dialogue + GRPO (group relative policy optimization — tối ưu chính sách nhóm tương đối) với hierarchical reward (phần thưởng phân cấp): dialogue-level (profile consistency cosine) + utterance-level (coherence/nonrep/natural/biz), turn-level advantage (credit assignment từng lượt).
- Business profile transition mechanism: 73 fine-grained intents / 9 groups, transition matrix 9×9 ước lượng empiric từ real trajectories + stay probability pstay = 0,1.

## Method (tóm tắt cốt lõi)
- Data: 242,438 sessions call thật → desensitize + transcription correction + quality filter → 72,296 valid dialogues (432,457 utterances, avg 7 turns). 10,000 dialogue–profile pairs annotate GPT-5 → LoRA fine-tune Qwen3.5-9B thành profile extractor gϕ (validate 1,000 pairs: 95,4% valid).
- SFT: quintuple (product info; history; user profile; biz profile; target utterance), 97,126 utterances, LoRA 2×A100 3 epochs lr 2e-4 max 1,024 out tokens (~14 h).
- GRPO: G=8 dialogues rollout/context, user simulator = trainable policy, customer service agent (DeepSeek-R1 backbone + SOP graph + RAG) = fixed environment; 4,000 profiles; 8×H200 2 epochs (~20 h). Reward: r_t = 0,5·r_profile + 0,5·r_utterance với r_utterance = 0,30·coh + 0,15·nonrep (cos prev >0,8 → 0) + 0,25·natural + 0,30·biz; judge Gemini 3.1 Pro, 1–5 → (s−1)/4.
- Agent: SOP = directed graph (V,E) stages; RAG retrieve intent + candidate stages + templates, filter by SOP state; output JSON (next stage, response).

## Key Findings
- Table 1 PPL (perplexity — độ bất định; lower = align real distribution better): SFT-only 58,48 → +BizProfile 43,04 (−15,44) → +UserProfile 22,24 (−36,24) → Full SFT 17,52 → Full+GRPO 17,49. User profile conditioning dominant: riêng user profile beat business profile 22,24 vs 43,04.
- Table 2 (3,000 sessions/generator, same agent + protocol): Full Model colloquial 4,97 (SFT 4,46; GPT-5 4,21; DeepSeek-V3 3,22); utterance length 11,14 chars (GPT-5 44,54; DeepSeek-V3 153,96); user profile adherence 92,55% (SFT 84,29%; LLMs ≤84,05%); agent score long-tail intent 3,49 (thấp nhất — stress agent mạnh nhất; LLMs 4,18–4,45); business profile compliance 52,25% (GPT-5 62,01% cao hơn nhưng verbose).
- Dataset sinh: 3,000 sessions, ~20,000 utterance pairs, 58% utterances là scenario-specific intents; human spot-check 500 samples/metric Cohen's κ ≥ 0,72 với judge.
- Prior-work anchor: multi-turn RL giảm persona drift (lệch persona) >55% (Abdulhai 2025).

## Actionable Insights
- Persona modeling quan trọng hơn business context khi simulate user: +UserProfile giảm PPL 36,24 vs +BizProfile 15,44. Ví dụ: khi tạo caller giả cho call center, gán demographics + Big Five (vd "nam 40–55, thu nhập không ổn định, trực tiếp, Extraversion thấp") chứ không chỉ "sẽ hỏi về khoản vay".
- Closed-loop simulator–agent = factory stress-test: dùng simulator profile-conditioned để sinh long-tail intent (bottom 20% frequency) interactions, agent score thấp nhất = corpus giá trị nhất để train robustness. Ví dụ: trước khi deploy chatbot bán hàng, sinh 3,000 cuộc hội thoại persona-đa dạng → phát hiện intent hiếm agent trả lời tệ nhất.
- Voice ≠ text: benchmark colloquial naturalness + utterance length riêng; model viết-style (GPT-5 44,54 chars) không phù hợp telephony. Ví dụ: nếu chạy voice AI outbound, đánh giá độ ngắn gọn khẩu ngữ trước khi chọn model.
- Privacy-safe data pipeline: 242,438 raw → 72,296 usable sau desensitize + auto-profile 95,4% valid — recipe build từ call log riêng đã ẩn danh mà không cần expert annotate từng cuộc.

## Assumptions & Limitations
- Phải có real call log domain riêng (ít nhất ~10K samples để annotate profile) + GPU budget (SFT 2×A100 14h + GRPO 8×H200 20h).
- Paper thừa nhận: user profile static — không capture dynamic shift attitude/emotion trong cuộc hội thoại; validated 1 domain (financial marketing outbound calls) duy nhất, chưa cross-domain; chưa đo downstream intent-recognition accuracy tăng bao nhiêu (chỉ đo agent stress score).
- [MY OWN] Business compliance metric bị confound: score cao có thể chỉ do explicit verbalization (GPT-5 62%) chứ không realism; judge Gemini 3.1 Pro và GPT-5 annotation có thể bias vendor; pstay=0,1 hard-coded chưa tune.

## Metadata
- 2026, Bairong Inc. (Juan Li, Fangshu Chang, Xinyi Jiang, Ling Huang, Yunzhang Chen), cs.CL, https://arxiv.org/abs/2610.32435, citation count: [NOT FOUND] (paper quá mới)
