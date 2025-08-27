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
from agents.debugging_agent import DebuggingAgent
from utils.session_manager import SessionManager
from utils.llm_client import LLMClient
from utils.tool_manager import ToolManager

class Orchestrator:
    def __init__(self):
        self.session_manager = SessionManager()
        self.tool_manager = ToolManager(session_manager=self.session_manager)

    def run_workflow(self, initial_query: str):
        print("Orchestrator: Starting workflow...")

        # Initialize agents with session manager
        lang_expert = LanguageExpert(session_manager=self.session_manager)
        clar_agent = ClarificationAgent(session_manager=self.session_manager)
        idea_gen = IdeaGenerator(session_manager=self.session_manager)
        analysis_agent = AnalysisAgent(session_manager=self.session_manager)
        synth_agent = SynthesizerAgent(session_manager=self.session_manager)
        report_agent = ReportAgent(session_manager=self.session_manager)
        org_agent = OrganizerAgent(session_manager=self.session_manager)
        pres_agent = PresenterAgent(session_manager=self.session_manager)
        qa_agent = QualityAssuranceAgent(session_manager=self.session_manager)
        tasker_agent = TaskerAgent(session_manager=self.session_manager)
        backend_expert = BackendExpert(session_manager=self.session_manager)
        frontend_expert = FrontendExpert(session_manager=self.session_manager)
        fullstack_expert = FullstackExpert(session_manager=self.session_manager)
        debug_agent = DebuggingAgent(session_manager=self.session_manager)

        # Phase 1: Query Processing
        print("--- Phase 1: Query Processing ---")

        try:
            # 1. Language Expert
            formalized_query = lang_expert.formalize_query(initial_query)
            print(f"Language Expert Output: {formalized_query}")
            self.session_manager.add_agent_action("LanguageExpert", "formalize_query", {"query": initial_query}, {"formalized_query": formalized_query})

            # 2. Clarification Agent
            clarified_content = clar_agent.clarify_objectives(formalized_query)
            clar_agent.save_clarified_content(clarified_content)
            print(f"Clarification Agent Output:\n{clarified_content}")
            print(f"Clarification ToDo: {clar_agent.get_clarification_todo()}")
            self.session_manager.add_agent_action("ClarificationAgent", "clarify_objectives", {"query": formalized_query}, {"clarified_content": clarified_content, "clarification_todo": clar_agent.get_clarification_todo()})

            # 3. Idea Generator
            idea_content = idea_gen.generate_features(clarified_content)
            idea_gen.save_idea_content(idea_content)
            print(f"Idea Generator Output:\n{idea_content}")
            self.session_manager.add_agent_action("IdeaGenerator", "generate_features", {"clarified_content": clarified_content}, {"idea_content": idea_content})

            # 4. Quality Assurance (after Idea Generation)
            if qa_agent.review_content(idea_content, "Idea"): 
                print("Idea content approved by QA.")
                self.session_manager.add_agent_action("QualityAssuranceAgent", "review_content", {"content": idea_content, "content_type": "Idea"}, {"status": "approved"})
            else:
                print("Idea content rejected by QA. Aborting.")
                self.session_manager.add_agent_action("QualityAssuranceAgent", "review_content", {"content": idea_content, "content_type": "Idea"}, {"status": "rejected"})
                return

            # 5. Analysis Agent
            analysis_content = analysis_agent.gather_and_analyze(idea_content)
            analysis_agent.save_analysis_content(analysis_content)
            print(f"Analysis Agent Output:\n{analysis_content}")
            self.session_manager.add_agent_action("AnalysisAgent", "gather_and_analyze", {"idea_content": idea_content}, {"analysis_content": analysis_content})

            # 6. Quality Assurance (after Analysis)
            if qa_agent.review_content(analysis_content, "Analysis"): 
                print("Analysis content approved by QA.")
                self.session_manager.add_agent_action("QualityAssuranceAgent", "review_content", {"content": analysis_content, "content_type": "Analysis"}, {"status": "approved"})
            else:
                print("Analysis content rejected by QA. Aborting.")
                self.session_manager.add_agent_action("QualityAssuranceAgent", "review_content", {"content": analysis_content, "content_type": "Analysis"}, {"status": "rejected"})
                return

            # 7. Synthesizer Agent
            synthesized_content = synth_agent.synthesize_content(idea_content, analysis_content)
            synth_agent.save_synthesized_content(synthesized_content)
            print(f"Synthesizer Agent Output:\n{synthesized_content}")
            self.session_manager.add_agent_action("SynthesizerAgent", "synthesize_content", {"idea_content": idea_content, "analysis_content": analysis_content}, {"synthesized_content": synthesized_content})

            # 8. Report Agent
            roadmap_report = report_agent.generate_roadmap(synthesized_content)
            report_agent.save_report_content(roadmap_report, "pre_implementation_report.md")
            print(f"Report Agent Output (Pre-implementation):\n{roadmap_report}")
            self.session_manager.add_agent_action("ReportAgent", "generate_roadmap", {"synthesis_content": synthesized_content}, {"roadmap_report": roadmap_report})

            # 9. Organizer Agent
            organized_synthesis = org_agent.beautify_content(synthesized_content)
            org_agent.save_organized_content(organized_synthesis, "organized_synthesis.md")
            print(f"Organizer Agent Output:\n{organized_synthesis}")
            self.session_manager.add_agent_action("OrganizerAgent", "beautify_content", {"content": synthesized_content}, {"organized_synthesis": organized_synthesis})

            # 10. Presenter Agent
            phase1_summary = "Phase 1 (Query Processing) completed successfully. We have formalized the query, clarified objectives, generated initial ideas, performed market analysis, synthesized findings, and created a pre-implementation roadmap."
            presentation = pres_agent.present_phase_summary("Phase 1 Summary", phase1_summary)
            pres_agent.save_presentation_content(presentation, "phase1_summary.md")
            print(f"Presenter Agent Output:\n{presentation}")
            self.session_manager.add_agent_action("PresenterAgent", "present_phase_summary", {"phase_name": "Phase 1 Summary", "summary_content": phase1_summary}, {"presentation": presentation})

            print("--- Phase 1: Query Processing Completed ---")

            # Phase 2: Implementation Phase
            print("\n--- Phase 2: Implementation Phase ---")

            # 1. Tasker Agent
            tasks = tasker_agent.classify_features(synthesized_content)
            backend_tasks = tasks["backend"]
            frontend_tasks = tasks["frontend"]
            print(f"Tasker Agent Output - Backend Tasks: {backend_tasks}")
            print(f"Tasker Agent Output - Frontend Tasks: {frontend_tasks}")
            self.session_manager.add_agent_action("TaskerAgent", "classify_features", {"synthesis_content": synthesized_content}, {"tasks": tasks})

            # 2. Backend Expert
            backend_summary = backend_expert.develop_backend(backend_tasks)
            backend_expert.save_backend_summary(backend_summary)
            print(f"Backend Expert Output:\n{backend_summary}")
            self.session_manager.add_agent_action("BackendExpert", "develop_backend", {"backend_tasks": backend_tasks}, {"backend_summary": backend_summary})

            # 3. Quality Assurance (after Backend Development)
            if qa_agent.review_content(backend_summary, "Backend"): 
                print("Backend development approved by QA.")
                self.session_manager.add_agent_action("QualityAssuranceAgent", "review_content", {"content": backend_summary, "content_type": "Backend"}, {"status": "approved"})
            else:
                print("Backend development rejected by QA. Aborting.")
                self.session_manager.add_agent_action("QualityAssuranceAgent", "review_content", {"content": backend_summary, "content_type": "Backend"}, {"status": "rejected"})
                return

            # 4. Frontend Expert
            frontend_summary = frontend_expert.develop_frontend(frontend_tasks)
            frontend_expert.save_frontend_summary(frontend_summary)
            print(f"Frontend Expert Output:\n{frontend_summary}")
            self.session_manager.add_agent_action("FrontendExpert", "develop_frontend", {"frontend_tasks": frontend_tasks}, {"frontend_summary": frontend_summary})

            # 5. Fullstack Expert
            fullstack_report = fullstack_expert.check_integrity(backend_summary, frontend_summary)
            print(f"Fullstack Expert Output:\n{fullstack_report}")
            self.session_manager.add_agent_action("FullstackExpert", "check_integrity", {"backend_summary": backend_summary, "frontend_summary": frontend_summary}, {"fullstack_report": fullstack_report})

            # 6. Report Agent (Post-implementation)
            post_impl_report = report_agent.generate_roadmap(fullstack_report) # Reusing generate_roadmap for post-impl report
            report_agent.save_report_content(post_impl_report, "post_implementation_report.md")
            print(f"Report Agent Output (Post-implementation):\n{post_impl_report}")
            self.session_manager.add_agent_action("ReportAgent", "generate_roadmap", {"synthesis_content": fullstack_report}, {"post_impl_report": post_impl_report})

            # 7. Synthesizing Agent (Post-implementation)
            post_synthesized_content = synth_agent.synthesize_content(backend_summary, frontend_summary) # Reusing for post-impl synthesis
            synth_agent.save_synthesized_content(post_synthesized_content, "post_synthesis.md")
            print(f"Post-implementation Synthesizer Agent Output:\n{post_synthesized_content}")
            self.session_manager.add_agent_action("SynthesizerAgent", "synthesize_content", {"backend_summary": backend_summary, "frontend_summary": frontend_summary}, {"post_synthesized_content": post_synthesized_content})

            # 8. Organizer Agent (Phase 2)
            organized_post_synthesis = org_agent.beautify_content(post_synthesized_content)
            org_agent.save_organized_content(organized_post_synthesis, "organized_post_synthesis.md")
            print(f"Organizer Agent Output (Phase 2):\n{organized_post_synthesis}")
            self.session_manager.add_agent_action("OrganizerAgent", "beautify_content", {"content": post_synthesized_content}, {"organized_post_synthesis": organized_post_synthesis})

            # 9. Debugging Agent (Placeholder - actual implementation would involve more logic)
            # debug_agent.debug_issues("Simulated issue: API endpoint not responding.") # Removed direct call
            # self.session_manager.add_agent_action("DebuggingAgent", "debug_issues", {"issue": "Simulated issue: API endpoint not responding."}, {"status": "simulated_debug_run"}) # Removed direct call

            # 10. Presenter Agent (Phase 2)
            phase2_summary = "Phase 2 (Implementation) completed successfully. We have classified tasks, developed backend and frontend, performed fullstack integration, and generated post-implementation reports."
            presentation = pres_agent.present_phase_summary("Phase 2 Summary", phase2_summary)
            pres_agent.save_presentation_content(presentation, "phase2_summary.md")
            print(f"Presenter Agent Output:\n{presentation}")
            self.session_manager.add_agent_action("PresenterAgent", "present_phase_summary", {"phase_name": "Phase 2 Summary", "summary_content": phase2_summary}, {"presentation": presentation})

            print("--- Phase 2: Implementation Phase Completed ---")

        except Exception as e:
            error_message = f"An error occurred during workflow execution: {e}"
            print(error_message)
            # Call the DebugTool via ToolManager
            debug_report = self.tool_manager.execute_tool("DebugTool", "debug", error_message=error_message, context="Workflow execution error")
            print(f"Debug Tool Report:\n{debug_report}")
            self.session_manager.add_agent_action("Orchestrator", "error_handling", {"error": error_message}, {"debug_report": debug_report})

        print(f"Orchestrator: Workflow completed. Session ID: {self.session_manager.get_session_id()}")


