from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class SynthesizerAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/synthesizer_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def synthesize_content(self, idea_content: str, analysis_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        combined_content = f"Ideas:\n{idea_content}\n\nAnalysis:\n{analysis_content}"
        synthesized_content = self.client.generate_content(self.prompt + "\n" + combined_content)
        return synthesized_content

    def save_synthesized_content(self, content: str, filename: str = "synthesis.md"):
        with open("/home/ubuntu/Ardi_agent/synthesis.md", "w") as f:
            f.write(content)
        print("Synthesized content saved to synthesis.md")


