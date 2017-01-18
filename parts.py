import wiringpi

class trencher:
    def tilt(self, servo, amount):
        return

    def spin(self, servo, amount):
        return

    def origin(self):
        return

    def manual(self):
        # Loop to be called when the operator needs manual overdrive
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
