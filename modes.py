import XboxController

global Heat, Pump, Belt
Heat, Pump, Belt = False, False, False

class modes:
    
    def __init__(self):
        self.controller = XboxController.XboxController(
            controllerCallBack=None,
            deadzone=30,
            scale=100,
            invertYAxis=True)

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
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.trencherMode)
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
        def yMove(value):
            if value > 1:
                print "Move Left"
            if value < 1:
                print "Move Right"
            if value == 0:
                print "Stop y movement."
            return
    
        def xMove(value):
            if value > 1:
                print "Move forwards"
            if value < 1:
                print "Move backwards"
            if value == 0:
                print "Stop x movement."
            return
    
        if value == 1:
            print "Entering Position Mode..."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.can)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, yMove)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, xMove)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.A, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return
    
    
    def trencherMode(self, value):
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
        def toggleBelt(value):
            if value == 1:
                global Belt
                Belt = not Belt
                if Belt == True:
                    print "Belt is on."
                else:
                    print "Belt is off."
            return
    
        def rollBeltForwards(value):
            if value == 1:
                print "Roll Belt Forwards"
            if value == 0:
                print "Stop Belt movement."
            return
    
        def rollBeltBackwards(value):
            if value == 1:
                print "Roll Belt Backwards"
            if value == 0:
                print "Stop Belt Movement"
            return
    
        def tilt(value):
            if value > 1:
                print "Tilt trencher forwards"
            if value < 1:
                print "Tilt trencher backwards"
            if value == 0:
                print "Stopping Trencher tilt movement"
            return
    
        def zMove(value):
            if value > 1:
                print "Move Trencher Up"
            if value < 1:
                print "Move Trencher Down"
            if value == 0:
                print "Stopping Trencher z movement"
            return
    
        def xMove(value):
            if value > 1:
                print "Move Trencher forwards"
            if value < 1:
                print "Move Trencher backwards"
            if value == 0:
                print "Stopping Trencher x movement"
            return
    
        if value == 1:
            print "Entering Dig Mode..."
            self.controller.setupControlCallback(self.controller.XboxControls.Y, self.universal)
            self.controller.setupControlCallback(self.controller.XboxControls.B, self.empty)
            self.controller.setupControlCallback(self.controller.XboxControls.A, toggleBelt)
            self.controller.setupControlCallback(self.controller.XboxControls.RB, rollBeltForwards)
            self.controller.setupControlCallback(self.controller.XboxControls.LB, rollBeltBackwards)
            self.controller.setupControlCallback(self.controller.XboxControls.RTHUMBY, tilt)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBY, zMove)
            self.controller.setupControlCallback(self.controller.XboxControls.LTHUMBX, xMove)
            self.controller.setupControlCallback(self.controller.XboxControls.X, self.empty)
            print "Ready"
        return
