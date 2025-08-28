import json
from utils.llm_client import LLMClient
from utils.rate_limiter import RateLimiter
from utils.session_manager import SessionManager

class ClarificationAgent:
    def __init__(self, session_manager: SessionManager = None):
        with open("prompts/clarification_agent.md", "r") as f:
            self.prompt = f.read()
        self.client = LLMClient(session_manager=session_manager)
        self.rate_limiter = RateLimiter(calls_per_minute=10) # Adjust rate limit as needed
        self.clarification_todo = {
            "Audience": False,
            "Comprehensive": False
        }

    def clarify_objectives(self, query: str) -> str:
        self.rate_limiter.wait_for_next_call()
        # Instruct the LLM to output clarification needs in a structured format (JSON)
        llm_prompt = self.prompt + "\n\n" + \
                     "Based on the following query, identify any ambiguities or missing information. " + \
                     "Respond with a JSON object indicating whether 'Audience' and 'Comprehensive' aspects are clear. " + \
                     "Example: {\"Audience\": true, \"Comprehensive\": false}\n\nQuery: " + query
        
        clarified_response = self.client.generate_content(llm_prompt)
        
        try:
            # Attempt to parse the LLM's response as JSON
            clarification_status = json.loads(clarified_response)
            if isinstance(clarification_status, dict):
                self.clarification_todo["Audience"] = clarification_status.get("Audience", False)
                self.clarification_todo["Comprehensive"] = clarification_status.get("Comprehensive", False)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse clarification status from LLM response: {clarified_response}")
            # Fallback: if JSON parsing fails, assume some clarification is needed
            self.clarification_todo["Audience"] = False
            self.clarification_todo["Comprehensive"] = False

        # Generate a more detailed clarified content based on the original prompt and LLM's understanding
        detailed_clarification_prompt = self.prompt + "\n\n" + \
                                        "Based on the query: \"" + query + "\", provide a clarified version. " + \
                                        "If there are still ambiguities (as per clarification_todo), mention them. " + \
                                        "Clarification Status: " + str(self.clarification_todo) + "\n\nClarified Content: "
        clarified_content = self.client.generate_content(detailed_clarification_prompt)

        return clarified_content

    def get_clarification_todo(self):
        return self.clarification_todo

    def save_clarified_content(self, content: str):
        with open("/home/ubuntu/Ardi_agent/clarify.md", "w") as f:
            f.write(content)
        print("Clarified content saved to clarify.md")


