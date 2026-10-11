# [2605.31455v1] DRIFT: Tách Rollout và Fine-Tuning Trọng số Quan trọng cho Tối ưu Hóa Đa Lượt Hiệu quả

## Vấn đề
LLMs ngày càng deployed trong multi-turn interactive settings (cài đặt tương tác đa lượt) nơi users hoặc environments cung cấp lightweight feedback (phản hồi nhẹ). Nhưng optimizing behavior presents sharp dilemma: online RL effectively address multi-turn dynamics nhưng prohibitively expensive (quá tốn kém) do cost generate full correction trajectories (lượt hành trình sửa chữa) tại mỗi update. Offline SFT efficient nhưng suffer from distribution shift (dịch chuyển phân phối) và behavioral collapse (sụp đổ hành vi).

## Đóng góp
1. **DRIFT framework**: Decouples (tách) rollout từ optimization. Sample offline interaction trajectories từ fixed reference policy, derive return-based importance weights, optimize via weighted SFT
2. **Theoretical insight**: KL-regularized RL objective tương đương importance-weighted supervised learning — DRIFT operationalize (vận hành hóa) insight này
3. **Empirical results**: Match hoặc exceed multi-turn RL baselines while maintaining SFT efficiency

## Phương pháp (tóm tắt cốt lõi)
DRIFT: (1) Sample multi-turn correction trajectories once từ frozen reference policy — không cần repeated rollouts; (2) Assign mỗi trajectory exponential weight derived từ KL-regularized multi-turn objective; (3) Train target model bằng importance-weighted SFT. Key: decouple trajectory generation (offline, once) từ optimization (online, efficient). Avoids repeated rollouts during training while optimizing accuracy và efficiency across turns.

## Kết quả chính
- Qwen2.5-3B-Instruct: DRIFT matches hoặc surpasses RL baselines trên most benchmarks
- Qwen2.5-7B-Instruct: DRIFT improves all-benchmark average từ 64.8% → 68.3%
- Training efficiency: DRIFT comparable to SFT-based methods, much faster than RL
- Multi-turn correction rate: DRIFT achieves higher correction rate in early turns
- Single-turn training: improves turn 1 accuracy nhưng little gain on later turns
- Multi-turn training: learns correction under negative feedback, substantial improvements beyond math

## Insight có thể áp dụng ngay
1. **Tách rollout khỏi optimization**: Khi train multi-turn AI agent, không cần repeated online rollouts. Sample trajectories once từ reference policy, optimize offline. Ví dụ: khi train customer service AI, generate correction trajectories once, then fine-tune offline — tiết kiệm compute.

2. **Importance weighting cho offline training**: Dùng return-based weights để upweight (tăng trọng) useful behaviors trong collected trajectories. Ví dụ: khi train AI advisor, weight successful correction trajectories cao hơn failed ones — model học từ successes.

3. **Multi-turn training > single-turn**: Single-turn chỉ improve turn 1. Multi-turn training learns to correct under negative feedback. Ví dụ: khi train AI coding assistant, train với multi-turn corrections (try → fail → fix → succeed), không chỉ single-shot solutions.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Short-horizon, verifier-guided correction với lightweight deterministic feedback
- Verifier provides unambiguous correctness signal
- Small number of correction attempts per episode

**Hạn chế paper thừa nhận:**
- Intended for short-horizon correction — không适用于 stochastic/preference-based feedback
- Offline rollout coverage limitation — only upweight behaviors in collected trajectories
- May miss strategies online RL could discover through exploration

**Hạn chế paper KHÔNG nói:**
- Tested primarily on math reasoning — generalizability unclear
- 3B-8B models only — larger models untested
- Assumes verifier availability — real-world verification harder
- Fixed reference policy quality limits upper bound
- Không compare cost savings quantitatively

## Metadata
- Năm: 2026
- Tác giả: Jian Mu, Tianyi Lin, Chengwei Qin, Zhongxiang Dai, Yao Shu
- Category: cs.LG, cs.CL
- Link PDF: https://arxiv.org/pdf/2605.31455v1
- Citation count: [EXTRACTION FAILED]
