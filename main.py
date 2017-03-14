import XboxController
import sys
import time

global Heat, Pump, Belt
Heat, Pump, Belt = False, False, False

if __name__ == "__main__":
    # def controlCallBack(controlId, value):
    #     print "Control id = {}, Value = {}".format(controlId, value)
    #     # return controlId, value

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

