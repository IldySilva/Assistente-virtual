import pyttsx3 
from gtts import gTTS
import os
try:
        speaker=pyttsx3.init()
        v=speaker.getProperty("voice")
        print(v)
        speaker.setProperty("voice",speaker.getProperty("voices")[0].id)
except Exception as e:
    print(e)

def speak(speech):

    try:    
        tts=gTTS(text=speech,lang="pt")
        tts.save("/tmp/lunaSPeech.mp3")
        os.system("mpg321 /tmp/lunaSPeech.mp3")
    except Exception as e:
        print(e)

speak("SISTEMA Iniciado")