from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # 1
CONTROL_PIN = 18
GPIO.setup(CONTROL_PIN, GPIO.OUT)

@route('/')   # 2
def index():
    return template('home.tpl')
    
@route('/on') # 3
def index():
    GPIO.output(CONTROL_PIN, 1)
    return template('home.tpl')
    
@route('/off') # 4
def index():
    GPIO.output(CONTROL_PIN, 0)
    return template('home.tpl')    
        

try: 
    run(host='0.0.0.0', port=80)  # 5
finally:  
    print('Cleaning up GPIO')
    GPIO.cleanup()
