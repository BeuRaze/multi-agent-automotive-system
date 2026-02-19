from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_llm


def writer_agent(research_data: str) -> str:
    """
    Writer Agent:
    Responsible for converting raw research data
    into a professional, structured automotive report.
    """

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an Automotive Technical Writer.\n"
            "Your job is to take raw vehicle research data "
            "and format it into a clean, professional report.\n\n"
            "Structure the output using the following sections:\n"
            "1. Overview\n"
            "2. Engine Specifications\n"
            "3. Performance Details\n"
            "4. Features & Technology\n"
            "5. Conclusion\n\n"
            "Make it clear, well-formatted, and professional."
        ),
        ("human", "{input}")
    ])

    chain = prompt | llm

    response = chain.invoke({"input": research_data})

    return response.content
