
import os
import requests

def speak(text):
    key = os.getenv("ELEVENLABS_API_KEY")
    url = "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID"
    headers = {
        "xi-api-key": key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    r = requests.post(url, headers=headers, json=payload)
    with open("output.mp3", "wb") as f:
        f.write(r.content)
    os.system("start output.mp3")  # Works on Windows
