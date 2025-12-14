from services.ollama_service import get_ollama_response
from utils.prompts import ATS_PROMPT

def analyze_resume(resume_text, job_description):
    prompt = ATS_PROMPT.format(resume=resume_text, job_description=job_description)
    return get_ollama_response(prompt)