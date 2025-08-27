from openai import OpenAI
from utils.rate_limiter import RateLimiter
import json

class TaskerAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/tasker_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def classify_features(self, synthesis_content: str) -> dict:
        self.rate_limiter.wait_for_next_call()
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt + "\n\nOutput should be a JSON object with 'backend' and 'frontend' keys, each containing a list of tasks."},
                {"role": "user", "content": synthesis_content}
            ]
        )
        try:
            tasks = json.loads(response.choices[0].message.content)
            return tasks
        except json.JSONDecodeError:
            print("Error: Could not parse JSON from LLM response. Returning empty tasks.")
            return {"backend": [], "frontend": []}


