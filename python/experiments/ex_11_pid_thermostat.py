import os
import glob
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

heat_pin = 18 
base_dir = '/sys/bus/w1/devices/'   # (1)
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
GPIO.setup(heat_pin, GPIO.OUT)
heat_pwm = GPIO.PWM(heat_pin, 500)
heat_pwm.start(0)

old_error = 0 # (2)
old_time = 0
measured_temp = 0
p_term = 0
i_term = 0 
d_term = 0

def read_temp_raw():  # (3)
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():  # (4)
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
        
def constrain(value, min, max): # (5)
    if value < min :
        return min
    if value > max :
        return max
    else: 
        return value

def update_pid():   # (6)
    global old_time, old_error, measured_temp, set_temp
    global p_term, i_term, d_term
    now = time.time()               
    dt = now - old_time # (7)
    error = set_temp - measured_temp # (8)
    de = error - old_error       # (9)

    p_term = kp * error                     # (10)
    i_term += ki * error                    # (11)
    i_term = constrain(i_term, 0, 100)      # (12)
    d_term = (de / dt) * kd                 # (13)
                                
    old_error = error     
    # print((measured_temp, p_term, i_term, d_term))  
    output = p_term + i_term + d_term      # (14)
    output = constrain(output, 0, 100)       
    return output

set_temp = input('Enter set temperature in C ')  # (15)
kp = input('kp: ')
ki = input('ki: ')
kd = input('kd: ')

old_time = time.time() # (16)
try:
    while True:
        now = time.time()
        if  now > old_time + 1 : # ()17)
            old_time = now 
            measured_temp = read_temp()
            duty = update_pid()
            heat_pwm.ChangeDutyCycle(duty)
        
            print(str(measured_temp) + ', ' + str(set_temp) + ', ' + str(duty))
finally:
    GPIO.cleanup()