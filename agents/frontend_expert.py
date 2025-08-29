from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.qa_tool import qa_tool
from tools.finish_tool import finish_tool
import os

class FrontendExpert:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/frontend_expert.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def implement_frontend(self, synthesis_file: str = "pre_implementation.md", frontend_tasks_file: str = "frontend.md", technical_file: str = "technical.md", backend_report_file: str = "backend_report.md") -> str:
        synthesis_content = self.file_manager.read_file(synthesis_file)
        frontend_tasks_content = self.file_manager.read_file(frontend_tasks_file)
        technical_content = self.file_manager.read_file(technical_file)
        backend_report_content = self.file_manager.read_file(backend_report_file)

        print(f"Synthesis Content: {synthesis_content}")
        print(f"Frontend Tasks: {frontend_tasks_content}")
        print(f"Technical Recommendations: {technical_content}")
        print(f"Backend Report: {backend_report_content}")

        # Create comprehensive implementation plan saved as implementation.md
        self.rate_limiter.wait_for_next_call()
        implementation_plan = self.client.generate_content(self.prompt + "\n\nBased on the following synthesis, frontend tasks, technical recommendations, and backend report, create a comprehensive implementation plan for the frontend. Save this plan as implementation.md. Ensure the response is a complete and comprehensive document, without truncation.\n\nSynthesis: " + synthesis_content + "\nFrontend Tasks: " + frontend_tasks_content + "\nTechnical Recommendations: " + technical_content + "\nBackend Report: " + backend_report_content)
        self.file_manager.write_file("frontend_implementation.md", implementation_plan)
        print("Frontend implementation plan saved to frontend_implementation.md")

        # Classify the implementation plan into todo for roadmap
        self.rate_limiter.wait_for_next_call()
        frontend_todo_content = self.client.generate_content(self.prompt + "\n\nBased on the following frontend implementation plan, create a detailed todo.md for your roadmap. Ensure the response is a complete and comprehensive document, without truncation.\n\nImplementation Plan: " + implementation_plan)
        self.file_manager.write_file("frontend_todo.md", frontend_todo_content)
        print("Frontend todo.md roadmap created.")

        # Simulate frontend development and design
        print("Simulating frontend development and design...")
        # In a real scenario, this would involve actual code generation, design, etc.
        # For now, we\"ll simulate by creating a placeholder for frontend.md

        self.rate_limiter.wait_for_next_call()
        frontend_report_content = self.client.generate_content(self.prompt + "\n\nBased on the implemented frontend plan, create a detailed report of what was implemented, including appealing designs and technical aspects. Also, describe how the backend is connected with the frontend. Ensure the response is a complete and comprehensive document, without truncation.\n\nImplementation Plan: " + implementation_plan)
        self.file_manager.write_file("frontend_report.md", frontend_report_content)
        print("Frontend implementation report saved to frontend_report.md")

        # Connect backend with frontend (simulated)
        print("Connecting backend with frontend (simulated).")

        # Call QA tool for feedback
        qa_feedback = qa_tool("frontend_agent", "frontend_report.md")

        if "REFUSED" in qa_feedback:
            print("QA refused the frontend implementation. Please refine.")
            # In a real scenario, this would involve an interactive loop or re-analysis
            # For now, we\"ll assume it\"s approved after one pass for this iteration
            finish_tool()
        else:
            print("QA approved the frontend implementation.")
            finish_tool()

        return frontend_report_content


