from openai import OpenAI
from utils.rate_limiter import RateLimiter

class LanguageExpert:
    def __init__(self):
        with open("Ardi_agent/prompts/language_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def formalize_query(self, query: str) -> str:
        self.rate_limiter.wait_for_next_call()
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content


