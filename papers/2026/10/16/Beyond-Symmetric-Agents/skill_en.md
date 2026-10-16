# Skill: cognitive-diversity-multi-agent-debate
Source: 2609.35875v1
Type: framework

## When to use this skill
- Building multi-agent systems (MAS) and wondering whether to use debate between agents.
- Want to leverage cognitive diversity between agents instead of copying the same agent.
- Working with small open-weight models.

## When NOT to use
- Only using a single agent, no multi-agent system.
- Want to use debate for many rounds of exchange (debate only has benefit in the first round).

## Required input
- Multiple agents with different personalities/methods (cognitive diversity).
- Measurable questions/tasks with benchmark headroom.
- A mechanism to aggregate results (pooling/voting) from independent agents.

## Steps
1. Build agents with different personalities (don't copy the same agent).
2. Instead of having agents debate for many rounds, limit debate to 1-2 rounds of exchange (benefit is only in the first round).
3. Let agents work independently, then aggregate results (pooling/voting) instead of having them debate.
4. Combine agents with different accuracy levels (mixed teams) instead of homogeneous teams.
5. Track claim precision and accuracy to evaluate effectiveness.

## Expected output
- Mixed teams overturn 63.7% of wrong round-one majorities vs 42.9% for homogeneous.
- Independent biographies pooled reach 64.6% vs debate's 55.6% (+8.9pp).
- Debate benefit only in first exchange (84.6% at one round, 87.2 at two, flat through five).

## Example application
Solopreneur building a content-writing MAS: instead of 3 agents with the same prompt debating about content, create 3 agents with different viewpoints (one focused on SEO, one on engagement, one on accuracy), let each write independently, then pool the best result.

## Gotchas
- Debate is not always better than solo generation (loses by 1.04pp).
- Debate only has benefit in the first exchange, then plateaus.
- Persona teams reduce claim precision to 51.8% — don't over-use personas.
