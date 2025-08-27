from openai import OpenAI
from utils.rate_limiter import RateLimiter

class DebuggingAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/debugging_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def debug_issues(self, issue_description: str) -> str:
        self.rate_limiter.wait_for_next_call()
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": issue_description}
            ]
        )
        debug_report = response.choices[0].message.content
        return debug_report


