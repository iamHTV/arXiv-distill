# [2610.00905v1] Understanding Issues, Causes and Solutions in Open-Source LLM-based Multi-Agent Systems

## Problem
With the advancement of LLM-based multi-agent systems (MAS), an increasing number of open-source projects emerge, but there is no systematic study of issues, causes, and solutions in these projects.

## Contribution
- Analyze 944 issues from open-source MAS projects.
- Classify 17 issue categories, with Orchestration & Execution Issue at 22.0% (most frequent).
- Identify 540 causes from 57.2% of 944 issues, classified into 14 cause categories.
- Identify 427 solutions, addressing 45.2% of 944 issues, classified into 10 solution categories.

## Method (core summary)
Collect 944 issues from open-source MAS projects (AutoGen, etc.). Classify issues into 17 categories. Extract causes from 57.2% of issues, classified into 14 cause categories. Extract 427 solutions from 45.2% of issues, classified into 10 solution categories.

## Key Findings
- Orchestration & Execution Issue: 22.0% (most frequent issue).
- Memory & State Management Issue: 14.7%.
- Feature Request: 13.2%.
- Implementation Issue: 10.6%.
- Tool Issue: 9.2%.
- Integration Issue: 6.7%.
- Other categories each under 10%.
- Workflow Problem (WP): 29.4% (most frequent cause).
- Tool Integration Problem (TIP): 11.7%.
- Memory Problem (MP): 11.1%.
- 427 solutions, addressing 45.2% of 944 issues.
- Optimize Workflow (OW): 26.0% (most frequent solution).
- Adjust Configuration (AC): 15.0%.
- Optimize Tool Integration (OTI): 11.9%.
- Optimize Infrastructure (OI): 11.0%.
- Documentation Issue has highest resolution rate (76.9%), Output Issue lowest (24.1%).

## Actionable Insights
- The biggest problem in MAS is orchestration & execution (coordination and execution), at 22.0%. Apply: solopreneur building MAS should invest in execution flow and coordination between agents, not just individual agents.
- The most common cause is Workflow Problem (29.4%). Apply: when debugging MAS, check the workflow first, not jump directly into individual agent code.
- The most common solution is Optimize Workflow (26.0%). Apply: optimizing MAS workflow will solve most problems, no need for big architecture changes.
- Documentation Issue has highest resolution rate (76.9%), Output Issue lowest (24.1%). Apply: investing in documentation helps solve problems faster.

## Assumptions & Limitations
- Based on 944 issues from specific open-source MAS projects; may not represent all projects.
- Paper admits: automated filtering approach achieved 90.4% agreement rate, 48 disagreements reviewed again.
- Limitation paper doesn't mention: not evaluated on proprietary (non-open-source) MAS projects, not tested on many domains beyond software engineering.

## Metadata
- Year: 2026
- Authors: Asad Ur Rehman, Syed Mohammad Kashif, Ruiyin Li, Peng Liang, Zengyang Li, Arif Ali Khan (Wuhan University, Central China Normal University, University of Oulu)
- arXiv category: cs.AI, cs.SE
- PDF link: https://arxiv.org/pdf/2610.00905
