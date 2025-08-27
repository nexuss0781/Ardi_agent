# Ardi Agent System Architecture

## 1. Introduction

This document outlines the proposed architecture for the Ardi Agent system, an Agentic AI designed to automate the development and testing of full-stack applications. The system leverages multiple specialized AI agents working collaboratively to achieve complex tasks, emphasizing a pure Python implementation to maintain efficiency and avoid heavy frameworks.

## 2. Core Concepts

### 2.1 AI Agent vs. Agentic AI

The `ArdiAgent.md` document distinguishes between two key concepts:

- **AI Agent:** A single AI entity focused on automating a specific task.
- **Agentic AI:** A centralized system comprising multiple AI agents that collaborate to automate a given task. The Ardi Agent falls into this category, utilizing 16 distinct agents.

### 2.2 Design Philosophy

The core design philosophy for the Ardi Agent system, as derived from the requirements, includes:

- **Pure Python Implementation:** Avoidance of heavy frameworks like Langchain, Pydantic, and Pandas to ensure a lightweight, reliable, and memory-efficient environment (especially given the 512MB RAM constraint).
- **Modular Agent-Based System:** Each agent is a specialized module with a defined role, promoting clear separation of concerns and easier maintenance.
- **Orchestration-driven Workflow:** A central orchestrator will manage the flow between agents, ensuring the right agent receives the correct prompt and functional tools at each step.
- **Session Management:** The system must handle and maintain each agent's session throughout the task to retain context.
- **LLM Rate Limit Handling:** Mechanisms to manage and adhere to Large Language Model (LLM) rate limits.
- **Continuous Integration:** Emphasis on frequent commits and pushes to Git, even for minor achievements.

## 3. Agent Breakdown and Workflow

The Ardi Agent system is structured into two main phases: **Query Processing** and **Implementation**. Each phase involves a sequence of specialized agents.

### 3.1 Phase 1: Query Processing

This phase focuses on understanding the user's request, gathering necessary information, and generating a comprehensive technical roadmap. The agents involved and their interactions are as follows:

1.  **User Prompt Reception:** The process begins with receiving a user query.

2.  **Language Expert (LE):**
    *   **Role:** Formalizes the user query, clarifying any ambiguities. This agent acts as the initial interpreter of the user's intent.
    *   **Input:** Raw user query.
    *   **Output:** Formalized and clarified query.
    *   **Interaction:** If clarification is needed, it will interact with the Clarification Agent.

3.  **Clarification Agent (CA):**
    *   **Role:** Clarifies objectives, scope, and other project-related details. It functions like a developer interviewing a client, ensuring all prerequisites are met before development proceeds. It uses a `todo.md` checker for interview questions (e.g., Audience, Comprehensiveness).
    *   **Input:** Formalized query from Language Expert.
    *   **Output:** Clarified content saved as `clarify.md`. User confirmation is required before proceeding.
    *   **Interaction:** Interacts with the user for clarifications and updates its internal `todo.md` based on addressed points.

4.  **Idea Generator (IE):**
    *   **Role:** Outlines comprehensive feature analysis for the application without using external internet tools. This is an internal brainstorming and conceptualization step.
    *   **Input:** Clarified content from Clarification Agent.
    *   **Output:** Comprehensive feature analysis (e.g., `Idea.md`).
    *   **Interaction:** Passes its output to the Quality Assurance Agent for review.

5.  **Quality Assurance (QA) (Initial Review):**
    *   **Role:** Reviews the feasibility, quality, and other measurements of the Idea Generator's output. Acts as a gatekeeper for progression.
    *   **Input:** Output from Idea Generator.
    *   **Output:** Approval or rejection, with feedback if rejected.
    *   **Interaction:** If approved, the process continues.

6.  **Analysis Agent (AE):**
    *   **Role:** Gathers internet trends, analyzes similar company applications (pros and cons), assesses market control potential, and identifies essential features. It uses an internet tool and maintains its own `todo.md` for focused task completion.
    *   **Input:** Approved feature analysis (implicitly, after QA).
    *   **Output:** Analysis report saved as `Analysis.md`.
    *   **Interaction:** Utilizes an internet tool. Its output is reviewed by the Quality Assurance Agent.

