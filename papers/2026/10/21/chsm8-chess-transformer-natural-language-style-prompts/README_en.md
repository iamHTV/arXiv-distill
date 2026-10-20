# [2610.25356v1] CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts

## Core Value (1 sentence)
A 210M-parameter chess transformer can control playing style via free-text style prompts, with style adherence rising significantly after DPO (queens traded early 53%→67%, queenside castling 97.3%→99.7%) without weakening no-prompt strength (1792 vs 1797 Elo).

## Problem
Prior work controls chess models via rating or player identity, and does not accept open-ended requests like "castle queenside and storm the enemy king with your pawns". Existing models do not allow users to direct playing style through free natural language.

## Contribution
1. The first chess model (to authors' knowledge) that plays by free-form natural-language description of style, rather than rating, player identity, or templated prompt.
2. A fully open and reproducible pipeline: weights, datasets (including teacher labels used to train both the labeler and style model), complete recipe with prompts and configurations, inference code, and playable demos are public.
3. New datasets that did not exist before: high-quality corpus of 1.07B games filtered from 7.95B-game Lichess archive; online games of FIDE top 100; five style descriptions for each of 30.1M game sides; teacher labels and distillation set behind the labeler.

## Method
CHSM8-PT is pretrained on 1.07B filtered Lichess games (filtered by rating, time control, game quality), using factorized move representation and legal-move masking, without search, reaching 1837 Elo against strength-limited Stockfish. Then 30.1M game sides are labeled with natural-language style descriptions: Gemma-4-31B describes playing style of 3M game sides; Gemma-3-1B distilled from 2.4M non-contradictory descriptions labels the rest; each selected game side gets five descriptions. SFT attaches a frozen text encoder through gated cross-attention. DPO uses the same moves under a mismatched description as the rejected sample. After DPO, style adherence rises on every tested prompt. Design choices at every stage are made by fixed-budget automated search loops on top of standard architectures and training recipes. The work is fully open source and reproducible.

## KNOWLEDGE — Data & Concepts
- Architecture: 210M parameters, decoder following Llama recipe, text conditioning via Flamingo-style gated cross-attention
- Pretraining corpus: 1.07B games filtered from 7.95B-game Lichess archive (filtered by rating, time control, game quality); 49.1% games end 1-0, 44.7% 0-1
- Strength: 1837 Elo vs strength-limited Stockfish; beats every public model tested with no preference tuning/rewards/search, from 23M to 2.8B parameters, including one with 13x more parameters
- Training: Gemma-4-31B describes style of 3M game sides; Gemma-3-1B distilled from 2.4M clean descriptions labels 30.1M game sides × 5 descriptions each; SFT 27.1M sides × 5 descriptions; DPO 0.56M games (2% of corpus), 20 minutes on 1 GPU, 4,366 steps of batch 128
- Style adherence after DPO (2,000 games per prompt): queens traded early 53%→66.5%, pawn moves .290→.319, queenside castling 97.3%→99.7%
- No-prompt strength: SFT 1792 Elo, DPO 20-min run 1797 Elo, DPO full pass 1812 Elo (within noise)
- Alignment tax: SFT costs ~45 Elo without prompt (1792 vs 1837 pretrain)
- Main DPO recipe: label pairs, β=0.5, NLL 1.0, KL 1.0, body LR 2×10⁻⁷, conditioning LR 10⁻⁴, pinned no-text term
- Attack gap (Elo under attack prompt − Elo no prompt): DPO 20-min −150, DPO full pass −155, SFT −40
- Cost per game: SFT ~36 layer applications per position (K=5), DPO ~18 (K=2); SFT 2,400 games/second, DPO 3,750 games/second
- Automated search loop: ~70 short DPO runs (10-20 minutes per GPU), screened with 100 games per prompt; from round 6, 300 games no prompt, 300 games attack prompt, 150 games per other style prompt; 20 most promising re-evaluated at 1,000 games per prompt

## INSIGHT — Mechanism & Why
[DPO improves style adherence without weakening no-prompt strength] BECAUSE [DPO uses the same moves under matched and mismatched descriptions, so only the text can explain the preference, needing neither sampling nor a reward model]. This means [model behavior can be controlled via natural language without a large trade-off in base strength].
[Fixed-budget automated search loop finds better DPO configurations than hand-tuning] BECAUSE [each configuration is run for a fixed wall-clock budget, scored on a fixed validation set, and the next round is planned from results]. This means [automating experiment design reduces human error and finds better configurations faster].
[Style-move DPO reduces strength loss under attack prompt] BECAUSE [DPO is applied only to the top 10–50% of moves where the reference model's log-likelihood depends most on the label, while KL/NLL anchor covers the rest]. This means [balancing style adherence with strength by focusing preferences on important moves].
[Full-pass DPO does not improve over 20-minute run] BECAUSE [style adherence saturates early in the corpus; validation pair accuracy keeps rising but does not translate to better play]. This means [more DPO data is not always better; early stopping can be more effective].

## IDEA — Actionable Applications
1. Apply [DPO with label-swap pairs] to [controlling LLM agent behavior via natural language]: first step is to prepare paired data (same output, matched vs mismatched description), run DPO to make the agent follow style instructions without needing a reward model.
2. Apply [fixed-budget automated search loop] to [optimizing agent prompts or configuration]: first step is to set up a queue of configurations, each run for a fixed time, scored on a fixed validation set, automatically planning the next round from results.
3. Apply [distilling large teacher into small student for data labeling] to [building training datasets for agents]: first step is to use a large model (e.g., Gemma-4-31B) to label a small subset, then distill into a small model (e.g., Gemma-3-1B) to label the full corpus.

## WISDOM — General Principles
1. Principle: Model behavior can be controlled via natural language using DPO without a reward model, given paired data (same output, different conditions). Apply when: needing to control agent style/behavior via text instructions. Do not apply when: the task lacks a clear distinction between good and bad outputs.
2. Principle: Automated experiment design with fixed budget often beats manual hyperparameter tuning. Apply when: optimizing agent hyperparameters or architecture. Do not apply when: no validation set or clear metric exists for evaluation.

## Assumptions & Limitations
- Conditions that must hold: large corpus of high-quality games, a large model to generate style descriptions, GPU resources for pretraining and fine-tuning.
- Limitations acknowledged by paper: alignment tax (SFT costs ~45 Elo without prompt); no weak/strong play conditioning (every described player rated ≥ 2200); player prompts have modest effect (~1 point move match); adherence measured on a handful of prompts with hand-written metrics, not validated judgment of style; no search, so weaker than systems with search.
- Limitations paper does NOT mention: no evaluation on non-chess tasks; no comparison with other LLM behavior control methods (e.g., plain prompting, classifier-free guidance); no real inference cost comparison with larger models.

## Metadata
- Year: 2026
- Authors: Ilia Badanin
- arXiv Category: cs.LG
- PDF Link: https://arxiv.org/pdf/2610.25356
- arXiv ID: 2610.25356v1
- Label: [applied]
- Citation count: [not found]