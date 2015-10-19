import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

control_pin = 18     # (1)

GPIO.setup(control_pin, GPIO.OUT)
motor_pwm = GPIO.PWM(control_pin, 500)  # (2)
motor_pwm.start(0)                      # (3)

try:         
    while True:                         # (4)
        duty = input('Enter Duty Cycle (0 to 100): ')
        if duty < 0 or duty > 100:
            print('0 to 100')
        else:
            motor_pwm.ChangeDutyCycle(duty)
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()