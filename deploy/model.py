import json
import requests
import numpy as np

MODEL_URI = "http://localhost:8501/v1/models/review:predict"
CLASSES = ["NOT A 5-STAR REVIEW", "A 5-STAR REVIEW"]

def make_prediction(instances):
    payload = {
        "instances": [[instances]]
    }

    # Making POST request
    response = requests.post(MODEL_URI, json=payload)
    result = json.loads(response.content.decode('utf-8'))
    prediction = np.squeeze(result['predictions'][0])
    class_name = CLASSES[int(prediction > 0.5)]
    return class_name