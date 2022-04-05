
import random
import speech_recognition as sr
from Speaker import speak
def takeCommand():

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Ouvindo...")
            audio = r.listen(source)
        try :
            print("Reconhecendo,Aguarde...")
            query = r.recognize_google(audio, language = 'pt-pt')
            print(f"user said: {query}\n")

        except Exception as e:
            speak(random.choice(["Nao entendi","Repita por favor","Não consigo entender"]))
            print("Diga novamente a frase...")
            query = None

        return query

    except Exception as e:
        print(e)