from fastapi import FastAPI
import requests
import base64;

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Test"}

@app.get("/check-deepfake")
def check_deepfake():
    url = "https://ping.arya.ai/api/v1/deepfake-detection"
    with open("StephCurryReal.mp4", "rb") as video_file:
        video_data = video_file.read()
    base64_data = base64.b64encode(video_data).decode("utf-8")
    payload = {"doc_base64": str(base64_data), "req_id": "Detecting_Deepfake", "isIOS": False, "doc_type": "video", "orientation": 0, }
    headers = {
        'token': '9b24ff9ff5673c93f425b7e44b80fb1e',
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return {"Data:": response.text}
