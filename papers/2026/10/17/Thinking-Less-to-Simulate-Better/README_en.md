# [2609.30563v1] Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content

## Problem
- Platform policies are increasingly tested on artificial users, making agent fidelity important. However, convincing fake profiles could also manipulate perceived public opinion before elections. Validation has concentrated on agreement with human behaviour and has paid little attention to whether an agent behaves in line with the profile it was given.

## Contribution
- Study profiled eight Serbian participants through a questionnaire, a deep interview, and a written self-presentation, recorded their reactions to sixty-eight social media posts, and asked four language models to predict those reactions under five prompt conditions varying profile content and instruction style.
- Attitudinal content improved prediction over demographic backstories by a wide margin. Agents matched their stated profiles more closely than participants matched their own survey answers, and consistency proved unrelated to fidelity once profile information was present.
- Instructing models to respond intuitively and immediately rather than analytically gave the highest fidelity of any condition and cut the compression of individual differences from seven times the human level to three.

## Method (core summary)
- The study combines a small qualitative panel with a factorial computational experiment. Participants were profiled in depth and recorded their own reactions to a fixed set of social media posts, after which four language models predicted those same reactions under five prompt conditions.
- Eight adults living in Serbia took part. Ages ranged from 22 to 53 years with a mean of 31.0, and the panel included five women and three men.
- Sixty-eight posts in Serbian formed the stimulus set. Thirty-four posts address topics covered by the questionnaire and thirty-four address topics the questionnaire never raised, allowing in-domain and out-of-domain prediction to be separated.
- Four language models: Claude Sonnet 5, DeepSeek Instant, GPT 5.6 Terra, Grok Fast. Every model received every participant profile under five prompt conditions, and each prompt asked for a like or dislike judgment on all sixty-eight posts returned in a fixed comma-separated format.
- Five conditions: V4 demographics (age, gender, education, employment status, city of residence); V3 questionnaire (adds full questionnaire including trust battery, personality items, activity list, and political self-placement); V1 interview (adds interview transcript and free-text self-presentation — the richest profile); V2 inference (same content as V1 plus instruction to infer reactions from combinations of characteristics when a directly relevant attribute was absent); V5 intuitive (same content as V1 but instructed to respond immediately rather than analytically, to avoid weighing characteristics against one another, and to accept that some reactions would sit at odds with the stated profile).
- The design produced twenty configurations and 10,880 predicted reactions.
- Fidelity is agreement between an agent's prediction and the participant's actual reaction. Matthews correlation coefficient (MCC) is the primary measure.

## Key Findings
- 6 authors from various institutions, arXiv categories: cs.AI, cs.CL, cs.HC, cs.MA, cs.SI.
- Every one of the twenty configurations predicted individual reactions above chance, with MCC ranging from 0.275 (Claude Sonnet 5 given demographics alone) to 0.511 (Grok Fast under interview and intuitive conditions).
- Fidelity climbs from demographics condition to questionnaire condition, gains a little more from interview material, stays flat when inference instruction is added, and reaches its highest value under intuitive framing.
- V4 demographics: MCC 0.300; V3 questionnaire: MCC 0.406; V1 interview: MCC 0.434; V2 inference: MCC 0.434; V5 intuitive: MCC 0.473 (highest).
- Compression of individual differences: demographics 10.24×, questionnaire 7.54×, interview 7.14×, inference 7.88×, intuitive 3.14×, human 1.00×.
- The inference instruction failed to improve fidelity. Mean performance under that condition matched the interview condition exactly at 0.434, while profile-consistency rose from 0.754 to 0.826.
- Instructing models to respond immediately rather than analytically produced the highest mean fidelity of any condition and the best result for three models out of four.

## Actionable Insights
1. Attitudinal content improves prediction over demographic backstories. Application: when building user simulation agents, collect attitudinal content (beliefs, values, opinions) instead of only demographic information.
2. Instructing agents to respond immediately rather than analytically (intuitive prompting) gives highest fidelity. Application: tell agents "respond immediately, don't weigh characteristics against each other" when simulating user reactions on social media.

## Assumptions & Limitations
- Eight participants support statements about what happens within a rich-profile design. Claims about population parameters would need a different study.
- Model-level tests across four models cannot reach conventional significance under a Wilcoxon procedure; evidence for differences between conditions rests on item-level comparisons treating the 544 agent-post cells as observations.
- All participants live in Serbia, while the models tested are known to represent wealthy Western publics more accurately. Performance reported here may understate what the same designs would achieve elsewhere.
- Each configuration was run once, reactions were reduced to a binary choice, and two models were excluded because their outputs were incomplete.

## Metadata
- Year: 2026, authors: Ljubisa Bojic, Tijana Stanic, Jörg Matthes, Agariadne Dwinggo Samala, Bojana Dinic, Jue Wang, arXiv categories: cs.AI, cs.CL, cs.HC, cs.MA, cs.SI, PDF link: https://arxiv.org/pdf/2609.30563v1
