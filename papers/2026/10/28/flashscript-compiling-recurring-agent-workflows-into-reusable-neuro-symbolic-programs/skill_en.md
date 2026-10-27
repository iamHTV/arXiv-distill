# Skill: flashscript-nsp-compilation
Source: 2610.33876v1
Type: workflow

## When to use this skill
- You have a recurring agent task (weekly report, order processing, data analysis...) and want subsequent runs to be identical.
- Want to reduce inference cost (input tokens) and runtime of the agent on recurring work.
- Want testable, maintainable, reusable software instead of just saving a skill or memory.

## When NOT to use this skill
- Work that does not recur (each time completely different).
- When consistency is not needed (creative chatbot, free-form writing).

## Required inputs
- One successful agent run (trajectory) on the recurring task.
- FlashScript guidance (prompt template, tool descriptions, same agent trajectory used to write the skill).
- A coding agent (e.g., Claude Code) to write the NSP from guidance.
- An LLM to perform the llm<T> calls in the NSP.

## Steps to perform
1. Run the agent on the recurring task once successfully, record the full trajectory (reasoning + actions).
2. Write the NSP from the trajectory: actions become code, instance-specific values become parameters, each decision needing model judgment becomes a typed llm<T> call with declared return type.
3. Identify the three layers of model calls: input (unstructured text → typed value), computation (semantic decisions), output (render results in natural language).
4. Apply three techniques to reduce model calls: caching (store observed values, check condition before reusing), codify (replace repeated judgment with heuristic rule), clubbing (group independent questions into one call or run in parallel).
5. Bound each neural call: NSP selects inputs, checks response type, makes call at fixed point in code.
6. Run the NSP on each recurrence of the task, calling the model only when judgment is truly needed.

## Expected output
- NSP runs identically every time (same tools, same output).
- ~70× fewer input tokens vs skill-guided agent.
- ~1/3 runtime.
- Generalizes to unseen instances of the same template.

## Example application
An office worker has an agent that updates LA rental listings and flags scams every week. Previous run: agent inferred "LA" = Los Angeles, selected the corresponding sheet, fetched new listings, flagged listings requesting money transfer before first visit, summarized changes. Compiled to NSP: SHEETS = {'LA': 'Los Angeles'}, def rental_report(wb, city='LA'): name = SHEETS.get(city) or llm<wb.sheets>(city), new = fetch_merge(wb[name], SOURCES[name]), changes = diff(wb[name], new), scams = [r for r in new.rows if llm<bool>(f"Is this a scam? {r}")], wb[name] = highlight(new, changes, scams), return llm<str>(f"Summarize: {changes}"). Next run: run the NSP, identical to previous, using fewer tokens.

## Gotchas
- NSP does not remove nondeterminism, only localizes it — LLM calls can still vary output but only within bounded scope.
- Generalization depends on how many decisions are left for model calls: delegating more handles more variation but reduces consistency and efficiency.
- Needs a coding agent to write NSP from FlashScript guidance — not fully automatic yet.
- Caching only works for observed values (already seen in a previous run), not for new unseen values.