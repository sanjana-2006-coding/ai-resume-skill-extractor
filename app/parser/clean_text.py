# app/parser/clean_text.py
"""
Utility functions for cleaning and normalizing resume/job text.
"""

import re

def clean_text(text: str) -> str:
    """
    Lowercases, removes extra spaces, non-ASCII chars, and normalizes punctuation.
    Makes downstream extraction more accurate and consistent.
    """
    if not text:
        return ""

    # remove non-ASCII chars (optional but useful for many resumes)
    text = text.encode("ascii", errors="ignore").decode()

    text = text.lower()

    # replace weird separators with spaces
    text = re.sub(r"[\t\r\n]+", " ", text)

    # remove multiple spaces
    text = re.sub(r" +", " ", text)

    return text.strip()
