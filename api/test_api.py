import requests

url = "http://127.0.0.1:5000/detect-skills"
single_tests = {
    "job_descriptions": [
        "Python developer with Flask and AWS experience needed.",
        "React and JavaScript frontend developer position.",
        "Data scientist with machine learning and SQL skills required.",
        "Cloud engineer with Azure and AWS knowledge."
    ]
}

response = requests.post(url, json=single_tests)

import json
print(json.dumps(response.json(), indent=2), 'done')
