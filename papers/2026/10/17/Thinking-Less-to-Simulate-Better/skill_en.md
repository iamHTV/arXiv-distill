# Skill: intuitive-prompting-agent-simulation
Source: 2609.30563v1
Type: framework

## When to use this skill
- Building agents that simulate specific user responses on social media.
- Need to evaluate agent fidelity against actual user reactions.
- Can collect rich user profiles: questionnaire, deep interview, free-text self-presentation.

## When NOT to use this skill
- Simulating population-level responses rather than specific individuals.
- No detailed user profile data available for target users.
- Only need aggregate estimates, not individual differences.

## Input needed
- User profiles: questionnaire (demographics, beliefs, values, activities, political placement), deep interview transcript, free-text self-presentation.
- Set of social media posts for agents to react to (like/dislike).
- At least one LLM to generate responses.
- Fidelity metric (e.g., Matthews correlation coefficient).

## Steps to execute
1. Profile users: collect questionnaire, deep interview, and free-text self-presentation from each target user.
2. Build stimulus set of social media posts, including both in-domain (covered by profile) and out-of-domain topics.
3. Create five prompt conditions: V4 demographics (basic demographic info); V3 questionnaire (adds full questionnaire responses); V1 interview (adds interview transcript and self-presentation — richest profile); V2 inference (same content as V1 plus instruction to infer reactions from combinations of characteristics); V5 intuitive (same content as V1 but instructed to respond immediately rather than analytically).
4. Run each model under each condition on each user profile, collect like/dislike responses for all posts.
5. Evaluate fidelity by comparing agent responses to actual user reactions, using Matthews correlation coefficient (MCC) as primary measure.
6. Measure compression of individual differences via standard deviation across users.
7. Compare prompt conditions to identify which yields highest fidelity.

## Expected output
- Agent simulating user responses with highest fidelity under intuitive prompting (MCC up to 0.473 vs 0.300 for demographics alone).
- Compression of individual differences reduced from 10.24× (demographics) to 3.14× (intuitive), close to human level (1.00×).

## Application example
- Build agent simulating customer responses to social media posts about a new product: collect customer profiles via questionnaire and interview, use intuitive prompting (instruct agent to respond immediately, don't weigh characteristics against each other), evaluate fidelity with MCC against actual customer reactions.

## Gotchas
- Only 8 participants, all in Serbia; results may not transfer to other populations.
- Models are known to represent wealthy Western publics more accurately; performance may be understated elsewhere.
- Each configuration run once, reactions reduced to binary choice, two models excluded due to incomplete output.
- Intuitive instruction combines speed pressure, ban on justification, and permission to depart from profile — which element carries the effect is unclear.
