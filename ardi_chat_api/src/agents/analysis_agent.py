from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class AnalysisAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("Ardi_agent/prompts/analysis_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def gather_and_analyze(self, idea_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        response = self.client.generate_content(self.prompt + "\n" + idea_content)
        analysis = response
        return analysis

    def save_analysis_content(self, content: str):
        with open("/home/ubuntu/Ardi_agent/analysis.md", "w") as f:
            f.write(content)
        print("Analysis content saved to analysis.md")


