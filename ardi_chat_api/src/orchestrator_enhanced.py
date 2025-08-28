from src.agents.language_expert import LanguageExpert
from src.agents.clarification_agent import ClarificationAgent
from src.agents.idea_generator import IdeaGenerator
from src.agents.analysis_agent import AnalysisAgent
from src.agents.synthesizer_agent import SynthesizerAgent
from src.agents.report_agent import ReportAgent
from src.agents.organizer_agent import OrganizerAgent
from src.agents.presenter_agent import PresenterAgent
from src.agents.quality_assurance_agent import QualityAssuranceAgent
from src.agents.tasker_agent import TaskerAgent
from src.agents.backend_expert import BackendExpert
from src.agents.frontend_expert import FrontendExpert
from src.agents.fullstack_expert import FullstackExpert
from src.agents.debugging_agent import DebuggingAgent
from src.utils.session_manager import SessionManager
from src.utils.llm_client import LLMClient
from src.tools.finish_task_tool import FinishTaskTool

class EnhancedOrchestrator:
    def __init__(self):
        self.session_manager = SessionManager()
        self.finish_task_tool = FinishTaskTool(session_manager=self.session_manager)
        self.current_agent = None
        self.workflow_state = {
            "phase": 1,
            "current_step": "language_expert",
            "completed_agents": [],
            "workflow_data": {}
        }
        
        # Define the workflow sequence
        self.workflow_sequence = [
            {"agent": "language_expert", "phase": 1, "name": "Language Expert"},
            {"agent": "clarification_agent", "phase": 1, "name": "Clarification Agent"},
            {"agent": "idea_generator", "phase": 1, "name": "Idea Generator"},
            {"agent": "analysis_agent", "phase": 1, "name": "Analysis Agent"},
            {"agent": "synthesizer_agent", "phase": 1, "name": "Synthesizer Agent"},
            {"agent": "report_agent", "phase": 1, "name": "Report Agent"},
            {"agent": "organizer_agent", "phase": 1, "name": "Organizer Agent"},
            {"agent": "presenter_agent", "phase": 1, "name": "Presenter Agent"}
        ]

    def run_enhanced_workflow(self, initial_query: str):
        """Enhanced workflow that uses finish_task tool for agent transitions"""
        print("Enhanced Orchestrator: Starting workflow...")
        
        # Store the initial query
        self.workflow_state["workflow_data"]["initial_query"] = initial_query
        
        # Start with the first agent
        return self._execute_current_agent()

    def _execute_current_agent(self):
        """Execute the current agent in the workflow"""
        current_step = self.workflow_state["current_step"]
        
        if current_step == "language_expert":
            return self._execute_language_expert()
        elif current_step == "clarification_agent":
            return self._execute_clarification_agent()
        elif current_step == "idea_generator":
            return self._execute_idea_generator()
        elif current_step == "analysis_agent":
            return self._execute_analysis_agent()
        elif current_step == "synthesizer_agent":
            return self._execute_synthesizer_agent()
        elif current_step == "report_agent":
            return self._execute_report_agent()
        elif current_step == "organizer_agent":
            return self._execute_organizer_agent()
        elif current_step == "presenter_agent":
            return self._execute_presenter_agent()
        else:
            return "Workflow completed"

    def _execute_language_expert(self):
        """Execute Language Expert agent with enhanced prompt engineering"""
        try:
            lang_expert = LanguageExpert(session_manager=self.session_manager)
            initial_query = self.workflow_state["workflow_data"]["initial_query"]
            
            # Enhanced prompt for Language Expert with specific role and instructions
            enhanced_prompt = f"""
            You are the Language Expert in the Ardi Agent system, a specialized AI agent responsible for query formalization and linguistic analysis.
            
            **Your Role:**
            - Analyze user queries for clarity, completeness, and technical feasibility
            - Formalize informal language into structured requirements
            - Identify potential ambiguities or missing information
            - Prepare queries for downstream processing by other specialized agents
            
            **User Query:** "{initial_query}"
            
            **Your Tasks:**
            1. **Query Analysis:** Examine the query for:
               - Technical requirements and constraints
               - Functional specifications
               - User intent and goals
               - Scope and complexity
            
            2. **Language Formalization:** Transform the query into:
               - Clear, unambiguous language
               - Structured requirements format
               - Technical terminology where appropriate
               - Actionable specifications
            
            3. **Gap Identification:** Identify:
               - Missing technical details
               - Unclear requirements
               - Potential implementation challenges
               - Areas needing clarification
            
            4. **Output Format:** Provide:
               - Formalized query statement
               - Key requirements list
               - Identified gaps or ambiguities
               - Recommendations for next steps
            
            **Example Output Structure:**
            ```
            FORMALIZED QUERY: [Clear, structured version of the user request]
            
            KEY REQUIREMENTS:
            - [Requirement 1]
            - [Requirement 2]
            - [Requirement 3]
            
            IDENTIFIED GAPS:
            - [Gap 1 requiring clarification]
            - [Gap 2 needing technical details]
            
            RECOMMENDATIONS:
            - [Recommendation for Clarification Agent]
            - [Suggestion for technical approach]
            ```
            
            Please analyze the user query and provide your expert linguistic analysis following this structure.
            """
            
            llm_client = LLMClient(session_manager=self.session_manager)
            result = llm_client.generate_content(enhanced_prompt)
            
            # Store result and mark as completed
            self.workflow_state["workflow_data"]["language_expert_result"] = result
            self.workflow_state["completed_agents"].append("language_expert")
            
            # Signal completion and move to next agent
            completion = self.finish_task_tool.finish_task(
                "Language Expert", 
                result, 
                "clarification_agent"
            )
            
            # Update workflow state
            self.workflow_state["current_step"] = "clarification_agent"
            
            return {
                "agent": "Language Expert",
                "result": result,
                "status": "completed",
                "next_agent": "Clarification Agent",
                "workflow_state": self.workflow_state
            }
            
        except Exception as e:
            return {"error": f"Language Expert failed: {str(e)}"}

    def _execute_clarification_agent(self):
        """Execute Clarification Agent with enhanced prompt engineering"""
        try:
            clar_agent = ClarificationAgent(session_manager=self.session_manager)
            language_expert_result = self.workflow_state["workflow_data"].get("language_expert_result", "")
            
            # Enhanced prompt for Clarification Agent with specific role and instructions
            enhanced_prompt = f"""
            You are the Clarification Agent in the Ardi Agent system, a specialized AI agent responsible for requirement clarification and specification refinement.
            
            **Your Role:**
            - Analyze formalized queries for ambiguities and missing details
            - Generate specific clarifying questions for unclear requirements
            - Provide detailed specifications for implementation guidance
            - Bridge the gap between user intent and technical implementation
            
            **Input from Language Expert:** 
            {language_expert_result}
            
            **Your Tasks:**
            1. **Ambiguity Analysis:** Examine the formalized query for:
               - Vague or unclear specifications
               - Missing technical constraints
               - Undefined user interface requirements
               - Unclear business logic or workflows
               - Missing data requirements
            
            2. **Clarification Questions:** Generate specific questions about:
               - User interface preferences and design requirements
               - Data storage and management needs
               - User authentication and authorization requirements
               - Performance and scalability expectations
               - Integration requirements with external systems
               - Deployment and hosting preferences
            
            3. **Technical Specifications:** Provide detailed clarifications on:
               - Technology stack recommendations
               - Database schema considerations
               - API design requirements
               - Security and privacy requirements
               - Testing and quality assurance needs
            
            4. **Implementation Guidance:** Suggest:
               - Development approach (frontend-first, backend-first, full-stack)
               - Architecture patterns and best practices
               - Potential challenges and solutions
               - Timeline and milestone considerations
            
            **Output Format:**
            ```
            CLARIFICATION ANALYSIS:
            [Summary of identified ambiguities and areas needing clarification]
            
            SPECIFIC QUESTIONS:
            1. User Interface: [Questions about UI/UX requirements]
            2. Data Management: [Questions about data storage and handling]
            3. Authentication: [Questions about user management]
            4. Performance: [Questions about scalability and performance]
            5. Integration: [Questions about external system integration]
            
            TECHNICAL SPECIFICATIONS:
            - Technology Stack: [Recommended technologies and frameworks]
            - Architecture: [Suggested architectural approach]
            - Database: [Database design considerations]
            - Security: [Security requirements and recommendations]
            
            IMPLEMENTATION ROADMAP:
            - Phase 1: [Initial development phase]
            - Phase 2: [Secondary development phase]
            - Phase 3: [Final development phase]
            
            RECOMMENDATIONS FOR NEXT AGENT:
            [Specific guidance for the Idea Generator agent]
            ```
            
            Please analyze the Language Expert's output and provide comprehensive clarification following this structure.
            """
            
            llm_client = LLMClient(session_manager=self.session_manager)
            result = llm_client.generate_content(enhanced_prompt)
            
            # Store result and mark as completed
            self.workflow_state["workflow_data"]["clarification_agent_result"] = result
            self.workflow_state["completed_agents"].append("clarification_agent")
            
            # Signal completion
            completion = self.finish_task_tool.finish_task(
                "Clarification Agent", 
                result, 
                "idea_generator"
            )
            
            # Update workflow state
            self.workflow_state["current_step"] = "idea_generator"
            
            return {
                "agent": "Clarification Agent",
                "result": result,
                "status": "completed",
                "next_agent": "Idea Generator",
                "workflow_state": self.workflow_state
            }
            
        except Exception as e:
            return {"error": f"Clarification Agent failed: {str(e)}"}

    def continue_workflow(self):
        """Continue the workflow to the next agent"""
        return self._execute_current_agent()

    def get_workflow_status(self):
        """Get current workflow status"""
        return {
            "current_phase": self.workflow_state["phase"],
            "current_agent": self.workflow_state["current_step"],
            "completed_agents": self.workflow_state["completed_agents"],
            "total_agents": len(self.workflow_sequence),
            "progress_percentage": (len(self.workflow_state["completed_agents"]) / len(self.workflow_sequence)) * 100
        }

    def run_simple_workflow(self, query: str):
        """Simplified workflow for API usage - returns a direct response"""
        try:
            # Use LLM client for direct response
            llm_client = LLMClient(session_manager=self.session_manager)
            
            # Create a more conversational prompt
            enhanced_prompt = f"""
            You are Ardi, an AI development assistant. The user has asked: "{query}"
            
            Please provide a helpful, detailed response. If this is about development, 
            provide practical advice and suggestions. If it's a general question, 
            answer conversationally and helpfully.
            """
            
            response = llm_client.generate_content(enhanced_prompt)
            return response if response else "I'm sorry, I couldn't generate a response at the moment."
            
        except Exception as e:
            return f"Error processing your request: {str(e)}"

    def _execute_idea_generator(self):
        """Placeholder for Idea Generator - to be implemented"""
        return {"agent": "Idea Generator", "status": "not_implemented"}
    
    def _execute_analysis_agent(self):
        """Placeholder for Analysis Agent - to be implemented"""
        return {"agent": "Analysis Agent", "status": "not_implemented"}
    
    def _execute_synthesizer_agent(self):
        """Placeholder for Synthesizer Agent - to be implemented"""
        return {"agent": "Synthesizer Agent", "status": "not_implemented"}
    
    def _execute_report_agent(self):
        """Placeholder for Report Agent - to be implemented"""
        return {"agent": "Report Agent", "status": "not_implemented"}
    
    def _execute_organizer_agent(self):
        """Placeholder for Organizer Agent - to be implemented"""
        return {"agent": "Organizer Agent", "status": "not_implemented"}
    
    def _execute_presenter_agent(self):
        """Placeholder for Presenter Agent - to be implemented"""
        return {"agent": "Presenter Agent", "status": "not_implemented"}

