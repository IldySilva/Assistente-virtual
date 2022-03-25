import Runner as runner 
from Recognizer import takeCommand

while True:
    try:
        reconhecido=  takeCommand()
        if reconhecido !=None:
            runner.Runner(reconhecido)

    except Exception as e:
         print(e)     
                        



            
  
  