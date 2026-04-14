import json

def load_knowledge():
    with open("data/knowledge.json") as f:
        return json.load(f)

knowledge = load_knowledge()

def get_answer(query):
    query = query.lower()

    # 🎯 SPECIFIC PRO PLAN REQUEST
    if "pro" in query:
        return "Pro Plan: $79/month, unlimited videos, 4K resolution, AI captions."

    # 🎯 BASIC PLAN REQUEST
    if "basic" in query:
        return "Basic Plan: $29/month, 10 videos/month, 720p resolution."

    # 🎯 GENERAL PRICING
    if any(word in query for word in ["price", "pricing", "plan", "cost"]):
        return (
            "Basic Plan: $29/month, 10 videos/month, 720p resolution.\n"
            "Pro Plan: $79/month, unlimited videos, 4K resolution, AI captions."
        )

    return "I don't have that information."