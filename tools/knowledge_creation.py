from openai import OpenAI
from utils.rate_limiter import RateLimiter

class KnowledgeCreation:
    def __init__(self):
        with open("Ardi_agent/prompts/knowledge_creation.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def create_knowledge_base(self, topic: str, content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        user_content = f"Topic: {topic}\nContent: {content}"
        response = self.client.chat.completions.create(
            model="gpt-4o", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": user_content}
            ]
        )
        knowledge_entry = response.choices[0].message.content
        return knowledge_entry

    def save_knowledge_entry(self, content: str, filename: str = "knowledge_entry.md"):
        with open(f"/home/ubuntu/ardi_agent/{filename}", "w") as f:
            f.write(content)
        print(f"Knowledge entry saved to {filename}")


