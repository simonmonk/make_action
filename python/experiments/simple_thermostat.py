import os
import glob
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

heat_pin = 18 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
GPIO.setup(heat_pin, GPIO.OUT)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

set_temp = input('Enter set temperature in C ')
try:
    while True:
        measured_temp = read_temp()
        if set_temp > measured_temp:
            GPIO.output(heat_pin, True)
            print(str(measured_temp) + ', ' + str(set_temp) + ', 1')
        else:
            GPIO.output(heat_pin, False)
            print(str(measured_temp) + ', ' + str(set_temp) + ', 0')
	    time.sleep(1)
finally:
    GPIO.cleanup()