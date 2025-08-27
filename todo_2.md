# Todo List for Ardi_agent Improvements

## Phase 1: Clone repository and initial analysis
- [x] Clone the repository
- [x] Configure git user email and name

## Phase 2: Deep codebase analysis and documentation
- [ ] Analyze the existing codebase for workflow, agent interactions, and LLM usage.
- [ ] Identify partially implemented features and non-robust areas.
- [ ] Document bottlenecks and potential production issues.
- [ ] Create a detailed report of findings.

## Phase 3: Implement workflow orchestration and main entry point
- [x] Define a clear workflow for agents.
- [x] Implement `orchestrator.py` or `main.py` to manage agent flow.

## Phase 4: Replace OpenAI with Gemini 2.5 Flash and centralize configuration
- [ ] Remove all OpenAI API calls.
- [ ] Integrate Gemini 2.5 Flash for LLM interactions.
- [ ] Create a `.env` file for API tokens and other sensitive information.
- [ ] Centralize token location in a dedicated configuration file.

## Phase 5: Implement session history and action tracking
- [ ] Implement session history for LLM interactions.
- [ ] Ensure every agent action is tracked and stored.
- [ ] Enable the model to resume from where it stopped.
- [ ] Allow visibility into previous actions of other agents.

## Phase 6: Fix partially implemented features and make them robust
- [ ] Review and refactor all partially implemented features.
- [ ] Ensure all features are robust and production-ready.
- [ ] Remove any placeholder code.

## Phase 7: Address production bottlenecks and final testing
- [ ] Inspect and resolve any remaining uncovered bottlenecks.
- [ ] Conduct comprehensive testing of the entire application.

## Phase 8: Push changes to repository and deliver results
- [ ] Commit all changes to the local repository.
- [ ] Push changes to the remote repository.
- [ ] Provide a detailed report of all implemented changes and improvements.

