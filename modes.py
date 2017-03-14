import XboxController

class modes:
    
    def __init__(self):
        self.xboxCont = XboxController.XboxController(
            controllerCallBack=None,
            deadzone=30,
            scale=100,
            invertYAxis=True)
        
    def empty(self, value):
        return
    
    
    def universalMode(self, value):
        if value == 1:
            print "Entering Universal Mode... "
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.A, self.canMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.B, self.trencherMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.X, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.Y, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBY, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBX, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return
    
    
    def canMode(self, value):
        if value == 1:
            print "Entering Can Mode..."
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.Y, self.universalMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.B, self.meltMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.A, self.positionMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.X, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBY, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBX, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return
    
    
    def meltMode(self, value):
        def togglePump(value):
            if value == 1:
                global Pump
                Pump = not Pump
                if Pump == True:
                    print "Pump is on."
                else:
                    print "Pump is off."
            return
    
        def toggleHeat(value):
            if value == 1:
                global Heat
                Heat = not Heat
                if Heat == True:
                    print "Heat Tape is on."
                else:
                    print "Heat Tape is off."
            return
    
        def zMove(value):
            if value > 1:
                print "Move Can Up"
            if value < 1:
                print "Move Can Down"
            if value == 0:
                print "Stop z movement."
            return
    
        if value == 1:
            print "Entering Melt Mode..."
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.Y, self.canMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.B, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.A, togglePump)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.X, toggleHeat)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBY, zMove)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBX, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return
    
    
    def positionMode(self, value):
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
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.Y, self.canMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBY, yMove)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBX, xMove)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.X, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.A, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.B, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return
    
    
    def trencherMode(self, value):
        if value == 1:
            print "Entering Trencher Mode..."
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.Y, self.universalMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.A, self.digMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.X, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.B, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBY, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBX, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LB, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RTHUMBY, self.empty)
            print "Ready"
        return
    
    
    def digMode(self, value):
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
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.Y, self.universalMode)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.B, self.empty)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.A, toggleBelt)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RB, rollBeltForwards)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LB, rollBeltBackwards)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.RTHUMBY, tilt)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBY, zMove)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTHUMBX, xMove)
            self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.X, self.empty)
            print "Ready"
        return
