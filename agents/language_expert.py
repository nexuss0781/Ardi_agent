from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class LanguageExpert:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/language_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def formalize_query(self, query: str) -> str:
        self.rate_limiter.wait_for_next_call()
        return self.client.generate_content(self.prompt + "\n" + query)


