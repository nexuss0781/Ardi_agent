from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.finish_tool import finish_tool

class TechnicalAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/technical_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def generate_implementation_plan(self, synthesis_file: str = "pre_implementation.md") -> str:
        synthesis_content = self.file_manager.read_file(synthesis_file)
        print(f"Synthesis Content for Technical Plan: {synthesis_content}")

        self.rate_limiter.wait_for_next_call()
        technical_plan_content = self.client.generate_content(self.prompt + "\n\nBased on the following synthesis, create a comprehensive implementation plan and a technical roadmap. The scope is limited only to the synthesis content. Ensure the response is a complete and comprehensive document, without truncation.\n\n" + synthesis_content)

        self.file_manager.write_file("technical.md", technical_plan_content)
        finish_tool()

        return technical_plan_content

    def generate_technical_report(self, post_implementation_file: str = "post_implementation.md") -> str:
        post_implementation_content = self.file_manager.read_file(post_implementation_file)
        print(f"Post-Implementation Content for Technical Report: {post_implementation_content}")

        self.rate_limiter.wait_for_next_call()
        technical_report_content = self.client.generate_content(self.prompt + "\n\nBased on the following post-implementation report and the codebase, change the implementation report to a technical report of what was implemented. Ensure the response is a complete and comprehensive document, without truncation.\n\n" + post_implementation_content)

        self.file_manager.write_file("technical_report.md", technical_report_content)
        finish_tool()

        return technical_report_content


