ATS_PROMPT = """
You are an advanced ATS resume evaluator.

Compare the RESUME with the JOB DESCRIPTION and provide:

ATS_SCORE: <number out of 100>

1. Matching Skills
2. Missing Skills
3. Strengths
4. Weaknesses
5. Improvement Suggestions

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}
"""