
import os
import requests
import sys

def speak(text, voice_id):
    key = os.getenv("ELEVENLABS_API_KEY")
    if not key:
        raise ValueError("ELEVENLABS_API_KEY non impostata nelle variabili d'ambiente.")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": key,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Errore API: {response.status_code} - {response.text}")

    with open("output.mp3", "wb") as f:
        f.write(response.content)

    if sys.platform.startswith("win"):
        os.system("start output.mp3")
    elif sys.platform.startswith("darwin"):
        os.system("open output.mp3")
    else:
        os.system("xdg-open output.mp3")

# Esempio di utilizzo:
# speak("Ciao, questa è una prova!", "INSERISCI_IL_TUO_VOICE_ID")
