
from gtts import gTTS
import os
import sys

def speak(text, lang='it'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    
    if sys.platform.startswith("win"):
        os.system("start output.mp3")
    elif sys.platform.startswith("darwin"):
        os.system("open output.mp3")
    else:
        os.system("xdg-open output.mp3")

# Esempio di utilizzo:
# speak("Ciao, questa è una prova!")
