from agent.graph import build_graph

graph = build_graph()

print("🎬 AutoStream AI Agent")
print("Convert conversations into leads 🚀\n")

state = {}

try:
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("👋 Exiting AutoStream...")
            break

        state["user_input"] = user_input
        state = graph.invoke(state)

        print("Bot:", state.get("response", "⚠️ No response generated"))

except KeyboardInterrupt:
    print("\n👋 Exiting AutoStream (Ctrl+C detected). Goodbye!")