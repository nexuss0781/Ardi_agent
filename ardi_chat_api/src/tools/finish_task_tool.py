"""
Finish Task Tool - Allows agents to signal completion and trigger workflow progression
"""

class FinishTaskTool:
    def __init__(self, session_manager=None):
        self.session_manager = session_manager
        
    def finish_task(self, agent_name: str, task_result: str, next_agent: str = None):
        """
        Signal that the current agent has finished its task
        
        Args:
            agent_name (str): Name of the agent finishing the task
            task_result (str): Result or output of the completed task
            next_agent (str): Optional - name of the next agent to execute
            
        Returns:
            dict: Status and information about the task completion
        """
        completion_data = {
            "status": "task_completed",
            "agent": agent_name,
            "result": task_result,
            "next_agent": next_agent,
            "timestamp": self._get_timestamp()
        }
        
        # Log the completion if session manager is available
        if self.session_manager:
            self.session_manager.add_agent_action(
                agent_name, 
                "finish_task", 
                {"task_result": task_result, "next_agent": next_agent}, 
                completion_data
            )
        
        return completion_data
    
    def _get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()

