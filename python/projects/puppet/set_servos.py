#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
  
def map(value, from_low, from_high, to_low, to_high):
  from_range = from_high - from_low
  to_range = to_high - to_low
  scale_factor = float(from_range) / float(to_range)
  return to_low + (value / scale_factor)
  
  
def set_angle(channel, angle):
  pulse = int(map(angle, 0, 180, servoMin, servoMax))
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
while (True):
  angle = input("Angle:")
  set_angle(0, angle)
  set_angle(1, angle)
  set_angle(2, angle)
  set_angle(3, angle)
