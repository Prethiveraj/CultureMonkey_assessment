# CultureMonkey Internship Assessment – Skill Trend Detector API

This project is part of the CultureMonkey Internship Assessment.
It uses **Python** and **Flask** to build a REST API that detects **technical skills** from job descriptions and classifies them as either:

* `emerging`: less common skills
* `established`: widely used, popular skills

The classification is based on how frequently each skill appears in real-world job postings.

---

## How to Run (Setup Instructions)

```bash
git clone https://github.com/Prethiveraj/CultureMonkey_assessment.git
cd CultureMonkey_assessment/api

python -m venv venv
venv\Scripts\activate  # Windows
python app.py
```

Server will be running at:

```
http://127.0.0.1:5000
```

---

## API Usage Guide

### Endpoint:

```
POST /detect-skills
```

### Request Body:

```json
{
  "job_description": "We are looking for a developer with experience in Python, React, and machine learning."
}
```

### Example Response:

```json
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
```

---

## Google Colab – Data Analysis

📊 Explore the dataset, word frequency, and skill trends:
👉 [Google Colab Link]([https://colab.research.google.com/drive/your_colab_file_id_here](https://colab.research.google.com/github/Prethiveraj/CultureMonkey_assessment/blob/main/analysis/job.ipynb))

---

## Demo Video

🎥 Watch the project demo:
👉 [Google Drive Demo Video]([https://drive.google.com/file/d/your_demo_file_id/view?usp=sharing](https://drive.google.com/drive/folders/1oe_lVClZpOc50l1MlsRvuGiUXTttO5kW?usp=sharing))

---

## What's Included

* `app.py` – Flask REST API
* `model.py` – Skill classification logic
* `dataset.csv` – Source job descriptions
* `job_market_analysis.ipynb` – EDA notebook (Colab)
* `README.md` – Instructions and documentation
* `test_api.py` – Sample API testing script
