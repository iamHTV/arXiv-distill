# [2608.24569v2] When "Must" Becomes "Maybe": Erosion of Workflow Constraints in LLM Agent Handoffs

## Problem
LLM agents build on one another's work through summaries, plans, and other intermediate artifacts. These records let a downstream agent continue without revisiting the complete upstream context. We uncover a hidden loss in this process: handoffs can carry tasks forward while eroding judgments already established upstream. A requirement that must be satisfied before action becomes a caveat that the next agent may acknowledge and set aside.

## Contribution
- Uncover erosion of workflow constraints in LLM agent handoffs.
- Find ownership deferral causes 76.7% blocker deactivation; multihop compression causes 97.2%.
- Monitoring the full blocker description raises recognition from 6.2% to 99.2% and reduces forbidden action from 85.2% to 0.0%.
- Authorization-check prompt reduces forbidden action to 1.6%.

## Method (core summary)
Study handoff between LLM agents via intermediate artifacts. Measure blocker deactivation, forbidden action, recognition. Test interventions: full blocker description, authorization-check prompt, full insertion, repair, stop label.

## Key Findings
- Ownership deferral: 76.7% blocker deactivation, 60.8% forbidden action.
- Multihop compression: 97.2% blocker deactivation, 31.9% forbidden action.
- Normal handoff: 100.0% deactivation, 54.2% forbidden action.
- Full blocker description: recognition 6.2% → 99.2%, forbidden action 85.2% → 0.0%.
- Authorization-check prompt: forbidden action 85.2% → 1.6%.
- Full insertion: blocker recognition 6.2% → 99.2%, forbidden action 85.2% → 0.0%.
- Schema-preserving compression: 27.8% deactivation, no forbidden actions.
- Light summarization: 25.0% deactivation, forbidden action 0.0%.

## Actionable Insights
- Don't let downstream agent decide whether a "must" requirement must be satisfied: write full blocker description in intermediate artifact. Apply: solopreneur building agent pipeline should require upstream agent to clearly record must-satisfy constraints, not let downstream agent skip them.
- Use authorization-check prompt to reduce forbidden action from 85.2% to 1.6%. Apply: when building agent pipeline, add authorization check before executing important actions.
- Use full insertion (insert full blocker info) instead of light summarization to keep constraints. Apply: when handing off tasks between agents, transfer full blocker information, not just summary.

## Assumptions & Limitations
- Requires multi-step agent pipeline with handoffs; doesn't apply if only single agent.
- Paper admits: evaluated on specific tasks; may differ on other tasks.
- Limitation paper doesn't mention: not evaluated on many domains beyond tasks used, not tested on real intervention cost.

## Metadata
- Year: 2026
- Authors: Yiheng Sun, Huifei Wang, Yancheng Zhu, Zhenyu Li, Zebin Zhao, Yifan Yuan (Shenzhen University)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2608.24569
