from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class BackendExpert:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/backend_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def develop_backend(self, backend_tasks: list) -> str:
        self.rate_limiter.wait_for_next_call()
        tasks_str = "\n".join(backend_tasks)
        user_content = f"Develop backend for the following tasks:\n{tasks_str}"
        response = self.client.generate_content(self.prompt + "\n" + user_content)
        backend_summary = response
        return backend_summary

    def save_backend_summary(self, content: str):
        with open("/home/ubuntu/Ardi_agent/backend.md", "w") as f:
            f.write(content)
        print("Backend summary saved to backend.md")


