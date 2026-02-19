from app.researcher_agent import researcher_agent
from app.writer_agent import writer_agent


def run_multi_agent_system(user_query: str) -> str:
    """
    Orchestrator:
    Controls the workflow between agents.

    Step 1: Send user query to Researcher Agent
    Step 2: Pass research output to Writer Agent
    Step 3: Return final structured response
    """

    print("\n[Orchestrator] Sending query to Researcher Agent...\n")
    research_output = researcher_agent(user_query)

    print("\n[Orchestrator] Research complete. Sending to Writer Agent...\n")
    final_output = writer_agent(research_output)

    print("\n[Orchestrator] Writing complete. Returning final result...\n")

    return final_output