7.  **Quality Assurance (QA) (Analysis Review):**
    *   **Role:** Reviews the Analysis Agent's output for quality and completeness.
    *   **Input:** Output from Analysis Agent.
    *   **Output:** Approval or rejection, with feedback if rejected.
    *   **Interaction:** If approved, the process continues.

8.  **Synthesizer Agent (SA):**
    *   **Role:** Integrates and synthesizes the content from `Idea.md` and `Analysis.md` into one organized document.
    *   **Input:** `Idea.md` and `Analysis.md`.
    *   **Output:** Synthesized document saved as `Synthesis.md`.

9.  **Report Agent (RA) (Pre-implementation):**
    *   **Role:** Reads `Synthesis.md` and generates a future implementation roadmap and outlines the technology stack required to build the application. This acts as a pre-implementation technical document.
    *   **Input:** `Synthesis.md`.
    *   **Output:** Pre-implementation technical document.

10. **Organizer Agent (OA) (Phase 1):**
    *   **Role:** Beautifies the content of `Synthesis.md` with emojis, conciseness, and user-friendly formatting for improved readability.
    *   **Input:** `Synthesis.md`.
    *   **Output:** Beautified `Synthesis.md`.

11. **Presenter Agent (PA) (Phase 1):**
    *   **Role:** Summarizes the work done in Phase 1 and outlines the next steps. Awaits user confirmation to proceed to Phase 2.
    *   **Input:** Summary of Phase 1 activities.
    *   **Output:** Presentation to the user.

### 3.2 Phase 2: Implementation Phase

This phase focuses on the actual development, testing, and post-implementation documentation of the application. The agents involved are:

1.  **Tasker Agent (TA):**
    *   **Role:** Classifies features from `Synthesis.md` into backend and frontend tasks.
    *   **Input:** `Synthesis.md`.
    *   **Output:** Grouped backend and frontend tasks.

2.  **Backend Expert (BE):**
    *   **Role:** Implements the backend functionalities. Its work is reviewed by the Quality Assurance Agent.
    *   **Input:** Backend tasks from Tasker Agent.
    *   **Output:** Implemented backend code and `backend.md` documenting the work.
    *   **Interaction:** Passes its output to the Quality Assurance Agent.

3.  **Quality Assurance (QA) (Backend Review):**
    *   **Role:** Reviews the backend implementation.
    *   **Input:** Output from Backend Expert.
    *   **Output:** Approval or rejection, with feedback if rejected.
    *   **Interaction:** If approved, the process continues.

4.  **Frontend Expert (FE):**
    *   **Role:** Implements the frontend functionalities, with a focus on aesthetics, modern views, and user experience.
    *   **Input:** Frontend tasks from Tasker Agent.
    *   **Output:** Implemented frontend code and `frontend.md` documenting the work.

5.  **Fullstack Expert (FSE):**
    *   **Role:** Ensures end-to-end functionality, performs testing, and checks the integrity of the integrated backend and frontend.
    *   **Input:** Implemented backend and frontend components.
    *   **Output:** Tested and integrated application.

6.  **Report Agent (RA) (Post-implementation):**
    *   **Role:** Writes post-implementation technical documentation, covering every implemented feature.
    *   **Input:** Implemented features.
    *   **Output:** Post-implementation technical documentation.

7.  **Synthesizing Agent (SA) (Post-implementation):**
    *   **Role:** Synthesizes the post-implementation frontend and backend final documentation (`backend.md` and `frontend.md`).
    *   **Input:** `backend.md` and `frontend.md`.
    *   **Output:** Post-synthesized document (`Post-synthesized.md`).

8.  **Organizer Agent (OA) (Phase 2):**
    *   **Role:** Beautifies the post-synthesized documentation.
    *   **Input:** `Post-synthesized.md`.
    *   **Output:** Beautified `Post-synthesized.md`.

9.  **Debugging Agent (DA):**
    *   **Role:** Handles and debugs any issues that arise during or after implementation.
    *   **Input:** Bug reports or identified issues.
    *   **Output:** Debugged code and resolution.

