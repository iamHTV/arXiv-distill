# [2610.09043] Careful Judge: Safe and Efficient Human-AI Collaborative Decision Making

## Problem
Prior work has two branches, neither solving safety and efficiency together: (1) selective escalation with conformal prediction guarantees safety but does NOT learn from feedback, so a biased model must escalate nearly every human query when risk tolerance is small; (2) feedback-learning methods (RLHF, prediction-powered inference/PPI) improve efficiency but have NO safety guarantee — adaptive learning invalidates calibrated guardrails. Naively combining the two is worse: sharing scarce feedback makes learning noisier and safety more conservative.

## Contribution
- Formalizes human-AI collaboration as a statistical decision problem with a flexible offline-online schedule.
- Derives an exact Brier risk decomposition into four sources — aleatoric ambiguity (irreducible randomness), excess risk, epistemic uncertainty (learnable), systematic bias — each motivating one module.
- Residual Gauss: a Bayesian GP (Gaussian process) rectifier that propagates feedback across similar cases.
- Confident Jack: weighted cross-conformal calibration that controls risk at EVERY time step, reuses adaptively-selected labels, and tolerates arbitrary black-box model updates.

## Method
Four-module pipeline: (1) Residual Gauss fits a GP on the human-AI residual — linear mean captures systematic bias, kernel captures local correlation; (2) Confident Jack calibrates the escalation threshold; (3) Exacting Gates accepts the rectified AI decision only when rectified confidence exceeds the threshold; (4) Active Max selects the most informative queries to ask humans. Between checkpoints, online assumed-density filtering; offline, refit rectifier + rebuild calibration.

## Key Findings
- Four real safety-critical datasets: nuPlan (driving, 10,000 stream), HateBench (hate speech, 7,054), iSafetyBench (workplace hazard video, 1,100), ASIMOV (robotic tool use, 1,437).
- iSafetyBench at 5% tolerance: CARE escalates 21.7% of queries vs SE 57.1% (−62%).
- HateBench: query savings 49–66% vs SE, 26–48% vs PPI+SE; relative error reduction 15.5–70.5% across 8 black-box models (raw error 14.5–44.7%).
- Overall: 25–81% fewer human queries vs baselines. SE/PPI query rate rises +28.0pp/+11.8pp when switching to direct (overconfident) confidence; CARE stays stable.

## Actionable Insights
- Route review by risk, not confidence: set a confidence gate at tolerance ε; content moderation could auto-approve ~78% instead of ~43%.
- Reuse every expert label for BOTH model improvement and gate calibration — do not split scarce labels into two separate piles.
- Model local correlation (GP kernel) so one correction fixes a whole neighborhood: one flagged intersection corrects similar intersections.

## Assumptions & Limitations
- Binary classification; i.i.d. stream; the oracle (label source) is always correct.
- Efficiency is highest when the AI is well-trained and misalignment has clear structure.
- Paper has NO Limitations section; not tested on multi-class, regression, or non-stationary streams.
- Max GP feature dimension in experiments is 256 — scaling to much higher features is unverified.

## Metadata
- Year 2026, arXiv 2610.09043, category stat.ML (cs.AI, cs.LG), PDF: https://arxiv.org/pdf/2610.09043, citations: not found (submitted 6 Oct 2026).
