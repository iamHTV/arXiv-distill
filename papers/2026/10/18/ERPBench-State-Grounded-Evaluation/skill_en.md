# Skill: State-Grounded Evaluation for Computer-Use Agents in Business Software

Source: 2609.17885v2
Type: evaluation-method

## When to use this skill
- You are building a computer-use agent (CUA) to interact with business software (ERP, CRM) and need to evaluate real-world reliability.
- You want to ensure the agent doesn't just see on-screen success messages but actually writes correct values to the database.
- You need a harness with human-in-the-loop approval for risky actions before production deployment.

## When NOT to use this skill
- Simple applications without complex business software interaction.
- You don't have a test database to check field values after agent execution.

## Input required
- Test business software system (ERPNext or equivalent) running in Docker.
- Task YAML files specifying prompt, start URL, expected field values, grader configuration.
- Test database with seed data (fixture) populated via API.
- Harness that runs agents from screenshots and simulates mouse/keyboard input.

## Steps to execute
1. Build evaluation tasks across three complexity tiers: T1 (single record), T2 (multi-field coordination), T3 (multi-screen chained workflows).
2. Score each task with three graders: Database grader (checks field values in DB), Stage grader (Navigation, Interaction, Commit, Database), Log grader (action count, duration, token cost).
3. Set up harness in two modes: Deployment (commit/irreversible actions require human approval) and Evaluation (auto-approver).
4. Run each task for multiple independent runs, score each run against ground-truth database values.
5. Identify failure modes by stage to localize where the agent fails.

## Expected output
- A CUA evaluation system that measures real enterprise reliability.
- Knowledge of which stage the agent fails at (navigation, data entry, commit, or database persistence).
- A harness with human-in-the-loop approval for risky actions.
- Success rate reports by tier and by stage.

## Example application
You build an agent to automatically create invoices in business accounting software. Instead of just checking whether the agent clicked the "Save" button, verify the "amount" field value in the database after the agent runs. If the agent clicks save but the DB value is wrong, evaluate as failure. Actions that delete records or send invoices must await human approval before execution.

## Gotchas
- Strong general GUI performance does not predict enterprise reliability.
- Agents can navigate to the right screen and click save, but the database value may still be wrong (silent failure).
- Open-weight models collapse on complex tiers (T2, T3), reaching 0–3% vs 34% on T1.