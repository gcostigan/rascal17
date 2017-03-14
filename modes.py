import XboxController
import motor
import relay

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

# Motor 5
ENB5 = [1, 4]
DIR5 = [1, 5]
PUL5 = [1, 6]
motor5 = motor.Motor(ENB5, DIR5, PUL5)

# Motor 6
ENB6 = [1, 7]
DIR6 = [2, 0]
PUL6 = [2, 1]
motor6 = motor.Motor(ENB6, DIR6, PUL6)

# Heat Tape
HTPin = [3, 2]
heat_tape_relay = relay.Relay(HTPin)

# Pump
PumpPin = [3, 3]
pump_relay = relay.Relay(PumpPin)


class Modes:

    def __init__(self):
        self.controller = XboxController.XboxController(
            controllerCallBack=None,
            deadzone=30,
            scale=100,
            invertYAxis=True)
        global Heat, Pump, Belt
        Heat, Pump, Belt = False, False, False

    @staticmethod
    def empty(value):
        return

    def start(self):
        self.controller.start()
        return

    def stop(self):
        self.controller.stop()
        return

    def universal(self, value):
        if value == 1:
            print "Entering Universal Mode... "
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.can)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.trencher_mode)
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
                global Pump
                Pump = not Pump
                if Pump:
                    print "Pump is on."
                else:
                    print "Pump is off."
            return
    
        def toggle_heat(val):
            if val == 1:
                global Heat
                Heat = not Heat
                if Heat:
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
                print "Move Left"
            if val < 1:
                print "Move Right"
            if val == 0:
                print "Stop y movement."
            return
    
        def x_move(val):
            if val > 1:
                print "Move forwards"
            if val < 1:
                print "Move backwards"
            if val == 0:
                print "Stop x movement."
            return
    
        if value == 1:
            print "Entering Position Mode..."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.can)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, y_move)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, x_move)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return

    def trencher_mode(self, value):
        if value == 1:
            print "Entering Trencher Mode..."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.universal)
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.dig)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return

    def dig(self, value):
        def toggle_belt(val):
            if val == 1:
                global Belt
                Belt = not Belt
                if Belt:
                    print "Belt is on."
                    motor6.enable()
                else:
                    print "Belt is off."
            return
    
        def roll_belt_forwards(val):
            if val == 1:
                print "Roll Belt Forwards"
            if val == 0:
                print "Stop Belt movement."
            return
    
        def roll_belt_backwards(val):
            if val == 1:
                print "Roll Belt Backwards"
            if val == 0:
                print "Stop Belt Movement"
            return
    
        def tilt(val):
            if val > 1:
                print "Tilt trencher forwards"
            if val < 1:
                print "Tilt trencher backwards"
            if val == 0:
                print "Stopping Trencher tilt movement"
            return
    
        def z_move(val):
            if val > 1:
                print "Move Trencher Up"
            if val < 1:
                print "Move Trencher Down"
            if val == 0:
                print "Stopping Trencher z movement"
            return
    
        def x_move(val):
            if val > 1:
                print "Move Trencher forwards"
            if val < 1:
                print "Move Trencher backwards"
            if val == 0:
                print "Stopping Trencher x movement"
            return
    
        if value == 1:
            print "Entering Dig Mode..."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.universal)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.A, toggle_belt)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, roll_belt_forwards)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, roll_belt_backwards)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, tilt)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, z_move)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, x_move)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            print "Ready"
        return
