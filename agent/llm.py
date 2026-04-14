import os
from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
        api_key=os.getenv("GROQ_API_KEY")
    )