from flask import Blueprint, render_template, request
from models.resume_analyzer import analyze_resume
from services.file_parser_service import extract_text
import re

resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    ats_score = None

    if request.method == "POST":
        job_description = request.form.get("job_description")

        if "resume_file" in request.files and request.files["resume_file"].filename:
            resume_text = extract_text(request.files["resume_file"])
        else:
            resume_text = request.form.get("resume")

        if resume_text and job_description:
            feedback = analyze_resume(resume_text, job_description)
            match = re.search(r"ATS_SCORE\s*:\s*(\d+)", feedback)
            if match:
                ats_score = int(match.group(1))

    return render_template("index.html", feedback=feedback, ats_score=ats_score)