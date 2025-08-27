# Ardi Agent

Ardi Agent is an Agentic AI system designed to automate the development of backend, frontend, or full-stack applications, including end-to-end testing. It operates in two main phases, each involving multiple specialized AI agents.

## Project Structure

```
Ardi_agent/
├── agents/                 # Contains individual AI agents
│   ├── __init__.py
│   ├── analysis_agent.py
│   ├── backend_expert.py
│   ├── clarification_agent.py
│   ├── debugging_agent.py
│   ├── frontend_expert.py
│   ├── fullstack_expert.py
│   ├── idea_generator.py
│   ├── language_expert.py
│   ├── organizer_agent.py
│   ├── presenter_agent.py
│   ├── quality_assurance_agent.py
│   ├── report_agent.py
│   ├── synthesizer_agent.py
│   └── tasker_agent.py
├── prompts/                # Stores prompts for each agent
│   ├── analysis_agent.md
│   ├── backend_expert.md
│   ├── chatting_tool.md
│   ├── clarification_agent.md
│   ├── debugging_agent.md
│   ├── frontend_expert.md
│   ├── fullstack_expert.md
│   ├── idea_generator.md
│   ├── internet_tool.md
│   ├── knowledge_creation.md
│   ├── language_expert.md
│   ├── organizer_agent.md
│   ├── presenter_agent.md
│   ├── quality_assurance_agent.md
│   ├── quiz_creator.md
│   ├── report_agent.md
│   ├── synthesizer_agent.md
│   └── tasker_agent.md
├── tools/                  # Contains various utility tools
│   ├── __init__.py
│   ├── chatting_tool.py
│   ├── file_manager.py
│   ├── internet_tool.py
│   ├── knowledge_creation.py
│   └── quiz_creator.py
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── rate_limiter.py
├── .gitignore
├── ArdiAgent.md
├── clarify.md
├── idea.md
├── main.py
├── README.md
├── synthesis.md
└── todo.md
```

## Phases of Operation

### Phase 1: Query Processing
This phase focuses on understanding the user's request and generating a detailed plan. It involves the following agents:

*   **Language Expert:** Formalizes the user's query.
*   **Clarification Agent:** Clarifies objectives and scope, creating a `todo.md` for unaddressed points.
*   **Idea Generator:** Outlines comprehensive feature analysis without internet access.
*   **Analysis Agent:** Gathers internet trends, performs competitor analysis, and identifies potential features (simulated in the current code).
*   **Synthesizer Agent:** Combines the ideas and analysis into a synthesized document.
*   **Quality Assurance Agent:** Reviews content at various stages.
*   **Report Agent:** Generates a pre-implementation roadmap.
*   **Organizer Agent:** Beautifies the synthesized content for readability.
*   **Presenter Agent:** Summarizes Phase 1 and prepares for Phase 2.

### Phase 2: Implementation Phase
This phase focuses on the actual development and testing of the application.

*   **Tasker Agent:** Classifies features into backend and frontend tasks.
*   **Backend Expert:** Develops the backend (simulated).
*   **Frontend Expert:** Develops the frontend (simulated).
*   **Fullstack Expert:** Checks the integrity of the integrated backend and frontend.
*   **Report Agent:** Generates post-implementation documentation.
*   **Synthesizing Agent:** Synthesizes post-implementation reports.
*   **Organizer Agent:** Beautifies post-synthesized documentation.
*   **Debugging Agent:** Handles debugging (placeholder).
*   **Presenter Agent:** Presents the final results to the user.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nexuss0781/Ardi_agent.git
    cd Ardi_agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install openai
    ```

3.  **Set up OpenAI API Key:**
    Ensure your `OPENAI_API_KEY` environment variable is set. The agents use the `openai` Python library to interact with the LLM.

## Usage

To run the Ardi Agent, execute the `main.py` script:

```bash
python3.11 main.py
```

The `main.py` script will initiate the query processing phase, and the agents will interact to generate the project plan and simulated implementation. Follow the prompts in the terminal to provide input to the Clarification Agent.

## LLM Integration and Rate Limiting

All agents are integrated with an LLM (currently configured to use `gemini-2.5-flash` or similar models). A `RateLimiter` utility is included to manage API call frequency, although its full integration across all agents is an ongoing task.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. (Note: A `LICENSE` file is not currently included in the repository and would need to be added.)


