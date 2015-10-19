import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red_pin = 18
orange_pin = 23
green_pin = 24

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(orange_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

def set_leds(red, orange, green):    # (1)
    GPIO.output(red_pin, red)
    GPIO.output(orange_pin, orange)
    GPIO.output(green_pin, green)

try:         
    while True:
        set_leds(1, 0, 0)
        time.sleep(3)
        set_leds(1, 1, 0)
        time.sleep(0.5)
        set_leds(0, 0, 1)
        time.sleep(5)
        set_leds(0, 1, 0)
        time.sleep(0.5)
          
finally:  
    print("Cleaning up")
    GPIO.cleanup()