from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.quez_tool import quez_tool
from tools.finish_tool import finish_tool
from tools.file_manager import FileManager

class LanguageExpert:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/language_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def formalize_query(self, query: str, clarify_md_attached: bool = False) -> str:
        if clarify_md_attached:
            # If clarify.md is attached, it means the user wants to start from communication agent (step 2)
            # The orchestrator should handle this by calling the Clarification Agent directly.
            # This method is for formalizing the initial query.
            return "Clarify.md attached. Please proceed to the Clarification Agent."

        self.rate_limiter.wait_for_next_call()
        formalized_query = self.client.generate_content(self.prompt + "\n" + query)

        while True:
            response = quez_tool(f"Your formalized query is: {formalized_query}. Is this correct?", options=["Yes", "No"])
            if response == "Yes":
                self.file_manager.write_file("Query.md", formalized_query)
                finish_tool()
                return formalized_query
            else:
                formalized_query = self.client.generate_content(self.prompt + "\n" + "User wants to refine the query. Original query: " + query + "\nPrevious formalized query: " + formalized_query + "\nPlease refine the query based on user\"s implicit feedback.")



