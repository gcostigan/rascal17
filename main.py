import modes
import sys
import time
import shiftReg

DATA1, CLOCK1, SHIFT1 = 4, 5, 6
s1 = shiftReg(DATA1, CLOCK1, SHIFT1, 1)

DATA2, CLOCK2, SHIFT2 = 7, 8, 9
s2 = shiftReg(DATA2, CLOCK2, SHIFT2, 2)

# Shift Register pins
# Motor 1
ENB1 = [1,0]
DIR1 = [1,1]
PUL1 = [1,2]

# Motor 2
ENB2 = [1,3]
DIR2 = [1,4]
PUL2 = [1,5]

# Motor 3
ENB3 = [1,6]
DIR3 = [1,7]
PUL3 = [2,0]

# Motor 4
ENB4 = [1,1]
DIR4 = [1,2]
PUL4 = [2,3]

# Motor 5
ENB5 = [2,4]
DIR5 = [2,5]
PUL5 = [2,6]

# Motor 6
ENB6 = [2,7]
DIR6 = [3,0]
PUL6 = [3,1]

# Relay
HTPin = [3,2]
PumpPin = [3,3]

#
global Heat, Pump, Belt
Heat, Pump, Belt = False, False, False


def empty(value):
    return


def universalMode(value):
    if value == 1:
        print "Entering Universal Mode... "
        xboxCont.setupControlCallback(xboxCont.XboxControls.A, canMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.B, trencherMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.X, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.Y, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, empty)
        print "Ready"
    return


def canMode(value):
    if value == 1:
        print "Entering Can Mode..."
        xboxCont.setupControlCallback(xboxCont.XboxControls.Y, universalMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.B, meltMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.A, positionMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.X, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, empty)
        print "Ready"
    return


def meltMode(value):
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
        xboxCont.setupControlCallback(xboxCont.XboxControls.Y, canMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.B, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.A, togglePump)
        xboxCont.setupControlCallback(xboxCont.XboxControls.X, toggleHeat)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, zMove)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, empty)
        print "Ready"
    return


def positionMode(value):
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
        xboxCont.setupControlCallback(xboxCont.XboxControls.Y, canMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, yMove)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, xMove)
        xboxCont.setupControlCallback(xboxCont.XboxControls.X, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.A, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.B, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, empty)
        print "Ready"
    return


def trencherMode(value):
    if value == 1:
        print "Entering Trencher Mode..."
        xboxCont.setupControlCallback(xboxCont.XboxControls.Y, universalMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.A, digMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.X, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.B, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LB, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, empty)
        print "Ready"
    return


def digMode(value):
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
        xboxCont.setupControlCallback(xboxCont.XboxControls.Y, universalMode)
        xboxCont.setupControlCallback(xboxCont.XboxControls.B, empty)
        xboxCont.setupControlCallback(xboxCont.XboxControls.A, toggleBelt)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RB, rollBeltForwards)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LB, rollBeltBackwards)
        xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, tilt)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, zMove)
        xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, xMove)
        xboxCont.setupControlCallback(xboxCont.XboxControls.X, empty)
        print "Ready"
    return

if __name__ == "__main__":
    # def controlCallBack(controlId, value):
    #     print "Control id = {}, Value = {}".format(controlId, value)
    #     # return controlId, value

    xboxCont = XboxController.XboxController(
        controllerCallBack=None,
        deadzone=30,
        scale=100,
        invertYAxis=True)

    try:
        #start the controller
        xboxCont.start()
        print "Xbox controller running"
        universalMode(1)
        print "Main loop started"
        while True:
            time.sleep(1)

    #Ctrl C
    except KeyboardInterrupt:
        print "User cancelled"

    #error
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    finally:
        #stop the controller
        xboxCont.stop()

