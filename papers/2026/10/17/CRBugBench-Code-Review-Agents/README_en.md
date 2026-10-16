# 2610.13668 — (When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection

## Problem
- Human review velocity cannot keep up with agentic code generation, tempting a "lights-off software factory" (AI writes AND reviews, no human). Existing benchmarks treat human comments as ground truth — a poor proxy: arbitrary nitpicking accepted via social dynamics, or too narrow to capture valid AI findings.

## Contribution
- CRBugBench: bug-grounded code review benchmark — 1,800 tasks (1,000 across 98 GitHub OSS repos + 800 proprietary industry repos at one large company), 5 languages. Pipeline: (1) bugs from addressed human comments in PR discussions (caught before merge); (2) bugs from human-submitted bug-fix PRs traced back to the introducing PR (escaped after merge).
- Evaluation protocol: agent gets a sandboxed repo at the introducing commit, explores/experiments, writes review.md self-ranked by severity; an LLM judge panel matches each finding to the ground-truth bug.

## Method
- Measures recall@5 (bugs caught within top-5 comments) across models/harnesses; logistic regression on repo/PR/bug features (RQ2); trajectory analysis (RQ3); design-choice ablations (RQ4: prompts, multi-agent, reasoning effort).

## Key Findings
- Best agent (claude-opus-5 + copilot-cli) catches 71.9% of bugs within top-5; rose from 47.7% (opus-4.6) to 71.9% (opus-5) in 5 months (Feb→Jul 2026). Opus-5-xhigh: 79.6% of pre-merge-caught bugs, 64.2% of post-merge-escaped bugs.
- Agents still miss 20%+ of human-found bugs → human-in-the-loop remains necessary. Proprietary repos: drop up to 25.5% — bugs need project context, not inferrable from diffs.
- RQ2: weaker on larger/heterogeneous PRs, bug-fixing PRs, non-functional/low-severity bugs, bugs requiring non-local reasoning.
- RQ3: agents spend most turns reading/searching, rarely execute (opus-5: 9.7% of turns; gpt-5.6-sol: 6.9%); half of opus-5 runs end by turn 35 vs turn 17 (gpt-5.6-sol); agents trust misleading PR descriptions and miss repository-wide behavior + external library semantics.
- RQ4: exploration-nudging prompts +5.8% (1.10× cost); multi-agents +4.7% (5.55× cost); reasoning effort 36%→57% (23.22× cost). Pareto front: gpt-5.6-luna for cheap, opus-4.8/5 for performance.

## Actionable Insights
- Scale review effort to PR complexity: small homogeneous PRs → cheap configs; large heterogeneous PRs → stronger models + higher reasoning + human review; split unrelated changes into smaller PRs.
- Steer agents with custom instructions by priority (usability, portability, backward compatibility, maintainability) — by default agents focus on severe functional bugs.
- Feed repository knowledge when reviewing proprietary/large repos — project-context bugs are where agents are weakest (-25.5%).

## Assumptions & Limitations
- Benchmark measures bug-finding (objective), not subjective/domain-specific review aspects — humans retain project values + maintainability.
- Proprietary portion from a single company; recall@5 may overstate if only the top comment is checked.
- Not stated: the LLM judge panel may miss differently-phrased findings; fast model evolution dates the numbers quickly.

## Metadata
- 2026, Chenyang Yang (CMU), Hao He, Ti-Chung Cheng, Jenna Butler, Emerson Murphy-Hill, Carmen Badea, Christian Bird (Microsoft/Microsoft Research), cs.SE, https://arxiv.org/pdf/2610.13668
