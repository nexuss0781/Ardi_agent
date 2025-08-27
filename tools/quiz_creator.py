from openai import OpenAI
from utils.rate_limiter import RateLimiter

class QuizCreator:
    def __init__(self):
        self.client = OpenAI()
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed

    def create_quiz(self, topic: str, num_questions: int) -> str:
        self.rate_limiter.wait_for_next_call()
        prompt = f"Generate a {num_questions}-question quiz on the topic of 
'{topic}'. For each question, provide the question and the answer."
        response = self.client.chat.completions.create(
            model="gpt-4o", # Or another suitable model
            messages=[
                {"role": "system", "content": "You are a quiz generator. Create clear and concise quiz questions and answers."},
                {"role": "user", "content": prompt}
            ]
        )
        quiz_content = response.choices[0].message.content
        return quiz_content


