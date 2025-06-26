from flask import Flask, request, jsonify
import pandas as pd
from model import build_count, match_skills
app = Flask(__name__)


data_base = pd.read_csv("dataset.csv")
corpus = data_base["job_description_text"].dropna().tolist()
freq_counter = build_count(corpus)


@app.route("/detect-skills", methods=["POST"])
def detect_skills():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "job_description" in data:
        text = data["job_description"]
        if not text:
            return jsonify({"error": "Empty job description"}), 400
        return jsonify(match_skills(text, freq_counter))


    if "job_descriptions" in data:
        texts = data["job_descriptions"]
        if not isinstance(texts, list) or not texts:
            return jsonify(
                {"error": "Provide a'job_descriptions'"} 
            ), 400
        return jsonify([match_skills(t, freq_counter) for t in texts])

    return jsonify(
        {"job_descriptions' in the JSON body"}
    ), 400


if __name__ == "__main__":
    app.run(debug=True)
