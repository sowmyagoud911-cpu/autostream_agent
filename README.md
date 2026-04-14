# 🚀 AutoStream AI Agent – Social-to-Lead Workflow

## 🚀 Overview
AutoStream AI Agent is a conversational AI system built for a SaaS product that converts user conversations into qualified business leads.

It simulates a real-world AI sales assistant using:

Intent classification
RAG-based knowledge retrieval
Multi-turn memory
Controlled tool execution (lead capture)
---

## 🧠 Features
🔍 Intent Detection (Greeting / Pricing / High Intent)
📚 RAG-based Knowledge Retrieval (JSON Knowledge Base)
🧠 Multi-turn Conversation Memory (State Management)
🛠️ Tool Execution (Lead Capture Function)
🤖 LLM-powered fallback using ChatGroq (LLaMA 3.1)
---

## ⚙️ Tech Stack
Python 3.9+
LangChain
LangGraph
ChatGroq (LLaMA 3.1)
JSON-based RAG system
dotenv for environment variables
---

## ▶️ How to Run
1. Clone Repository
git clone https://github.com/your-username/autostream_agent.git
cd autostream_agent
2. Install Dependencies
pip install -r requirements.txt
3. Set Environment Variables
Create a .env file:
GROQ_API_KEY=your_api_key_here
4. Run:
   python main.py

## 🏗️ Architecture

The AutoStream AI Agent is built using a state-driven conversational architecture powered by LangGraph. The system is designed to simulate a real-world SaaS lead generation workflow where user inputs are processed step-by-step through controlled states.

When a user sends a message, it first goes through an intent classification module that categorizes the input into greeting, pricing inquiry, or high-intent lead. Based on this classification, the system decides the next action.

If the query is related to pricing or product information, the system uses a lightweight RAG pipeline that retrieves responses from a structured local JSON knowledge base. This ensures factual and consistent responses without hallucination.

For high-intent users, the system transitions into a multi-turn lead collection flow. It sequentially collects user details such as name, email, and platform, storing them in a shared state dictionary.

LangGraph is chosen because it provides structured state transitions and ensures deterministic execution flow, making it suitable for production-level agent design. It also prevents premature tool execution and maintains clear separation between reasoning and actions.

State management is handled using a Python dictionary that persists across multiple conversation turns, allowing the agent to maintain context throughout the interaction.

## 📲 WhatsApp Integration (Concept)
The agent can be integrated with WhatsApp using Twilio API and webhook architecture.

🔄 Flow:
User sends message on WhatsApp
Twilio receives message and triggers webhook
Backend (Flask/FastAPI) receives request
Message is passed to LangGraph agent
Agent processes intent + state
Response is sent back via Twilio API

## Expected Conversation Flow
Step-by-Step Workflow 
1. Greeting 
○ User: “Hi, tell me about your pricing.” 
2. Knowledge Retrieval (RAG) 
○ Agent retrieves pricing from the knowledge base 
○ Agent responds accurately 
3. Intent Shift 
○ User: “That sounds good, I want to try the Pro plan for my YouTube channel.” 
4. Lead Qualification 
○ Agent detects high-intent 
○ Agent asks for: 
■ Name 
■ Email 
5. Tool Execution 
○ Once all details are collected 
○ Agent calls mock_lead_capture() 

🧠 State Management:
Each user is identified by phone number (session ID)
State stored in Redis / Database
Enables multi-turn conversation memory
Ensures continuous chat flow across messages

✅ Summary

This system demonstrates a production-style AI agent that combines:

Intent classification
RAG-based knowledge retrieval
Stateful multi-turn conversation
Controlled tool execution

It simulates a real-world SaaS WhatsApp AI lead generation assistant.
