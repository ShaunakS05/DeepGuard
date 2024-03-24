from google.cloud import speech
from moviepy.editor import *

client = speech.SpeechClient.from_service_account_file('backend/keygoogle.json')

# mp4audio = "realVideoTrump.mp4"

def extractSpeech(mp4audio):

    #mp4audio = "backend/KobeTestVideo.MP4"
    video = VideoFileClip(mp4audio)
    video.audio.write_audiofile("output.mp3")
    file_name = "output.mp3"

    with open(file_name, 'rb') as f:
        mp3_data = f.read()


    audio_file = speech.RecognitionAudio(content=mp3_data)

    config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    response = client.recognize(
        config=config,
        audio=audio_file
    )

    transcripts = []

    for result in response.results:
        # Loop through each alternative in the result
        for alternative in result.alternatives:
            # Add the transcript to the list
            transcripts.append(alternative.transcript)

    # Check if there are any transcripts
    if transcripts:
        # Join all transcripts into one single string
        all_transcripts = ' '.join(transcripts)
        # print("Hello")
        # print(all_transcripts)
        return all_transcripts
    else:
        return ("No transcripts found in the response.")
    
#extractSpeech()
