import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

step_pin = 24
dir_pin = 25
ms1_pin = 23
ms2_pin = 18

GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(ms1_pin, GPIO.OUT)
GPIO.setup(ms2_pin, GPIO.OUT)

period = 0.02

def step(steps, direction, period):  
  GPIO.output(dir_pin, direction)  
  for i in range(0, steps):
    GPIO.output(step_pin, True)
    time.sleep(0.000002)
    GPIO.output(step_pin, False)
    time.sleep(period)

def step_mode(mode):
    GPIO.output(ms1_pin, mode & 1)
    GPIO.output(ms2_pin, mode & 2)

try:
    print('Command letter followed by number');
    print('p20 - set the inter-step period to 20ms (control speed)');
    print('m - set stepping mode (0-none 1-half, 2-quater, 3-eighth)');
    print('f100 - forward 100 steps');
    print('r100 - reverse 100 steps');
    
    while True:
        command = raw_input('Enter command: ')
        parameter_str = command[1:] # from char 1 to end
        parameter = int(parameter_str)
        if command[0] == 'p':
            period = parameter / 1000.0
        elif command[0] == 'm':
            step_mode(parameter)
        elif command[0] == 'f':
            step(parameter, True, period)
        elif command[0] == 'r':
            step(parameter, False, period)

finally:
    print('Cleaning up')
    GPIO.cleanup()