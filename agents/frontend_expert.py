from openai import OpenAI
from utils.rate_limiter import RateLimiter

class FrontendExpert:
    def __init__(self):
        with open("Ardi_agent/prompts/frontend_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def develop_frontend(self, frontend_tasks: list) -> str:
        self.rate_limiter.wait_for_next_call()
        tasks_str = "\n".join(frontend_tasks)
        user_content = f"Develop frontend for the following tasks:\n{tasks_str}"
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": user_content}
            ]
        )
        frontend_summary = response.choices[0].message.content
        return frontend_summary

    def save_frontend_summary(self, content: str):
        with open("/home/ubuntu/ardi_agent/frontend.md", "w") as f:
            f.write(content)
        print("Frontend summary saved to frontend.md")


