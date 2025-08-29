from agents.quality_assurance_agent import QualityAssuranceAgent
from utils.session_manager import SessionManager

class QATool:
    def __init__(self, session_manager: SessionManager = None):
        self.qa_agent = QualityAssuranceAgent(session_manager=session_manager)

    def review(self, agent_name: str, file_to_review: str) -> str:
        return self.qa_agent.review(agent_name, file_to_review)


def qa_tool(agent_name: str, file_to_review: str) -> str:
    # This is a wrapper function to make it callable directly as qa_tool()
    # In a real system, the orchestrator would instantiate QATool and call its review method.
    # For simulation purposes, we'll create a temporary instance.
    temp_qa_tool = QATool()
    return temp_qa_tool.review(agent_name, file_to_review)


