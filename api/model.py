from collections import Counter
import re
from statistics import quantiles            

SKILL_WORDS = {
    "python", "javascript", "typescript", "react", "next.js", "node.js",
    "flask", "fastapi", "django",
    "pytorch", "tensorflow", "machine learning", "deep learning",
    "large language models", "llm",
    "sql", "mongodb", "postgresql", "data science",
    "aws", "azure", "gcp"
}

def filter_words(text: str) -> list[str]:
    if not text:
        return []
    text_lc = text.lower()
    return [skill for skill in SKILL_WORDS if skill in text_lc]


def build_count(job_descriptions: list[str]) -> Counter:
    doc_freq = Counter()
    for jd in job_descriptions:
        doc_freq.update(set(filter_words(jd)))
    return doc_freq


def number_hold(freq_counter: Counter) -> int:

    if not freq_counter:
        return 1
    q1, _, _ = quantiles(freq_counter.values(), n=4, method="inclusive")
    return max(1, int(q1))

def match_skills(text: str, freq_counter: Counter) -> dict:
    found = filter_words(text)

    if not found:
        return {"No skills detected."}

    q1_threshold = number_hold(freq_counter)

    total = []
    for skills in sorted(set(found)):
        freq = freq_counter.get(skills, 0)
        if freq < q1_threshold:
            label = "emerging"
        else:
            label = "established"
        score = round(freq / max(freq_counter.values(), default=1), 2)
        total.append(
            {"skill": skills, "trend_score": score,
             "category": label}
        )

    return {"skills": total}

