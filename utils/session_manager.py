import json
import os
from datetime import datetime

class SessionManager:
    def __init__(self, session_id: str = None):
        self.session_id = session_id if session_id else datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_dir = os.path.join("sessions", self.session_id)
        os.makedirs(self.session_dir, exist_ok=True)
        self.history_file = os.path.join(self.session_dir, "history.json")
        self.actions_file = os.path.join(self.session_dir, "actions.json")
        self.llm_history = self._load_history(self.history_file)
        self.agent_actions = self._load_history(self.actions_file)

    def _load_history(self, file_path: str):
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        return []

    def _save_history(self, data, file_path: str):
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add_llm_interaction(self, prompt: str, response: str, model: str):
        self.llm_history.append({
            "timestamp": datetime.now().isoformat(),
            "type": "llm_interaction",
            "prompt": prompt,
            "response": response,
            "model": model
        })
        self._save_history(self.llm_history, self.history_file)

    def add_agent_action(self, agent_name: str, action_name: str, inputs: dict, outputs: dict):
        self.agent_actions.append({
            "timestamp": datetime.now().isoformat(),
            "type": "agent_action",
            "agent_name": agent_name,
            "action_name": action_name,
            "inputs": inputs,
            "outputs": outputs
        })
        self._save_history(self.agent_actions, self.actions_file)

    def get_llm_history(self):
        return self.llm_history

    def get_agent_actions(self):
        return self.agent_actions

    def get_session_id(self):
        return self.session_id



