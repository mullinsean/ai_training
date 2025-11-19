# AI Adoption Training Program

Welcome to the AI Adoption Training materials repository! This five-workshop series is designed to help you understand and effectively use Large Language Models (LLMs) and AI tools in your work.

## 📚 Workshop Series Overview

This training program consists of five workshops scheduled over six weeks:

1. **Workshop 1**: Introduction to LLMs & Context Engineering *(2 hours)*
2. **Workshop 2**: AI for Writing, Analysis & Communications *(1 hour)*
3. **Workshop 3**: AI for Operational Excellence *(1 hour)*
4. **Workshop 4**: AI for Advanced Research Techniques *(1 hour)*
5. **Workshop 5**: Advanced AI Topics — Coding, Models & Agents *(1 hour)*

**Recommendation**: Join Workshop 1 to build foundational knowledge, then select additional workshops based on your interests and work needs.

---

## 📊 Workshop Materials

### Workshop 1: Introduction to LLMs & Context Engineering
**Date**: October 29, 2025

**Topics Covered**:
- How LLMs work: tokens, model knowledge, context windows, and tool calls
- Thinking models vs. fast models
- Strengths and limitations of LLMs
- Handling hallucinations and building confidence
- The art of prompting: roles, tasks, formats, and constraints
- Context window management techniques
- Best practices for building prompt libraries

**Materials**:
- [Download slide deck](./slide_deck/AI%20Training%20-%20Workshop%201%20-%20TA%20-%202025.10.29.pdf?raw=1)

**Examples**:

