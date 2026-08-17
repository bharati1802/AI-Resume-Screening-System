# AI-Powered Resume Screening System

An AI-powered web application that automates the initial screening of resumes by comparing a candidate's resume with a given job description.

The system extracts resume text, processes the text using Natural Language Processing (NLP), calculates a matching score using TF-IDF and Cosine Similarity, identifies matched and missing skills, and stores screening results in an SQLite database.

---

## 📌 Project Overview

Recruiters often receive a large number of resumes for a single job opening. Manually reviewing and comparing every resume with the job description can be time-consuming.

The **AI-Powered Resume Screening System** provides an automated first-level screening process.

The user uploads a resume and enters a job description. The application then:

1. Extracts text from the resume.
2. Cleans and preprocesses the text.
3. Converts the resume and job description into TF-IDF vectors.
4. Calculates their similarity using Cosine Similarity.
5. Calculates a resume-job matching score.
6. Extracts technical skills from both documents.
7. Identifies matched skills.
8. Identifies missing skills.
9. Stores the screening result in SQLite.
10. Displays the result through a web interface.

---

## 🎯 Problem Statement

Resume screening is an important part of the recruitment process, but manually reviewing a large number of resumes can require significant time and effort.

Recruiters need to compare:

- Candidate skills
- Candidate experience
- Job requirements
- Technical skills
- Relevant keywords

This project aims to automate the **initial resume screening process** by using NLP and text similarity techniques.

The system does not replace a recruiter. Instead, it works as a **first-level screening and decision-support tool**.

---

## 💡 Solution

The application compares the content of a resume with a job description using NLP-based text similarity.

It provides:

- Resume-to-job matching score
- Matched technical skills
- Missing technical skills
- Stored screening history

This allows users to quickly understand how closely a resume matches a particular job description.

---

# ✨ Key Features

- 📄 Upload resumes in PDF format
- 📝 Upload resumes in DOCX format
- 🔍 Automatic resume text extraction
- 🧹 Text preprocessing using NLP techniques
- 📊 TF-IDF based text vectorization
- 📐 Cosine Similarity calculation
- 🎯 Resume-job matching score
- 🧠 Technical skill extraction
- ✅ Matched skills detection
- ❌ Missing skills detection
- 💾 SQLite database integration
- 🌐 Flask web application
- ⚡ Dynamic result display using JavaScript
- 🧪 Individual module testing
- 🔧 Git and GitHub version control

---

# 🔄 Application Workflow

```text
                    ┌─────────────────────┐
                    │    Upload Resume    │
                    │      PDF / DOCX     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Resume Parser    │
                    │                     │
                    │ Extract Resume Text │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Text Processing   │
                    │        NLP          │
                    │                     │
                    │ Lowercase           │
                    │ Remove Special Chars│
                    │ Normalize Spaces    │
                    └──────────┬──────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │       Resume Analysis        │
                └──────────────┬───────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌───────────────────┐       ┌───────────────────┐
       │      TF-IDF       │       │   Skill Matching  │
       │    Vectorization  │       │                   │
       └─────────┬─────────┘       └─────────┬─────────┘
                 │                           │
                 ▼                           ▼
       ┌───────────────────┐       ┌───────────────────┐
       │ Cosine Similarity │       │ Matched Skills    │
       │    Calculation    │       │ Missing Skills    │
       └─────────┬─────────┘       └─────────┬─────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Screening Result  │
                    │                     │
                    │ Matching Score      │
                    │ Matched Skills      │
                    │ Missing Skills      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SQLite Database   │
                    └─────────────────────┘