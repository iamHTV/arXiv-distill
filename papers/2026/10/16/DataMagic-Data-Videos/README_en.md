# [2609.33403v1] DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration

## Problem
Data videos communicate data insights through dynamic charts, voice narration, and synchronized animations, and have become a widely adopted form of data storytelling. However, their production requires multidisciplinary expertise spanning data analysis, narrative design, and video editing. Static visualization tools lack narrative and animation capabilities; authoring tools rely on pre-prepared charts rather than raw data; and pixel-level generation models, while capable of end-to-end synthesis, cannot guarantee...

## Contribution
- Introduce DataMagic: a declarative multi-agent system for authoring data videos.
- DataMagic improves quality to 3.89 (+83%) with success rates above 95%, compared to direct generation methods that achieve only 2.13/5 with execution success rates between 48.62% and 86.24%.
- DataMagic significantly improves creation efficiency (79.7% reduction in task time) and reduces perceived cognitive load.
- Animation scores increase from 1.84 to 4.03 (+120%); Narrative scores improve from 2.00 to 3.43 (+72%); Intent and Aesthetic dimensions improve by more than 50%; Insight improves by 49.5%.
- DeepSeek-V3.2 improves its execution rate from 48.62% to 96.33%.

## Method (core summary)
DataMagic is a declarative multi-agent system for authoring data videos. Agents are responsible for different roles (planner, coordinator, etc.) and orchestrate the creation of data videos. The system uses declarative specification to structure the data video.

## Key Findings
- Direct generation methods: 2.13/5 quality, execution success 48.62%–86.24%.
- DataMagic: 3.89/5 quality (+83%), execution success rates above 95%.
- Creation efficiency: 79.7% reduction in task time (39.2 → 8.0 minutes).
- Animation: 1.84 → 4.03 (+120%); Narrative: 2.00 → 3.43 (+72%); Intent and Aesthetic: >50%; Insight: +49.5%.
- DeepSeek-V3.2: execution rate 48.62% → 96.33%.

## Actionable Insights
- Use declarative multi-agent system for authoring data videos instead of static visualization tools or chart-based authoring tools. Apply: solopreneur making data videos should use DataMagic to automate the video creation process, reducing time and cost.
- Separate planning and orchestration to stabilize execution rate above 95%. Apply: when building agent-based video creation system, use planner agent and coordinator agent to ensure stability.

## Assumptions & Limitations
- Requires raw data to create data videos; doesn't apply without data.
- Paper admits: evaluated on user study with a certain number of users; may differ on other datasets.
- Limitation paper doesn't mention: not evaluated on many domains beyond numerical data, not tested on real cost of multi-agent system.

## Metadata
- Year: 2026
- Authors: Yupeng Xie, Zhenyang Wang, Liangwei Wang, Jiayi Zhu, Zhouan Shen, Yuyu Luo
- arXiv category: cs.HC
- PDF link: https://arxiv.org/pdf/2609.33403
