import requests

url = "http://127.0.0.1:5000/detect-skills"
payload = {
    "job_description": "Experience with Python, TensorFlow, javascript, java, aws and diffusion models required."
}

response = requests.post(url, json=payload)

import json
print(json.dumps(response.json(), indent=2), 'done')
