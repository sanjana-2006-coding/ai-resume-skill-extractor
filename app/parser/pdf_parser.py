# app/parser/pdf_parser.py
"""
PDF text extraction helper using pdfplumber.
Returns the concatenated text of all pages (or empty string).
Works for most text-based PDFs. If a resume is a scanned image,
you'd need OCR (not required for MVP).
"""

import pdfplumber
from typing import Optional

def extract_text_from_pdf(path: str) -> str:
    """
    Extract text from a PDF file and return it as a single string.
    If extraction fails or file has no text, returns an empty string.
    """
    text_pages = []
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_pages.append(page_text)
    except Exception as e:
        # don't crash the pipeline — return empty string and let caller handle it
        return ""
    return "\n".join(text_pages)
