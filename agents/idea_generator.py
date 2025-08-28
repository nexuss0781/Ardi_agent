from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class IdeaGenerator:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/idea_generator.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def generate_features(self, clarified_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        features = self.client.generate_content(self.prompt + "\n\nEnsure the response is a complete and comprehensive document, without truncation." + "\n" + clarified_content)
        return features

    def save_idea_content(self, content: str):
        with open("/home/ubuntu/Ardi_agent/idea.md", "w") as f:
            f.write(content)
        print("Idea content saved to idea.md")


