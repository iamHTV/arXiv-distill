# [2610.11899v1] Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent Systems

## Problem
LLMs are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation (RAG), workflow, coding agent, and AI agent. Whether these labels denote genuine architectural forms or serve as branding has not been assessed systematically.

## Contribution
- Describe seven recurring forms of LLM-integrated systems: LLM chats, custom agents, RAG, AI-enhanced workflows, copilots, coding agents, and agentic RAG (in part).
- Each form characterized by four structural dimensions: architectural pattern, control of execution and point of user intervention, number of agent calls per task, and tool use.
- Illustrative corpus of 22 systems from research publications and vendor documentation.

## Method (core summary)
Survey of LLM-integrated systems from research and vendor sources, describing seven forms in a common vocabulary of agents and tools. Each form characterized by architecture, human role, number of agent calls per task, and tools used.

## Key Findings
- Labels carry architectural content, clearest in vendor usage: copilot denotes a router-worker architecture running a host application under step-by-step user confirmation; agent label coincides with AI-planned multi-step execution where user sees only outcome.
- Coding agents from four major providers share one architecture: reason-and-act loop delegating to subagents.

## Actionable Insights
- Don't confuse marketing labels with actual architecture: copilot ≠ agent ≠ workflow. Apply: solopreneur choosing AI tools should look at actual architecture (router-worker, multi-step, etc.) rather than just marketing names.
- Use the common vocabulary (7 forms, 4 structural dimensions) to compare AI tools. Apply: when evaluating AI tools, classify by architecture, number of agent calls, human control, and tools used.

## Assumptions & Limitations
- Based on survey of 22 systems from research and vendor sources; may not cover all systems on the market.
- Paper admits: agentic RAG only described partially.
- Limitation paper doesn't mention: not evaluated on real effectiveness of each form, not tested on many domains beyond software engineering.

## Metadata
- Year: 2026
- Author: Irene Weber (University of Applied Sciences Kempten, Germany)
- arXiv category: cs.AI
- PDF link: https://arxiv.org/pdf/2610.11899
