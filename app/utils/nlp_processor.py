import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text):
    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def create_tfidf_vectors(resume_text, job_description):
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(
        [resume_text, job_description]
    )

    return tfidf_matrix


def calculate_similarity(tfidf_matrix):
    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix


def calculate_matching_score(resume_text, job_description):
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    tfidf_matrix = create_tfidf_vectors(
        resume_text,
        job_description
    )

    similarity_matrix = calculate_similarity(tfidf_matrix)

    similarity_score = similarity_matrix[0][1]

    matching_score = similarity_score * 100

    return matching_score