import RPi.GPIO as GPIO
import time

servo_pin = 18

# Tweak these values to get full range of servo movement
deg_0_pulse = 0.5   # ms (1)
deg_180_pulse = 2.5 # ms
f = 50.0   #50Hz = 20ms between pulses (2)

# Do some calculations on the pulse width parameters
period = 1000 / f # 20ms  (3)
k = 100 / period         # duty 0..100 over 20ms (4)
deg_0_duty = deg_0_pulse * k  # (5)
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k  # (6)

# Initialize the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)  # (7)
pwm = GPIO.PWM(servo_pin, f)      
pwm.start(0)

def set_angle(angle):   # (8)
    duty = deg_0_duty + (angle / 180.0) * duty_range
    pwm.ChangeDutyCycle(duty)

try:
    while True:    # (9)
        angle = input("Enter angle (0 to 180): ")
        set_angle(angle)
finally:
    print("Cleaning up")
    GPIO.cleanup()
