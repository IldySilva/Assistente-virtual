
import speech_recognition as sr
from Speaker import speak
def takeCommand():

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)

        try :
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'pt-pt')
            print(f"user said: {query}\n")

        except Exception as e:
            print(e)
            speak("Nao entendi")
            print("Say that again please...")
            query = None

        return query

    except Exception as e:
        print(e)