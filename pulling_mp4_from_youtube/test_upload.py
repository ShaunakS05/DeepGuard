import requests

# The URL of your FastAPI endpoint
url = 'http://127.0.0.1:8000/uploadvideo/'

# The path to the MP4 file you want to upload
file_path = 'downloaded_video.mp4'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    # Define the files in the request (form field name, file-like object, content type)
    files = {'video': (file.name, file, 'video/mp4')}
    
    # Send the POST request with the file
    response = requests.post(url, files=files)
    
    # Print out the response from the server
    print(response.text)