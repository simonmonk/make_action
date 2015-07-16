# 03_rgb.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com
# Based on Recipe 9.9 in The Raspberry Pi Cookbook by Simon Monk.

from Tkinter import *       # tkinter provides the graphical user interface (GUI)
import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# Start Pulse Width Modulation (PWM) on the red, green and blue channels to 
# control the brightness of the LEDs.
# Follow this link for more info on PWM: http://en.wikipedia.org/wiki/Pulse-width_modulation
pwmRed = GPIO.PWM(18, 500)
pwmRed.start(100)

pwmGreen = GPIO.PWM(23, 500)
pwmGreen.start(100)

pwmBlue = GPIO.PWM(24, 500)
pwmBlue.start(100)


# group together all of the GUI code into a class called App
class App:
    
    # this function gets called when the app is created
    def __init__(self, master):
        # A frame holds the various GUI controls
        frame = Frame(master)
        frame.pack()
        
        # Create the labels and position them in a grid layout
        Label(frame, text='Red').grid(row=0, column=0)
        Label(frame, text='Green').grid(row=1, column=0)
        Label(frame, text='Blue').grid(row=2, column=0)
        
        # Create the sliders and position them in a grid layout
        # the 'command' attribute specifys a method to call when
        # a slider is moved
        scaleRed = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateRed)
        scaleRed.grid(row=0, column=1)
        scaleGreen = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateGreen)
        scaleGreen.grid(row=1, column=1)
        scaleBlue = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateBlue)
        scaleBlue.grid(row=2, column=1)

    # These methods called whenever a slider moves
    def updateRed(self, duty):
        # change the led brightness to match the slider
        pwmRed.ChangeDutyCycle(float(duty))

    def updateGreen(self, duty):
        pwmGreen.ChangeDutyCycle(float(duty))
    
    def updateBlue(self, duty):
        pwmBlue.ChangeDutyCycle(float(duty))

# Set the GUI running, give the window a title, size and position
root = Tk()
root.wm_title('RGB LED Control')
app = App(root)
root.geometry("200x150+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()