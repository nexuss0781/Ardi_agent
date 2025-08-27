import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.session_manager import SessionManager

load_dotenv()

class LLMClient:
    def __init__(self, session_manager: SessionManager = None):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.session_manager = session_manager

    def generate_content(self, prompt: str):
        try:
            response = self.model.generate_content(prompt)
            if self.session_manager:
                self.session_manager.add_llm_interaction(prompt, response.text, "gemini-1.5-flash")
            return response.text
        except Exception as e:
            print(f"Error generating content with Gemini: {e}")
            return None


