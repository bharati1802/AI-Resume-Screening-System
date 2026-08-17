from app.utils.resume_parser import extract_resume_text
from app.utils.nlp_processor import clean_text


file_path = "uploads/BHARATI PATIL.Python developer.pdf"

text = extract_resume_text(file_path)

cleaned_text = clean_text(text)

print("----- ORIGINAL TEXT -----")
print(text[:500])

print("\n----- CLEANED TEXT -----")
print(cleaned_text[:500])