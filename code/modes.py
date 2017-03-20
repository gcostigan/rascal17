import XboxController
import os
import sys
import relay

'''
import motor
import relay
import actuator

# Shift Register pins
# Motor 1
ENB1 = [0, 0]
DIR1 = [0, 1]
PUL1 = [0, 2]
motor1 = motor.Motor(ENB1, DIR1, PUL1)

# Motor 2
ENB2 = [0, 3]
DIR2 = [0, 4]
PUL2 = [0, 5]
motor2 = motor.Motor(ENB2, DIR2, PUL2)

# Motor 3
ENB3 = [0, 6]
DIR3 = [0, 7]
PUL3 = [1, 0]
motor3 = motor.Motor(ENB3, DIR3, PUL3)

# Motor 4
ENB4 = [1, 1]
DIR4 = [1, 2]
PUL4 = [1, 3]
motor4 = motor.Motor(ENB4, DIR4, PUL4)
'''

# Heat Tape
HTPin = 6
heat_tape_relay = relay.Relay(HTPin)

# Pump
PumpPin = 4
pump_relay = relay.Relay(PumpPin)

'''
LA1_dir1 = [1, 6]
LA1_dir2 = [1, 7]
LA1 = actuator.Actuator(LA1_dir1, LA1_dir2)

LA2_dir1 = [2, 0]
LA2_dir2 = [2, 1]
LA2 = actuator.Actuator(LA2_dir1, LA2_dir2)
'''


class Modes:

    def __init__(self):
        self.controller = XboxController.XboxController(
            controllerCallBack=None,
            deadzone=30,
            scale=100,
            invertYAxis=True)
        self.controller.setupControlCallback(self.controller.XboxControls.XBOX, self.stop)
        self.exc_info = []
        global Belt
        Belt = False

    @staticmethod
    def empty(value):
        return

    def start(self):
        self.controller.start()
        return

    def stop(self, value):
        if value:
            print "Stopping controller"
            self.controller.stop()
            self.exc_info = KeyboardInterrupt
            raise self.controller

    def universal(self, value):
        if value == 1:
            print "Entering Universal Mode... "
            os.system('clear')
            print "----------Universal Mode----------"
            print "A = Can Mode."
            print "B = Trencher Mode."
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.can)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.trencher)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return

    def can(self, value):
        if value == 1:
            print "Entering Can Mode..."
            os.system('clear')
            print "-------------Can Mode-------------"
            print "A = Position Mode."
            print "B = Melt Mode."
            print "Y = Universal Mode."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.universal)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.melt)
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.position)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return

    def melt(self, value):
        def toggle_pump(val):
            if val == 1:
                status = pump_relay.toggle()
                if status:
                    print "Pump is on."
                else:
                    print "Pump is off."
            return
    
        def toggle_heat(val):
            if val == 1:
                status = heat_tape_relay.toggle()
                if status:
                    print "Heat Tape is on."
                else:
                    print "Heat Tape is off."
            return
    
        def z_move(val):
            if val > 1:
                print "Move Can Up"
            if val < 1:
                print "Move Can Down"
            if val == 0:
                print "Stop z movement."
            return
    
        if value == 1:
            print "Entering Melt Mode..."
            os.system('clear')
            print "------------Melt Mode-------------"
            print "A = Toggle pump power."
            print "X = Toggle heat power."
            print "Y = Can Mode."
            print "LTHUMBY = Move can up/down."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.can)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.A, toggle_pump)
            self.controller.setupControlCallback(self.controller.XboxControls.X, toggle_heat)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, z_move)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return

    def position(self, value):
        def y_move(val):
            if val > 1:
                print "Moving can left"
            if val < 1:
                print "Moving can right."
            if val == 0:
                print "Stopping can y-movement."
            return
    
        def x_move(val):
            if val > 1:
                print "Moving can forwards."
            if val < 1:
                print "Moving can backwards."
            if val == 0:
                print "Stopping can x-movement."
            return
    
        if value == 1:
            print "Entering Position Mode..."
            os.system('clear')
            print "----------Position Mode-----------"
            print "Y = Can Mode."
            print "LTHUMBX = Move forwards/backwards."
            print "LTHUMBY = Move left/right."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.can)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, y_move)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, x_move)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready."
        return

    def trencher(self, value):
        def y_move(val):
            if val > 1:
                print "Moving trencher left."
            if val < 1:
                print "Moving trencher right"
            if val == 0:
                print "Stopping trencher y-movement."
            return
        
        if value == 1:
            print "Entering Trencher Mode..."
            os.system('clear')
            print "----------Trencher Mode-----------"
            print "A = Dig Mode."
            print "Y = Universal Mode."
            print "LTHUMBY = Move left/right."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.universal)
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.dig)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, y_move)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready."
        return

    def dig(self, value):
        def toggle_belt(val):
            if val == 1:
                global Belt
                Belt = not Belt
                if Belt:
                    print "Belt is now on."
                    # motor6.enable()
                else:
                    print "Belt is now off."
            return
    
        def roll_belt_forwards(val):
            if val == 1:
                print "Rolling belt forwards."
            if val == 0:
                print "Stopping belt movement."
            return
    
        def roll_belt_backwards(val):
            if val == 1:
                print "Rolling belt backwards."
            if val == 0:
                print "Stopping belt movement."
            return
    
        def tilt(val):
            if val > 1:
                print "Tilting trencher forwards."
            if val < 1:
                print "Tilting trencher backwards."
            if val == 0:
                print "Stopping Trencher tilt movement."
            return
    
        def z_move(val):
            if val > 1:
                print "Moving trencher up."
            if val < 1:
                print "Moving trencher down."
            if val == 0:
                print "Stopping trencher z-movement."
            return
    
        def x_move(val):
            if val > 1:
                print "Moving trencher forwards."
            if val < 1:
                print "Moving trencher backwards."
            if val == 0:
                print "Stopping trencher x-movement."
            return
    
        if value == 1:
            print "Entering Dig Mode..."
            os.system('clear')
            print "-------------Dig Mode-------------"
            print "A = Toggle belt power."
            print "Y = Trencher Mode."
            print "RB = Roll belt forwards."
            print "LB = Roll belt backwards."
            print "LTHUMBX = Move trencher forwards/backwards."
            print "LTHUMBY = Move trencher up/down."
            print "LTHUMBY = Tilt trencher up/down."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.trencher)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.A, toggle_belt)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, roll_belt_forwards)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, roll_belt_backwards)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, tilt)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, z_move)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, x_move)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            print "Ready."
        return
