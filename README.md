# AI Resume Skill Extractor (MVP)

A lightweight, fast MVP that extracts skills from PDF resumes, identifies job-required skills, and computes a match score using NLP + fuzzy matching. Includes both a CLI tool and a Streamlit UI.

### 🚀 Tech Stack
- **Python**
- **pdfplumber** (PDF text extraction)
- **spaCy** (text preprocessing)
- **FuzzyWuzzy + Levenshtein** (similarity-based skill matching)
- **Streamlit** (interactive UI)

---

## ✨ Features
- Extracts text from **PDF resumes** (text-based, not OCR).
- Cleans and normalizes resume and job description text.
- Identifies skills across multiple categories:
  - Programming Languages  
  - Frameworks  
  - Databases  
  - Cloud & DevOps  
  - ML/AI  
  - Tools  
- Fuzzy matching to detect skills even with partial/inexact matches.
- Produces:
  - **Match score (%)**
  - **Matched skills**
  - **Resume skills (categorized)**
  - **Job skills (categorized)**
- Streamlit UI with **JSON summary download**.
- CLI mode for quick terminal executions.

---

## 📁 Project Structure
ai-resume-skill-extractor/
├── app/
│ ├── parser/
│ │ ├── pdf_parser.py
│ │ └── clean_text.py
│ ├── extractor/
│ │ ├── entities.py
│ │ └── skill_extractor.py
│ ├── matcher/
│ │ └── job_matcher.py
│ ├── main.py
│ └── web_app.py
├── docs/
│ ├── architecture.png
│ └── screenshots/
└── README.md