import wiringpi

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
class trencher:
    def tilt(self, servo, amount):
        return

    def spin(self, servo, amount):
        return

    def origin(self):
        return

    def manual(self):
        # Loop to be called when the operator needs manual overdrive
        while(True):
            spin.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
            spin.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
            # continuously spinning forward or backward, 100 steps is just a guess for now!
            #need a break statement
        return


class ice_extracter:
    def heat(self, amount):
        return

    def move_z(self, amount):
        return

    def overheat(self,temp):
        #If temp above threshold shut it off
        return

class railing:
    def move_x(self, amount):
        return

    def move_y(self, amount):
        return
