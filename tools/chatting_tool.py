from openai import OpenAI
from utils.rate_limiter import RateLimiter

class ChattingTool:
    def __init__(self):
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def send_message(self, recipient: str, message: str) -> str:
        self.rate_limiter.wait_for_next_call()
        # In a real scenario, this would involve sending a message to a user or another agent.
        # For now, we'll use LLM to simulate a response from the recipient.
        prompt = f"Simulate a response from {recipient} to the message: 
'{message}'"
        response = self.client.chat.completions.create(
            model="gpt-4o", # Or another suitable model
            messages=[
                {"role": "system", "content": f"You are simulating a chat participant named {recipient}. Respond concisely to the user's message."},
                {"role": "user", "content": prompt}
            ]
        )
        return f"Message sent to {recipient}. Simulated response from {recipient}: {response.choices[0].message.content}"

    def receive_message(self, sender: str) -> str:
        # This is a placeholder for the actual implementation.
        # In a real scenario, this would involve receiving a message from a user or another agent.
        return f"Message received from {sender}: Hello from {sender}! (simulated)"


