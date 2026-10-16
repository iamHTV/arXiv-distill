# Skill: self-evolving-multi-agent-translation
Source: 2609.38660v2
Type: workflow

## When to use this skill
- Translating long content (movie subtitles, educational videos, multi-page documents) that needs consistent terminology and style.
- Have multiple episodes/parts in the same series to accumulate context.
- Want to update translation prompts continuously without retraining the model.

## When NOT to use
- Translating single sentences or short passages without long-range context.
- No related content in the same series to accumulate memory.

## Required input
- Source content to translate (subtitles, videos, documents).
- List of target locales (languages) to translate into.
- A judge-refiner system that can score translation quality and suggest prompt edits.
- Glossary and style from previous episodes (if available).

## Steps
1. Split long content into overlapping windows of 5, 10, 20 sentences with 50% overlap.
2. Use the multi-agent SMART system with dynamic router to select the right translator agent for each segment.
3. After each segment is translated, let judge-refiner score quality and update the translation prompt based on detected errors (no retraining).
4. Accumulate series-level memory: save translated terminology and style into a glossary for subsequent segments.
5. First 30% of content used for test-time training (prompt adjustment), remaining 70% for held-out evaluation.
6. Repeat for subsequent episodes, using the refined glossary and prompt from previous sets.

## Expected output
- Reduce average penalty 6.9% vs strongest agent system on Subtitle Arena.
- Maintain terminology and style consistency across multiple episodes.

## Example application
Solopreneur translates a software tutorial video series into 15 languages. Use SMART to translate each segment, then judge-refiner scores and refines the translation prompt after each segment. Save software terminology into a glossary used for all videos in the series. Translation quality stays consistent without retraining the model for new series.

## Gotchas
- Only effective when there is related content in the same series to accumulate memory.
- Not effective for single-sentence or short-passage translation.
- Default backbone is Claude Sonnet 4.6; effectiveness on other models unknown.
