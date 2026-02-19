from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_llm


def researcher_agent(query: str) -> str:
    """
    Researcher Agent:
    Responsible for collecting raw automotive data.
    Returns factual, technical details only.
    """

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an Automotive Research Specialist.\n"
            "Your job is to collect detailed technical specifications about vehicles.\n"
            "Return raw factual information only.\n"
            "Do NOT format nicely.\n"
            "Do NOT summarize.\n"
            "Provide structured technical bullet information."
        ),
        ("human", "{input}")
    ])

    chain = prompt | llm

    response = chain.invoke({"input": query})

    return response.content
