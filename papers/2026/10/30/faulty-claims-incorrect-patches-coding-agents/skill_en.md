# Skill: cot-claim-audit (claim-level CoT audit for coding agents)
Source: 2610.32338
Type: evaluation-method / workflow

## When to use this skill
- Reviewing (checking) a patch produced by a coding agent BEFORE merge — especially complex tasks (SWE-bench Pro-like: patches of hundreds of lines, multiple potential defects).
- Building monitoring or a checkpoint for a coding-agent pipeline: verify the claims the agent believes before it submits a patch.
- Post-hoc audit: a patch passes tests but its behavior is suspect — a plausible patch.
- Do NOT use: the model does not expose its native CoT (chain of thought) — closed models degrade to agent-framework thoughts with far less detail; no access to the repository at its base commit + task statement + library docs to verify against.

## Inputs required
- The coding agent's trajectory with per-step native CoT (open-weight reasoning models: DeepSeek, Qwen, ...), or recorded thoughts from the agent framework.
- The repository at the task's base commit (to verify claims about the original implementation).
- The original task statement.
- Access to library documentation for claims about dependencies/APIs.
- The validation test suite plus the ability to run execution probes and targeted tests.

## Steps
1. **Extract claims:** for each CoT step, extract reasoning units — the smallest self-contained proposition that can be independently judged true/false — with a verbatim quote from the CoT and the referenced files. Classify each unit: O (original implementation — code/library behavior or structure), G (implementation gap — what the code lacks vs the requirement), S (semantic constraint — what the task requires), F (fix mechanism — whether the proposed mechanism satisfies the requirement). Drop non-checkable content (navigation, editing intentions, test status).
2. **Verify claims:** judge each unit supported / refuted / unresolved with gathered evidence: O → trace actual code behavior; G → compare implementation against requirement; S → reconstruct the requirement from the task statement and find a distinguishing input; F → search for a counterexample under the claim's conditions. Attach a citation to every judgment (file+line, doc excerpt). Refuted = faulty claim. Record quotes — a judgment whose quote is not in the CoT is discarded.
3. **Prioritize key faulty claims:** keep ONLY refuted claims that the final patch still builds on (check: does the patch depend on the claim? did later evidence revise it?). Discard the rest — 96.7% of PASSING trajectories contain faulty claims (presence is a weak signal); only ~1 in 26 faulty claims is key. Expected yield: ~1 key claim per failing trajectory.
4. **Correct before submission:** send a correction message to the agent right before submission, stating the refuted claim + evidence citation + instruction to revise the patch. Verify the agent produces the targeted fix — expect a small focused edit: median 13 lines changed (vs median 101 original), ~17 extra steps. Newer models follow corrections more reliably (100% of replays for Flash/Qwen3.8 vs 77–87% for older models).
5. **Anti-pattern scan:** flag hedged claims ("Probably exact", "likely", "should be") and shortcut statements ("tests won't check", "only needs to pass validation") in the reasoning → queue the patch for human review EVEN IF tests pass — these signal the agent narrowed the task to what is tested.
6. **Targeted verification after the fix:** run targeted tests for the behavior the faulty claim referenced plus execution probes (real function calls with distinguishing inputs) — do NOT trust the validation suite: 129 of 162 replays fix the defect but tests do not show it (tests do not exercise the fixed behavior). Check requirement scope: two thirds of faulty S claims are scope errors (overgeneralization/omission).

## Expected output
- A per-claim verdict table: claim quote, type O/G/S/F, verdict supported/refuted/unresolved, evidence citation.
- The list of key faulty claims + correction messages sent + the revised patch (with targeted fix, median ~13 lines).
- A flag list of anti-patterns (hedged/shortcut statements) needing human review.
- Verified real numbers: corrections fix the linked defect in 89.0% (162/182); pass more tests 18.7%; additionally resolve 11.5% (single claim) — 40.4% pass more tests and 21.3% resolve when ALL key claims of a trajectory are corrected in one message; resolution rises 53.0%→58.5% on average across the four models.

## Example application
- An agent fixes a shop checkout bug: CoT claim O "cart.total() already applies the discount" → Step 2 reads cart.py: total() has no discount logic → refuted, citation cart.py L40-58. Step 3: the new patch's fee calculation calls total() → the patch builds on the claim → KEY. Step 4: correction "total() does not apply the discount — the fee must add the discount explicitly" → agent revises 13 lines, targeted fix present. Step 5: scan finds "probably the tax module handles rounding" → flag for review. Step 6: targeted discount-fee test passes + probe on a legacy cart confirms. Merge safely.

## Gotchas
- The faulty-claim COUNT is a weak indicator: unresolved trajectories have more faulty claims mainly because they have more claims overall (1.97× faulty but 1.62× units); the error rate is only 0.9–2.1 points higher; 96.7% of resolved trajectories still contain faulty claims. Do not conclude "many faulty claims = broken agent".
- Verification must check BEHAVIOR, not identifiers: 53.3% of errors are misstatements (wrong behavior), only 11.3% misreferences (wrong object) — every object in a claim exists and the claim looks plausible; only tracing the code reveals it is wrong.
- The 9.6% error rate is a LOWER BOUND: assessment precision 86.3%, recall unchecked — the real rate may be higher; the assessment agent buries each key claim among ~26 other faulty claims, so Step 3 (prioritization) is mandatory — never dump all faulty claims to the agent (noise).
- Correction does not guarantee resolution: defect fixed 89% but resolved only 11.5% — other defects remain or tests miss the fixed behavior. Multi-claim trajectories: correcting ALL key claims in ONE message (40.4% pass more tests, 21.3% resolve) beats piecemeal corrections (8.8% resolve).
- Closed-model limitation: commercial models hide the native CoT → the skill degrades (framework thoughts are short, claim-poor). Combine with step-level monitoring (repeated actions, untested fixes) instead.
- About 1/3 of failing patches have NO faulty claim in the reasoning (defects arise during editing: wrong hunk line counts, moved-but-not-added functions) → claim audit does not replace code review; add a reasoning-vs-edits consistency check (trace each hunk back to the claim that motivated it).
