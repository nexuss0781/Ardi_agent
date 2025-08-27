from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class FrontendExpert:
    def __init__(self):
        with open("Ardi_agent/prompts/frontend_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def develop_frontend(self, frontend_tasks: list) -> str:
        self.rate_limiter.wait_for_next_call()
        tasks_str = "\n".join(frontend_tasks)
        user_content = f"Develop frontend for the following tasks:\n{tasks_str}"
        response = self.client.generate_content(self.prompt + "\n" + user_content)
        frontend_summary = response
        return frontend_summary

    def save_frontend_summary(self, content: str):
        with open("/home/ubuntu/ardi_agent/frontend.md", "w") as f:
            f.write(content)
        print("Frontend summary saved to frontend.md")


