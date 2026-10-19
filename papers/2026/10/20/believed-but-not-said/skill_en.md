# Skill: believed-but-not-said
Source: 2610.22138v1
Type: framework

## When to use this skill
- Evaluating multi-agent LLM system robustness when a few agents may persistently assert false claims (peer-pressure attack).
- Need to detect hidden belief collapse that never surfaces in the public transcript.
- Want to select models for multi-agent systems based on peer-pressure robustness, not just baseline accuracy.

## When NOT to use this skill
- Assuming larger groups are automatically more robust (the paper shows a 10-agent group is not significantly more robust than one agent).
- Measuring robustness only via baseline accuracy (knowledge does not predict robustness).

## Required inputs
- A group of N LLM agents discussing a factual item.
- A subset of adversarial agents (sybils) assigned to argue for a fixed false claim.
- A private probe mechanism: after each round, each benign agent answers the question in a separate call hidden from peers.
- An LLM judge to label private answers (TRUE/MANIPULATED/MIXED/UNCERTAIN) and public stances (ENDORSE/REJECT/HEDGE/IGNORE-DRIFT/UNRELATED).
- Number of discussion rounds (e.g., 16), shuffled speaking order each round.

## Steps
1. Set up an N-agent discussion; each agent speaks once per round in a random reshuffled order, conditioning on recent shared history (previous H=5 rounds).
2. Designate k adversarial agents (k ∈ {0,1,3}) who argue for a fixed false claim whenever the topic arises; benign agents get ordinary personas, no warning.
3. After each round, run a private probe: each benign agent answers the factual question in a separate call hidden from peers.
4. Label each benign utterance's public stance toward the manipulated claim.
5. Compute Final Private Infection (FPI): share of benign agents privately holding the false answer at the final step.
6. Classify each exposed turn by crossing private belief × public stance: robust correction, silent knower, social accommodation, performative endorsement, full infection, hidden infection, inconsistent.
7. Compute public endorsement rate and truth-knower correction (fraction of TRUE-private turns that explicitly REJECT the claim).
8. Compare FPI across k=0, k=1, k=3 conditions; one attacker produces ~74% of the infection rate of three sybils.
9. Intervene early: infection starts fast (~80% of final infection by round 4), so intervene in the first few rounds.

## Expected output
- A clear assessment of how much the group is infected at the private-belief level (not just transcript), identifying which models are truly robust to peer pressure.

## Example application
- A company uses a multi-agent system to fact-check content before publishing; run a stress test with one sybil agent repeatedly asserting a false claim, tracking each benign agent's private answer; if many agents privately hold the false belief despite a clean transcript, the model is not robust enough for the fact-checking system.

## Gotchas
- Do not conclude larger groups are more robust just because they have more agents — social redundancy does not automatically yield robustness.
- Do not evaluate only via the public transcript — about two-thirds of infections are never publicly endorsed.
- Do not infer robustness from baseline knowledge — a model knowing 85% of facts may abandon 80% of them under attack.
- Late intervention (after round 4) is less effective because infection has already plateaued.

## Self-check
- Can someone who has not read the original paper follow these 9 steps? [YES] — each step is a concrete action.
- Which step is most vague? Step 6 (failure taxonomy crossing two channels) needs clear public-stance judging criteria.
- Is the Input section sufficient? [YES] — agent group, adversarial agents, private probe, judge, number of rounds are all covered.

## Dry run (hypothetical scenario)
- Scenario: A company's 5-agent system fact-checks news before publishing; wants to know which model resists false claims spreading through chat.
- Run the skill: (1) Set up 5 agents discussing a fact; (2) designate 1 sybil agent to assert a false claim repeatedly; (3) after each round, privately probe each benign agent; (4) label public stance and private answer; (5) compute FPI at the final step; (6) if FPI is high (>40%) despite a clean transcript, the model is not robust enough — choose another model or add early-intervention mechanisms.

## Verdict: [SKILL VALID]
