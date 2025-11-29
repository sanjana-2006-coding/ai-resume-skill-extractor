# app/extractor/entities.py
"""
Skill keyword dictionary for extraction.
You can expand this list anytime. For your resume project,
keep it simple and focused on software/AI skills.
"""

SKILL_KEYWORDS = {
    "programming_languages": [
        "python", "java", "c", "c++", "javascript", "typescript", "go", "rust"
    ],
    "web_frameworks": [
        "django", "flask", "fastapi", "react", "nodejs", "express", "nextjs"
    ],
    "databases": [
        "mysql", "postgresql", "mongodb", "sqlite", "oracle"
    ],
    "cloud": [
        "aws", "azure", "gcp", "docker", "kubernetes"
    ],
    "ml_ai": [
        "machine learning", "deep learning",
        "tensorflow", "pytorch", "sklearn", "nlp"
    ],
    "tools": [
        "git", "github", "jira", "postman", "linux"
    ],
}
