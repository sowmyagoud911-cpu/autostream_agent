import json

def load_knowledge():
    with open("data/knowledge.json") as f:
        return json.load(f)

knowledge = load_knowledge()

def get_answer(query):
    query = query.lower()

    # FIX: handle more variations
    if any(word in query for word in ["price", "pricing", "plan", "cost"]):
        return knowledge["pricing"]

    if any(word in query for word in ["policy", "refund", "support"]):
        return knowledge["policies"]

    return "I don't have that information."