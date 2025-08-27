from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class KnowledgeCreation:
    def __init__(self):
        with open("Ardi_agent/prompts/knowledge_creation.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def create_knowledge_base(self, topic: str, content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        user_content = f"Topic: {topic}\nContent: {content}"
        knowledge_entry = self.client.generate_content(self.prompt + "\n" + user_content)
        return knowledge_entry

    def save_knowledge_entry(self, content: str, filename: str = "knowledge_entry.md"):
        with open(f"/home/ubuntu/Ardi_agent/{filename}", "w") as f:
            f.write(content)
        print(f"Knowledge entry saved to {filename}")


