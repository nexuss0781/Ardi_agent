from openai import OpenAI
from utils.rate_limiter import RateLimiter

class AnalysisAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/analysis_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def gather_and_analyze(self, idea_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": idea_content}
            ],
            max_tokens=4000 # Increased token limit
        )
        analysis = response.choices[0].message.content
        return analysis

    def save_analysis_content(self, content: str):
        with open("/home/ubuntu/Ardi_agent/analysis.md", "w") as f:
            f.write(content)
        print("Analysis content saved to analysis.md")