10. **Presenter Agent (PA) (Phase 2):**
    *   **Role:** Presents the final outcome to the user, similar to Phase 1.
    *   **Input:** Final application and documentation.
    *   **Output:** Presentation to the user.

## 4. Agent List

The `ArdiAgent.md` document lists the following 15 agents:

1.  Language Expert (LE)
2.  Clarification Agent (CA)
3.  Idea Expert (IE)
4.  Analysis Expert (AE)
5.  Synthesizer Agent (SA)
6.  Quality Assurance (QA)
7.  Report Agent (RA)
8.  Organizer Agent (OA)
9.  Tasker Agent (TA)
10. Backend Expert (BE)
11. Frontend Expert (FE)
12. Debugger Agent (DA)
13. Technical Expert (TE)
14. Testing Checker (TC)
15. Presenting Agent (PA)

Note: The document mentions 


16 agents, but only lists 15. I will proceed with the listed 15 agents and assume the discrepancy is a minor oversight or that one agent serves a dual role.

## 5. Tools

The system will integrate various tools to facilitate its operations. These are categorized as File Management and Other Tools.

### 5.1 File Management Tools

These tools enable agents to interact with the file system for reading, writing, and managing project-related files:

-   **Write:** Create new files.
-   **Read:** Read content from files.
-   **Edit:** Add content to existing files.
-   **Modify:** Replace content within files.
-   **Delete:** Remove files.
-   **List Directory:** List contents of a directory.
-   **Save Version:** Copy project to a backup location.
-   **Restore Version:** Revert project from a backup.
-   **Read Folder:** Bulk reading of files within a folder.
-   **Ignore File:** Remove a specific file from the system context.
-   **Ignore Folder:** Remove a specific folder from the system context.
-   **Remove File:** Remove a file from the current context.
-   **Remove Folder:** Remove a folder from the current context.
-   **View Context:** Display remaining tokens and a list of files in the current context.

### 5.2 Other Tools

Beyond file management, the system will utilize:

-   **Quiz Creator:** For generating quizzes.
-   **Knowledge Creation:** For creating and managing knowledge bases.
-   **Internet:** For gathering external information (e.g., internet trends).
-   **Chatting:** For communication, likely with the user or between agents.
-   **Terminal Integration:** For executing shell commands or interacting with the command line.

## 6. Implementation Guidelines

To ensure the system remains lightweight and efficient, the following guidelines will be strictly adhered to during implementation:

-   **Pure Python:** All logic will be implemented using pure Python, avoiding heavy frameworks that could increase memory footprint or slow down execution.
-   **Minimal Framework Usage:** Frameworks like Pydantic and Pandas are to be avoided unless absolutely necessary and a lightweight alternative cannot be found.
-   **Agent Session Management:** Each agent will maintain its session to preserve context throughout its operation.
-   **LLM Rate Limit Handling:** The system will incorporate mechanisms to manage and respect LLM API rate limits.
-   **Functional Tools:** Tools provided to agents will be functional and tailored to their specific needs.
-   **Orchestration:** A central orchestrator will be responsible for directing queries and prompts to the correct agents, ensuring a smooth workflow.

## 7. Development Workflow

-   **Continuous Commits:** The development process will involve frequent commits and pushes to the Git repository, even for minor achievements. This ensures progress is regularly saved and tracked.
-   **`todo.md` Management:** The `todo.md` file will be actively used to track progress and manage tasks throughout the development lifecycle.

## 8. Future Considerations

While not the immediate focus, the system acknowledges that agent prompts and the building of LLM tools are critical aspects that will be addressed in future iterations. The current priority is to establish the core agent sequences and levels, ensuring a robust and efficient workflow.

## 9. Conclusion

The Ardi Agent system is envisioned as a powerful Agentic AI capable of automating complex software development tasks. By adhering to a pure Python, modular, and orchestrated architecture, the system aims to deliver a lightweight, efficient, and scalable solution. The detailed breakdown of agents, their roles, and the implementation guidelines will serve as a roadmap for successful development.

---

**Author:** Manus AI
**Date:** August 27, 2025

