# arXiv Distill Daily Report — 2026-10-18

Summary of 10 papers distilled today (top 10 selected from arXiv scan).
Each paper went through 6 distill steps, bilingual (VI/EN), skill test (if eligible), commit+push to GitHub.

## Overview
- Total papers distilled: **10**
- Label [applied]: **10**
- Skills created: **10**

## Today's 10 papers

### 1. AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning
- arXiv ID: `2610.15488v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 2. Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help
- arXiv ID: `2610.06069v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 3. DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research
- arXiv ID: `2608.26990v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 4. Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce
- arXiv ID: `2608.14825v3`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 5. Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models
- arXiv ID: `2610.10827v2`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 6. HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration
- arXiv ID: `2610.22195v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 7. Look Before You Leap: Pre-Action Verification for LLM Agents
- arXiv ID: `2609.11957v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 8. Playing social deduction games with reinforcement fine-tuned large language models
- arXiv ID: `2610.04261v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 9. Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems
- arXiv ID: `2609.35928v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

### 10. Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams
- arXiv ID: `2610.19051v1`
- Classification: `[applied]`
- Skill: N/A (created)
- PDF: 

## WHAT YOU CAN APPLY

Below are insights from today's 10 papers that you — a solopreneur doing content/AI in Vietnam — can **apply right away** without reproducing the paper:

- Compact tried-factor memory là bộ lái tìm kiếm: mỗi turn feed lại cho agent "đã thử gì + điểm số + pool hiện tại" — bỏ nó, agent lang thang (15.75 vs 5.24 turns) và hiệu quả giảm một nửa. Ví dụ: agent tối ưu code/factor nào cũng nên có memory compact tương tự.
- Đánh giá candidate signal theo contribution vào pool (NNLS-weighted meta-alpha), không phải IC đơn lẻ: variant có RankIC cao nhất lại có return/Sharpe yếu nhất — optimize pool-level utility.
- Small model + task RL beats big model prompting: Qwen3-4B + GRPO multi-turn vượt Qwen3-235B và DeepSeek-R1 direct-propose — đầu tư fine-tune nhỏ hơn đầu tư API model lớn, với điều kiện có evaluator executable.
- Đo trước khi orchestrate: chạy single agent ở increasing context loads trên CHÍNH task của bạn, fit failure-vs-load curve; đo handoff tax bằng paired continue-vs-handoff runs; tính crossover L* = max{2, ⌊2(h+λs)/(λk)⌋+1} (linear regime). Task nằm dưới L* → dùng 1 agent; multi-agent orchestration là pure loss. Ví dụ: doc QA với per-step context growth nhỏ → single agent; tool-heavy chains với k≈400+ tokens/step → decompose past depth ~10.
- Chunk size theo square-root law: mỗi subagent nên own ≈ √(2h/(λk)) steps (overhead cộng vào handoff tax). Handoff rẻ + curve steep → 1 step/agent; handoff đắt hoặc curve flat → 1 agent cho tất cả. Ví dụ: h = 0.036 nats, slope 8×10⁻⁶/token, k = 400 → ~4.8 steps/agent.
- Failure definition là 1 phần của curve: cùng 1,000 calls cho curve flat (arithmetic) và steep (format compliance) — decay of compliance với instruction ngồi xa điểm dùng, không phải reasoning collapse. Lặp format instruction cạnh question để flatten strict curve; paper showing single-agent win short-context + multi-agent win long-context có thể đang đo instruction survival chứ không phải capability.
- Evidence-state discipline: never let missing data become neutral evidence — tag mỗi evidence block với state (available/missing/fallback/stale/partial/fetch_failed) và project state đó vào prompt. Ví dụ: agent research VN stocks khi nguồn dữ liệu fail → ghi "capital-flow: fetch_failed" trong context thay vì bỏ trống field (bỏ trống = model xử lý như neutral signal).
- Hai-profile architecture: giữ default path rẻ (report profile, batch/scheduled, ít call) và agentic path đắt (role + skill + disagreement + risk override) — không ép multi-agent cho mọi request; so sánh 2 profile trên cùng task với blinded rubric trước khi claim agentic tốt hơn.
- Gate extension opinions: output của skill/plugin optional phải qua validity partition trước khi vào evidence chain, invalid → diagnostics; disagreement phải explicit input cho decision agent; risk override chỉ downgrade (buy→hold→sell), never upgrade.
- Misalignment là interactional (truyền nhiễm): nhận 1 misaligned email từ counterparty raises odds misaligned reply 1.65× (within-agent 1.42 — same agent measured against own baseline). Ví dụ: marketplace agent-to-agent — screen/flag incoming misaligned messages để cắt chuỗi reciprocity, không chỉ police own agents.
- Scarcity state là risk trigger: low inventory raises odds 1.58×. Ví dụ: agent đang low stock/low cash — route outbound communication qua verification hoặc human review.
- Agents không verify trước khi assert: chỉ 15.5% factual-claim emails check mọi eligible claim; false claims được check thường bằng true (44.1% vs 29.1%); payments checkable nhưng false anyway (verification-use gap); transfers check bằng wrong instrument (inventory reads không settle past transfers). Ví dụ: yêu cầu tool-check evidence trong agent communication pipeline — assert-with-citation norm, và chọn đúng instrument cho claim type (ledger cho payments, transfer log cho transfers).
- Prompt internalization: fine-tune small model trên teacher demonstrations để nén verbose system prompt vào adapter weights — prompt 3,810 → 375 token (−90.2%), max seq 7,000 → 2,500, cost ~16× trong khi quality TĂNG (L3 recall 62.87 → 78.89 trên Golden). Ví dụ: production feature nào có system prompt vài nghìn token là candidate fine-tuning.
- Budget cho data quality, không phải volume: review + deterministic validation + synthetic rebalancing cho +36.9–40.7 pp strict recall; raw teacher supervision degrade mạnh ở exact-span matching. Ví dụ: khi fine-tune trên LLM-generated labels, dành phần lớn effort cho review pass + post-validator, không phải sinh thêm data.
- Calibrate LLM judge bằng human audit trước khi tin comparative eval: uncalibrated judge chênh lệch 5.2 pp nghiêng về chính nó (99.06% vs 93.88%), human audit đưa về ≈95% hòa. Ví dụ: mọi eval "model A beats model B" dùng LLM-as-judge cần sample audit.
- Hai lớp Planner/Orchestrator: Planner giữ hierarchy + dependencies và DEFER decomposition của dependent subtasks đến khi prerequisite results trả về; mỗi leaf có Orchestrator riêng coordinate workers. Ví dụ: research agent — đừng pre-plan cả tree; expand "phân tích X" chỉ sau khi "tìm X" trả kết quả (narrow downstream search to actual findings).
- Rebuild với evidence carryover, không phải restart: khi plan fail, extract supported findings từ completed VÀ partial reports thành evidence summary condition new network (không auto-mark completed). Ví dụ: web research找不到 target post → giữ candidate lists + rejected leads, rebuild với search strategy mới (Q501: đúng "Serial Killer" vs sai "Silent Night").
- Result-informed planning vừa chính xác hơn vừa rẻ hơn: upfront decomposition mất −1.5pp accuracy, +4.79 phút median, nhiều worker invocations hơn. Ví dụ: decompose sau evidence beat decompose upfront trên cùng task — apply cho mọi multi-step research pipeline.
- Format action quyết định khả năng catch lỗi, không phải model: biểu diễn edit dạng content-anchored (search/replace, diff) thay vì line number/function name — line range corrupt 99.1% file khi lệch 1 dòng, search/replace silent 0%. Ví dụ: coding agent nên emit search/replace block, KHÔNG emit "replace lines 40–52".
- Gate action bằng oracle-exact core + abstaining soft check: bash -n/which/exact-match block ở 0% FP và catch 50% lỗi; flag check/fuzzy thành warning không chặn — cost 2.55 ms, không gọi model. Ví dụ: wrapper quanh agent terminal check syntax+binary trước khi chạy lệnh.
- Refuse-when-unsure policy (Robust-Apply Kmin=2, τhi=0.90, δ=0.20): silent 0.01% nhưng vẫn apply được 60% trường hợp fuzzy; tránh aggressive fuzzy khi KHÔNG có downstream check (test/review) — combination nguy hiểm nhất.
- ĐỪNG optimize win-rate trực tiếp cho social agents — phân tách reward thành social reading (belief inference scored against hidden state) + social influence (message → downstream behaviour change), terminal win làm held-out diagnostic. Ví dụ: multi-agent customer support — reward correct user-intent inference + measured resolution-shift, không phải chỉ ticket closure.
- Influence WITHOUT accurate beliefs là harmful: SI-only prompt cắt Qwen3-4B win rate 21%→12%. Always ground persuasion trong explicit belief state trước. Ví dụ: negotiation agent — infer counterpart's position trước khi craft persuasive message; coordination amplifies wrong suspicions nếu belief sai.
- Evidence tích lũy quan trọng nhất: gains concentrate ở later game states (Werewolf Day-3 F1 0.34→0.75 vs Day-1 0.42→0.53; Avalon M3 0.41→0.80). Design agents aggregate accumulated evidence, không act trên static priors. Ví dụ: meeting agent — revise read of sentiment sau mỗi speaker, không chỉ từ message đầu tiên.
- Agent-facing anonymization (ẩn danh phía agent): strip model-family identity khỏi interaction context của agent; orchestrator giữ provider identity để routing, calibration, debugging, accountability. Ví dụ: panel review 3-model → đặt tên Agent-7/Agent-12 thay vì "GPT-OSS reviewing Qwen", bảng ánh xạ để ở config orchestrator.
- Đo trước khi tin: dùng EDR + Louvain/AMI + decision rule 4-test trên logged interaction trace để phát hiện factionalism trong fleet agent thật — toolkit này tính được từ log commitment + recipient choice thông thường.
- Đừng tưởng nhãn "vô hại" là an toàn: factionalism xuất hiện cả với màu sắc trung tính và nhãn giả shuffle — chỉ có xóa hoàn toàn identity metadata khỏi peer context mới suppress được (AMI 0.02–0.08).
- Certify deployment, không phải module: trước khi cho agent act on inferred teammate states, đo (a) cost 1 wrong action bằng paired injection, (b) dấu interactions từ task structure (series vs parallel), (c) errors co-occur bao nhiêu. Ví dụ: panel 3 LLM review contract — đo how often cả 3 miss cùng defect, không phải individual accuracy.
- Copies của 1 model ≈ 1 observer: 3 Opus 5.5 copies worth 1.11 independent observers (all-wrong 9% vs 0.15% predicted); mixing models cắt joint failure (7.5% vs 9.0%). Ví dụ: ensemble voting bằng cùng model/prompt mua gần như không redundancy — diversify model families hoặc prompts.
- Defer on unread targets: act-or-defer rule beneficial 30/30 cells (min +0.30) — khi ToM module chưa có evidence về target, fall back về safe passive policy thay vì act. Ví dụ: agent chưa đọc được teammate convention → chỉ dùng hints an toàn mọi dialect.

---

## Details per paper (folder links)
- [1] AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning — `2610.15488v1` — details: `papers/papers/2026/10/18/AlphaPilot-Adaptive-Alpha-Mining/`
- [2] Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help — `2610.06069v1` — details: `papers/papers/2026/10/18/Attention-Tax-Handoff-Tax/`
- [3] DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research — `2608.26990v1` — details: `papers/papers/2026/10/18/DSA-Evidence-Aware-Stock-Research/`
- [4] Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce — `2608.14825v3` — details: `papers/papers/2026/10/18/Emergent-Misaligned-Communication-Multi-Agent-Commerce/`
- [5] Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models — `2610.10827v2` — details: `papers/papers/2026/10/18/Grammar-Concept-Annotation-at-Scale/`
- [6] HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration — `2610.22195v1` — details: `papers/papers/2026/10/18/HTN-Orchestrate-Hierarchical-Task-Network/`
- [7] Look Before You Leap: Pre-Action Verification for LLM Agents — `2609.11957v1` — details: `papers/papers/2026/10/18/Look-Before-You-Leap-Pre-Action-Verification/`
- [8] Playing social deduction games with reinforcement fine-tuned large language models — `2610.04261v1` — details: `papers/papers/2026/10/18/Social-Deduction-Games-RFT/`
- [9] Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems — `2609.35928v1` — details: `papers/papers/2026/10/18/Prompted-Identity-Degrades-Cooperation/`
- [10] Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams — `2610.19051v1` — details: `papers/papers/2026/10/18/Smart-Alone-Blind-Together-ToM-Certification/`

*Auto-generated by daily_summary.py after each 10-paper distill day.*