from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import sys
import os

# Add the src directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.orchestrator import Orchestrator
from src.utils.llm_client import LLMClient
from src.utils.session_manager import SessionManager

chat_bp = Blueprint('chat', __name__)

# Global session manager for maintaining conversation context
session_manager = SessionManager()
llm_client = LLMClient(session_manager=session_manager)

@chat_bp.route('/chat', methods=['POST'])
@cross_origin()
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        user_message = data['message']
        
        # For simple chat, use the LLM client directly
        # For complex development tasks, use the orchestrator
        if data.get('use_orchestrator', False):
            orchestrator = Orchestrator()
            # Run workflow in a simplified manner for API
            response = orchestrator.run_simple_workflow(user_message)
        else:
            # Simple chat response using LLM client
            response = llm_client.generate_content(user_message)
        
        if response is None:
            return jsonify({'error': 'Failed to generate response'}), 500
        
        return jsonify({
            'response': response,
            'session_id': session_manager.get_session_id()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/chat/history', methods=['GET'])
@cross_origin()
def get_chat_history():
    try:
        history = session_manager.get_llm_history()
        return jsonify({'history': history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/chat/session', methods=['POST'])
@cross_origin()
def new_session():
    try:
        global session_manager, llm_client
        session_manager = SessionManager()
        llm_client = LLMClient(session_manager=session_manager)
        return jsonify({
            'message': 'New session created',
            'session_id': session_manager.get_session_id()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

