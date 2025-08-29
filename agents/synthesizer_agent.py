from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.finish_tool import finish_tool

class SynthesizerAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/synthesizer_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def synthesize(self, idea_file: str = "idea.md", analysis_file: str = "Analysis.md") -> str:
        idea_content = self.file_manager.read_file(idea_file)
        analysis_content = self.file_manager.read_file(analysis_file)

        combined_content = f"Idea:\n{idea_content}\n\nAnalysis:\n{analysis_content}"

        self.rate_limiter.wait_for_next_call()
        synthesized_content = self.client.generate_content(self.prompt + "\n\nOrganize and synthesize the following content into a pre-implementation document. Beautify it for readability by adding emojis in a professional, non-technical way. Ensure the response is a complete and comprehensive document, without truncation.\n\n" + combined_content)

        self.file_manager.write_file("pre_implementation.md", synthesized_content)
        finish_tool()

        return synthesized_content


