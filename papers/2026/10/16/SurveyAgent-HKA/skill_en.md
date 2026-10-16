# Skill: surveyagent-hka-scientific-survey
Source: 2609.05938v1
Type: framework

## When to use this skill
- Generating scientific surveys or resource documents using LLM.
- Want to improve survey quality by combining human knowledge (human knowledge augmentation).
- Have reference documents and want to create well-structured surveys.

## When NOT to use
- No reference documents to generate surveys from.
- Don't need structured surveys, only need short summaries.

## Required input
- Scientific reference documents (papers, reports, etc.).
- Human knowledge to augment (e.g. expert review and editing).
- An LLM system that can generate surveys.

## Steps
1. Collect reference documents related to the survey topic.
2. Use LLM to generate survey draft (outline, section content).
3. Combine human knowledge: experts review, edit, and supplement content (human knowledge augmentation).
4. Apply components like citation expansion, re-ranking, clustering, few-shot learning to improve quality.
5. Evaluate survey quality (citation quality, key-point recall, heading match).

## Expected output
- Citation quality: CS (14.95% P, 19.53% R, 16.94% F1), Medicine (16.78% P, 22.95% R, 19.39% F1).
- Key-point recall: 53.85% (CS), 57.07% (medicine).
- With human augmentation: citation F1 increases 3.86% (CS), +2.62% (Medicine).

## Example application
Solopreneur writing a survey on "AI in healthcare": collect related papers, use LLM to generate survey draft, then have medical experts review and edit (human augmentation). Combine citation expansion and re-ranking to improve citation quality and survey structure.

## Gotchas
- Need enough reference documents and human knowledge for augmentation to be effective.
- Components like citation expansion, re-ranking, clustering, few-shot learning are all important, don't skip them.
- Real cost of human augmentation not yet evaluated.
