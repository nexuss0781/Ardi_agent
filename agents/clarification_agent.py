import json
from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.quez_tool import quez_tool
from tools.finish_tool import finish_tool
from tools.file_manager import FileManager
import os

class ClarificationAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/clarification_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def clarify_query(self, query_file: str = "Query.md", clarify_file: str = None) -> str:
        if clarify_file and self.file_manager.file_exists(clarify_file):
            # If clarify.md is provided by orchestrator, read it and proceed
            clarify_content = self.file_manager.read_file(clarify_file)
            # Here, the agent should analyze the clarify_content and ensure all questions are addressed.
            # For now, we'll assume it's clear enough if the file exists.
            # In a real scenario, this would involve more complex LLM interaction to verify clarity.
            print(f"Clarify.md provided: {clarify_content}")
            # If clear, just call finish_task
            self.summarize_and_confirm(clarify_content)
            return clarify_content

        # Read the initial query from Query.md
        initial_query = self.file_manager.read_file(query_file)
        print(f"Initial Query: {initial_query}")

        clarification_areas = [
            "Comprehensivity of the project",
            "Similar app existence and user's preference",
            "Features user explicitly doesn't want",
            "Specific UI/UX layout or component needs",
            "Constraints (e.g., budget, timeline, technology stack)"
        ]

        clarified_points = []
        for area in clarification_areas:
            self.rate_limiter.wait_for_next_call()
            clarification_prompt = self.prompt + f"\n\nBased on the query: '{initial_query}', please clarify the following area: {area}. If the query is already clear on this point, state 'No further clarification needed for this area.'. Otherwise, ask a precise question to get the necessary information.\n\nClarification for {area}:"
            response = self.client.generate_content(clarification_prompt)
            print(f"Clarification for {area}: {response}")
            if "No further clarification needed" not in response:
                # In a real scenario, this would involve an interactive loop with the user via quez_tool
                # For now, we'll simulate a direct clarification based on the LLM's response
                clarified_points.append(f"- {area}: {response}")

        final_clarification = f"Initial Query: {initial_query}\n\nClarified Points:\n" + "\n".join(clarified_points)
        if not clarified_points:
            final_clarification = f"Initial Query: {initial_query}\n\nNo further clarifications were needed. The query is clear."

        self.summarize_and_confirm(final_clarification)
        return final_clarification

    def summarize_and_confirm(self, content_to_summarize: str):
        self.rate_limiter.wait_for_next_call()
        summary_prompt = self.prompt + f"\n\nSummarize the following user needs and clarifications concisely, then ask if this summary is correct. Summary to be confirmed: {content_to_summarize}"
        summary = self.client.generate_content(summary_prompt)

        response = quez_tool(f"Is this summary correct?\n\n{summary}", options=["Yes", "No"])
        if response == "Yes":
            self.file_manager.write_file("create.md", content_to_summarize)
            # Simulate moving the file to private_dir. In a real orchestrator, this would be handled externally.
            # For now, we'll just print a message.
            print("create.md moved to private_dir (simulated by orchestrator).")
            finish_tool()
        else:
            print("User disagreed with the summary. Please re-run the clarification process or provide more details.")
            # In a real scenario, this would loop back or ask for more input.



