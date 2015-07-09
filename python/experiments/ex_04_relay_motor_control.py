#ex_01_basic_motor_control.py

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

motor_pin = 18

GPIO.setup(motor_pin, GPIO.OUT)


try:         
    while True:
        GPIO.output(motor_pin, True)  # Motor on
        time.sleep(5)                 # delay 0.5 seconds
        GPIO.output(motor_pin, False) # Motor off
        time.sleep(2)                 # delay 0.5 seconds
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()