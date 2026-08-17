from app.utils.resume_parser import extract_resume_text
from app.utils.matcher import analyze_resume


file_path = "uploads/BHARATI PATIL.Python developer.pdf"


resume_text = extract_resume_text(file_path)


job_description = """
We are looking for a Junior AI Engineer with strong Python skills.
The candidate should have knowledge of Machine Learning, NLP,
Generative AI, Pandas, NumPy, Scikit-learn and Flask.
Experience with TensorFlow, PyTorch and Docker is preferred.
"""


result = analyze_resume(
    resume_text,
    job_description
)


print("========== RESUME ANALYSIS ==========")

print("\nMatching Score:")
print(f"{result['matching_score']:.2f}%")


print("\nMatched Skills:")
for skill in result["matched_skills"]:
    print("-", skill)


print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print("-", skill)