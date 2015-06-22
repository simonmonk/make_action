import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

control_pin = 18

GPIO.setup(control_pin, GPIO.OUT)

is_on = False

def input_time(prompt):
    try:
        time_str = raw_input(prompt)
        hr_min = time_str.split(':')
        on_hour = int(hr_min[0])
        on_min = int(hr_min[1])
        return (on_hour, on_min)
    except:
        print('Incorrect Time Format (HH:MM)')
        return (0, 0)

try:         
    while True:
        on_hour, on_min = input_time('Enter Start Time (HH:MM)')
        on_hour, on_min = input_time('Enter End Time (HH:MM)')
        now = datetime.datetime.now()
        if not is_on and now.hour == on_hour and now.minute == on_min:
            is_on = True
            GPIO.write(control_pin, True)
        if is_on and now.hour == off_hour and now.minute == off_min:
            is_on = False
            GPIO.write(control_pin, False)            
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()