# 2601.10589 Safety Self-Play (SSP): Be Your Own Red Teamer

## Problem

Current safety alignment methods cho LLMs depend heavily vào static external red teaming — sử dụng fixed defense prompts hoặc pre-collected adversarial datasets. Dẫn đến rigid defense (phòng thủ cứng nhắc) overfits known patterns và fails to generalize (không tổng quát hóa được) cho novel, sophisticated threats (mối đe dọa mới, tinh vi). Mỗi lần attacker tạo jailbreak mới, defense phải manually update → reactive, not proactive.

## Contribution

1. Safety Self-Play (SSP) — single LLM acts concurrently as BOTH Attacker (tạo jailbreaks) và Defender (refuse harmful requests) trong unified RL loop. Self-play dynamics tạo evolving attack strategies → uncover vulnerabilities → strengthen defenses simultaneously.
2. Reflective Experience Replay Mechanism — experience pool accumulated throughout self-play process. UCB (Upper Confidence Bound) sampling strategy focus on failure cases with low rewards → learn from past hard mistakes while balancing exploration and exploitation.
3. Demonstrate: SSP autonomously evolves robust defense, outperforms baselines trained on static adversarial datasets, achieves lowest refusal rate (best safety-usability balance).

## Method (tóm tắt cốt lõi)

(1) Unified RL loop: single LLM alternates between Attacker role (generate jailbreak attempts) và Defender role (refuse/respond); (2) Attacker gets reward for successful jailbreaks, Defender gets reward for correct refusals; (3) Reflective Experience Replay: maintain experience pool of past attack-defense interactions, UCB sampling prioritizes failure cases (low Defender reward = successful attacks); (4) Defender learns from accumulated failures → progressive strengthening; (5) Attacker evolves strategies through self-play dynamics → generates diverse attacks without explicit diversity reward.

## Key Findings

- SSP achieves lowest Attack Success Rate (ASR) on HarmBench — better defense than static methods
- Lowest refusal rate on OR-Bench — best safety-usability balance (doesn't over-block safe queries)
- Self-Reminder và SmoothLLM: reduce attacks BUT higher refusal rates (over-defensive)
- SSP generates diverse attacks without explicit diversity reward — diversity emerges from adversarial self-play
- Ablation: removing UCB sampling OR replay degrades performance — integrated design essential
- SSP's standalone attack capability competitive with dedicated attack methods
- Autonomous evolution — no manual adversarial dataset curation needed

## Actionable Insights

1. Khi deploy LLM safety alignment, dùng self-play thay vì static red teaming — model tự discover vulnerabilities và patch. Ví dụ: fintech company deploy chatbot → SSP auto-discovers jailbreak patterns specific to financial advice domain, patches defenses without manual red team.
2. Reflective Experience Replay quan trọng — focus training vào failure cases (successful attacks). Ví dụ: khi Defender fail trên 5% queries, replay those failures 3-5× more frequently trong training → Defender learns to handle them.
3. Safety-usability balance achievable — SSP achieves lowest refusal rate while maintaining strong defense. Ví dụ: customer service bot không over-block legitimate queries about returns/refunds while still blocking harmful requests.

## Assumptions & Limitations

- Giả sử: single LLM can effectively play both roles — capability may be model-dependent
- Limitation: Self-play convergence may be slow for very capable attackers
- Limitation: Evaluated primarily on English jailbreak benchmarks
- Limitation: RL training cost — self-play loop adds training overhead
- Limitation (tự thấy): Attacker capability bounded by model's own knowledge — model can't discover attacks it doesn't know about. External red teaming still needed for novel attack vectors.

## Metadata

- Năm: 2026
- Tác giả: Hao Wang, Yanting Wang, Hao Li, Rui Li, Lei Sha
- Category: cs.AI, cs.CL
- Link PDF: https://arxiv.org/pdf/2601.10589
- Citation count: N/A
- Nhãn: [applied]
- Skill: safety-self-play-alignment