| # | Description | Model | Supporting Files |
|---|-------------|-------|------------------|
| 1 | [Knowledge cutoff date](https://claude.ai/share/41b9c015-70f5-4d0c-a1b6-1a06b1652622) | Claude Sonnet 4.5 | |
| 2 | [Speech summary (simple)](https://claude.ai/share/bf761bf1-82ad-4f7a-8cd1-9e1bea823073) | Claude Sonnet 4.5 | |
| 3 | [Speech summary (with generated prompt)](https://claude.ai/share/00762401-0402-4005-b28a-c2e640ee6b83) | Claude Sonnet 4.5 | |
| 4 | [Generating a prompt for summarizing a speech](https://claude.ai/share/42ed94b9-8091-4a4c-ab88-ccdc1aa17651) | Claude Sonnet 4.5 | |
| 5 | [Generating project proposal from data + template](https://gemini.google.com/share/0311815fbafc) | Gemini Pro 2.5 | [file 1](./examples/workshop1/Project%20Backyard%20Fusion%20-%20Project%20Proposal.pdf?raw=1), [file 2](./examples/workshop1/2-Sample-Briefing-Note.pdf?raw=1) |

### Workshop 2: AI for Writing, Analysis & Communications
**Date**: November 14, 2025 @ 2pm EST

**Topics Covered**:
- Using AI for professional writing and editing
- Content analysis and summarization
- Communications strategy and messaging
- Document transformation and formatting

**Materials**:
- [Download slide deck](./slide_decks/AI%20Adoption%20Training%20-%20Workshop%20%232%20-%202025.11.14.pdf?raw=1)

**Examples**:

#### Writing a Synthesis Memo (Budget 2025 example)

| # | Process Step | Activity | Example |
|---|--------------|----------|---------|
| 1 | Prepare Background Materials | Extract key elements of Budget 2025<br>Conduct media + stakeholder scan | Budget 2025 highlights: [chat](https://claude.ai/share/39130465-8e87-42f3-a497-2d8b83e27e0f), [output](https://claude.ai/public/artifacts/a5d8c616-3960-48ef-83d5-d46243902ac4)<br>Media/stakeholder scan: [chat](https://gemini.google.com/share/1f9039ad51ca), [output](https://docs.google.com/document/d/1cPRbp3oeI-QTctMVzrjaasX6Az3CGWKUwMKHyjc17uw/edit?usp=sharing) |
| 2 | Generate a rough outline of memo | Review and iterate | Rough outline: [chat](https://claude.ai/share/a5c640d2-22a9-44e4-a09e-ecc95cb61615) |
| 3 | Generate an annotated outline of memo | Include data sources, references | Annotated outline: [chat](https://claude.ai/share/84967d15-7596-49f7-8257-120e4a2473d0), [output](https://claude.ai/public/artifacts/b7066444-4193-4a07-86b3-34f5d3b8c7d8) |
| 4 | Generate rough draft of memo | Optional: Apply a template and/or style guide<br>Review and iterate | Rough draft: [chat](https://claude.ai/share/073f3710-9039-4dcc-af6b-fb8973d003c9), [output](https://claude.ai/public/artifacts/67051f83-9aec-467f-970f-f3f0eb78a60e) |
| 5 | Generate final draft of memo | Review, proof-read and iterate | Do this in a word processor! |

#### Generating Additional Documents (Extending the memo)

| # | Document Type | Concept | Example |
|---|---------------|---------|---------|
| 1 | Blog Post | Applying a style guide | Creating a style guide: [chat](https://chatgpt.com/share/691755ed-beec-8001-92e9-ece1fcbd2452)<br>Blog post: [chat](https://claude.ai/share/8a5d3762-d62e-4e6c-beae-b86739598718), [output](https://claude.ai/public/artifacts/d511f07e-13bd-4ece-b6a2-a6077da42ee9) |
| 2 | Social Media Posts | Using examples | Social media posts: [chat](https://claude.ai/share/2ead7529-1d37-4fb5-8ffa-f9cfd7b4f232) |
| 3 | Article for The Economist | Using Claude Skill to apply a style guide | Creating Claude Skill: [chat](https://claude.ai/share/01171078-5c5f-4c65-bb76-0b690cbf6423), [output](https://claude.ai/public/artifacts/ac89f54e-e0f5-4f4a-9a2e-9f0262831298)<br>Writing article: [chat](https://claude.ai/share/466648f2-657a-40c4-a2b2-4ade2442753d), [output](https://claude.ai/public/artifacts/f60fbd48-02be-4868-a9c3-64cab232ba27) |
| 4 | Slide deck | Experimental: testing the [perplexity.ai](https://www.perplexity.ai/) slide deck feature | Slide deck: [chat](https://www.perplexity.ai/search/turn-this-into-a-slide-deck-ou-SUrZ5Im5SK2Uv75.FmTaNg?preview=1), [output](https://www.perplexity.ai/apps/6deb94dd-fca6-49f4-b050-0978dbfb4734) |

### Workshop 3: AI for Operational Excellence
**Date**: November 19, 2025 @ 2pm EST

**Topics Covered**:
- AI for project management workflows
- Connecting to data sources (direct uploads, project files, shared drives, MCP)
- Data and quantitative analysis with Excel
- Productivity techniques (scheduling, image generation, research analysis)
- Enhancing creativity through brainstorming and prototyping

**Materials**:
- [Download slide deck](./slide_decks/AI%20Adoption%20Training%20-%20Workshop%20%233%20-%202025.11.19.pdf?raw=1)

**Examples**:

#### Project Management (Slide 6)
- [Project Overview Example: "Beyond Zero"](./examples/workshop3/Project%20Overview%20Example%20(Beyond%20Zero).pdf?raw=1) - Sample project overview document for context

#### Data Analysis with Excel (Slide 11)
Fuel consumption ratings analysis using [NRCan open data](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64):

| # | Process Step | Activity | Chat Transcript | Outputs |
|---|--------------|----------|-----------------|---------|
| 1 | Explore Data Set | Generate table of average fuel efficiency by manufacturer | [chat](https://claude.ai/share/eb9d0574-4d06-41e2-b646-7b9807ebc057) | [csv](https://claude.ai/public/artifacts/1beaf9e3-ae3c-4570-838a-8eec5c4b8da7), [md](https://claude.ai/public/artifacts/ea5fd518-5e90-4477-b3f1-0bf785679df8) |
| 2 | Build a Model in Excel | Build model that calculates value of fuel efficiency savings between two vehicles | [chat](https://claude.ai/share/eb9d0574-4d06-41e2-b646-7b9807ebc057) | [xlsx](./examples/workshop3/hybrid_breakeven_calculatorv2.xlsx?raw=1) |
| 3 | Investigate Trends | What vehicles have shown biggest increase in fuel efficiency? What was the average increase from introducing a hybrid model? | [chat](https://claude.ai/share/81ac273d-7df3-489c-a29d-684a1630fb4e) | [fuel efficiency xlsx](./examples/workshop3/fuel_economy_analysis.xlsx?raw=1), [hybrid intro xlsx](./examples/workshop3/hybrid_improvements.xlsx?raw=1) |
| 4 | Generating Insights | Ask model to generate insights from the data | [chat](https://claude.ai/share/81ac273d-7df3-489c-a29d-684a1630fb4e) | [md](https://claude.ai/public/artifacts/c990ca4a-383e-4794-9a84-a9d728653e75) |

#### Productivity Techniques (Slides 12-14)
- **Slide 12**: [Scheduling research in ChatGPT](https://chatgpt.com/share/691dcf3f-9234-8001-bedd-beb52d2650f0) - Example of automated weekly macro brief
- **Slide 13**: [Image generation with Gemini 2.5 Flash Image](https://gemini.google.com/app/09fce6860b70c65e) - Example of image editing using text prompts
- **Slide 14**: [NotebookLM for research synthesis](https://notebooklm.google.com/notebook/ea1a2092-36a8-47ee-9727-dfb48baa4293) - Example exploring rapid AI adoption research

### Workshop 4: AI for Advanced Research Techniques
**Date**: December 4, 2025 @ 2pm EST

**Topics Covered**:
- Advanced search and information gathering
- Literature review and synthesis
- Data analysis and visualization
- Research documentation and reporting

**Materials**:
- Slide deck *(Coming soon)*

### Workshop 5: Advanced AI Topics — Coding, Models & Agents
**Date**: December 12, 2025 @ 2pm EST

**Topics Covered**:
- Introduction to coding with AI assistants
- Understanding different model architectures
- AI agents and autonomous systems
- API integration and custom applications

**Materials**:
- Slide deck *(Coming soon)*

---

## 🛠️ Tools You Can Use

Follow along with these LLM platforms:
- [Claude](https://claude.ai) - Anthropic's AI assistant
- [ChatGPT](https://chat.openai.com) - OpenAI's conversational AI
- [Google Gemini](https://gemini.google.com) - Google's multimodal AI
- [Perplexity](https://www.perplexity.ai) - AI-powered search and answer engine

---

## 📖 Additional Resources

### Prompting Guides
- **ChatGPT**: [OpenAI Prompt Engineering Best Practices](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- **Claude**: [Claude Prompt Engineering Guide](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices)
- **Gemini**: [Gemini Prompting Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)

### Use Cases & Examples
- [Claude Use Cases](https://claude.com/resources/use-cases) - Real-world examples and applications
- [ChatGPT for Government: Prompt-Pack for Leaders (OpenAI Academy)](https://academy.openai.com/home/blogs/government-prompt-pack-for-leaders) - Practical prompts for government leaders

### Project Management & Operational Excellence
- [AI Use Cases in Project Management](https://thedigitalprojectmanager.com/project-management/ai-use-cases-in-project-management/) - Comprehensive guide to AI applications in PM
- [NotebookLM: The Complete Guide](https://medium.com/@shivashanker7337/notebooklm-the-complete-guide-updated-october-2025-1c9ebf5c14f6) - Detailed guide to Google's research tool
- [Introducing Gemini 2.5 Flash Image ("Nano Banana")](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/) - Google's image generation and editing model
- [Claude can now create Excel files and PowerPoints](https://www.tomsguide.com/ai/claude/claude-can-now-create-excel-files-and-powerpoints-for-you-heres-how-to-use-this-new-feature) - Tutorial on Claude's spreadsheet capabilities
- [Advancing Claude for Financial Services](https://www.anthropic.com/news/advancing-claude-for-financial-services) - Claude's enhanced data analysis features

### Video Resources
- [Andrej Karpathy: "Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- [Andrej Karpathy: "How I use LLMs"](https://www.youtube.com/watch?v=EWvNQjAaOHw)

### AI Economics & Policy
- [The Economics of the AI Boom - Sean Mullin, Canada2020 Conference (September 2025)](https://www.seanmullin.ca/presentations/Economics_of_the_AI_Boom-Canada2020-Sept2025.pdf?raw=1)

### Educational Programs
- [Alberta AI Masterclass](https://masterclass.albertaaiacademy.com/)
- [Using Generative AI - University of Waterloo Writing Centre](https://uwaterloo.ca/writing-and-communication-centre/Resources-AI-Overview) - Writing and communication guidance for AI use
- [Guide on the Use of Generative AI (Government of Canada)](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/guide-use-generative-ai.html) - Official guidance on responsible AI use

---

## 📧 Contact

**Instructor**: Sean Mullin  
**Email**: sean.mullin@gmail.com  
**Website**: [www.seanmullin.com](https://www.seanmullin.com)

---

## 📝 License

These materials are provided for educational purposes for training participants.

---

*Last updated: November 19, 2025*
