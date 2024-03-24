from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from audioDetection import audioDetection1
from texttospeech import extractSpeech
#from textdecypher import textDetection
import requests
import base64
from moviepy.editor import *
import json

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Data": "Test"}

@app.post("/check-audio-deepfake")
async def check_audio_deepfake(mp4video: UploadFile):
    contents = await mp4video.read()
    with open(mp4video.filename, "wb") as f:
        video = VideoFileClip(mp4video.filename)
        video.audio.write_audiofile("output.mp3")
        result= audioDetection1("output.mp3")
        return {"result": result}

#@app.post("/check-text-deepfake")
#def check_text_deepfake(context):
 #   text = extractSpeech()
  #  response = textDetection(context, text)
   # return {"result": response}


@app.post("/check-visual-deepfake")
async def check_visual_deepfake(file_upload: UploadFile):
    contents = await file_upload.read()
    url = "https://ping.arya.ai/api/v1/deepfake-detection"
    base64_data = base64.b64encode(contents).decode("utf-8")
    payload = {"doc_base64": str(base64_data), "req_id": "Detecting_Deepfake", "isIOS": False, "doc_type": "video", "orientation": 0, }
    headers = {
        'token': '9b72fe9af0336a95f32ee5bf4bd1af19',
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text
