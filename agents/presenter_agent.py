class PresenterAgent:
    def __init__(self):
        pass

    def present_phase_summary(self, phase_name: str, summary_content: str) -> str:
        # This is a placeholder for the actual implementation.
        # In a real scenario, this would involve presenting the summary to the user
        # and awaiting confirmation.
        presentation = f"## {phase_name} Summary\n\n"
        presentation += f"{summary_content}\n\n"
        presentation += "_Awaiting user confirmation to proceed to the next phase._"
        return presentation

    def save_presentation_content(self, content: str, filename: str = "phase_summary.md"):
        with open(f"/home/ubuntu/ardi_agent/{filename}", "w") as f:
            f.write(content)
        print(f"Presentation content saved to {filename}")


