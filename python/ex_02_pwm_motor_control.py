#ex_02_pwm_motor_control.py

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

motor_pin = 18

GPIO.setup(motor_pin, GPIO.OUT)
motor_pwm = GPIO.PWM(motor_pin, 500)
motor_pwm.start(0)

try:         
    while True:
        duty = input('Enter Duty Cycle (0 to 100): ')
        if duty < 0 or duty > 100:
            print('0 to 100')
        else:
            motor_pwm.ChangeDutyCycle(duty)
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()