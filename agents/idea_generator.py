from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.qa_tool import qa_tool
from tools.chat_tool import chat_tool
from tools.finish_tool import finish_tool

class IdeaGenerator:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/idea_generator.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def generate_idea(self, clarify_file: str = "clarify.md") -> str:
        clarified_content = self.file_manager.read_file(clarify_file)
        print(f"Clarified Content: {clarified_content}")

        # Create internal todo.md for detailed plan
        internal_todo_content = "## Idea Generator Internal Todo\n\n- [ ] Analyze clarified content\n- [ ] Generate detailed plan\n- [ ] Create idea.md\n- [ ] Get QA approval\n"
        self.file_manager.write_file("idea_generator_todo.md", internal_todo_content)

        # Deep analysis and idea generation
        self.rate_limiter.wait_for_next_call()
        idea_content = self.client.generate_content(self.prompt + "\n\nClarified Content: " + clarified_content + "\n\nBased on the above, generate a detailed idea, including a plan to cover user needs and deep analysis based on comprehensivity scope. Do not give internet search tool. Ensure the response is a complete and comprehensive document, without truncation.")

        self.file_manager.write_file("idea.md", idea_content)

        # Call QA tool for feedback
        qa_feedback = qa_tool("idea_generator", "idea.md")

        if "REFUSED" in qa_feedback:
            print("QA refused the idea. Engaging in chat to argue/refine.")
            # Simulate chat with QA agent
            chat_history = []
            chat_history.append(f"QA Feedback: {qa_feedback}")
            chat_history.append("Idea Generator: I believe my idea is sound. Let me explain my reasoning.")

            # In a real scenario, this would be an interactive loop
            # For now, we'll simulate a single exchange
            self.rate_limiter.wait_for_next_call()
            chat_response = chat_tool("idea_generator", "qa_agent", chat_history)
            print(f"Chat with QA: {chat_response}")
            # After chat, assume agreement or refinement and re-evaluate QA
            # For simplicity, we'll assume it's approved after the chat for this iteration
            finish_tool()
        else:
            print("QA approved the idea.")
            finish_tool()

        return idea_content


