import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isTaskbarOpen, setIsTaskbarOpen] = useState(true);
  const [workflowStatus, setWorkflowStatus] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const API_BASE_URL = 'http://localhost:5000/api';

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Add welcome message on component mount
  useEffect(() => {
    const welcomeMessage = {
      sender: 'ai',
      text: 'Witaj! 🇵🇱 Jestem Ardi Agent - Twój inteligentny asystent. Jak mogę Ci dzisiaj pomóc?',
      agent: 'Ardi Agent',
      timestamp: new Date().toISOString()
    };
    setMessages([welcomeMessage]);
  }, []);

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
    const interval = setInterval(fetchWorkflowStatus, 5000);

    return () => clearInterval(interval);
  }, []);

  const simulateTyping = () => {
    setIsTyping(true);
    setTimeout(() => setIsTyping(false), 1500);
  };

  const handleSendMessage = async () => {
    if (input.trim() === '' || isLoading) return;

    const newMessage = { 
      sender: 'user', 
      text: input,
      timestamp: new Date().toISOString()
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInput('');
    setIsLoading(true);
    simulateTyping();

    try {
      // Start workflow with user query
      const response = await axios.post(`${API_BASE_URL}/workflow/start`, { query: input });
      
      if (response.data.result && response.data.result.result) {
        setMessages((prevMessages) => [...prevMessages, { 
          sender: 'ai', 
          text: response.data.result.result,
          agent: response.data.result.agent,
          timestamp: new Date().toISOString()
        }]);
      }
      
      // Update workflow status
      setWorkflowStatus(response.data.workflow_status);
      
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prevMessages) => [...prevMessages, { 
        sender: 'ai', 
        text: 'Przepraszam, wystąpił błąd podczas przetwarzania Twojej wiadomości. Spróbuj ponownie.',
        agent: 'System',
        timestamp: new Date().toISOString()
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleContinueWorkflow = async () => {
    if (isLoading) return;
    
    setIsLoading(true);
    simulateTyping();

    try {
      const response = await axios.post(`${API_BASE_URL}/workflow/continue`);
      
      if (response.data.result && response.data.result.result) {
        setMessages((prevMessages) => [...prevMessages, { 
          sender: 'ai', 
          text: response.data.result.result,
          agent: response.data.result.agent,
          timestamp: new Date().toISOString()
        }]);
      }
      
      // Update workflow status
      setWorkflowStatus(response.data.workflow_status);
      
    } catch (error) {
      console.error('Error continuing workflow:', error);
      setMessages((prevMessages) => [...prevMessages, { 
        sender: 'ai', 
        text: 'Wystąpił błąd podczas kontynuowania procesu.',
        agent: 'System',
        timestamp: new Date().toISOString()
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const formatTime = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString('pl-PL', { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'completed': return '#22c55e';
      case 'running': return '#f59e0b';
      case 'error': return '#ef4444';
      default: return '#6b7280';
    }
  };

  return (
    <div className="chat-container">
      {/* Enhanced Taskbar */}
      <div className={`taskbar ${isTaskbarOpen ? 'open' : 'closed'}`}>
        <button 
          onClick={() => setIsTaskbarOpen(!isTaskbarOpen)} 
          className="taskbar-toggle"
          aria-label={isTaskbarOpen ? 'Zamknij panel' : 'Otwórz panel'}
        >
          {isTaskbarOpen ? '✕' : '☰'}
        </button>
        
        <div className="taskbar-content">
          <h3 className="polish-accent">Status Procesu</h3>
          
          {workflowStatus ? (
            <div className="workflow-info">
              <div className="status-item">
                <p><strong>Faza:</strong> {workflowStatus.current_phase}</p>
              </div>
              
              <div className="status-item">
                <p><strong>Aktualny Agent:</strong> {workflowStatus.current_agent}</p>
              </div>
              
              <div className="status-item">
                <p><strong>Postęp:</strong> {Math.round(workflowStatus.progress_percentage)}%</p>
                <div className="progress-bar">
                  <div 
                    className="progress-fill" 
                    style={{ width: `${workflowStatus.progress_percentage}%` }}
                  ></div>
                </div>
              </div>
              
              <div className="status-item">
                <p><strong>Ukończone:</strong> {workflowStatus.completed_agents.length}/{workflowStatus.total_agents}</p>
              </div>
              
              {workflowStatus.completed_agents.length > 0 && (
                <button 
                  onClick={handleContinueWorkflow} 
                  className="continue-btn"
                  disabled={isLoading}
                >
                  {isLoading ? 'Przetwarzanie...' : 'Kontynuuj do Następnego Agenta'}
                </button>
              )}
              
              <div className="agent-list">
                <h4>Agenci:</h4>
                {workflowStatus.completed_agents.map((agent, index) => (
                  <div key={index} className="agent-item completed">
                    <span className="agent-status">✓</span>
                    <span className="agent-name">{agent}</span>
                  </div>
                ))}
                {workflowStatus.current_agent && (
                  <div className="agent-item current">
                    <span className="agent-status">⚡</span>
                    <span className="agent-name">{workflowStatus.current_agent}</span>
                  </div>
                )}
              </div>
            </div>
          ) : (
            <div className="no-workflow">
              <p>Brak aktywnego procesu</p>
              <p className="help-text">Wyślij wiadomość, aby rozpocząć nowy proces.</p>
            </div>
          )}
        </div>
      </div>

      {/* Enhanced Chat Window */}
      <div className="chat-window">
        <div className="chat-header">
          <div className="header-content">
            <h2>Ardi Agent Chat</h2>
            <div className="connection-status">
              <div className="status-indicator online"></div>
              <span>Połączony</span>
            </div>
          </div>
        </div>

        <div className="messages-display">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              {msg.agent && (
                <div className="message-header">
                  <div className="agent-label">{msg.agent}</div>
                  {msg.timestamp && (
                    <div className="message-time">{formatTime(msg.timestamp)}</div>
                  )}
                </div>
              )}
              <div className="message-content">{msg.text}</div>
            </div>
          ))}
          
          {isTyping && (
            <div className="message ai typing-indicator">
              <div className="agent-label">Ardi Agent</div>
              <div className="typing-animation">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          )}
          
          <div ref={messagesEndRef} />
        </div>

        <div className="message-input-area">
          <div className="input-container">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Napisz swoją wiadomość... (Enter aby wysłać, Shift+Enter dla nowej linii)"
              className="message-input"
              disabled={isLoading}
              rows={1}
            />
            <button 
              onClick={handleSendMessage} 
              className={`send-button ${isLoading ? 'loading' : ''}`}
              disabled={isLoading || input.trim() === ''}
            >
              {isLoading ? '⏳' : '📤'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatWindow;

