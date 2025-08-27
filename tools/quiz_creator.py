from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter

class QuizCreator:
    def __init__(self):
        self.client = LLMClient()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def create_quiz(self, topic: str, num_questions: int) -> str:
        self.rate_limiter.wait_for_next_call()
        prompt = f"Generate a {num_questions}-question quiz on the topic of \n\'{topic}\
'. For each question, provide the question and the answer."
        quiz_content = self.client.generate_content(f"You are a quiz generator. Create clear and concise quiz questions and answers." + "\n" + prompt)
        return quiz_content


