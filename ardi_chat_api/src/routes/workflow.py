from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import sys
import os

# Add the src directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.orchestrator_enhanced import EnhancedOrchestrator

workflow_bp = Blueprint('workflow', __name__)

# Global orchestrator instance to maintain workflow state
orchestrator = EnhancedOrchestrator()

@workflow_bp.route('/workflow/start', methods=['POST'])
@cross_origin()
def start_workflow():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'error': 'Query is required'}), 400
        
        user_query = data['query']
        
        # Start the enhanced workflow
        result = orchestrator.run_enhanced_workflow(user_query)
        
        return jsonify({
            'status': 'workflow_started',
            'result': result,
            'workflow_status': orchestrator.get_workflow_status()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@workflow_bp.route('/workflow/continue', methods=['POST'])
@cross_origin()
def continue_workflow():
    try:
        # Continue to the next agent in the workflow
        result = orchestrator.continue_workflow()
        
        return jsonify({
            'status': 'workflow_continued',
            'result': result,
            'workflow_status': orchestrator.get_workflow_status()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@workflow_bp.route('/workflow/status', methods=['GET'])
@cross_origin()
def get_workflow_status():
    try:
        status = orchestrator.get_workflow_status()
        return jsonify({
            'workflow_status': status
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@workflow_bp.route('/workflow/reset', methods=['POST'])
@cross_origin()
def reset_workflow():
    try:
        global orchestrator
        orchestrator = EnhancedOrchestrator()
        return jsonify({
            'status': 'workflow_reset',
            'message': 'Workflow has been reset to initial state'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

