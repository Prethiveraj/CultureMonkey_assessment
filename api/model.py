from collections import Counter
import re

word_skills = {
    "python", "javascript", "react", "node.js", "flask", "fastapi",
    "pytorch", "tensorflow", "machine learning", "deep learning",
    "large language models","sql", "mongodb", "data science", "aws", "azure"
}

def filter_words(text):
    text = text.lower()
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text)
    return [skill for skill in word_skills if skill in text]

def build_count(job_descriptions):
    all_skills = []
    for job_desc in job_descriptions:
        skills = filter_words(job_desc)
        all_skills.extend(skills)
    return Counter(all_skills)

def match_skills(text,count):
    try:
        found_skills = filter_words(text)
    except Exception as issue:
        return {"error": "problem:" + str(issue)}

    if not found_skills:
        return {"message": "Nothing found ."}

    max_freq = max(count.values()) or 1
    total_result = []

    unique_skills = list(set(found_skills))

    for skill in unique_skills:
        freq = count.get(skill, 0)
        score = freq / max_freq
        if score < 0.4:
            label = "emerging"
        else:
            label = "established"

        total_result.append({
            "skill": skill,
            "category": label,
            "trend_score": round(score, 2)
        })

    return {"Found_skills": total_result}

# Test data
job_descriptions = [
    "Python developer with Flask and AWS experience needed.",
    "React and JavaScript frontend developer position.",
    "Data scientist with machine learning and SQL skills required.",
    "Cloud engineer with Azure and AWS knowledge."
]
