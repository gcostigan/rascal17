import wiringpi
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17, 22, 23, 24] #CHANGE NUMBERS WHEN WE KNOW WHAT PINS TO USE!

class trencher:
    def tilt(self, amount):
        if (amount > 0):
            #dir foward
        else:
            #dir backward

    def spin(self, amount):
        if (amount > 0):
            #dir foward
        else:
            #dir backward

    def origin(self):
        return

    def manual(self):
        # Loop to be called when the operator needs manual overdrive
        while(True):
            #continuously spinning forward or backward
            #need a break statement
        return


class ice_extracter:
    def heat(self, on_off): #assuming heating is an on/off operation was can use true/false. If value we can change to amount
        while(True):
            #send current to can to heat up
        return

    def move_z(self, amount):
        canStepper.step(amount, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
        return

    def overheat(self,temp):
        if temp>200 #change this to whatever temp we need
            #turn off current to can
        return

class railing:
    def move_x(self, amount):
        railStepperx.step(amount, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
        return

    def move_y(self, amount):
        railSteppery.step(amount, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
        return
