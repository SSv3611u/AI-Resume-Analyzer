import ollama
from config import Config

def get_ollama_response(prompt):
    try:
        response = ollama.chat(
            model=Config.OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error communicating with Ollama: {str(e)}"