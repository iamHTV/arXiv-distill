# [2610.36813] Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue

## Core Value (1 sentence)

When an agent needs to predict user behavior from dialogue content, prioritize actual decision history over statements in chat — because LLMs overestimate how often users keep their word (predicting .69 when reality is .40) and fail to capture how behavior varies by agent persona, so aggregate accuracy hides large per-agent errors.

## Problem

Web systems increasingly predict users' decisions from what users say in dialogue, but when interests partly conflict, users may promise cooperation and then not follow through. Systems that rely on such promises — such as sales or service agents deciding what concession to offer next — may grant concessions to users who then do not keep their promises, at a cost to the party each agent represents. Existing research does not link a user's statement to that user's earlier decisions, the counterpart, and the later action. Aggregate accuracy also does not reveal which error a predictor makes: relying on statements gains accuracy on kept statements and loses it on broken ones, and the two can cancel.

## Contribution

1. An evaluation design that ties a predictor's use of dialogue to separately recorded actions, split by whether statements were kept, whether they were inconsistent with users' earlier decisions, and the agent the user faced.
2. Evidence that eight LLM predictors relied on stated decisions beyond how often they were kept.
3. Evidence that the predictions missed how users' behavior varied with agent persona and trait compatibility, and that pooled metrics concealed both errors.
4. Design implications for dialogue-based user modeling: how much weight a user's statement receives should depend on the user's earlier decisions and on the agent, and predictions should be checked against what users later do with each agent.

## Method

