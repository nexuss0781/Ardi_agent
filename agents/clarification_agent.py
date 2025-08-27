from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class ClarificationAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/clarification_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.clarification_todo = {
            "Audience": False,
            "Comprehensive": False
        }

    def clarify_objectives(self, query: str) -> str:
        self.rate_limiter.wait_for_next_call()
        clarified_content = self.client.generate_content(self.prompt + "\n" + query)
        
        # Placeholder for actual logic to update clarification_todo based on LLM output
        # For now, we'll assume the LLM clarifies these points.
        self.clarification_todo["Audience"] = True
        self.clarification_todo["Comprehensive"] = True

        return clarified_content

    def get_clarification_todo(self):
        return self.clarification_todo

    def save_clarified_content(self, content: str):
        with open("/home/ubuntu/Ardi_agent/clarify.md", "w") as f:
            f.write(content)
        print("Clarified content saved to clarify.md")


