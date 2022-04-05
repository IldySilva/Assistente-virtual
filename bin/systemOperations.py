
import os
import RPi.GPIO as GPIO
import Speaker as Speaker

class EletricOperations:

    def turnOnThePin(pin):
        GPIO.output(pin, GPIO.HIGH)
        Speaker.speak("lampada numero "+str(pin) + " acessa")

        
    def turnOffThePin(pin):
        GPIO.output(pin, GPIO.LOW)
        Speaker.speak("lampada numero "+str(pin) + " apagada ")

