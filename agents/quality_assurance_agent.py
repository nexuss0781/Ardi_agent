from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class QualityAssuranceAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("Ardi_agent/prompts/quality_assurance_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def review_content(self, content: str, content_type: str) -> bool:
        self.rate_limiter.wait_for_next_call()
        
        # Enhanced prompt for QA review, asking for specific reasons for rejection
        qa_prompt = self.prompt + "\n\n" + \
                    f"Review the following {content_type} content. " + \
                    "State clearly if it is \"Approved\" or \"Rejected\". " + \
                    "If rejected, provide specific reasons and suggestions for improvement. " + \
                    f"\n\nContent Type: {content_type}\nContent: {content}"
        
        review_result = self.client.generate_content(qa_prompt)
        
        if "approved" in review_result.lower():
            print(f"Reviewing {content_type} content... Approved by QA.")
            return True
        else:
            print(f"Reviewing {content_type} content... Rejected by QA.\nReason: {review_result}")
            # In a more advanced system, this 'review_result' could be parsed
            # and fed back to the generating agent for iterative refinement.
            return False


