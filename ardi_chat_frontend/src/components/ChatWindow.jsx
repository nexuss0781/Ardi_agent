import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isTaskbarOpen, setIsTaskbarOpen] = useState(true);
  const [workflowStatus, setWorkflowStatus] = useState(null);
  const messagesEndRef = useRef(null);

  const API_BASE_URL = 'https://5000-iep1nvuomnd2rgy54tmep-94c1dd2b.manusvm.computer/api';

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Fetch workflow status periodically
  useEffect(() => {
    const fetchWorkflowStatus = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/workflow/status`);
        setWorkflowStatus(response.data.workflow_status);
      } catch (error) {
        console.error('Error fetching workflow status:', error);
      }
    };

    fetchWorkflowStatus();
    const interval = setInterval(fetchWorkflowStatus, 5000); // Update every 5 seconds

    return () => clearInterval(interval);
  }, []);

  const handleSendMessage = async () => {
    if (input.trim() === '') return;

    const newMessage = { sender: 'user', text: input };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInput('');

    try {
      // Start workflow with user query
      const response = await axios.post(`${API_BASE_URL}/workflow/start`, { query: input });
      
      if (response.data.result && response.data.result.result) {
        setMessages((prevMessages) => [...prevMessages, { 
          sender: 'ai', 
          text: response.data.result.result,
          agent: response.data.result.agent
        }]);
      }
      
      // Update workflow status
      setWorkflowStatus(response.data.workflow_status);
      
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prevMessages) => [...prevMessages, { sender: 'ai', text: 'Error: Could not get a response.' }]);
    }
  };

  const handleContinueWorkflow = async () => {
    try {
      const response = await axios.post(`${API_BASE_URL}/workflow/continue`);
      
      if (response.data.result && response.data.result.result) {
        setMessages((prevMessages) => [...prevMessages, { 
          sender: 'ai', 
          text: response.data.result.result,
          agent: response.data.result.agent
        }]);
      }
      
      // Update workflow status
      setWorkflowStatus(response.data.workflow_status);
      
    } catch (error) {
      console.error('Error continuing workflow:', error);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  return (
    <div className="chat-container">
      {/* Collapsible Taskbar */}
      <div className={`taskbar ${isTaskbarOpen ? 'open' : 'closed'}`}>
        <button onClick={() => setIsTaskbarOpen(!isTaskbarOpen)} className="taskbar-toggle">
          {isTaskbarOpen ? '✕' : '☰'}
        </button>
        <div className="taskbar-content">
          <h3>Workflow Progress</h3>
          {workflowStatus ? (
            <div>
              <p><strong>Phase:</strong> {workflowStatus.current_phase}</p>
              <p><strong>Current Agent:</strong> {workflowStatus.current_agent}</p>
              <p><strong>Progress:</strong> {Math.round(workflowStatus.progress_percentage)}%</p>
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ width: `${workflowStatus.progress_percentage}%` }}
                ></div>
              </div>
              <p><strong>Completed:</strong> {workflowStatus.completed_agents.length}/{workflowStatus.total_agents}</p>
              
              {workflowStatus.completed_agents.length > 0 && (
                <button onClick={handleContinueWorkflow} className="continue-btn">
                  Continue to Next Agent
                </button>
              )}
            </div>
          ) : (
            <p>No active workflow</p>
          )}
        </div>
      </div>

      {/* Chat Window */}
      <div className="chat-window">
        <div className="messages-display">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              {msg.agent && <div className="agent-label">{msg.agent}:</div>}
              {msg.text}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>
        <div className="message-input-area">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message..."
            className="message-input"
          />
          <button onClick={handleSendMessage} className="send-button">
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatWindow;

