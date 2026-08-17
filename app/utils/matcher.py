import re


SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "natural language processing",
    "generative ai",
    "genai",
    "rag",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "keras",
    "opencv",
    "computer vision",
    "flask",
    "fastapi",
    "django",
    "rest api",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "power bi",
    "tableau"
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return found_skills


def find_matched_skills(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    return matched_skills


def find_missing_skills(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    return missing_skills


def analyze_resume(resume_text, job_description):
    from app.utils.nlp_processor import calculate_matching_score

    matching_score = calculate_matching_score(
        resume_text,
        job_description
    )

    matched_skills = find_matched_skills(
        resume_text,
        job_description
    )

    missing_skills = find_missing_skills(
        resume_text,
        job_description
    )

    return {
        "matching_score": matching_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }