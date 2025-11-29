# app/matcher/job_matcher.py
"""
Simple job matching logic:
- Flattens skill dictionaries into normalized sets
- Computes match percentage = (matched skills) / (job skills)
- Returns score (0-100) and the list of matched skills
"""

from typing import Dict, List, Tuple


def flatten_skill_dict(skills_dict: Dict[str, List[str]]) -> set:
    """Flatten dict values to a set of lowercase skill tokens."""
    items = []
    for vals in skills_dict.values():
        if vals:
            items.extend(vals)
    return set([x.lower() for x in items])


def match_resume_to_job(resume_skills: Dict[str, List[str]], job_skills: Dict[str, List[str]]) -> Tuple[float, List[str]]:
    """
    Returns (score_percent, matched_skills_list).
    Score percent = matched_count / total_job_skills * 100
    """
    resume_set = flatten_skill_dict(resume_skills)
    job_set = flatten_skill_dict(job_skills)

    if not job_set:
        return 0.0, []

    matched = sorted(list(resume_set.intersection(job_set)))
    score = (len(matched) / len(job_set)) * 100.0
    return round(score, 2), matched
