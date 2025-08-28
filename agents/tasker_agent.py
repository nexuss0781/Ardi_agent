from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
import json

class TaskerAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/tasker_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def classify_features(self, synthesis_content: str) -> dict:
        self.rate_limiter.wait_for_next_call()
        response_content = self.client.generate_content(self.prompt + "\n\nOutput should be a JSON object with \'backend\' and \'frontend\' keys, each containing a list of tasks." + "\n" + synthesis_content)
        try:
            tasks = json.loads(response_content)
            return tasks
        except json.JSONDecodeError:
            print("Error: Could not parse JSON from LLM response. Returning empty tasks.")
            return {"backend": [], "frontend": []}


