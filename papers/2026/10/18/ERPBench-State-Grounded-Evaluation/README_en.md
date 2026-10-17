# [2609.17885v2] ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software

## Problem
Computer-use agents (CUAs) that operate through screenshots and simulated actions are advancing rapidly, yet their evaluation remains anchored to general desktop and web tasks. Enterprise Resource Planning (ERP) systems run finance, procurement, inventory, and customer operations worldwide, and pose distinct challenges for CUAs: dense interfaces, coordinated multi-step interactions, and errors that alter persistent business records rather than surfacing on screen. Existing enterprise computer-use benchmarks rely on proprietary platforms or on simulated approximations. A visually plausible interaction is not enough — an agent may navigate to the correct screen, click expected controls, and observe a success confirmation, yet leave the business record unchanged or wrong.

## Contribution
- Introduces ERPBench, a benchmark that evaluates screenshot-only agents on a live and reproducible ERPNext system and scores each task against ground-truth values in its database.
- Presents a production-grade harness that gates agent actions behind human approval for safe deployment.
- Evaluates six closed and open-source agents, demonstrating that strong general performance does not transfer to enterprise reliability.
- Characterizes failure modes specific to enterprise workflows.

## Method
- ERPBench built on a live, self-hosted ERPNext instance (open-source ERP spanning finance, procurement, inventory, customer management).
- Agents operate from screenshots only; each task graded against ground-truth data in the database.
- Three graders: Database grader (reads target field values from ERPNext via Frappe REST API), Stage grader (Navigation, Interaction, Commit, Database stages), Log grader (action count, turns, latency, token cost).
- Harness runs in two modes: Deployment (commit/irreversible actions require human approval before execution) and Evaluation (auto-approver approves all actions).
- Six agents evaluated: Claude Sonnet 4.6, Qwen3-VL-32B, OpenCUA-32B, UI-TARS-1.5-7B, OpenCUA-7B, Holo3-35B-A3B.
- Three complexity tiers: T1 (20 single-record tasks: text-edit, select/toggle, create), T2 (multi-field coordination, 6-9 fields per record), T3 (multi-screen chained workflows, 2-4 linked documents).
- Each task executed for 5 independent runs per model per configuration.

## Key Findings
- Claude Sonnet 4.6 achieves 94% (T1), 100% (T2), 100% (T3), approaching human reference.
- Holo3-35B-A3B and Qwen3-VL-32B reach only 34% and 32% on T1, fall to 0–3% on T2 and T3.
- OpenCUA-7B fails every task.
- Some agents save in up to 85% of runs but write the correct value in as few as 3%.
- UI-TARS reaches target in 95% of runs and fires save in 68%, but only 9% leave correct value in database.
- Strong general GUI performance does not translate to enterprise reliability.
- Humans achieve 96–100% on T1, 90–95% on T2, 87–100% on T3.

## Actionable Insights
1. Evaluate agents against database state (state-grounded), not just screenshots. Apply: when building agents for business software, verify target field values in the database after agent execution, don't just trust on-screen success messages. First step: Set up a test database and write a script to check target field values after each agent run.
2. Use a harness with human-in-the-loop approval for risky actions. Apply: commit or irreversible actions (delete records, send payments) must await human approval before execution. First step: Add a user confirmation step before executing any data-write or notification action.
3. Decompose agent runs into stages (Navigation, Interaction, Commit, Database) to localize failures. Apply: when evaluating agents, score each stage separately rather than just overall success/failure. First step: Log each stage of agent execution and categorize failures by stage.

## Assumptions & Limitations
- Evaluated on ERPNext (open-source); results may differ on proprietary ERP systems (SAP, Oracle).
- Only 6 agents evaluated; does not generalize to all CUAs.
- Tasks are synthetic (pre-created); may not represent real-world business tasks.
- Test environment runs in Docker; may differ from production environments.

## Metadata
- Year: 2026, Authors: Kratika Bhagtani, Kusha Sridhar, Maziyar Baran Pouyan, Yuying Zhao, Eugene Siow (Accenture Agentic AI Center of Excellence), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.17885v2