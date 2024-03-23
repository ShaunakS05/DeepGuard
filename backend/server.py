from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from audioDetection import audioDetection1
from texttospeech import extractSpeech
from textdecypher import textDetection
import requests
import base64
from moviepy.editor import *

app = FastAPI()

origins = [
    'https://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

@app.get("/")
def home():
    return {"Data": "Test"}

@app.post("/check-audio-deepfake")
def check_audio_deepfake(mp4audio):
    video = VideoFileClip(mp4audio)
    video.audio.write_audiofile("output.mp3")
    result= audioDetection1("output.mp3")
    return {"result": result}

@app.post("/check-text-deepfake")
def check_text_deepfake(context):
    text = extractSpeech()
    response = textDetection(context, text)
    return {"result": response}


@app.post("/check-visual-deepfake")
def check__visual_deepfake(video):
    url = "https://ping.arya.ai/api/v1/deepfake-detection"
    with open(video, "rb") as video_file:
        video_data = video_file.read()
    base64_data = base64.b64encode(video_data).decode("utf-8")
    payload = {"doc_base64": str(base64_data), "req_id": "Detecting_Deepfake", "isIOS": False, "doc_type": "video", "orientation": 0, }
    headers = {
        'token': '9b24ff9ff5673c93f425b7e44b80fb1e',
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return {"Data:": response.text}
