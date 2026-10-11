# Skill: LDKE Knowledge Editing
Source: 2605.29826
Type: framework

## When to use this skill

- When needing to update specific facts in LLM/MLLM without retraining
- When edits need to generalize to related queries
- When preserving unrelated knowledge is critical

- Do NOT use when: wholesale update needed; no gradient access; too many edits for batch

## Input needed

- LLM/MLLM with gradient access
- Fact to edit (old → new)
- Related queries for propagation testing
- Unrelated queries for locality testing

## Steps

1. **Fast Localization** — Gradient-based attribution identifies critical layers (top-K, typically 2-5).
2. **Disentanglement Classification** — Route relevant inputs through edited pathway, irrelevant through original.
3. **Targeted Layer Update** — Update only critical layers, minimize interference.
4. **Propagation Testing** — Verify edits generalize to related queries.
5. **Locality Testing** — Verify unrelated knowledge preserved.

## Expected output

- High propagation rate
- High locality
- Efficient localization

## Example application

Company CEO change: localize layers → update → test propagation ("Who runs X?") → test locality (other facts unchanged).

## Gotchas

- Layer localization may not be exact
- Disentanglement boundary ambiguous for semi-related facts
- Edits may cascade unexpectedly
- Gradient attribution quality varies
