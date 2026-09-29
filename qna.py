import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def get_answer(question: str) -> str:

    # Offline fallback answers
    q = question.lower().strip()

    if "largest ocean" in q:
        return "The Pacific Ocean is the largest ocean in the world."

    if "capital of india" in q:
        return "The capital of India is New Delhi."

    if "what is ai" in q or "artificial intelligence" in q:
        return "Artificial Intelligence (AI) is technology that enables computers to perform tasks that normally require human intelligence."

    if "cpu" in q:
        return "CPU stands for Central Processing Unit. It processes instructions and performs calculations in a computer."

    # Try Gemini first
    try:
        prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and simply.

Question:
{question}

Give a short and easy-to-understand answer.
"""

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception:
        # Fallback when Gemini quota is unavailable
        return (
            "Gemini API is currently unavailable. "
            "Please try a basic question such as "
            "'Which is the largest ocean?'"
        )