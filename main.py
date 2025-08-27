from agents.language_expert import LanguageExpert
from agents.clarification_agent import ClarificationAgent
from agents.idea_generator import IdeaGenerator
from agents.analysis_agent import AnalysisAgent
from agents.synthesizer_agent import SynthesizerAgent
from agents.report_agent import ReportAgent
from agents.organizer_agent import OrganizerAgent
from agents.presenter_agent import PresenterAgent
from agents.quality_assurance_agent import QualityAssuranceAgent
from agents.tasker_agent import TaskerAgent
from agents.backend_expert import BackendExpert
from agents.frontend_expert import FrontendExpert
from agents.fullstack_expert import FullstackExpert

def run_phase1(user_query: str):
    print("--- Phase 1: Query Processing ---")

    # Initialize agents
    lang_expert = LanguageExpert()
    clar_agent = ClarificationAgent()
    idea_gen = IdeaGenerator()
    analysis_agent = AnalysisAgent()
    synth_agent = SynthesizerAgent()
    report_agent = ReportAgent()
    org_agent = OrganizerAgent()
    pres_agent = PresenterAgent()
    qa_agent = QualityAssuranceAgent()

    # 1. Language Expert
    formalized_query = lang_expert.formalize_query(user_query)
    print(f"Language Expert Output: {formalized_query}")

    # 2. Clarification Agent
    clarified_content = clar_agent.clarify_objectives(formalized_query)
    clar_agent.save_clarified_content(clarified_content)
    print(f"Clarification Agent Output:\n{clarified_content}")
    print(f"Clarification ToDo: {clar_agent.get_clarification_todo()}")

    # 3. Idea Generator
    idea_content = idea_gen.generate_features(clarified_content)
    idea_gen.save_idea_content(idea_content)
    print(f"Idea Generator Output:\n{idea_content}")

    # 4. Quality Assurance (after Idea Generation)
    if qa_agent.review_content(idea_content, "Idea"): 
        print("Idea content approved by QA.")
    else:
        print("Idea content rejected by QA. Aborting.")
        return

    # 5. Analysis Agent
    analysis_content = analysis_agent.gather_and_analyze(idea_content)
    analysis_agent.save_analysis_content(analysis_content)
    print(f"Analysis Agent Output:\n{analysis_content}")

    # 6. Quality Assurance (after Analysis)
    if qa_agent.review_content(analysis_content, "Analysis"): 
        print("Analysis content approved by QA.")
    else:
        print("Analysis content rejected by QA. Aborting.")
        return

    # 7. Synthesizer Agent
    synthesized_content = synth_agent.synthesize_content(idea_content, analysis_content)
    synth_agent.save_synthesized_content(synthesized_content)
    print(f"Synthesizer Agent Output:\n{synthesized_content}")

    # 8. Report Agent
    roadmap_report = report_agent.generate_roadmap(synthesized_content)
    report_agent.save_report_content(roadmap_report, "pre_implementation_report.md")
    print(f"Report Agent Output (Pre-implementation):\n{roadmap_report}")

    # 9. Organizer Agent
    organized_synthesis = org_agent.beautify_content(synthesized_content)
    org_agent.save_organized_content(organized_synthesis, "organized_synthesis.md")
    print(f"Organizer Agent Output:\n{organized_synthesis}")

    # 10. Presenter Agent
    phase1_summary = "Phase 1 (Query Processing) completed successfully. We have formalized the query, clarified objectives, generated initial ideas, performed market analysis, synthesized findings, and created a pre-implementation roadmap."
    presentation = pres_agent.present_phase_summary("Phase 1 Summary", phase1_summary)
    pres_agent.save_presentation_content(presentation, "phase1_summary.md")
    print(f"Presenter Agent Output:\n{presentation}")

    print("--- Phase 1: Query Processing Completed ---")
    return synthesized_content

def run_phase2(synthesized_content: str):
    print("\n--- Phase 2: Implementation Phase ---")

    # Initialize agents
    tasker_agent = TaskerAgent()
    backend_expert = BackendExpert()
    frontend_expert = FrontendExpert()
    fullstack_expert = FullstackExpert()
    qa_agent = QualityAssuranceAgent()
    report_agent = ReportAgent()
    synth_agent = SynthesizerAgent()
    org_agent = OrganizerAgent()
    pres_agent = PresenterAgent()

    # 1. Tasker Agent
    tasks = tasker_agent.classify_features(synthesized_content)
    backend_tasks = tasks["backend"]
    frontend_tasks = tasks["frontend"]
    print(f"Tasker Agent Output - Backend Tasks: {backend_tasks}")
    print(f"Tasker Agent Output - Frontend Tasks: {frontend_tasks}")

    # 2. Backend Expert
    backend_summary = backend_expert.develop_backend(backend_tasks)
    backend_expert.save_backend_summary(backend_summary)
    print(f"Backend Expert Output:\n{backend_summary}")

    # 3. Quality Assurance (after Backend Development)
    if qa_agent.review_content(backend_summary, "Backend"): 
        print("Backend development approved by QA.")
    else:
        print("Backend development rejected by QA. Aborting.")
        return

    # 4. Frontend Expert
    frontend_summary = frontend_expert.develop_frontend(frontend_tasks)
    frontend_expert.save_frontend_summary(frontend_summary)
    print(f"Frontend Expert Output:\n{frontend_summary}")

    # 5. Fullstack Expert
    fullstack_report = fullstack_expert.check_integrity(backend_summary, frontend_summary)
    print(f"Fullstack Expert Output:\n{fullstack_report}")

    # 6. Report Agent (Post-implementation)
    post_impl_report = report_agent.generate_roadmap(fullstack_report) # Reusing generate_roadmap for post-impl report
    report_agent.save_report_content(post_impl_report, "post_implementation_report.md")
    print(f"Report Agent Output (Post-implementation):\n{post_impl_report}")

    # 7. Synthesizing Agent (Post-implementation)
    post_synthesized_content = synth_agent.synthesize_content(backend_summary, frontend_summary) # Reusing for post-impl synthesis
    synth_agent.save_synthesized_content(post_synthesized_content, "post_synthesis.md")
    print(f"Post-implementation Synthesizer Agent Output:\n{post_synthesized_content}")

    # 8. Organizer Agent (Phase 2)
    organized_post_synthesis = org_agent.beautify_content(post_synthesized_content)
    org_agent.save_organized_content(organized_post_synthesis, "organized_post_synthesis.md")
    print(f"Organizer Agent Output (Phase 2):\n{organized_post_synthesis}")

    # Debugging Agent (Placeholder - actual implementation would involve more logic)
    # debug_agent = DebuggingAgent()
    # debug_agent.debug_issues()

    # 9. Presenter Agent (Phase 2)
    phase2_summary = "Phase 2 (Implementation) completed successfully. We have classified tasks, developed backend and frontend, performed fullstack integration, and generated post-implementation reports."
    presentation = pres_agent.present_phase_summary("Phase 2 Summary", phase2_summary)
    pres_agent.save_presentation_content(presentation, "phase2_summary.md")
    print(f"Presenter Agent Output:\n{presentation}")

    print("--- Phase 2: Implementation Phase Completed ---")

if __name__ == "__main__":
    initial_query = "Develop a web application for managing tasks."
    synthesized_content_from_phase1 = run_phase1(initial_query)
    if synthesized_content_from_phase1:
        run_phase2(synthesized_content_from_phase1)


