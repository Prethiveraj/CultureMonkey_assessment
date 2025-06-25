from flask import Flask, request, jsonify
from model import match_skills
import pandas as pd
from collections import Counter
import re

app = Flask(__name__)

data_base = pd.read_csv("dataset.csv")
data_base = data_base.dropna(subset=['job_description_text'])

def filter_words(text):
    return re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())

freq_counter = Counter(data_base['job_description_text'].apply(filter_words).sum())

@app.route("/detect-skills", methods=["POST"])
def skill_detected():
    data = request.get_json()

    if not data or "job_description" not in data:
        return jsonify({"error": "Please provide 'job_description'"}), 400

    words = data["job_description"]

    try:
        result = match_skills(words, freq_counter)
        return jsonify(result)
    except Exception as problem:
        return jsonify("Something went wrong details" + str(problem)), 500

if __name__ == "__main__":
    app.run(debug=True)
