# 🚀 AutoStream AI Agent – Social-to-Lead Workflow

## 🚀 Overview
This project implements a conversational AI agent that converts user interactions into qualified leads.

---

## 🧠 Features
- Intent Detection (Greeting, Inquiry, High Intent)
- RAG-based Knowledge Retrieval (JSON)
- Multi-turn Memory (State Management)
- Lead Capture Tool Execution

---

## ⚙️ Tech Stack
- Python 3
- LangChain
- LangGraph
- ChatGroq (LLM)
- JSON-based RAG

---

## ▶️ How to Run
1. Clone the repository  
2. Install dependencies:
```bash
pip install -r requirements.txt
3. Run:
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
Step 1: Greeting

User: "Hi"
Bot: Welcome message

Step 2: Pricing Inquiry (RAG)

User: "Tell me pricing"
Bot: Returns pricing from JSON knowledge base

Step 3: Intent Shift

User: "I want Pro plan for YouTube"
Bot: Detects high intent

Step 4: Lead Qualification

Bot asks:

Name
Email
Platform
Step 5: Tool Execution

After collecting all data:

Lead is stored using mock_lead_capture()

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