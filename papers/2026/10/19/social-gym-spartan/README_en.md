# 2608.09128v1 Social Gym and SPARTAN: Benchmarking and Improving LLM Social Reasoning via Multi-Agent Game Tournaments

## Problem
- Measuring the social reasoning of LLM agents has no objective ground truth like math/logic: evaluation falls back on LLM judges — costly, subjective, noisy — and models get no reliable signal to learn from.
- Prior work evaluates single games or relies on LLM judges → cannot compare across games, cannot separate failures caused by game structure from model capability.

## Contribution
- Social Gym: 21 multi-agent social games in 5 categories with rule-decided outcomes → verifiable, objective, no LLM judge needed; an Elo tournament produces a unified leaderboard.
- Role-conditioned Elo: separate Elo-Main (majority/cooperative role) and Elo-Alt (minority/deceptive role) for 6 hidden-role games.
- SPARTAN (Self-Play and Reflect-Transfer): training-free, 3-stage play–reflect–transfer loop producing a transferable playbook.

## Method
- Social Gym extends SOTOPIA; FSM engine handles phase transitions; partial observability at 3 scopes: Public / Team-Private / Private.
- 5 categories: Normal-Form (6: Prisoner's Dilemma, Chicken, Battle of the Sexes, Stag Hunt, Minority Game, Rock-Paper-Scissors); Economic (3: Public Goods, Centipede, Bargaining); Bluffing (4: Liar's Dice, Skull, Coup, Sheriff of Nottingham); Hidden-Role Deduction (6: Chameleon, Insider, Spyfall, Undercover, Resistance, Werewolves); Social Strategy (2: Survivor, Dead Last).
- Elo: BT-MLE (Bradley-Terry maximum likelihood), anchor mean 1000, 95% bootstrap CIs; fit on 17 competitive games; 4 cooperative games (Stag Hunt, Public Goods, Battle of the Sexes, Centipede) scored by win rate; 560+ episodes per model.
- SPARTAN: (1) Play — model M plays N self-play games → trajectories {τ1..τN}; (2) Reflect — M sees trajectories + outcomes (win/loss per role) → writes a first-person, game-agnostic playbook covering deception, detection, persuasion, information management, coalition dynamics, timing; R1 = Reflect(M, τ1:N); (3) Transfer — prepend the playbook to the system prompt.

## Key Findings
- Leaderboard overall Elo (win rate): GPT-5-mini 1110 [1099,1120] 63.5%; GPT-4o 1030 [1021,1039] 47.5%; Gemma3-27B 1004 [995,1013] 42.0%; GPT-4o-mini 998 [989,1006] 40.5%; Qwen3-32B 968 [959,976] 33.9%; Qwen3-4B 961 [952,970] 33.2%; Qwen2.5-3B 926 [917,935] 25.6%.
- Per-game inversion: Qwen3-32B is first on Chicken (1328 Elo) yet last on Werewolves (817); no model is uniformly strong.
- Role gap: the gap usually favors the minority/deceptive role; for the strongest models it reverses under matched-capability self-play (minority side weaker).
- Parroting effect: Qwen2.5-3B frequently parrots (paraphrases the previous speaker) → a near-zero-information move that gives the deceptive side cover, explaining last place (926).
- SPARTAN within-game (GPT-5-mini, n=30/condition, CI ±18pp): alt side (structurally weaker) 24% → 36/36/43/35% under R1–R4 (peak R3); main side 76% → 66/59/67/63% (worst R2). Per-game peaks: Werewolves R3 63%, Resistance R3 40%, Spyfall R2 46%. The bulk of gain arrives at R1; extra rounds redistribute rather than accumulate — contradicting the iterated-reflection assumption of Reflexion/Self-Refine.
- Cross-game 1→n: alt-side injection median +7pp, max +27pp; main-side median −7pp, four cells below −20pp — a playbook generated on a different game still helps the weaker side.
- Multigame n→1: does NOT stack — broader source sets do not beat Single-R1, except held-out Resistance: Rwcsu lifts alt from 23% to 47%.
- Strong-to-weak distillation: Rwcsu (GPT-5-mini, never saw Resistance) into 6 students: three students (Qwen3-32B, Qwen3-4B, GPT-4o-mini) gain +13 to +24pp on the Spies side; the favored side moves ≤ ±5pp; Qwen2.5-3B and Gemma3-27B gain on neither side.
- Open-weights Qwen3-32B: largely null — only Prisoner's Dilemma (action-channel, single discrete token) shows a clean lift 13%→58% (+45pp), Resistance +34pp; the other four games are flat. Qwen3-32B reflection codifies its own parroting into the playbook without eliminating it. As teacher: PD transfers +17 to +77pp; Resistance mixed (+10/−20/−10pp).

## Actionable Insights
1. "Lift the weaker side" pattern: reflection playbooks help the structurally weaker role, not the strong one. Apply: when an AI agent handles an asymmetric task (e.g. buyer-side negotiation), generate the playbook from self-play on the weak role, not the strong one.
2. R1 already contains the bulk of gain (24→36%); more rounds only redistribute. Apply: one reflection round is enough for a new playbook; iterate only when a per-game peak is measured.
3. Game-agnostic playbooks transfer cross-game and to weaker models, but are capacity-dependent: 32B open-weights models are near-null except on action-channels reducible to a single discrete token. Apply: use SPARTAN only for workflows that reduce to a few discrete decisions; small models cannot learn discussion-heavy workflows.

## Assumptions & Limitations
- Conditions: games need rule-decided outcomes to be verifiable; the model needs enough capacity to learn from discussion-heavy trajectories.
- Stated limitations: external validity — fixed rules, many real interactions have no win/loss criterion; modest sample size (n=30/condition → CI ±18pp, several effects within range); no placebo-playbook control — content effects not fully separable from prompt perturbation; reflection constrained to natural-language prose, no tools/retrieval/scratchpad.
- Unstated limitations: playbooks reflect the teacher's own behavior (including parroting) → distillation can transmit bad habits; 560+ episodes/model is still small for a 21-game suite; self-play opponents are the same model → no measurement vs humans.
- Ethics: dual-use risk (deception, persuasion, coalition manipulation); the paper discourages adversarial human-facing use.

## Metadata
- Year 2026; authors Keyu He, Xuhui Zhou, Maarten Sap (Carnegie Mellon University); categories cs.CL / cs.AI / cs.MA; PDF https://arxiv.org/pdf/2608.09128v1; citation count: not found.
