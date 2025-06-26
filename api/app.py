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

all_words = []
for data in data_base['job_description_text']:
    all_words.extend(filter_words(data))
freq_counter = Counter(all_words)

@app.route("/detect-skills", methods=["POST"])
def detect_skills():    
    data = request.get_json()
    
    if not data:
        return jsonify({"No data provided"}), 400
    
    try:
        if "job_description" in data:
            words = data["job_description"]
            if not words:
                return jsonify({"Empty job desp"}), 400
                
            result = match_skills(words, freq_counter)
            return jsonify(result)
        
        elif "job_descriptions" in data:
            texts = data["job_descriptions"]
            if not isinstance(texts, list) or not texts:
                return jsonify({"Provide list of job desp"}), 400
            
            results = []
            for text in texts:
                try:
                    skills = match_skills(text, freq_counter)
                    results.append(skills)
                except Exception as problem:
                    results.append({"error": str(problem)})
            
            return jsonify(results)
        
        else:
            return jsonify({"use the job desp"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)


