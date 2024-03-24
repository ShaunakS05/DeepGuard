from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pytube import YouTube
from audioDetection import audioDetection1
from texttospeech import extractSpeech
# from textdecypher import textDetection
import io
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


@app.get("/mp4/")
def get_mp4(youtube_link: str):
    # Instantiate a YouTube object using the provided link
    yt = YouTube(youtube_link)
    
    # Select the highest quality progressive stream
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    if not stream:
        raise HTTPException(status_code=404, detail="Suitable video stream not found")

    # Define a generator to buffer video data
    def iter_video():
        with io.BytesIO() as video_buffer:
            # Stream the video content into the buffer
            stream.stream_to_buffer(buffer=video_buffer)
            # Reset buffer's current position to the beginning
            video_buffer.seek(0)
            # Stream content from buffer to response
            while chunk := video_buffer.read(4096):
                yield chunk

    # Return streaming response
    return StreamingResponse(iter_video(), media_type="video/mp4")

# Curl Command to Download video to your local directory:
# curl -o downloaded_video.mp4 "http://127.0.0.1:8000/mp4/?youtube_link=https://www.youtube.com/shorts/jcNzoONhrmE"

@app.get("/thumbnail_and_title/")
def get_thumbnail_and_title(youtube_link: str="https://www.youtube.com/shorts/jcNzoONhrmE"):
    # Instantiate a YouTube object using the provided link
    yt = YouTube(youtube_link)

    # Return streaming response
    return {"Title": yt.title , "Thumbnail_URL":yt.thumbnail_url}

# Curl Command to get thumnail:
# curl http://127.0.0.1:8000/thumbnail_and_title/?youtube_link=https://www.youtube.com/shorts/jcNzoONhrmE
