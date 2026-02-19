import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

def get_llm():
    """
    This function creates and returns
    a configured Groq LLM instance.
    """

    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0.3  # Lower temperature = more structured output
    )
