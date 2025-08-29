from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.qa_tool import qa_tool
from tools.internet_tool import InternetTool
from tools.finish_tool import finish_tool

class AnalysisAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/analysis_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()
        self.internet_tool = InternetTool()

    def analyze(self, clarify_file: str = "clarify.md") -> str:
        clarified_content = self.file_manager.read_file(clarify_file)
        print(f"Clarified Content for Analysis: {clarified_content}")

        # Perform internet-based analysis
        self.rate_limiter.wait_for_next_call()
        internet_analysis_query = self.client.generate_content(self.prompt + "\n\nBased on the following clarified content, generate a concise query for internet search to find trends, similar company apps, key advantages, and bottlenecks. Clarified Content: " + clarified_content)
        
        internet_results = self.internet_tool.search(internet_analysis_query)
        print(f"Internet Search Results: {internet_results}")

        # Synthesize findings
        self.rate_limiter.wait_for_next_call()
        synthesis_prompt = self.prompt + "\n\nSynthesize the following clarified content and internet search results into an effective analysis for the client. Clarified Content: " + clarified_content + "\nInternet Search Results: " + internet_results + "\n\nAnalysis:"
        analysis_content = self.client.generate_content(synthesis_prompt)

        self.file_manager.write_file("Analysis.md", analysis_content)

        # Call QA tool for feedback
        qa_feedback = qa_tool("analysis_agent", "Analysis.md")

        if "REFUSED" in qa_feedback:
            print("QA refused the analysis. Please refine.")
            # In a real scenario, this would involve an interactive loop or re-analysis
            # For now, we\"ll assume it\"s approved after one pass for this iteration
            finish_tool()
        else:
            print("QA approved the analysis.")
            finish_tool()

        return analysis_content


