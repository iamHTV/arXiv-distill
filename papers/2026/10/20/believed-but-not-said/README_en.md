# [2610.22138v1] Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions

## Core value (1 sentence)
Measure hidden belief collapse in multi-agent LLM discussions: track each agent's private answer (via a hidden per-round probe) alongside its public stance, to detect false-belief infection that never surfaces in the transcript.

## Problem
Prior work failed to address that multi-agent systems assume peers will catch each other's errors, while the coordination channel is also an attack surface: a few sybil agents repeatedly asserting a plausible false answer can change what most agents privately believe while the public transcript barely reveals it.

## Contribution
- A controlled 10-agent factual discussion over 16 rounds with k ∈ {0, 1, 3} adversarial agents (sybils) repeatedly arguing for a fixed false claim; benign agents receive ordinary personas without the false claim and are not warned.
- Dual measurement: each round, every benign agent gives a public chat utterance and a private probe answer via a separate call hidden from peers; both are judged independently.
- Failure taxonomy crossing private belief × public stance: robust correction, silent knower, social accommodation, performative endorsement, full infection, inconsistent.
- Evaluation of six models across three factual-QA datasets (COUNTERFACT, POPQA, SIMPLEQA; 40/53/50 items), 18 model×dataset cells.

## Method
Each run is a chatroom of N=10 agents discussing one factual item for T=16 rounds; all agents in a run share the same base model. Vary the number of adversarial agents k ∈ {0,1,3}, leaving 10−k benign agents. Adversarial agents each argue for a fixed false claim whenever the topic arises; benign agents get ordinary discussion personas with no false claim and no warning. The attacker only posts messages — no weight editing, no hidden-state access, no control of benign agents. Each round, every agent speaks exactly once in a random reshuffled order, conditioning on recent shared history (previous H=5 rounds) and the current round. Conversations start from a neutral discussion seed. After each round, each benign agent answers the probe question in a separate private call whose response is hidden from other agents and never posted. A judge labels each private answer TRUE / MANIPULATED / MIXED / UNCERTAIN; an agent is infected at a step if its label is manipulated. Independently, a judge labels each benign utterance's public stance toward the manipulated claim as ENDORSE / REJECT / HEDGE / IGNORE-DRIFT / UNRELATED. Key metrics: Final Private Infection (FPI) = share of benign agents privately holding the false answer at the final step; turn-level infection; public endorsement; truth-knower correction (fraction of TRUE-private turns that explicitly REJECT the claim).

## KNOWLEDGE — Data & figures
- No attacker (k=0): benign groups stable, FPI averages 0.6%, never exceeds 3% in any of the 18 model×dataset cells, 0.2% initial infection.
- Single adversary: average FPI 44.8% (range 19–74%).
- Three adversaries: average FPI 60.5% (range 27–81%).
- One attacker produces 74% of the infection rate observed with three sybils.
- Pair (N=2, one attacker + one benign): 45.6% of lone benign agents end up with the false answer vs 39.3% in the 10-agent group — redundancy barely helps.
- Under three attackers: benign agents privately hold the false answer in 51.6% of exposed turns but publicly endorse it in only 19.7% (2.6× as many turns carry false private belief as endorse publicly).
- Only 34.3% of turns with a false private answer publicly endorse the claim; the rest hedge, ignore, or reject.
- Agents privately retaining the true answer publicly reject the false claim in only 61.9% of turns; in the rest they stay silent, hedge, or go along.
- Knowledge does not predict robustness: HY3 and GPT-OSS-120B both know 85% of facts pre-discussion; under three attackers GPT-OSS-120B abandons 80% of known facts while HY3 abandons 25%.
- Social cascade: holding attacker count fixed, an uninfected agent's probability of switching in a round rises with the number of benign peers already converted, from 9% (none) to 66% (5+), monotonically up to four converted peers.
- Self-internalization: agents holding truth who see the claim — if they correct publicly, only 2.3% hold false after the round; if they endorse, 39.7% do; silent/hedge falls between.
- Infection onset fast: 5/6 models reach half their final infection within one round; ~80% of final infection is in place by round 4; curves plateau rather than climb; final plateaus range 31% (HY3) to 76% (GPT-OSS-120B).
- Re-asking agents their own view: they keep 86.4% of false answers and return to truth only 9.1%; final infection falls from 58.8% to 53.1%, still a majority. Anonymizing their own messages leaves results unchanged — not mere self-consistency.
- Six models: HY3-PREVIEW, QWEN3.5-FLASH, MISTRAL-SMALL-3.2 (24B), GEMMA-4 (26B), GEMINI-2.5-FLASH-LITE, GPT-OSS-120B. Temperature 0.7. One conversation per item × model × k.
- Judge: deepseek-v4-flash for both public stance and private answers; independent judge claude-sonnet-5.5 relabeled 200 private answers with 87.5% agreement (Cohen's κ=0.82).
- arXiv category: cs.AI

## INSIGHT — Mechanism & why
[Hidden belief infection exceeds what transcripts reveal] BECAUSE [agents privately hold the false answer but rarely endorse it publicly; transcript-level monitoring reveals only about a third of infected turns]. This means [monitoring only the public transcript is insufficient; agents' private answers must be tracked rather than only public messages].
[One attacker causes most of the damage] BECAUSE [a 10-agent group is not significantly more robust than one agent against persistent false claims; social redundancy does not automatically yield robustness]. This means [larger group size does not help; intervene early — the detection/intervention window is the first few rounds].
[Base knowledge does not predict robustness] BECAUSE [two models knowing the same 85% of facts abandon 25% vs 80% of them under attack]. This means [robustness is a distinct, model-specific property that must be measured directly, not inferred from baseline accuracy].
[Infection starts fast and is hard to reverse] BECAUSE [5/6 models reach half their final infection within one round; ~80% is in place by round 4; curves plateau]. This means [the window for detection or intervention is the first few rounds].

## IDEA — What to apply
Apply an adversarial peer-pressure test to model selection for enterprise multi-agent systems: step 1 is to run a group discussion with one agent repeatedly asserting a false claim, tracking each benign agent's private answer after each round.
Monitor agents' private answers rather than only public messages: step 1 is to log each agent's private answer after every discussion round, so hidden answers remain visible even when the transcript looks unchanged.

## WISDOM — General principle
Principle: Social redundancy in agent groups does not automatically create robustness against false-belief infection; public messages should be treated as untrusted input, and robustness to peer pressure must be measured directly at the level of individual agents.

## Assumptions & Limitations
- Conditions for validity: multi-agent factual discussion, public communication corrupted in-context by adversarial agents, homogeneous model groups, shuffled speaking order.
- Limitations acknowledged by the paper: only groups of 2 and 10 agents compared, no network topology variation or model mixtures; attacker acts only in context (parametric attacks like knowledge editing are a different mechanism); all labels come from an LLM judge (deepseek-v4-flash), with an independent judge (claude-sonnet-5.5) relabeling 200 private answers at 87.5% agreement (κ=0.82); public stance in free-form chat is harder to label than one-sentence answers, so public endorsement rates may be underestimated.
- Limitations the paper does NOT mention: operational cost of recording every agent's private answer each round at scale; latency impact of parallel private probes; stability over discussions longer than 16 rounds.

## Metadata
- Year: 2026
- Authors: Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, Wooseong Yang, Yuwei Han, Philip S. Yu (University of Illinois Chicago)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.22138v1
- arXiv ID: 2610.22138v1
- Label: [applied]
- Skill: believed-but-not-said | Test: [SKILL VALID]
