from langgraph.graph import StateGraph
from agent.intent import detect_intent
from agent.rag import get_answer
from agent.tools import mock_lead_capture


def intent_node(state):
    user_input = state["user_input"]

    # STEP 1: Detect intent
    intent = detect_intent(user_input)
    state["intent"] = intent

    # STEP 2: Greeting
    if intent == "greeting":
        state["response"] = "Hi! Welcome to AutoStream 🚀"

    # STEP 3: Pricing / Info → RAG
    elif intent == "pricing":
        answer = get_answer(user_input)
        state["response"] = answer + "\n\n👉 Would you like to get started with a plan?"

    # STEP 4: High Intent → START FORM (IMPORTANT FIX)
    elif intent == "high_intent":
        state["collecting"] = "name"   # START FROM NAME (FIX)
        state["response"] = "Great! Let's get you started 🚀\n\nWhat is your name?"

    # STEP 5: Lead Collection Flow
    elif state.get("collecting"):

        # NAME STEP
        if state["collecting"] == "name":
            state["name"] = user_input
            state["collecting"] = "email"
            state["response"] = "Please provide your email."

        # EMAIL STEP
        elif state["collecting"] == "email":
            state["email"] = user_input
            state["collecting"] = "platform"
            state["response"] = "Which platform? (YouTube/Instagram)"

        # PLATFORM STEP → FINAL TOOL CALL
        elif state["collecting"] == "platform":
            state["platform"] = user_input

            # CALL TOOL ONLY HERE (correct behavior)
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            state["collecting"] = None
            state["response"] = "🎉 You're successfully registered!"

    else:
        state["response"] = "Can you clarify?"

    return state


# BUILD GRAPH
def build_graph():
    graph = StateGraph(dict)

    graph.add_node("intent", intent_node)

    graph.set_entry_point("intent")

    graph.set_finish_point("intent")

    return graph.compile()