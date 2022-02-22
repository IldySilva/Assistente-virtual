import datetime
import Speaker as Speaker
import random

def tellTime():
    time=datetime.datetime.now()
    Speaker.speak(time.strftime("%H:%M"))

def tellDate():
    data=datetime.date.today().strftime("%d/%m/%Y")
    fala=random.choice(["hoje é " + data,"exatamente "+ data,data,])
    Speaker.speak(fala)

 
def dayOfWeek():
    
    dia = datetime.datetime.today().weekday() + 1

    Dias = {1: 'Segunda', 2: 'Terça-feira',
            3: 'Quarta',  4: 'Quinta-feira',
            5: 'Sexta-feira',   6: 'Sábado',
            7: 'Domingo'}

    if dia in Dias.keys():
        dias_semana = Dias[dia]
        Speaker.speak(random.choice(["Hoje é " + dias_semana,dias_semana]))
async def howIsWheather():
    Speaker.speak("Em que cidade")
  