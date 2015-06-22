import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

control_pin = 18

GPIO.setup(control_pin, GPIO.OUT)

try:         
    while True:
        duration_str = input("On time in minutes: ")
        duration = int(duration_str) * 60
        
        GPIO.output(control_pin, True)
        time.sleep(duration)
        GPIO.output(control_pin, False)            
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()