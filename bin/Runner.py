
import Speaker as Speaker
from actions.basics import tellTime,tellDate,dayOfWeek
import random
import os
import RPi.GPIO as GPIO
from systemOperations import EletricOperations


# Pin definitions
relay1=21
relay2=20
relay3=16

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)

GPIO.output(relay1, GPIO.HIGH)
GPIO.output(relay2, GPIO.HIGH)
GPIO.output(relay3, GPIO.HIGH)

def Runner(speech):

    try: 
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
            Speaker.speak(results)
      
        if 'toca musica' or "tocar musica" in speech.lower():
            songs_dir = "/music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
    
        if "como" and "estás"  in speech.lower():
                Speaker.speak(random.choice(["Estou bem,obrigado","tudo na boa","muito bem","estou indo","nada mal","bem,e você?","na boa,e você?"]))
        if "estou" and "bem" in speech.lower():
                Speaker.speak(random.choice(["isso é bom","maravilha","muito bom","felizmente","entendido"]))

        if  "teu" and "nome" in speech.lower():
                Speaker.speak(random.choice(["me chamo Luna","meu nome é Luna","Luna,Assistente Virtual"]))

        if "lista" and "de" and "comandos" in speech.lower():
                Speaker.speak(random.choice(["eu consigo acionar cargas eletricas ,fazer pesquisas na internet e executar programas"]))
        
        if "está tudo bem" in speech.lower():
                Speaker.speak("Boa")
    
        if "acende"  and "primeira" in speech.lower:
            EletricOperations().turnOnThePin(relay1)
         
        if "acende" and "segunda" in speech.lower:
            EletricOperations().turnOnThePin(relay2) 
        
        if "acende"  and "terceira" in speech.lower:
            EletricOperations().turnOnThePin(relay3)   

        if "apaga"  and "terceira" in speech.lower:
            EletricOperations().turnOffThePin(relay3)  

        if "apaga"  and "segunda" in speech.lower:
            EletricOperations().turnOffThePin(relay2) 

        if "apaga" and  "primeira" in speech.lower:
             EletricOperations().turnOffThePin(relay1)      


    except Exception as e:
        print(e)