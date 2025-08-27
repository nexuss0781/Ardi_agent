from openai import OpenAI
from utils.rate_limiter import RateLimiter

class SynthesizerAgent:
    def __init__(self):
        with open("Ardi_agent/prompts/synthesizer_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def synthesize_content(self, idea_content: str, analysis_content: str) -> str:
        self.rate_limiter.wait_for_next_call()
        combined_content = f"Ideas:\n{idea_content}\n\nAnalysis:\n{analysis_content}"
        response = self.client.chat.completions.create(
            model="gemini-2.5-flash", # Or another suitable model
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": combined_content}
            ]
        )
        synthesized_content = response.choices[0].message.content
        return synthesized_content

    def save_synthesized_content(self, content: str, filename: str = "synthesis.md"):
        with open("/home/ubuntu/ardi_agent/synthesis.md", "w") as f:
            f.write(content)
        print("Synthesized content saved to synthesis.md")


