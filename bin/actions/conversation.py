from Speaker import speaker
import controllers
def whatNow():
    speaker.speak("Sou o seu assistente estou aqui para automatizar algumas das suas tarefas,"
                "consigo acionar cargas,"
                "colocar alarme, "
                "pesquisar na web,"
                "verificar o tempo,"
                "e dentre outras tarefas,"
                "o que quer que eu faça ")
def stopSpeak():
    speaker.stop()
    speaker.runAndWait()
def stopListening():
    print("parando de ouvir")
    controllers.canListen=False
def startListening():
    controllers.canListen=True


