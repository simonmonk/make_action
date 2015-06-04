import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

in_1_pin = 23
in_2_pin = 24
in_3_pin = 25
in_4_pin = 18

GPIO.setup(in_1_pin, GPIO.OUT)
GPIO.setup(in_2_pin, GPIO.OUT)
GPIO.setup(in_3_pin, GPIO.OUT)
GPIO.setup(in_4_pin, GPIO.OUT)

def forward(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)

def backwards(delay, steps):  
  for i in range(0, steps):
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)

  
def setStep(in1, in2, in3, in4):
  GPIO.output(in_1_pin, in1)
  GPIO.output(in_1_pin, in2)
  GPIO.output(in_1_pin, in3)
  GPIO.output(in_1_pin, in4)

while True:
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  forward(int(delay) / 1000.0, int(steps))
  steps = raw_input("How many steps backwards? ")
  backwards(int(delay) / 1000.0, int(steps))