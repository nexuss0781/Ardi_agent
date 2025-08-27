from orchestrator import Orchestrator

if __name__ == "__main__":
    initial_query = "Develop a web application for managing tasks."
    orchestrator = Orchestrator()
    orchestrator.run_workflow(initial_query)


