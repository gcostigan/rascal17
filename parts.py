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


class Motor(object):
    #intialize motors
    def _init_(self,pins):
        self.P1 = pins[0]
        self.P2 = pins[1]
        self.P3 = pins[2]
        self.p4 = pins[3]
        self.P5 = pins[4]
        self.P6 = pins[5]
        self.deg_per_step = 5.625 / 64
        self.steps_per_rev = int(360 / self.deg_per_step)
        self.step_angle = 0 #assume the way its pointing is zero
        for p in pins:
            GPIO.setup(p,GPIO.out)
            GPIO.output(p,0)

    def _set_rpm(self, rpm):
        '''Set the turn speed in RPM'''
        self._rpm = rpm
        self._T = (60.0 / rpm) / self.steps_per_rev
        ## T is the amount of time to stop between signals

    # This means you can set "rpm" as if it is an attribute and behind the scenes
    # its sets _T sttribute
    rpm = property(lambda self: self._rpm, _set_rpm

    def move_to(self, angle):
        '''Take the shortest route to a particular angle (degrees).'''
        #Make sure there is a 1:1 mapping between angle and stepper angle

        target_set_angle = 8 * (int(angle / self.deg_per_step) / 8)
        steps = target_set_angle - self.step_angle
        steps = (steps % self.steps_per_rev)
        if steps > self.steps_per_rev / 2:
            steps -= self.steps_per_rev
            print "moving" + `steps` + "steps"
            self._move_acw(-steps / 8)
        else:
            print "moving" + `steps` + "steps"
            self._move_cw(steps / 8)
        self.step_angle = target_step_angle

    def _move_acw(selfself, big_steps):
        GPIO.output(self.P1, 0)
        GPIO.output(self.P2, 0)
        GPIO.output(self.P3, 0)
        GPIO.output(self.P4, 0)
        GPIO.output(self.P5, 0)
        GPIO.output(self.P6, 0)
        for i range(big_steps):
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P5, 0)
            sleep(self._T)
            GPIO.output(self.P6, 0)
            sleep(self._T)

    def _move_cw(selfself, big_steps):
        GPIO.output(self.P1, 0)
        GPIO.output(self.P2, 0)
        GPIO.output(self.P3, 0)
        GPIO.output(self.P4, 0)
        GPIO.output(self.P5, 0)
        GPIO.output(self.P6, 0)
        for i range(big_steps):
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P5, 0)
            sleep(self._T)
            GPIO.output(self.P6, 0)
            sleep(self._T)
'''
if _name_ == "_main_":
    GPIO.setmode(GPIO.BOARD)
    m = Motor([]) ## NEED to input location of motors
    m.rpm = 5
    print "Pause in seconds: " + `m._T`
    m.move_to(90)
    sleep(1)
    m.move_to(0)
    sleep(1)
    m.move_to(-90)
    sleep(1)
    m.move_to(-180)
    sleep(1)
    m.move_to(0)
    GPIO.cleanup()

    .END

    ##This section confuses me -.-
    '''

'''
 def tilt(self, amount):
        if (amount > 0):
            #dir foward
        else:
            #dir backward
        return

    def spin(self, amount):
        if (amount > 0):
            #dir foward
        else:
            #dir backward
        return

    def move_x (self, amount):
        return

    def move_y (self, amount):
        return

    def origin(self):
        return

    def manual(self):
        # Loop to be called when the operator needs manual overdrive
        while(True):
            #continuously spinning forward or backward
            #need a break statement
        return


class ice_extracter:
    def heat(self, heat_on_off): #assuming heating is an on/off operation was can use true/false. If value we can change to amount
        while(True):
            #send current to can to heat up
        return

    def move_x(self, amount):
        return

    def move_y(self, amount):
        return

    def move_z(self, amount):
        return

    def overheat(self,temp):
        if temp > 200 #change this to whatever temp we need
            #turn off current to can
        return

    def pump(self,pump_on_off):
        return
'''
