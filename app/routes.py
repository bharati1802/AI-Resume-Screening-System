import os

from flask import Blueprint, request, jsonify, render_template

from app.database import get_all_results, save_screening_result
from app.utils.resume_parser import extract_resume_text
from app.utils.matcher import analyze_resume


main = Blueprint("main", __name__)

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"pdf", "docx"}


def allowed_file(filename):
    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in ALLOWED_EXTENSIONS


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/results")
def results():
    screening_results = get_all_results()

    formatted_results = []

    for result in screening_results:
        formatted_results.append({
            "id": result[0],
            "resume_filename": result[1],
            "job_description": result[2],
            "matching_score": result[3],
            "matched_skills": result[4],
            "missing_skills": result[5],
            "created_at": result[6]
        })

    return jsonify(formatted_results)


@main.route("/analyze", methods=["POST"])
def analyze():

    # Step 1: Check resume file
    if "resume" not in request.files:
        return jsonify({
            "error": "No resume file uploaded."
        }), 400

    resume_file = request.files["resume"]

    if resume_file.filename == "":
        return jsonify({
            "error": "Please select a resume file."
        }), 400

    # Step 2: Check file type
    if not allowed_file(resume_file.filename):
        return jsonify({
            "error": "Only PDF and DOCX files are supported."
        }), 400

    # Step 3: Get Job Description
    job_description = request.form.get(
        "job_description",
        ""
    ).strip()

    if not job_description:
        return jsonify({
            "error": "Job Description is required."
        }), 400

    # Step 4: Create uploads folder
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Step 5: Save uploaded resume
    file_path = os.path.join(
        UPLOAD_FOLDER,
        resume_file.filename
    )

    resume_file.save(file_path)

    # Step 6: Extract resume text
    try:
        resume_text = extract_resume_text(file_path)

    except Exception as error:
        return jsonify({
            "error": f"Could not extract resume text: {str(error)}"
        }), 500

    # Step 7: Analyze resume
    try:
        analysis_result = analyze_resume(
            resume_text,
            job_description
        )

    except Exception as error:
        return jsonify({
            "error": f"Resume analysis failed: {str(error)}"
        }), 500

    # Step 8: Get analysis values
    matching_score = analysis_result["matching_score"]

    matched_skills = analysis_result["matched_skills"]

    missing_skills = analysis_result["missing_skills"]

    # Step 9: Save result in SQLite
    try:
        result_id = save_screening_result(
            resume_file.filename,
            job_description,
            matching_score,
            matched_skills,
            missing_skills
        )

    except Exception as error:
        return jsonify({
            "error": f"Database save failed: {str(error)}"
        }), 500

    # Step 10: Return final result
    return jsonify({
        "message": "Resume analyzed successfully.",
        "result_id": result_id,
        "resume_filename": resume_file.filename,
        "matching_score": round(matching_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    })