from app.utils.resume_parser import extract_resume_text
from app.utils.matcher import (
    find_matched_skills,
    find_missing_skills
)


file_path = "uploads/BHARATI PATIL.Python developer.pdf"


resume_text = extract_resume_text(file_path)


job_description = """
We are looking for a Junior AI Engineer with strong Python skills.
The candidate should have knowledge of Machine Learning, NLP,
Generative AI, Pandas, NumPy, Scikit-learn and Flask.
Experience with TensorFlow, PyTorch and Docker is preferred.
"""


matched_skills = find_matched_skills(
    resume_text,
    job_description
)


missing_skills = find_missing_skills(
    resume_text,
    job_description
)


print("Matched Skills:")
for skill in matched_skills:
    print("-", skill)


print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)