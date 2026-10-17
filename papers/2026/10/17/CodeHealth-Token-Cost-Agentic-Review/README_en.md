# [2610.21914v1] CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests

## Problem
- Organizations increasingly delegate code review to multi-agent LLM pipelines billed per token. Low code quality raises human maintenance effort, but its effect on agent review cost has not been measured. Prior work does not address whether a code quality metric predicts the token cost of agentic review and fix.

## Contribution
- Pre-registered observational study of 465 agent-authored PRs from 246 repositories in AIDev, jointly stratified by CodeHealth and footprint under repository caps.
- Frozen five-agent review-and-fix pipeline processed every PR with three different LLMs. Per LLM, fitted a mixed model of log tokens on CodeHealth and log PR footprint, with a repository random intercept.
- For all three LLMs the CodeHealth coefficient was negative, with 95% CI excluding zero; each CodeHealth point was associated with 3.5% to 6.1% lower token cost. CodeHealth was unrelated to PR footprint, so PR size does not explain the association.

## Method (core summary)
- Pre-registered observational study: 465 agent-authored PRs from 246 repositories in AIDev, jointly stratified by CodeHealth and footprint under repository caps.
- Frozen five-agent review-and-fix pipeline processed every PR with three different LLMs.
- Per LLM, fitted a mixed model of log tokens on CodeHealth and log PR footprint, with a repository random intercept.
- CodeHealth™ (CH) is a composite, deterministic score between 1 and 10 that aggregates several source-level quality signals into a single file-level measure.

## Key Findings
- 4 authors from Lund University and CodeScene AB, arXiv category: cs.SE.
- 465 PRs, 246 repositories, 3 LLMs.
- For all three LLMs the CodeHealth coefficient was negative, with 95% CI excluding zero.
- Each CodeHealth point was associated with 3.5% to 6.1% lower token cost, holding footprint, language, and repository constant.
- Footprint itself is essentially unrelated to baseline CodeHealth in this sample.
- Two of three registered smells predicted fix cost; batch fixing left median CodeHealth unchanged.
- Association located in the review stage: agents iterated more on unhealthy code without writing more comments.
- Adjusting for the size of scored files absorbed the association (mediation by file size).

## Actionable Insights
1. Code quality predicts token cost of agentic review and fix. Application: monitor CodeHealth (or similar quality metric) to predict inference cost of agent review and fix.
2. Effect is modest per point (3.5% to 6.1% lower token cost per CodeHealth point) and not due to PR size. Application: refactoring to improve code quality can reduce agent review cost, not just because PRs are smaller.

## Assumptions & Limitations
- Pre-registered observational study — cannot conclude causality.
- Each PR run only once.
- Focused on 3 specific LLMs.
- Adjusting for scored file size absorbed the association (mediation by file size).

## Metadata
- Year: 2026, authors: Lo Gullstrand Heander, Markus Borg, Emma Söderberg, Christofer Rydenfält (Lund University, CodeScene AB), arXiv category: cs.SE, PDF link: https://arxiv.org/pdf/2610.21914v1
