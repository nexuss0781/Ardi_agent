from agents.debugging_agent import DebuggingAgent
from utils.session_manager import SessionManager

class DebugTool:
    def __init__(self, session_manager: SessionManager = None):
        self.debugging_agent = DebuggingAgent(session_manager=session_manager)

    def debug(self, error_message: str, context: str = "") -> str:
        """
        Calls the DebuggingAgent to analyze and suggest solutions for an error.
        Args:
            error_message (str): The error message or description of the issue.
            context (str): Additional context related to the error (e.g., traceback, relevant code).
        Returns:
            str: A report from the DebuggingAgent with analysis and suggested solutions.
        """
        issue_description = f"Error: {error_message}\nContext: {context}"
        debug_report = self.debugging_agent.debug_issues(issue_description)
        return debug_report


