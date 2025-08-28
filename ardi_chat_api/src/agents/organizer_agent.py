from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class OrganizerAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/organizer_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def beautify_content(self, content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        beautified_content = self.client.generate_content(self.prompt + "\n" + content)
        return beautified_content

    def save_organized_content(self, content: str, filename: str = "organized_synthesis.md"):
        with open(f"/home/ubuntu/Ardi_agent/{filename}", "w") as f:
            f.write(content)
        print(f"Organized content saved to {filename}")


