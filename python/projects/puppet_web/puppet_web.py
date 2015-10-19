from Adafruit_PWM_Servo_Driver import PWM  
from pygame import mixer
import time
import dweepy # 1

pwm = PWM(0x40)
mixer.init()   
mixer.music.load("pepe_1.wav")

dweet_key = 'pepe_the_puppet'  # 2

servoMin = 150  # Min pulse length out of 4096     
servoMax = 600  # Max pulse length out of 4096

dance = [     
  #lh  lf  rf  rh
  [130, 20, 20, 130],
  [30, 160, 160, 30],    
  [90, 90, 90, 90]
]

delay = 0.2   
  
def map(value, from_low, from_high, to_low, to_high):  
  from_range = from_high - from_low
  to_range = to_high - to_low
  scale_factor = float(from_range) / float(to_range)
  return to_low + (value / scale_factor)
  
  
def set_angle(channel, angle):  
  pulse = int(map(angle, 0, 180, servoMin, servoMax))
  pwm.setPWM(channel, 0, pulse)
  
def dance_step(step):  
  set_angle(0, step[0])
  set_angle(1, step[1])
  set_angle(2, step[2])
  set_angle(3, step[3])
  
def dance_pupet():    # 3
    for i in range(1, 10):
        for step in dance:
            dance_step(step)
            time.sleep(delay)
    
pwm.setPWMFreq(60)   

      
while True:
    try:   # 2
        for dweet in dweepy.listen_for_dweets_from(dweet_key):   # 4
            print("Dance Pepe! Dance!")
            mixer.music.play()
            dance_pupet()
    except Exception:
        pass
