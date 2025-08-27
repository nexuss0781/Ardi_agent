from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class LanguageExpert:
    def __init__(self):
        with open("Ardi_agent/prompts/language_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def formalize_query(self, query: str) -> str:
        self.rate_limiter.wait_for_next_call()
        return self.client.generate_content(self.prompt + "\n" + query)


