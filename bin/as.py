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
#  Set LED pin as output
while True:
        GPIO.output(led_pin, GPIO.HIGH) # Turn LED on
        print("aceso")
        time.sleep(1)
                         # Delay for 1 second
        GPIO.output(led_pin, GPIO.LOW)  # Turn LED off
        print("apagado")
        time.sleep(1)    
                       