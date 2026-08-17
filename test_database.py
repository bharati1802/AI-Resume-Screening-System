from app.database import (
    create_table,
    save_screening_result,
    get_all_results
)


print("Creating SQLite database...")

create_table()

print("Database and table created successfully.")


# Sample analysis result
resume_filename = "BHARATI PATIL.Python developer.pdf"

job_description = """
Looking for a Python Developer with experience in
Machine Learning, NLP, Generative AI, Pandas,
NumPy, Scikit-learn, Flask, TensorFlow, PyTorch and Docker.
"""

matching_score = 38.91

matched_skills = [
    "python",
    "machine learning",
    "nlp",
    "generative ai",
    "pandas",
    "numpy",
    "scikit-learn",
    "flask"
]

missing_skills = [
    "tensorflow",
    "pytorch",
    "docker"
]


print("\nSaving screening result...")


result_id = save_screening_result(
    resume_filename,
    job_description,
    matching_score,
    matched_skills,
    missing_skills
)


print(f"Screening result saved successfully.")
print(f"Inserted Result ID: {result_id}")


print("\nReading results from database...")

results = get_all_results()


print("\n----- DATABASE RESULTS -----")


for result in results:
    print(f"\nID: {result[0]}")
    print(f"Resume: {result[1]}")
    print(f"Matching Score: {result[3]:.2f}%")
    print(f"Matched Skills: {result[4]}")
    print(f"Missing Skills: {result[5]}")
    print(f"Created At: {result[6]}")


print("\nSQLite insertion test PASSED.")