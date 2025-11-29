# app/web_app.py
"""
Simple Streamlit UI for the AI Resume Skill Extractor MVP.
Upload a PDF resume, paste a job description, click Analyze.
Downloads a JSON summary as well.
"""

import streamlit as st
import tempfile
import os
import json

from parser.pdf_parser import extract_text_from_pdf
from parser.clean_text import clean_text
from extractor.skill_extractor import extract_skills
from matcher.job_matcher import match_resume_to_job

st.set_page_config(page_title="AI Resume Skill Extractor", layout="centered")
st.title("AI Resume Skill Extractor (MVP)")

st.markdown(
    "Upload a PDF resume and paste a job description. "
    "This tool extracts skills from the resume and shows a match score."
)

resume_file = st.file_uploader("Upload resume (PDF)", type=["pdf"])
job_text = st.text_area("Paste job description here", height=200)

if st.button("Analyze"):
    if not resume_file:
        st.error("Please upload a resume PDF file.")
    elif not job_text.strip():
        st.error("Please paste the job description.")
    else:
        # Save temporary resume
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        tmp.write(resume_file.getvalue())
        tmp.close()
        try:
            # Pipeline
            raw = extract_text_from_pdf(tmp.name)
            cleaned_resume = clean_text(raw)
            cleaned_job = clean_text(job_text)

            resume_skills = extract_skills(cleaned_resume)
            job_skills = extract_skills(cleaned_job)
            score, matched = match_resume_to_job(resume_skills, job_skills)

            # Display results
            st.metric("Match Score (%)", score)
            st.subheader("Matched Skills")
            st.write(matched or "No matched skills found")
            st.subheader("Resume Skills (by category)")
            st.json(resume_skills)
            st.subheader("Job Skills (by category)")
            st.json(job_skills)

            # Downloadable JSON
            summary = {
                "resume_skills": resume_skills,
                "job_skills": job_skills,
                "matched_skills": matched,
                "score_percent": score
            }
            st.download_button(
                "Download JSON Summary",
                data=json.dumps(summary, indent=2),
                file_name="summary.json",
                mime="application/json"
            )
        finally:
            try:
                os.remove(tmp.name)
            except Exception:
                pass
