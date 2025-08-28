from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class PresenterAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/presenter_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def present_phase_summary(self, phase_name: str, summary_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        user_content = f"Phase Name: {phase_name}\nSummary: {summary_content}"
        presentation = self.client.generate_content(self.prompt + "\n" + user_content)
        return presentation

    def save_presentation_content(self, content: str, filename: str = "phase_summary.md"):
        with open(f"/home/ubuntu/Ardi_agent/{filename}", "w") as f:
            f.write(content)
        print(f"Presentation content saved to {filename}")


