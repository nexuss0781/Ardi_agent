from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class FullstackExpert:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/fullstack_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def check_integrity(self, backend_summary: str, frontend_summary: str) -> str:
        self.rate_limiter.wait_for_next_call()
        combined_summary = f"Backend Summary:\n{backend_summary}\n\nFrontend Summary:\n{frontend_summary}"
        integrity_report = self.client.generate_content(self.prompt + "\n" + combined_summary)
        return integrity_report


