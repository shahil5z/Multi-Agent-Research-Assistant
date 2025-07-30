import os
from dotenv import load_dotenv
from groq import Groq

def load_groq_config():
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")
    return {"api_key": api_key, "model": "llama-3.3-70b-versatile"}