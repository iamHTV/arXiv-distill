# Skill: Safety Self-Play Alignment
Source: 2601.10589
Type: workflow

## Khi nào dùng skill này

- Khi cần proactive safety alignment (căn chỉnh an toàn chủ động) cho LLM — model tự discover và patch vulnerabilities, không cần manual red teaming
- Khi static adversarial datasets overfit known patterns — cần evolving defense
- Khi muốn balance safety và usability — minimize over-blocking legitimate queries

- KHÔNG dùng khi: RL training infrastructure unavailable; model too weak to play both attacker/defender; external red team mandated by regulation

## Input cần có

- LLM to align (base or already instruction-tuned)
- Harmful request dataset for initial calibration
- RL training infrastructure
- Safety evaluation benchmarks (HarmBench, OR-Bench)

## Các bước thực hiện

1. **Initialize Roles** — Configure single LLM to alternate between Attacker role (generate jailbreaks for harmful requests) and Defender role (refuse/respond to requests). Set up RL reward: Attacker rewarded for successful bypasses, Defender rewarded for correct refusals.

2. **Self-Play Loop** — Run alternating episodes: (a) Attacker generates jailbreak attempts for harmful queries; (b) Defender evaluates and responds/refuses; (c) Compute rewards based on outcome; (d) Update both roles via RL.

3. **Reflective Experience Replay** — Maintain experience pool of all attack-defense interactions. Use UCB sampling to prioritize: (a) Low Defender reward = successful attacks (learn from failures); (b) Balance exploration (new attack patterns) and exploitation (known vulnerabilities).

4. **Evaluate Safety-Usability Balance** — Test on: (a) HarmBench — Attack Success Rate should decrease; (b) OR-Bench — Refusal rate on safe queries should remain low. Target: low ASR + low refusal rate.

5. **Iterate Until Convergence** — Continue self-play until: (a) ASR stabilizes at low level; (b) No new attack patterns emerge; (c) Refusal rate doesn't increase further.

## Output mong đợi

- Lower ASR than static adversarial training
- Lower refusal rate than over-defensive methods (Self-Reminder, SmoothLLM)
- Diverse attack generation without explicit diversity reward

## Ví dụ áp dụng

Scenario: Healthcare chatbot safety alignment. (1) Initialize: LLM alternates Attacker (tries to extract medical advice for harmful purposes) and Defender (refuses harmful medical queries, responds to legitimate ones); (2) Self-play 1000 episodes: Attacker discovers "ask for friend" bypass, Defender learns to detect it; (3) Experience replay: focus on 5% failure cases where Attacker succeeded; (4) Result: ASR drops from 35% to 8%, refusal rate on legitimate queries stays at 3%.

## Gotchas

- Model capability bound: LLM can't discover attacks beyond its own knowledge. Supplement with external red teaming for novel vectors.
- Convergence time: may need 1000+ episodes for complex domains. Monitor ASR plateau.
- UCB exploration constant: tune to balance exploring new attacks vs. exploiting known weaknesses.
- Attacker-Defender imbalance: if one role is much stronger, training destabilizes. Use capability matching.
