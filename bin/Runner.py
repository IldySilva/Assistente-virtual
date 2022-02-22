import Speaker as Speaker
from actions.basics import tellTime,tellDate,dayOfWeek
import webbrowser
import random
import subprocess
import os
import time
import RPi.GPIO as GPIO

# Pin definitions
led_pin = 12

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

def Runner(speech):
    if  "horas"  and "que" in speech.lower():
        tellTime()
    if  "data de hoje" in speech.lower():
        tellDate()
    if "dia" and "semana" in speech.lower():
        dayOfWeek()
    if  "luna" in speech.lower():
        Speaker.speak(random.choice(["Em que posso ajudar?","Olá","Tudo bem?","Oi","Aqui"]))
        
    if 'wikipedia' in speech.lower():
        Speaker.speak('Procurar na wikipedia')
        query = speech.replace("wikipedia", "")
        results = speech.summary(query, sentences =2)
        print(results)
        Speaker.speak(results)

    if  'abre o youtube' in speech.lower():
        Speaker.speak(random.choice(["ok","está bem","feito"]))
        url = "youtube.com"
        chrome_path = 'c:/program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    if 'toca musica' in speech.lower():
        songs_dir = "C:\\Users\\PC\music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
  
    if "aumenta" and "volume" in speech:
        val = float(int(10))

        proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
        proc.wait()
    if "como" and "estás"  in speech.lower():
            Speaker.speak(random.choice(["Estou bem,obrigado","tudo na boa","muito bem","estou indo","nada mal","bem,e você?","na boa,e você?"]))
    if "estou" and "bem" in speech.lower():
            Speaker.speak(random.choice(["isso é bom","maravilha","muito bom","felizmente","entendido"]))

    if  "teu" and "nome" in speech.lower():
            Speaker.speak(random.choice(["me chamo Luna","meu nome é Luna","Luna,Assistente Virtual"]))

    if "lista" and "de" and "comandos" in speech.lower():

            Speaker.speak("Muita coisa")
    if "está tudo bem" in speech.lower():
            Speaker.speak("obrigado")
    if "acende" in speech.lower():
         GPIO.output(led_pin, GPIO.HIGH)
    