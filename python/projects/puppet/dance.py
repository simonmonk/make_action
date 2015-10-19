from Adafruit_PWM_Servo_Driver import PWM   # 1
import time

pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4095     # 2
servoMax = 600  # Max pulse length out of 4095

dance = [      # 3
  #lh  lf  rf  rh
  [90, 90, 90, 90],
  [130, 30, 30, 130],
  [30, 130, 130, 30]    
]

delay = 0.2   # 4
  
def map(value, from_low, from_high, to_low, to_high):  # 5
  from_range = from_high - from_low
  to_range = to_high - to_low
  scale_factor = float(from_range) / float(to_range)
  return to_low + (value / scale_factor)
  
  
def set_angle(channel, angle):  # 6
  pulse = int(map(angle, 0, 180, servoMin, servoMax))
  pwm.setPWM(channel, 0, pulse)
  
def dance_step(step):  # 7
  set_angle(0, step[0])
  set_angle(1, step[1])
  set_angle(2, step[2])
  set_angle(3, step[3])
  

pwm.setPWMFreq(60)   # 8


while (True):   # 9
  for step in dance:
      dance_step(step)
      time.sleep(delay)
