### **AI Agent vs Agentic AI**

- **AI Agent:** A type of AI innovation that has only one agent to automate a given task.
    
- **Agentic AI:** Also an AI innovation, but it has many agents in a centralized system to automate a task.
    
The Followings are Examples of the two ai innovations namely Ardi Agent and Ardi Agent. Let's dive on.
### **Ardi  Agent**

- This is initiated by Devin AI.
    
- Agentic AI (Multiple Agents).
    
- 16 Agents.
    
- This is designed to automate Backend/Frontend or Full Stack app to End-to-End testing.
    
- Longer time, but saves your time.
    
- Same as ARDI Agent tools.
    
#### 
### **Detailed Flowchart Breakdown**

**Phase 1: Query Processing**

1. **User Prompt:** Receive a query.
    
2. **Language Expert:** Formalize query. Ambiguities will be clarified here.
    If confirmed as yes, the next step will continue 
3. **Clarification Agent:** Clarify objectives, scope and so on. There will be principles or questions should be answered before preceding dev. This is an interview question what developer asks their clients at the beginning of project. Create Todo.md todo checker for interview. Like 
      - [x] Audience : What users will use this app
      - [ ] comprehensive: how will be comprehensive this? Simple, Normal,Slightly Comprehensive , Comprehensive or Extensive Comprehensive.
    -  It sees the context , if some of them are addressed , it will erased the todo(checker).
    - don't worry about the aboves all will be included on the agent system prompt engineered text. the clarification areas will be included in the system prompt of this agent.

    -  after all it saved as clarify.md.
       
       If the final clarified content satisfied the user and they confirmed as yes, the next step will continue 
4. **Idea Generator:** without using internet, Outline Comprehensive Feature analysis about the app.
    *  Then Quality assurance agent review this feasibility , Quality or other measirements. If passed the next level will continue.

5. **Analysis Agent:** it uses an Internet tool, to gather internet trends similar company's app, cons and pros, how the app will controll the market , what the app should have festures...etc. it will be also predefined what should covor then it will create also todo.md to carefully finish its task with absolute focus. Then when finished , it creates file called Analysis.md. then the document will reviewed by Quality Assurance Agent for this level. If passed next will continue.
    
6. **Synthesizer Agent:** Synthesize #4 and #5. READ Idea.md and Analysis.md then synthesis them in one Organized Document Called Synthesis.md.
    
7. **Report Agent:** Read Synthesized.md then write future implementation Roadmap and technology how to build the app that mentioned in Synthesized.md. it designed as pre implementation Technical Docs.
    
8. **Organizer Agent:** Read Synthesized.md and Beautify the content with Emojies,Consiseness, user-friendly format for Readability.
    
9. **Presenter Agent:** Summarizes what we it do and next step. Then await users for phase 2.
    

**Phase 2: Implementation phase**

1. **Tasker Agent:** Classify features to Backend and Frontend. The tasker agent read synthesis.md then grouped it to frontend and backend.

2. **Backend Expert:**  Finish backend work If given backend work. Then it reviewed by Quality Assurance. If passed , next step will Continue.
     If passed , next step will Continue.
     After all it saves what it done as backend.md
     
3. **Frontend Expert:** Finish frontend work If given. The frontend prompt 
    Will very tailored for aesthetic and modern view and UX.
     After all it saves what it done as frontend.md.

4. **Fullstack Expert:** End-to-end functionality, test & check integrity.
   This phase ensure all are working as expected.

5. **Report Agent:** Post-implementation docs. Again it will write technical docs but it is after the implementation. Every implemented festure will covor and written.

6. **Synthesizing Agent:** Synthesize post-implementation frontend and backend final docs defined at #2 & #3. Then creates Post-synthesized.md

7. **Organizer Agent:** Beautify synthesized documentation.(Post-synthesized.md)
    
8. **Debugging Agent:** Any issue will be debugged.
    
9. **Presenter Agent:** Present to user. Similar to phase 1.

    **Agent List**

1. Language Expert (LE)
    
2. Clarification Agent (CA)
    
3. Idea Expert (IE)
    
4. Analysis Expert (AE)
    
5. Synthesizer Agent (SA)
    
6. Quality Assurance (QA)
    
7. Report Agent (RA)
    
8. Organizer Agent (OA)
    
9. Tasker Agent (TA)
    
10. Backend Expert (BE)
    
11. Frontend Expert (FE)
    
12. Debugger Agent (DA)
    
13. Technical Expert (TE)
    
14. Testing Checker (TC)
    
15. Presenting Agent (PA)
    
#### **Tools**

**File Management**

- **Write:** Create File
    
- **Read:** Read File
    
- **Edit:** Add Content
    
- **Modify:** Replace Content
    
- **Delete:** Delete Files
    
- **List Directory:** List Directory
    
- **Save Version:** Copy Project to Backup
    
- **Restore Version:** Revert from Backup
    
- **Read Folder:** Read Folder / Bulk Reading
    
- **Ignore File:** Remove File from System
    
- **Ignore Folder:** Remove Folder from System
    
- **Remove File:** Remove from Context
    
- **Remove Folder**
    
- **View Context:** Remaining Tokens and List of Files
    

**Other Tools**

- Quiz Creator
    
- Knowledge Creation
    
- Internet
    
- Chatting
    
- Terminal Integration
  
  
Remember the qbove tools isn't your focus just know them as i need for future. Don't talk about them.

Don't worry about Every agent prompts, your work is build this agent sequences and levels. The key is :
    *  Give prompt for right agent.
    *  retain workflow.
    *  handle and Keep Every Agent session throughout the model task..
    *  handle LLM Rate Limit.
    *  Give Functional tools.
    *  more importantly all agents have own prompts markdown by their name. The Orchestrator give a query and prompt to the LLM.then the LLM will be Engineered.

The key Important critical your rule you should follow is, use pure python files instead of langchain like agentic ai frameworks which they leading our app heavy and unreliable for render free environment which allows only 512mb ram. So when you built this app try to use pure Python for logic.

Avoid also heavy frameworks like pydantic, panda and so on. They all make an app slow at dev. And heavy. As a result use pure python ,reduce frameworks for workflow and logic. Thank you.

What's not your focus is:
- BUILDING TOOLS FOR LLM.
- PROMPTS



Add Comprehensive todo.md to the repo

Add The 'Ardi Agent.md' i provided to the repo.

Build the app

Critically when you achive sth even the minor one ; add , commit then push. Continuesly throughout your development consistently without asked about it.

