# [2608.25937v2] Candidate supply and answer selection shape the value of LLM judging in multi-agent systems

## Core value (1 sentence)
The value of LLM judging in multi-agent systems depends on both candidate supply (whether correct answers are present, frequent or recognisable) and the terminal answer-selection rule — combining answer frequency with judge ranking rescues outnumbered correct answers, lifting accuracy from 63.82% to 70.82–70.95%.

## Problem
Prior work failed to disentangle why multi-agent systems can generate a correct answer yet still report a wrong one, because candidate generation, peer communication and answer-selection rules usually change simultaneously — making it impossible to attribute system-level gains to any single operation.

## Contribution
- Conceptualizes multi-agent reasoning as an evolutionary pipeline: candidate generation → peer communication → terminal selection, where consensus without quality control exhibits memetic drift.
- Studies two questions: (1) when an LLM judge provides effective selection pressure by supplying a correctness signal for candidates; (2) when using that signal improves the reported answer.
- Analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR (Humanity's Last Exam analysed separately); replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks.
- Three findings: (1) a correct answer is often already present among generated candidates, but the system can still converge on and report a wrong answer; (2) judge reliability is not a fixed model trait — it varies with task, generator and correct-answer rarity; (3) combining answer frequency with judge evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82–70.95%, primarily by rescuing correct answers outnumbered by popular errors.

## Method
Evolutionary pipeline with three functional phases: (1) candidate generation — agents independently produce diverse answer candidates and supporting rationales; (2) information evolution — peer interaction lets agents repeat, adopt, revise or combine statements; (3) terminal selection — the system aggregates or filters candidates to produce a final output. Medical experiments on 7,350 case runs per protocol across 2,450 MedXpertQA medical reasoning questions under four controlled protocols: single-answer generation (1.00× cost baseline), five-answer majority voting without communication, an open committee with source-labelled peer review, and an anonymous evidence board pooling unlinked arguments. Offline ranking benchmark: repeated generator calls produce a full candidate bank defining question-level availability pgen (empirical fraction of correct candidates); a separate LLM judge call returns an ordering of anonymous candidate rationales; ranking reliability measured with rank AUC (probability a randomly selected correct candidate is ordered above an incorrect one from the same pool; 0.5 = chance). Terminal selection evaluated on 81,390 frozen candidate pools (k=8) from 16,278 questions across five benchmarks. Combining answer frequency with judge ranking via rank-power weighting (wi = (k−i)^t): robust accuracy plateau at t=2–4 (70.82–70.95%); first-ranked selection (t=5) achieves 69.04%.

## KNOWLEDGE — Data & figures
- Single response: 39.88% accuracy at 1.00× token cost.
- Majority voting: 41.06% accuracy at 4.96× token cost.
- Open committee: 42.20% accuracy at 10.73× token cost (+1.14 pp over majority vote, 95% CI 0.42–1.90).
- Evidence board: 41.89% accuracy at 6.07× token cost (+0.83 pp, 95% CI −0.05–1.74, CI includes zero — compatible with no difference).
- Generation–retention gap: 13.13–14.38 pp (oracle ceiling exceeds actual system accuracy).
- When most common initial answer is incorrect and an outnumbered correct candidate is present: open committee selects the most frequent incorrect answer in 73.25% of cases; evidence board in 59.61%.
- Communication topologies (star, complete, ring, hierarchical): 90.48–95.37% of runs end after one round; forcing six full rounds increases token use to 33×–49× without consistent accuracy gains.
- Judge rank AUC half-rise midpoint: pgen = 14.7% (95% CI 14.3–15.1%, R²=0.900) across 15,336 questions / 4 benchmarks; fixed-composition 2C/6W control: 12.2% (95% CI 11.8–12.6%, R²=0.887); HLE multiple-choice: 28.6%; HLE open-answer: 36.9%.
- Majority voting (t=0): 63.82% accuracy on 81,390 stored pools of size k=8.
- Unguided single-candidate sampling: 42.53%; shuffled-rank control: 42.47%.
- Hybrid selection (t=2–4): 70.82–70.95% accuracy (+7.00–7.13 pp over majority vote).
- First-ranked selection (t=5): 69.04% (+5.22 pp, 95% CI 4.85–5.59).
- Benchmark gains of first-ranked over majority voting: MMLU-Pro +4.3, GPQA +5.9, MedXpertQA +7.9, HLE MC +4.7, MuSR +10.6.
- Gains by correct-answer availability pgen: rare (0–0.125): +6.02 pp (95% CI 5.31–6.79, n=2,407); intermediate (0.125–0.625): +7.87 pp (95% CI 7.30–8.42, n=10,269); common (>0.625): −3.22 pp (majority voting already reliable).
- Question-level: first-ranked higher in 54.5% and lower in 24.5% of questions where correct candidates are present but less common; in majority-correct questions, majority voting higher in 17.6% vs 8.7% for first-ranked.
- Pool size: k=2 — first-ranked beats majority by 13.52 pp (95% CI 12.75–14.27); k=14 — +0.75 pp (CI includes zero); k=16 — −0.34 pp (CI −1.15–0.44).
- Judge selection cost-effectiveness: US$0.10–0.39 per 1,000 additional correct answers at k=2–6; US$6.28 at k=14; economically undefined at k=16.
- Small correct-minority pools (ppool < 0.25): judge beats majority by +40.1 pp at k=6 and +20.8 pp at k=16; high correct-fraction pools (ppool ≥ 0.25): majority beats judge by −4.0 pp at k=6 and −8.2 pp at k=16.
- arXiv category: cs.AI

## INSIGHT — Mechanism & why
[System generates correct answer but reports wrong one] BECAUSE [memetic drift and majority-biased cascades let popular errors overwhelm less frequent correct answers — a generation–retention bottleneck after generation]. This means [selection pressure independent of popularity is needed to preserve minority correct answers].
[Judge reliability is not a fixed model trait] BECAUSE [it varies with task, generator and correct-answer rarity; rank AUC falls below 0.5 when correct candidates are sparse]. This means [judge reliability must be evaluated in the specific regime where it will operate — not treated as a static benchmark score].
[Combining answer frequency with judge ranking lifts accuracy 63.82% → 70.82–70.95%] BECAUSE [answer frequency captures repeated support across independent trajectories; judge ranking can elevate a correct candidate outnumbered by popular errors]. This means [moderate rank weighting combines statistical stability of aggregation with content-sensitive correction for popular errors].

## IDEA — What to apply
Apply the combination of answer frequency + LLM judge ranking to enterprise multi-agent systems: step 1 is to use majority vote as the first step, then use an LLM judge to rank candidate proposals, combining both to select the final answer (rank weight t=2–4).
Evaluate judge reliability in the specific regime before deployment: step 1 is to measure rank AUC against correct-answer availability (pgen) in the actual candidate bank, not using a static benchmark score.

## WISDOM — General principle
Principle: The value of generating more candidates depends on whether those extra samples make correct answers present, frequent enough for voting, or leave a minority that an informative judge can recognise. Judges are not always helpful — when correct answers dominate the bank, majority voting is already reliable and judging can reduce accuracy.

## Assumptions & Limitations
- Conditions for validity: reasoning tasks with predefined correct answers, fixed candidate banks, LLM judge able to rank anonymous rationales.
- Limitations acknowledged by the paper: results on the studied systems; judge reliability varies across generator, task and availability regime; first-ranked selection reduces accuracy when correct answers dominate (>0.625 pgen).
- Limitations the paper does NOT mention: operational cost of running an LLM judge at scale; stability of rank AUC across model versions; latency impact of calling a judge per candidate bank.

## Metadata
- Year: 2026
- Authors: Jia-Hao Ji, Sijie Li, Jiabei Cheng, Zixi She, Jin-Tai Yu, Zhiyuan Yuan (Fudan University)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2608.25937v2
- arXiv ID: 2608.25937v2
- Label: [applied]
- Skill: candidate-supply-answer-selection | Test: [SKILL VALID]
