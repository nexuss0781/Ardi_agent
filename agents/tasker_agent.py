from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.finish_tool import finish_tool
import json

class TaskerAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/tasker_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def classify_features(self, synthesis_file: str = "pre_implementation.md") -> dict:
        synthesis_content = self.file_manager.read_file(synthesis_file)
        print(f"Synthesis Content for Task Classification: {synthesis_content}")

        self.rate_limiter.wait_for_next_call()
        response_content = self.client.generate_content(self.prompt + "\n\nBased on the following synthesis, classify all features mentioned into frontend and backend (database+backend) work. Output should be a JSON object with \"backend\" and \"frontend\" keys, each containing a list of tasks. Ensure the response is a complete and comprehensive JSON object, without truncation.\n\n" + synthesis_content)
        try:
            tasks = json.loads(response_content)
            backend_tasks = "\n".join(tasks.get("backend", []))
            frontend_tasks = "\n".join(tasks.get("frontend", []))

            self.file_manager.write_file("backend.md", backend_tasks)
            self.file_manager.write_file("frontend.md", frontend_tasks)

            finish_tool()
            return tasks
        except json.JSONDecodeError:
            print("Error: Could not parse JSON from LLM response. Returning empty tasks.")
            return {"backend": [], "frontend": []}


