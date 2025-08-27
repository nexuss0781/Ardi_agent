from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class QualityAssuranceAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/quality_assurance_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def review_content(self, content: str, content_type: str) -> bool:
        self.rate_limiter.wait_for_next_call()
        user_content = f"Content Type: {content_type}\nContent: {content}"
        review_result = self.client.generate_content(self.prompt + "\n" + user_content)
        
        # Based on the LLM\'s review_result, determine if content is approved or rejected.
        # For now, a simple check for a positive affirmation.
        if "approved" in review_result.lower() or "pass" in review_result.lower():
            print(f"Reviewing {content_type} content... Approved by QA.")
            return True
        else:
            print(f"Reviewing {content_type} content... Rejected by QA.\nReason: {review_result}")
            return False


