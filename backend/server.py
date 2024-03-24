from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
# from pytube import YouTube
from audioDetection import *
from texttospeech import extractSpeech
from textdecypher import textDetection
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
async def check_audio_deepfake(file_upload: UploadFile):
    contents = await file_upload.read()
    
    with open(file_upload.filename, "wb") as f:
        f.write(contents)
    
    video = VideoFileClip(file_upload.filename)
    video.audio.write_audiofile("audio_data/donald_trump/fake/output.mp3")
    deepfake_label, scores = returnAudioScores()
    scores_list = scores.tolist() if isinstance(scores, np.ndarray) else scores
    return {"DeepFake": deepfake_label, "Scores": scores_list}
    
    #with open(file_upload.filename, "wb") as f:
    #    video = VideoFileClip(file_upload.filename)
    #    video.audio.write_audiofile("audio_data/donald_trump/fake/output.mp3")
    #    return {"DeepFake": returnAudioScores()[0], "Scores": returnAudioScores[1]}

@app.post("/check-text-deepfake")
async def check_text_deepfake(file_upload: UploadFile, name: str=Form(), context: str=Form()):
    contents = await file_upload.read()
    with open(file_upload.filename, "wb") as f:
        f.write(contents)

    text = extractSpeech(file_upload.filename)
    response = textDetection(name, text, context)
    print(response)
    return response

"""
@app.post("/check-visual-deepfake")
async def check_visual_deepfake(file_upload: UploadFile):
    contents = await file_upload.read()
    url = "https://ping.arya.ai/api/v1/deepfake-detection"
    base64_data = base64.b64encode(contents).decode("utf-8")
    payload = {"doc_base64": str(base64_data), "req_id": "Detecting_Deepfake", "isIOS": False, "doc_type": "video", "orientation": 0, }
    headers = {
        'token': '9b77aacff76a6a9ca378e2b21ad0fc4d',
        'content-type': 'application/json'
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text
"""

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

@app.post("/title/")
def get_thumbnail_and_title(youtube_link: str="https://www.youtube.com/shorts/jcNzoONhrmE"):
    # Instantiate a YouTube object using the provided link
    yt = YouTube(youtube_link)

    # Return streaming response
    return yt.title
@app.post("/thumbnail/")
def get_thumbnail_and_title(youtube_link: str="https://www.youtube.com/shorts/jcNzoONhrmE"):
    # Instantiate a YouTube object using the provided link
    yt = YouTube(youtube_link)

    # Return streaming response
    return yt.thumbnail_url

# Curl Command to get thumnail:
# curl http://127.0.0.1:8000/thumbnail_and_title/?youtube_link=https://www.youtube.com/shorts/jcNzoONhrmE
