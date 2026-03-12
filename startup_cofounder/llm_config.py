from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7,
        max_tokens=1024,       # keep low to avoid rate limits
        max_retries=3,
    )