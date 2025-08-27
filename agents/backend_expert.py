from openai import OpenAI
from utils.rate_limiter import RateLimiter

class BackendExpert:
    def __init__(self):
        with open("Ardi_agent/prompts/backend_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def develop_backend(self, backend_tasks: list) -> str:
        self.rate_limiter.wait_for_next_call()
        tasks_str = "\n".join(backend_tasks)
        user_content = f"Develop backend for the following tasks:\n{tasks_str}"
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": user_content}
            ]
        )
        backend_summary = response.choices[0].message.content
        return backend_summary

    def save_backend_summary(self, content: str):
        with open("/home/ubuntu/ardi_agent/backend.md", "w") as f:
            f.write(content)
        print("Backend summary saved to backend.md")


