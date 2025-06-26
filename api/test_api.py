import requests

url = "http://127.0.0.1:5000/detect-skills"
single_tests = {
    "job_description": "Python developer with Flask and AWS experience needed."
}


response = requests.post(url, json=single_tests)

import json
print(json.dumps(response.json(), indent=2), 'done')
