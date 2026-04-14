import re
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant")

def detect_intent(user_input: str):
    text = user_input.lower()

    # FAST RULE-BASED (Top 1% improvement)
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    if any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    if any(word in text for word in ["yes", "yeah", "sure", "ok"]):
        return "high_intent"

    # LLM fallback
    prompt = f"""
    Classify intent:
    1. greeting
    2. pricing
    3. high_intent

    Input: {user_input}
    Output only one word.
    """

    response = llm.invoke(prompt).content.strip().lower()
    return response