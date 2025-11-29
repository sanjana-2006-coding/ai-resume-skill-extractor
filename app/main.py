# app/main.py
"""
Command-line entry point for the Resume Skill Extractor.
Usage:
    python app/main.py <resume_pdf_path> <job_description_txt_path>

This file ties the pipeline together:
- Parse PDF
- Clean text
- Extract skills
- Extract job-required skills
- Compute match score
"""

import sys
from parser.pdf_parser import extract_text_from_pdf
from parser.clean_text import clean_text
from extractor.skill_extractor import extract_skills
from matcher.job_matcher import match_resume_to_job


def extract_job_skills(job_text: str):
    """
    Job skill extraction is the same mechanism as resume extraction.
    Clean → skill_extractor.
    """
    cleaned = clean_text(job_text)
    return extract_skills(cleaned)


def main():
    if len(sys.argv) != 3:
        print("Usage: python app/main.py <resume.pdf> <job_description.txt>")
        sys.exit(1)

    resume_path = sys.argv[1]
    job_path = sys.argv[2]

    # -----------------------
    # 1. Extract resume text
    # -----------------------
    print("\n[+] Extracting resume text...")
    resume_raw = extract_text_from_pdf(resume_path)
    resume_clean = clean_text(resume_raw)

    # -----------------------
    # 2. Extract skills
    # -----------------------
    print("[+] Extracting skills from resume...")
    resume_skills = extract_skills(resume_clean)

    # -----------------------
    # 3. Extract job description skills
    # -----------------------
    print("[+] Extracting skills from job description...")
    with open(job_path, "r", encoding="utf-8") as f:
        job_text = f.read()

    job_skills = extract_job_skills(job_text)

    # -----------------------
    # 4. Match score
    # -----------------------
    print("[+] Matching resume with job...")
    score, matched = match_resume_to_job(resume_skills, job_skills)

    # -----------------------
    # Output
    # -----------------------
    print("\n==============================")
    print(" RESUME → JOB MATCH RESULTS")
    print("==============================")
    print(f"Match Score: {score}%")
    print(f"Matched Skills: {matched}")
    print("\nDone.\n")


if __name__ == "__main__":
    main()
