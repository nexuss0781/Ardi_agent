from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class DebuggingAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/debugging_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def debug_issues(self, issue_description: str) -> str:
        self.rate_limiter.wait_for_next_call()
        debug_report = self.client.generate_content(self.prompt + "\n" + issue_description)
        return debug_report


