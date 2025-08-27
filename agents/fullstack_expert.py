from openai import OpenAI
from utils.rate_limiter import RateLimiter

class FullstackExpert:
    def __init__(self):
        with open("Ardi_agent/prompts/fullstack_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def check_integrity(self, backend_summary: str, frontend_summary: str) -> str:
        self.rate_limiter.wait_for_next_call()
        combined_summary = f"Backend Summary:\n{backend_summary}\n\nFrontend Summary:\n{frontend_summary}"
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": combined_summary}
            ]
        )
        integrity_report = response.choices[0].message.content
        return integrity_report


