from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.finish_tool import finish_tool
import os

class FullstackExpert:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/fullstack_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def perform_e2e_test(self, codebase_path: str = "/home/ubuntu/Ardi_agent/") -> str:
        print(f"Performing End-to-End test on codebase: {codebase_path}")

        # Simulate reading codebase and key files
        # In a real scenario, this would involve parsing code, analyzing dependencies, etc.
        # For now, we'll just list some files.
        key_files = [
            "main.py",
            "orchestrator.py",
            "agents/language_expert.py",
            "agents/clarification_agent.py",
            "agents/idea_generator.py",
            "agents/analysis_agent.py",
            "agents/synthesizer_agent.py",
            "agents/technical_agent.py",
            "agents/tasker_agent.py",
            "agents/backend_expert.py",
            "agents/frontend_expert.py",
            "tools/quez_tool.py",
            "tools/finish_tool.py",
            "tools/file_manager.py",
            "tools/qa_tool.py",
            "tools/chat_tool.py",
            "tools/internet_tool.py",
            "backend.md",
            "frontend.md",
            "technical.md",
            "pre_implementation.md",
            "implementation.md",
            "backend_report.md",
            "frontend_report.md",
            "Query.md",
            "create.md",
            "idea.md",
            "Analysis.md",
        ]

        codebase_summary = ""
        for file in key_files:
            full_path = os.path.join(codebase_path, file)
            if self.file_manager.file_exists(full_path):
                codebase_summary += f"\n--- {file} ---\n" + self.file_manager.read_file(full_path)[:500] + "...\n"
            else:
                codebase_summary += f"\n--- {file} (Not Found) ---\n"

        # Simulate End-to-End testing for functionality and integrity
        self.rate_limiter.wait_for_next_call()
        test_report = self.client.generate_content(self.prompt + "\n\nPerform an End-to-End test for functionality and integrity of the backend and frontend based on the following codebase summary. Identify potential bugs and check database, backend, and frontend components. Ensure the response is a comprehensive test report, without truncation.\n\nCodebase Summary: " + codebase_summary)

        self.file_manager.write_file("e2e_test_report.md", test_report)
        print("End-to-End test report saved to e2e_test_report.md")

        # Check for issues and call finish_task if no issues
        if "No issues found" in test_report or "All tests passed" in test_report:
            print("No major issues found during E2E testing. Calling finish_task.")
            finish_tool()
        else:
            print("Issues found during E2E testing. Debugging agent might be needed.")
            # In a real scenario, this would trigger the debugging agent.

        return test_report


