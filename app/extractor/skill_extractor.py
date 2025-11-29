# app/extractor/skill_extractor.py
"""
Extracts skills from resume text using keyword matching + fuzzy matching.
Keeps it simple but effective for an MVP.
"""

from typing import Dict, List
from fuzzywuzzy import fuzz
from .entities import SKILL_KEYWORDS


def extract_skills(text: str) -> Dict[str, List[str]]:
    """
    Returns a dictionary of extracted skills per category.

    Uses:
        - Direct keyword matching
        - Fuzzy matching for partial/close matches
    """
    extracted = {category: [] for category in SKILL_KEYWORDS}

    for category, skills in SKILL_KEYWORDS.items():
        for skill in skills:
            # direct match
            if skill in text:
                extracted[category].append(skill)
                continue

            # fuzzy match (threshold = 80)
            if fuzz.partial_ratio(skill, text) >= 80:
                extracted[category].append(skill)

    return extracted
