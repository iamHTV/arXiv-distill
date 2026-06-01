# 2602.01011 Multi-Agent Teams Hold Experts Back

## Problem

Multi-agent LLM systems are increasingly deployed as autonomous collaborators where agents interact freely rather than executing fixed workflows. Prior work enforces coordination through fixed roles, workflows, or aggregation rules. But the open question: how well do self-organizing teams perform when coordination is unconstrained? Specifically, do LLM teams achieve strong synergy — where team performance matches or exceeds the best individual member?

## Contribution

1. Discovery: LLM multi-agent teams CONSISTENTLY FAIL to match expert agent performance — even when explicitly told who the expert is. Performance losses up to 41.1% on ML benchmarks. Counter-intuitive: human teams match expert performance when expertise is revealed.
2. Identify primary bottleneck: expert LEVERAGING, not identification. Teams identify correctly but fail to defer appropriately.
3. Discover "integrative compromise" behavior — LLM teams average expert and non-expert views rather than appropriately weighting expertise. Worsens with team size, correlates negatively with performance.
4. Trade-off revelation: consensus-seeking behavior improves robustness to adversarial agents, suggesting a trade-off between alignment and expertise utilization.

## Method (core summary)

2-tier study: (1) Human psychology tasks (Lost at Sea, NASA Moon Survival, Student Body President) with controlled expertise distribution — concentrated (1 expert) and distributed (multiple experts); (2) Frontier ML benchmarks with real model differences (Claude Opus 4/4.5, GPT-5, o3-mini, etc.) on task-specific teams. 4 information conditions: No Information (control), Expert Not Mentioned, Reveal Expert, Best Individual (single expert baseline). Decompose gap into Identification Gap and Expertise Leveraging Gap. Conversational analysis for behavioral patterns. 10-30 seeds per cell.

## Key Findings

- LLM teams underperform best individual by 6.3%-41.1% across all tasks, even when expert is revealed
- Expert Leveraging Gap >> Identification Gap — bottleneck is LEVERAGING, not IDENTIFICATION
- Integrative compromise: teams average expert + non-expert views, DON'T defer to expert
- Worsens with team size (more agents → more compromise → worse performance)
- Contrast with human teams: humans match expert performance once expertise is revealed
- Trade-off: consensus-seeking IMPROVES robustness to adversarial agents
- Teams consistently achieve "weak synergy" (match average member) but NOT "strong synergy" (match best member)
- Robust across: concentrated expertise, distributed expertise, multiple model combinations

## Actionable Insights

1. DON'T assume multi-agent systems are better than single expert models — in most cases, deploying 1 strong model is better than deploying a team. Example: medical diagnosis system — 1 Claude Opus 4.5 performs better than a team of 4 models because the team averages expert opinion with weaker opinions.
2. If you MUST use multi-agent, implement expertise-aware coordination mechanisms — don't let agents self-negotiate. Example: hardcode the expert model with final decision authority, other agents only contribute information, DON'T vote on final answer.
3. Consensus-seeking behavior can be a feature for adversarial robustness — if deployment environment has adversarial inputs (spam, jailbreak), multi-agent consensus naturally resists manipulation. Example: content moderation system — team of 3 models harder to jailbreak than single model.

## Assumptions & Limitations

- Assumption: evaluation metrics (L1 distance, accuracy) capture real performance differences
- Limitation: Study mainly on reasoning/knowledge tasks, not tested on creative/generation tasks
- Limitation: Fixed team size experiments (2-4 agents), not tested at larger scales
- Limitation: No training interventions — only observes behavior, doesn't propose fix
- Limitation (observed): "Integrative compromise" may be an artifact of RLHF training — models trained to be balanced/fair naturally average views. Different training (e.g., expert delegation training) could change behavior.

## Metadata

- Year: 2026
- Authors: Aneesh Pappu, Batu El, Hancheng Cao, Carmelo di Nolfo, Yanchao Sun, Meng Cao, James Zou
- Institution: Stanford (Knight-Hennessy Scholars)
- Category: cs.AI, cs.CL, cs.MA
- PDF: https://arxiv.org/pdf/2602.01011
- Citation count: N/A
- Classification: [applied]
- Skill: N/A — observational study, cautionary finding
