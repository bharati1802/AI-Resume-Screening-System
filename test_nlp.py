from app.utils.resume_parser import extract_resume_text
from app.utils.nlp_processor import calculate_matching_score


# Resume PDF path
file_path = "uploads/BHARATI PATIL.Python developer.pdf"


# Extract resume text
resume_text = extract_resume_text(file_path)


# Sample Job Description
job_description = """
We are looking for a Junior AI Engineer with strong Python skills.
The candidate should have knowledge of Machine Learning, NLP,
Generative AI, Pandas, NumPy, Scikit-learn and Flask.
Experience with Git and GitHub is preferred.
"""


# Calculate matching score
matching_score = calculate_matching_score(
    resume_text,
    job_description
)


print("Resume Text Length:")
print(len(resume_text))

print("\nMatching Score:")
print(f"{matching_score:.2f}%")