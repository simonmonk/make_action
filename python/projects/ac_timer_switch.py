import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

control_pin = 18

GPIO.setup(control_pin, GPIO.OUT)

try:         
    while True:   # 1
        duration_str = input("On time in minutes: ")   # 2
        duration = int(duration_str) * 60
        
        GPIO.output(control_pin, True)    # 3
        time.sleep(duration)
        GPIO.output(control_pin, False)   # 4
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()