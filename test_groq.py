import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

print("API KEY LOADED:", os.getenv("GROQ_API_KEY") is not None)

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

response = llm.invoke("Say hello in one sentence.")

print(response.content)

