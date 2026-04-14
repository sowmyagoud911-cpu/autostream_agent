from langgraph.graph import StateGraph
from agent.intent import detect_intent
from agent.rag import get_answer
from agent.tools import mock_lead_capture


def intent_node(state):
    user_input = state["user_input"].strip().lower()

    intent = detect_intent(user_input)
    state["intent"] = intent

    # =========================
    # 🧠 1. LEAD FLOW (PRIORITY FIRST)
    # =========================
    if state.get("collecting"):

        if state["collecting"] == "name":
            state["name"] = user_input
            state["collecting"] = "email"
            state["response"] = "Please provide your email."
            return state

        elif state["collecting"] == "email":
            state["email"] = user_input
            state["collecting"] = "platform"
            state["response"] = "Which platform? (YouTube/Instagram)"
            return state

        elif state["collecting"] == "platform":
            state["platform"] = user_input

            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            state["collecting"] = None
            state["response"] = "🎉 You're successfully registered!"
            return state

    # =========================
    # 🧠 2. NORMAL INTENT FLOW
    # =========================
    if intent == "greeting":
        state["response"] = "Hi! Welcome to AutoStream 🚀"

    elif intent == "pricing":
        state["response"] = get_answer(user_input)
        state["response"] += "\n\n👉 Would you like to start?"

    elif intent == "high_intent":
        state["collecting"] = "name"
        state["response"] = "Great! Let's start 🚀\nWhat is your name?"

    else:
        state["response"] = "Can you clarify?"

    return state


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("intent", intent_node)
    graph.set_entry_point("intent")
    graph.set_finish_point("intent")

    return graph.compile()