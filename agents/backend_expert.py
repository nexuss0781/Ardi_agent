class BackendExpert:
    def __init__(self):
        with open("prompts/backend_expert.md", "r") as f:
            self.prompt = f.read()

    def develop_backend(self, backend_tasks: list) -> str:
        # This is a placeholder for the actual implementation.
        # In a real scenario, this would involve writing actual backend code
        # based on the provided tasks.
        backend_summary = "Backend development completed for the following tasks:\n"
        for task in backend_tasks:
            backend_summary += f"- {task}\n"
        backend_summary += "\nBackend code and API endpoints are ready."
        return backend_summary

    def save_backend_summary(self, content: str):
        with open("/home/ubuntu/ardi_agent/backend.md", "w") as f:
            f.write(content)
        print("Backend summary saved to backend.md")


