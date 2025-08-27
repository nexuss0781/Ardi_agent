from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class ChattingTool:
    def __init__(self):
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def send_message(self, recipient: str, message: str) -> str:
        self.rate_limiter.wait_for_next_call()
        # In a real scenario, this would involve sending a message to a user or another agent.
        # For now, we\'ll use LLM to simulate a response from the recipient.
        prompt = f"Simulate a response from {recipient} to the message: \n\'{message}\'"
        response = self.client.generate_content(f"You are simulating a chat participant named {recipient}. Respond concisely to the user\'s message." + "\n" + prompt)
        return f"Message sent to {recipient}. Simulated response from {recipient}: {response}"

    def receive_message(self, sender: str) -> str:
        # This is a placeholder for the actual implementation.
        # In a real scenario, this would involve receiving a message from a user or another agent.
        return f"Message received from {sender}: Hello from {sender}! (simulated)"


