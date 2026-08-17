import sqlite3


DATABASE_NAME = "screening_results.db"


def get_connection():
    """
    SQLite database connection तयार करते.
    """
    connection = sqlite3.connect(DATABASE_NAME)

    return connection


def create_table():
    """
    screening_results table तयार करते.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS screening_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_filename TEXT NOT NULL,
            job_description TEXT NOT NULL,
            matching_score REAL NOT NULL,
            matched_skills TEXT,
            missing_skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    connection.close()


def save_screening_result(
    resume_filename,
    job_description,
    matching_score,
    matched_skills,
    missing_skills
):
    """
    Resume screening result SQLite database मध्ये save करते.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO screening_results (
            resume_filename,
            job_description,
            matching_score,
            matched_skills,
            missing_skills
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        resume_filename,
        job_description,
        matching_score,
        ", ".join(matched_skills),
        ", ".join(missing_skills)
    ))

    connection.commit()

    result_id = cursor.lastrowid

    connection.close()

    return result_id


def get_all_results():
    """
    Database मधील सर्व screening results मिळवते.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            resume_filename,
            job_description,
            matching_score,
            matched_skills,
            missing_skills,
            created_at
        FROM screening_results
        ORDER BY id DESC
    """)

    results = cursor.fetchall()

    connection.close()

    return results


if __name__ == "__main__":
    create_table()

    print("SQLite database created successfully.")
    print("Table 'screening_results' is ready.")