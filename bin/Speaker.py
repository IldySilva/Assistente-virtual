from gtts import gTTS
import os

def speak(textToSpeech:str):

    try:    
        tts=gTTS(text=textToSpeech,lang="pt")
        tts.save("/tmp/lunaSPeech.mp3")
        os.system("mpg321 /tmp/lunaSPeech.mp3")
    except Exception as e:
        print(e)

speak("Sistema Iniciado")