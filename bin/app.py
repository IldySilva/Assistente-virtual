import Runner as runner 
from Recognizer import takeCommand
from Runner import GPIO
GPIO.output(12, GPIO.LOW)

while True:
    reconhecido=  takeCommand()
    if reconhecido !=None:
        runner.Runner(reconhecido)

          
        



            
  
  