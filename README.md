# CultureMonkey_assessment

# 🧠 CultureMonkey Internship Assessment – Skill Trend Detector API

This project is part of the CultureMonkey Internship Assessment.  
It uses **Python** and **Flask** to build a REST API that detects **technical skills** from job descriptions and classifies them as either:

- `emerging`: less common skills
- `established`: widely used, popular skills

The classification is based on how frequently each skill appears in real-world job postings.

---

---

## ⚙️ How to Run (Setup Instructions)

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/Prethiveraj/CultureMonkey_assessment.git
cd CultureMonkey_assessment/api

python -m venv venv
venv\Scripts\activate  # Windows
python app.py
http://127.0.0.1:5000

## API Usage Guide

POST /detect-skills
{
  "job_description": "We are looking for a developer with experience in Python, React, and machine learning."
}

{
  "found_skills": [
    {
      "skill": "python",
      "category": "established",
      "trend_score": 0.89
    },
    {
      "skill": "react",
      "category": "established",
      "trend_score": 0.85
    },
    {
      "skill": "machine learning",
      "category": "emerging",
      "trend_score": 0.22
    }
  ]
}

