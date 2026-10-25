# Skill: inhibitory-message-passing-router

Source: 2610.24718
Type: framework

## When to use this skill

- Multi-agent groups need to combine distributed evidence to reach a scored decision (research, analysis, diagnosis).
- Want to keep accuracy stable as the agent group grows without token cost growing exponentially.
- Can identify which evidence sentences each agent holds and match them to outgoing message content.

## When NOT to use this skill

- Work requiring agents to exchange intermediate results not contained in original evidence (coding, planning, distributed computation).
- Tasks without clear evidence to match (creative writing, brainstorming).

## Input needed

- List of evidence sentences each agent holds (clearly listed, with source tags).
- Each agent's message written each round (under 100 words per message).
- Router rules: forward original evidence, once per round, only if receiver lacks it.

## Steps to execute

1. Each agent writes a message containing reasoning and answer, while restating the evidence sentences it holds (using rare words so the router can match them).
2. Router for each receiver: takes all evidence sentences restated in sender messages, keeps only the original sentences (not sender reasoning or answers).
3. Subtracts evidence sentences the receiver already holds in its own evidence.
4. Limits each evidence sentence to be delivered at most once per round per receiver (regardless of how many senders restate it).
5. Sends the filtered inbox to each receiver; agent reads inbox and writes a new message for the next round.

## Expected output

- Each receiver's inbox contains only original evidence sentences it lacks, without sender reasoning or answers.
- Inbox size does not grow with the number of agents in the group.
- Group accuracy stays stable or increases as group grows, tokens per run decrease.

## Example application

4-agent medical diagnosis group for chest pain: all read the chart (shared evidence suggesting heart attack), 3 agents query their own tools, each getting one result (private evidence). Standard message passing sends full messages (including most agents' "heart attack" conclusion) → patient misdiagnosed. Inhibitory router forwards only each missing test result (normal troponin, unequal arm pressures) → same conclusion: aortic dissection, correct.

## Gotchas

- Router does not assess credibility of forwarded evidence: a planted false sentence reduces accuracy (cannot withdraw evidence later corrected).
- Needs reliable provenance link between message and evidence it refers to; errors suppress useful evidence or leave redundant input.
- Does not establish when excluding sender reasoning/answers impedes collaboration on tasks needing intermediate result exchange (code, planning).
