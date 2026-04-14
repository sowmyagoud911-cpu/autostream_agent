import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import re

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)



def detect_intent(user_input: str):
    text = user_input.lower()

    # 🔥 STRICT MATCHING (fixes "propricing" issue)
    if re.search(r"\b(price|pricing|plan|cost)\b", text):
        return "pricing"

    if any(word in text for word in ["yes", "yeah", "ok", "sure", "let's start"]):
        return "high_intent"

    if re.search(r"\b(hi|hello|hey)\b", text):
        return "greeting"

    return "unknown"