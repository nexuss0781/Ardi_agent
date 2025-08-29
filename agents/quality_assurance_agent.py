from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager
from tools.file_manager import FileManager
from tools.chat_tool import chat_tool
from tools.qa_tool import qa_tool # Importing qa_tool to use its APPROVED/REFUSED signals

class QualityAssuranceAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/quality_assurance_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.file_manager = FileManager()

    def review(self, agent_name: str, file_to_review: str) -> str:
        content_to_review = self.file_manager.read_file(file_to_review)
        print(f"QA Agent: Reviewing {file_to_review} for {agent_name}.")

        # Create internal todo.md checker for deep test of quality
        internal_qa_todo = f"## QA Internal Todo for {agent_name}\n\n- [ ] Review content of {file_to_review}\n- [ ] Check against specific criteria for {agent_name}\n- [ ] Provide feedback (points out of 10)\n- [ ] Determine APPROVED/REFUSED\n"
        self.file_manager.write_file(f"qa_todo_{agent_name}.md", internal_qa_todo)

        self.rate_limiter.wait_for_next_call()
        # The QA agent's prompt should guide it to act as a client and argue for quality/feasibility.
        # It should also consider the specific criteria for each agent.
        qa_review_prompt = self.prompt + f"\n\nReview the following content from {agent_name} (file: {file_to_review}). Act as a client and argue for quality and feasibility. The criteria for this agent are: [Specify criteria based on agent_name, e.g., for Idea Generator: implementation features recommendations without internet tool; for Analysis Agent: justifies using internet tool for final features; for Backend Agent: tech stack selection correctness, SQL injection, bad codes; for Frontend Agent: aesthetic, color palettes, other frontend work].\n\nContent to review:\n{content_to_review}\n\nProvide your feedback, outlining points out of 10. If excellent, give 10 points and use the APPROVED tool. If not, reduce points and provide clear refinement areas, then use the REFUSED tool. If you need to discuss, use the chat_tool.\n\nQA Review:"

        qa_feedback = self.client.generate_content(qa_review_prompt)
        print(f"QA Feedback: {qa_feedback}")

        # Save suggestion as [agent_name]_qa.md
        self.file_manager.write_file(f"{agent_name}_qa.md", qa_feedback)

        # Simulate review_suggestion tool (placeholder)
        print(f"Simulating review_suggestion tool for {agent_name}_qa.md")

        # Determine if APPROVED or REFUSED based on LLM's feedback
        if "APPROVED" in qa_feedback.upper() and "10/10" in qa_feedback:
            print("QA: Excellent. APPROVED.")
            return "APPROVED"
        elif "REFUSED" in qa_feedback.upper():
            print("QA: REFUSED. Refinement needed.")
            return "REFUSED"
        else:
            # If neither explicitly approved nor refused, assume chat is needed or further refinement
            print("QA: Feedback provided. May require chat or further refinement.")
            # Simulate chat if needed
            # chat_tool("qa_agent", agent_name, ["Let's discuss this further."])
            return "NEEDS_REVIEW"


