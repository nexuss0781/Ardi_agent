from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.finish_tool import finish_tool
import os

class PresenterAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/presenter_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def present_work(self, post_implementation_file: str = "post_implementation.md", codebase_path: str = "/home/ubuntu/Ardi_agent/") -> str:
        post_implementation_content = self.file_manager.read_file(post_implementation_file)
        print(f"Post-Implementation Content for Presentation: {post_implementation_content}")

        # Gather key files for explanation
        key_files = [
            "pre_implementation.md",
            "backend_report.md",
            "frontend_report.md",
            "technical_report.md",
            "e2e_test_report.md",
            "todo.md",
            "WORKFLOW.md"
        ]

        key_files_content = ""
        for file in key_files:
            full_path = os.path.join(codebase_path, file)
            if self.file_manager.file_exists(full_path):
                key_files_content += f"\n--- {file} ---\n" + self.file_manager.read_file(full_path)[:1000] + "...\n"
            else:
                key_files_content += f"\n--- {file} (Not Found) ---\n"

        self.rate_limiter.wait_for_next_call()
        presentation_content = self.client.generate_content(self.prompt + "\n\nSummarize the whole work and implementation done throughout the phases. Present key files and explanations. Beautify with emojis. Ensure the response is a complete and comprehensive document, without truncation.\n\nPost-Implementation Summary: " + post_implementation_content + "\n\nKey Files and Explanations: " + key_files_content)

        self.file_manager.write_file("final_presentation.md", presentation_content)
        finish_tool()

        return presentation_content


