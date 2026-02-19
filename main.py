from app.orchestrator import run_multi_agent_system


if __name__ == "__main__":
    print("=== Multi-Agent Automotive System ===\n")

    user_query = input("Enter car name or automotive query: ")

    result = run_multi_agent_system(user_query)

    print("\n\n=========== FINAL OUTPUT ===========\n")
    print(result)
