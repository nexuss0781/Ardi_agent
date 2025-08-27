from openai import OpenAI
from utils.rate_limiter import RateLimiter

class QualityAssuranceAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/quality_assurance_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def review_content(self, content: str, content_type: str) -> bool:
        self.rate_limiter.wait_for_next_call()
        user_content = f"Content Type: {content_type}\nContent: {content}"
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": user_content}
            ]
        )
        review_result = response.choices[0].message.content
        
        # Based on the LLM's review_result, determine if content is approved or rejected.
        # For now, a simple check for a positive affirmation.
        if "approved" in review_result.lower() or "pass" in review_result.lower():
            print(f"Reviewing {content_type} content... Approved by QA.")
            return True
        else:
            print(f"Reviewing {content_type} content... Rejected by QA.\nReason: {review_result}")
            return False


