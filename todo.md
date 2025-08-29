## Multi-Agent Workflow Implementation Checklist

This checklist outlines the steps to fully implement the multi-agent workflow described in `WORKFLOW.md`.

### Phase 1: Understand the complete workflow and create a detailed todo.md
- [x] Read and analyze `WORKFLOW.md`.
- [x] Create `todo.md` with detailed implementation steps for each agent.

### Phase 2: Implement Language Expert Agent
- [x] Implement the Language Expert Agent's core logic.
- [x] Ensure the agent can formalize queries professionally.
- [x] Implement the `quez` tool for user confirmation.
- [x] Handle `clarify.md` attachment for starting from communication agent.
- [x] Create `Query.md` with the formalized query.
- [x] Implement `finish_tool` call.

### Phase 3: Implement Clarification Tool and Agent
- [x] Implement the Clarification Agent's core logic.
- [x] Implement reading `Query.md`.
- [x] Implement different clarification areas (comprehensivity, similar apps, unwanted features, UI/UX, constraints).
- [x] Handle `clarify.md` provided by orchestrator.
- [x] Implement `quez` tool for summarizing user needs and confirmation.
- [x] Create `create.md` with the final user output.
- [x] Implement `finish_task` call and file movement to `private_dir`.

### Phase 4: Implement Idea Generator Agent
- [x] Implement the Idea Generator Agent's core logic.
- [x] Implement reading `Clarify.md`.
- [x] Create `todo.md` for detailed plan (internal to Idea Generator).
- [x] Implement deep analysis based on comprehensivity scope.
- [x] Create `idea.md`.
- [x] Implement `qa_tool` call for Quality Assurance feedback.
- [x] Handle refinement areas and adjust plan.
- [x] Implement `chat_tool` for arguing with QA agent using `chat.md`.
- [x] Implement `finish_task` call after QA approval.

### Phase 5: Implement Analysis Agent
- [x] Implement the Analysis Agent's core logic.
- [x] Implement reading `clarify.md`.
- [x] Implement internet-based analysis (trends, similar apps, features, bottlenecks).
- [x] Synthesize findings into `Analysis.md`.
- [x] Implement `QA_tool` call.

### Phase 6: Implement Synthesis Agent
- [x] Implement the Synthesis Agent's core logic.
- [x] Implement reading `idea.md` and `analysis.md`.
- [x] Organize and synthesize content into `pre_implementation.md`.
- [x] Beautify for readability with emojis.
- [x] Implement `finish_task` call.

### Phase 7: Implement Technical Agent (for pre-implementation)
- [x] Implement the Technical Agent's core logic.
- [x] Implement reading `synthesis.md`.
- [x] Create comprehensive implementation plan and technical roadmap.

### Phase 8: Implement Task Agent
- [x] Implement the Task Agent's core logic.
- [x] Implement reading `Synthesis.md`.
- [x] Classify features into `frontend.md` and `backend.md`.

### Phase 9: Implement Backend Agent
- [x] Implement the Backend Agent's core logic.
- [x] Implement reading `synthesis.md`, `backend.md`, `technical.md`.
- [x] Create comprehensive plan in `implementation.md`.
- [x] Create `todo.md` checker for backend implementation.
- [x] Implement backend development based on `todo.md`.
- [x] Create `backend.md` for detailed implementation report.
- [x] Inherit infrastructure for frontend.
- [x] Include notes for frontend.
- [x] Implement `qa_tool` call.
- [x] Implement `finish_tool` call.

### Phase 10: Implement Frontend Agent
- [x] Implement the Frontend Agent's core logic.
- [x] Implement reading `synthesis.md`, `frontend.md`, `technical.md`, `backend.md`.
- [x] Create comprehensive implementation plan in `implementation.md`.
- [x] Classify implementation plan into `todo` for roadmap.
- [x] Implement appealing frontend designs and technical prompts.
- [x] Implement `finish_task` while editing `todo.md`.
- [x] Create `frontend.md`.
- [x] Connect backend with frontend.
- [x] Implement `qa_tool` call.
- [x] Implement `finish_tool` call.

### Phase 11: Implement Fullstack Agent
- [x] Implement the Fullstack Agent's core logic.
- [x] Implement reading codebase and key files.
- [x] Implement End-to-End testing for functionality and integrity.
- [x] Use different test tools.
- [x] Check database, backend, and frontend components.
- [x] Implement `finish_task` call.

### Phase 12: Implement Synthesizer Agent (for post-implementation)
- [x] Implement the Synthesizer Agent's core logic.
- [x] Implement reading `frontend.md` and `backend.md`.
- [x] Synthesize content into `post_implementation.md`.

### Phase 13: Implement Technical Agent (for post-implementation report)
- [x] Implement the Technical Agent's core logic.
- [x] Implement reading `post_implementation.md` and codebase.
- [x] Change implementation report to technical report.

### Phase 14: Implement Debugging Agent
- [x] Implement the Debugging Agent's core logic.
- [x] Implement `debug_tool` call.
- [x] Implement `continue_work` tool call.
- [x] Add debugging prompts.

### Phase 15: Implement Quality Assurance Agent
- [x] Implement the Quality Assurance Agent's core logic.
- [x] Implement client-like argumentation for quality and feasibility.
- [x] Implement differing requirements for each agent.
- [x] Implement `chat_tool` for conversational feedback.
- [x] Save suggestions as `[agent_name]_qa.md`.
- [x] Implement `review_suggestion` tool.
- [x] Create `todo.md` checker for deep quality test.
- [x] Implement `APPROVED` or `REFUSED` tool calls.

### Phase 16: Implement Presenter Agent
- [x] Implement the Presenter Agent's core logic.
- [x] Summarize whole work and implementation.
- [x] Present key files and explanations.
- [x] Implement `finish_task` call.

### Phase 17: Commit and push all changes
- [ ] Commit changes to the repository.
- [ ] Push changes to the remote repository.

### Phase 18: Report final implementation status to user
- [ ] Provide a summary of the completed implementation.
- [ ] Attach relevant files or links.

