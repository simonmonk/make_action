import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

control_pin = 18

GPIO.setup(control_pin, GPIO.OUT)

try:         
    while True:
        GPIO.output(control_pin, False)  
        time.sleep(5)                 
        GPIO.output(control_pin, True) 
        time.sleep(2)                 
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()