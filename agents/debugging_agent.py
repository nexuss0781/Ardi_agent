from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.finish_tool import finish_tool
from tools.debug_tool import debug_tool

class DebuggingAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/debugging_agent.md", "r") as f:
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
        
        # In a real scenario, this agent would dynamically decide to use tools
        # based on the debug_report or its internal reasoning.
        # For now, we'll simulate the debugging process and then call continue_work.
        print(f"Debugging Agent Report: {debug_report}")

        # Simulate that the issue is resolved and acknowledge the current agent
        # In a real scenario, this would be a more complex logic to determine if the issue is truly resolved.
        debug_tool("Debugging Agent has analyzed the issue and provided a report. Assuming issue is resolved for now.")
        finish_tool() # This will act as continue_work for the calling agent

        return debug_report


