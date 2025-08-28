from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class DebuggingAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("Ardi_agent/prompts/debugging_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def debug_issues(self, issue_description: str) -> str:
        self.rate_limiter.wait_for_next_call()
        
        # Enhanced prompt for debugging
        debug_prompt = self.prompt + "\n\n" + \
                       "Analyze the following issue description and provide a detailed debug report. " + \
                       "Include potential causes, steps to reproduce (if applicable), and actionable solutions. " + \
                       "If external tools (like file reader or shell commands) would be useful, suggest their use.\n\nIssue: " + issue_description
        
        debug_report = self.client.generate_content(debug_prompt)
        
        # Placeholder for actual tool integration logic
        # In a real scenario, this agent would dynamically decide to use tools
        # based on the debug_report or its internal reasoning.
        if "suggested_tool_use" in debug_report.lower():
            print("DebuggingAgent: Detected suggestion for tool use. (Placeholder for tool execution)")
            # Example: if the LLM suggests reading a log file, the agent would call a file reading tool here.

        return debug_report


