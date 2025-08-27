from openai import OpenAI
from utils.rate_limiter import RateLimiter

class IdeaGenerator:
    def __init__(self):
        with open("Ardi_agent/prompts/idea_generator.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def generate_features(self, clarified_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role": "system", "content": self.prompt + "\n\nEnsure the response is a complete and comprehensive document, without truncation."},
                {"role": "user", "content": clarified_content}
            ],
            max_tokens=4000 # Increased token limit
        )
        features = response.choices[0].message.content
        return features

    def save_idea_content(self, content: str):
        with open("/home/ubuntu/Ardi_agent/idea.md", "w") as f:
            f.write(content)
        print("Idea content saved to idea.md")


