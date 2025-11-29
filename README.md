# AI Resume Skill Extractor (MVP)

A lightweight NLP-based tool that extracts skills from PDF resumes, identifies job-required skills, and computes a match score using keyword matching and fuzzy similarity.  
Includes both a **CLI tool** and a **Streamlit UI**.

---

## 🚀 Tech Stack
- **Python 3.12**
- **pdfplumber** – PDF text extraction  
- **spaCy** – Text preprocessing  
- **FuzzyWuzzy + Levenshtein** – Similarity-based skill matching  
- **Streamlit** – Web UI  

---

## ✨ Features
- Extracts text from PDF resumes (non-OCR).
- Cleans and normalizes resume & job description text.
- Categorized skill recognition:
  - Programming Languages  
  - Frameworks  
  - Databases  
  - Cloud / DevOps  
  - ML / AI  
  - Tools
- Fuzzy matching to detect partial or misspelled skills.
- Produces:
  - **Match Score (%)**
  - **Matched Skills**
  - **Resume Skill Categories**
  - **Job Skill Categories**
  - **JSON Summary**
- Streamlit UI for interactive use.

---

## 📁 Project Structure

```text
ai-resume-skill-extractor/
├── app/
│   ├── parser/
│   │   ├── pdf_parser.py
│   │   └── clean_text.py
│   ├── extractor/
│   │   ├── entities.py
│   │   └── skill_extractor.py
│   ├── matcher/
│   │   └── job_matcher.py
│   ├── main.py
│   └── web_app.py
├── docs/
│   ├── architecture.png
│   └── screenshots/
└── README.md