The study uses the Personality-1260 dataset: 42 participants (Chinese university students, 21 female, mean age 22.1) completed the Chinese BFI-44 and played one game with each of five agents in random order. Each agent is GPT-4o prompted to be extremely high in one Big Five trait (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism). Each game has 6 rounds; in each round, user and agent may talk freely, then both decide whether to cooperate or defect, with the agent's decision revealed only after the user's. Mutual cooperation pays 2 points each, defecting against a cooperator pays 3 (the cooperator 0), mutual defection 0 each. Talking was optional; dialogue was empty in 276 of the 1,260 rounds. Eight open-weight LLMs (Qwen3.5-9B, Qwen3.8-27B, Gemma-4-12B, Gemma-4-31B, Seed-OSS-36B, GLM-4-32B, Ministral-3-14B, Olmo-3.1-32B) predicted each decision from 19 combinations of the decision record (R — both players' earlier decisions) and the dialogue (D — what users said). Conditions have 4 decision levels (none, Ro, Rc, R) and 5 dialogue levels (none, Do, Dc, Dt, D): 19 conditions. Prediction analyses use games 2–5 (1,008 rounds). Uncertainty comes from user bootstrap (50,000 draws of 42 users with replacement).

## KNOWLEDGE — Data & Concepts

- 1,260 rounds, 42 users, 5 agent personas, 8 open-weight LLMs as predictors.
- Decision record alone (R) AUC = .80 [.76, .85] separates cooperation from defection; dialogue alone (D) AUC = .70 [.64, .76]; both (R + D) AUC = .79 [.75, .83] — adding dialogue brings no detectable gain.
- The statement itself ranks poorly: with 96% of statements announcing cooperation, the statement separates cooperation from defection at AUC = .55.
- Adding current-round dialogue to current-game decisions changed accuracy on stated-decision rounds from .73 to .74: it raised accuracy on 470 rounds where the statement was kept from .76 to .95 (+.20 [.15, .25]) and lowered it on 176 rounds where it was broken from .65 to .17 (−.48 [−.52, −.44]).
- When users stated a decision they had not yet chosen (53 rounds, 20 users), predicted word-keeping probability rose from .13 without dialogue to .69 with dialogue, while users kept their word at .40 [.25, .58] — prediction moved from .27 below observed to .30 above it.
- One inserted sentence stating a decision moved agreement with the recorded decision from .75 to .98 when it matched and to .08 when it contradicted.
- Users cooperated in 70.6% of rounds with the Agreeableness agent and 54.5% with the Extraversion agent (+16.3 points); predicted cooperation was 64.5% and 63.1% (barely different).
- AUC ranged from .76 (Openness) to .82 (Neuroticism), no pair differed; predicted cooperation spanned 6.0 points across personas.
- Prediction bias in cooperation rate: +8.6 points with Extraversion agent and −6.0 points with Agreeableness agent; difference of 14.6 points between them.
- The higher users scored on the trait an agent expressed, the more they cooperated (+3.0 points per standard deviation); prediction bias fell increasingly short (−3.3 points per SD).
- Adding BFI scores or compatibility score to the prompt only reduced the bias slope by about a quarter (from −3.3 to −2.5 per SD); most of the bias remained.

## INSIGHT — Mechanism & Why

[LLMs overestimate how often users keep their word] happens BECAUSE [LLMs weight users' statements more heavily than users' behavior warrants: when users state a decision they have not yet chosen, predicted fulfillment jumps from .13 to .69 while reality is .40]. This means [dialogue-based prediction tends to trust promises too much, leading to undeserved concessions].

[Adding dialogue does not increase aggregate AUC (.80 → .79)] happens BECAUSE [it raises accuracy on kept statements but lowers it on broken ones, and the two cancel out, shifting errors onto rounds where users broke their word — nearly half of all defections]. This means [aggregate accuracy hides that the predictor is making errors in the opposite direction on the most important rounds].

[LLMs fail to capture how behavior varies by agent persona and trait compatibility] happens BECAUSE [predictions barely change between agents (64.5% vs 63.1%) while user behavior changes strongly (70.6% vs 54.5%), and near-zero pooled mean bias conceals per-agent differences of up to 14.6 points]. This means [a user representation that absorbs all choices into a general cooperation tendency loses information about the counterpart involved].

[Recording each statement linked to its outcome corrects most of the overestimation] happens BECAUSE [when each earlier statement is linked to its outcome, predicted word-keeping falls from .69 to .40, matching the observed rate]. This means [a predictor uses added information best when it states the relation to be predicted: the record links each statement to its outcome].

## IDEA — Actionable Applications

1. Track each user's word-keeping rate: before an agent decides to grant a concession based on a user's promise, the agent looks up that user's history of promises and their fulfillment rate. For whom: sales/service agents deciding concessions. First step: store a (promise, actual action) pair for each user in each interaction round.

2. Evaluate user-decision prediction separately per agent persona and per statement type (kept/broken), not just aggregate accuracy. For whom: teams building user models. First step: report accuracy separately for kept and broken statements, and per agent/persona.

3. Prioritize actual decision history over dialogue content when building models to predict user actions. For whom: ML engineers building user models. First step: in the prediction model input, provide the prior decision record (both players) before the current dialogue, because dialogue adds little to AUC.

## WISDOM — General Principle

- Principle: A user's promise in dialogue should not be treated as equivalent to actual behavior; the system should track each user's word-keeping rate and weigh new promises against history. Apply when an agent decides whether to grant concessions or transfer based on user promises. Do not apply when only a general trend is needed without per-user detail.

## Assumptions & Limitations

- Conditions that must hold: statements and actions recorded separately, repeated decisions forming a record to compare against statements, counterparts changing while actions and payoffs stay the same.
- Limitations acknowledged by the paper: 42 Chinese university students in short, low-stakes games; eight zero-shot predictors using Chinese prompts with reasoning disabled; all counterparts used GPT-4o; persona prompts changed language and decisions, confounding personality expression with behavioral reciprocity; compatibility uses one trait; analyses are exploratory and uncorrected; some subgroups were small (53 rounds from 20 users); prompt edits measure model sensitivity, while statement-action associations do not identify causal effects.
- Limitations the paper does NOT state: results may differ for other populations, longer relationships, and web tasks; prompting effects may differ on models with reasoning enabled; operational cost of storing statement-action history at scale is not evaluated.

## Metadata

- Year: 2026
- Authors: Baiqiao Zhang, Shuai Ma, Zhifeng Liao, Chao Zhou, Jianshu Wang, Yuhan Zhao, Chaoyue Zhang, Tongjun Si, Yuying Tang, Xiangxian Li, Yong-Jin Liu, Yulong Bian
- arXiv category: cs.CL
- PDF link: https://arxiv.org/pdf/2610.36813v1
- Citation count: [not found]