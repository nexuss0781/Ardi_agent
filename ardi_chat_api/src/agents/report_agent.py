from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class ReportAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/report_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def generate_roadmap(self, synthesis_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        roadmap = self.client.generate_content(self.prompt + "\n" + synthesis_content)
        return roadmap

    def save_report_content(self, content: str, filename: str = "report.md"):
        with open(f"/home/ubuntu/Ardi_agent/{filename}", "w") as f:
            f.write(content)
        print(f"Report content saved to {filename}")


