# Skill: codehealth-token-cost-prediction
Source: 2610.21914v1
Type: evaluation-method

## When to use this skill
- Predict inference cost of agent review and fix before running.
- Have code quality scores (CodeHealth or similar) for files in the PR.
- Need to predict token cost based on code quality, not just PR size.

## When NOT to use this skill
- No code quality scores available for files.
- Only need to estimate cost based on PR size (footprint).
- No agent review-and-fix pipeline to measure actual cost.

## Input needed
- Code quality score (CodeHealth, scale 1-10) for each file in the PR.
- PR footprint (diff size, lines changed).
- Programming language and repository information.
- Agent review-and-fix pipeline to measure actual cost (for validation).

## Steps to execute
1. Collect CodeHealth (or similar quality) scores for each file in the PR.
2. Collect PR footprint (diff size, lines changed).
3. Fit a mixed model of log tokens on CodeHealth and log PR footprint, with a repository random intercept.
4. CodeHealth coefficient is negative with 95% CI excluding zero — each CodeHealth point associated with 3.5% to 6.1% lower token cost.
5. Check if association is due to PR size (footprint is unrelated to baseline CodeHealth).
6. Association located in review stage — agents iterate more on unhealthy code without writing more comments.
7. Adjusting for scored file size absorbed the association (mediation by file size).

## Expected output
- Predicted inference cost for agent review and fix based on CodeHealth score.
- Each CodeHealth point higher associated with 3.5% to 6.1% lower token cost.

## Application example
- For a PR with average CodeHealth score of 4 (low), expected token cost is 14% to 24% higher than a PR with CodeHealth 8 (high) (4 points × 3.5% to 6.1%).

## Gotchas
- Pre-registered observational study — cannot conclude causality.
- Each PR run only once.
- Focused on 3 specific LLMs.
- Adjusting for scored file size absorbed the association — relation may be due to file size, not quality itself.
