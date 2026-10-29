# Skill: oa-rag-grounded-answer (ontology-grounded answering)
Source: 2610.36335
Type: framework / workflow

## When to use this skill
- Building a domain-specific Q&A bot or AI agent where answers must be faithful to a knowledge base — e.g. product FAQ, internal policy lookup, customer support.
- The domain already has structured data (an ontology, a knowledge graph, or a clear relational schema) and hallucination must be controlled.
- Do NOT use: open-domain chat with no knowledge base; domains with no ontology/schema to query; free-form document summarization with no need for formal verification.

## Inputs required
- A structured knowledge base: an OWL ontology or equivalent (entities, relations, axioms such as A ⊑ ∃r.B), or something exportable as concept cards.
- A SPARQL query endpoint or a reasoner that can check entailment, or a code-based simulation of both (exact matching + graph traversal).
- LLM access plus a ReAct interaction budget: the paper uses ~5.8 LLM calls per question; an 8,192-token context window suffices.
- The list of questions to answer.

## Steps
1. Pre-tool draft: prompt the LLM to answer using ONLY the input context and parametric knowledge; keep it as draft y-tilde. If the context suffices, skip ontology use and save cost.
2. Build concept cards for every ontology entity: fixed-order key:value record — name, definition, parents (inferred direct), children (inferred direct), stated relations ("r -> B"), comments, annotations. This is the text-based retrieval unit.
3. ReAct loop — one action per turn, each action a SPARQL query:
   - DESCRIBE "A": fetch A's concept card.
   - ASK {"A" "r" "B"}: check whether O |= A ⊑ ∃r.B is entailed by the reasoner → "ENTAILED" / "NOT ENTAILED". The prompt MUST warn about the open-world assumption: NOT ENTAILED does not mean false.
   - SELECT ?x WHERE {conditions}: retrieve entities/relations satisfying conditions.
   - Query fallback: empty SELECT → compare the question against concept cards with BM25, return top-k candidates for the agent to DESCRIBE next.
   - Name linking: exact match after normalization (case/whitespace/underscore) → ambiguous (return candidate list for disambiguation) → unknown-name fallback (BM25 pool of 200 names reranked by string similarity, top-5 suggestions so the agent can repair the query).
   Stop when a final answer is produced or the interaction budget is exhausted.
4. Filter observations: drop observations from failed tool calls, execution errors, or empty SELECTs → evidence digest E.
5. Answer: if E is non-empty → prompt P_fin with question + E + draft; if E is empty → prompt P_own answering from parametric knowledge.
6. Attribution turn: continue the same conversation with prompt P_att asking the LLM to (a) select cited evidence C-hat ⊆ E and (b) assign a grounding level g-hat: entailed / supported / related / unrelated. Output all three: answer + C-hat + g-hat.

## Expected output
- A final answer with cited ontology evidence (C-hat) and a 4-level grounding level (g-hat).
- An actionable reliability report: auto-publish entailed/supported answers; route related/unrelated to human review.
- Verified consequence from the paper: stronger grounding correlates with higher accuracy (Qwen Test 3: entailed 94.9% correct, supported 82.1%, remaining 72.1%).

## Example application
- Product advisor bot for an online shop. Customer asks: "Can laptop X handle 4K video editing?" Step 1 drafts "probably yes" from general knowledge. Step 3 DESCRIBE "laptop X" returns a concept card with stated relation "target use -> video editing 4K", and ASK {"laptop X" "target use" "video editing 4K"} returns ENTAILED. Steps 5–6 answer "Yes, laptop X is listed by the manufacturer for 4K video editing", grounding=entailed, citing the evidence card → publish without human review.

## Gotchas
- ASK "NOT ENTAILED" does NOT mean the statement is false (open-world assumption) — the agent prompt must instruct the LLM about this, otherwise the agent will deny correct statements.
- The grounding level is the LLM's self-assessment, NOT a formal guarantee of correctness — still sample-audit by humans.
- Retrieval is the main bottleneck: fully retrieved gold evidence is 23.6% for open questions vs 61.7% for MCQs. Questions without option cues need more DESCRIBE turns plus BM25 fallback.
- Definition-heavy information is poorly accessible to exact SPARQL — Test 2 open questions are the hardest case; put informal annotations (definitions, synonyms) into concept cards, don't rely on axioms alone.
- Ontology coverage sets the limit: questions outside the ontology vocabulary get unrelated grounding — don't force answers from evidence.
- Cap the interaction budget — the paper uses ~5.8 calls per question; unlimited loops waste tokens.
