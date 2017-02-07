import XboxController
import sys
import time

def universalMode():
    xboxCont.stop()
    xboxCont.setupControlCallback(xboxCont.XboxControls.A, canMode)
    xboxCont.setupControlCallback(xboxCont.XboxControls.B, trencherMode)
    xboxCont.start()

def canMode():
    xboxCont.stop()
    xboxCont.setupControlCallback(xboxCont.XboxControls.Y, universalMode)
    xboxCont.setupControlCallback(xboxCont.XboxControls.B, meltMode)
    xboxCont.setupControlCallback(xboxCont.XboxControls.A, positionMode)
    xboxCont.start()

def meltMode():
    xboxCont.stop()
    xboxCont.setupControlCallback(xboxCont.XboxControls.Y, universalMode)
    xboxCont.setupControlCallback(xboxCont.XboxControls.B, turnOffPump)
    xboxCont.setupControlCallback(xboxCont.XboxControls.A, turnOnPump)
    xboxCont.setupControlCallback(xboxCont.XboxControls.X, toggleHeat)
    xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, zMove)
    xboxCont.start()

def positionMode():
    xboxCont.stop()
    xboxCont.setupControlCallback(xboxCont.XboxControls.Y, canMode)
    xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, yMove)
    xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, xMove)

def trencherMode():
    xboxCont.stop()
    xboxCont.setupControlCallback(xboxCont.XboxControls.Y, universalMode)
    xboxCont.setupControlCallback(xboxCont.XboxControls.A, digMode)
    xboxCont.start()

def digMode():
    xboxCont.stop()
    xboxCont.setupControlCallback(xboxCont.XboxControls.Y, universalMode)
    xboxCont.setupControlCallback(xboxCont.XboxControls.B, stopBelt)
    xboxCont.setupControlCallback(xboxCont.XboxControls.A, runBelt)
    xboxCont.setupControlCallback(xboxCont.XboxControls.RB, rollBeltForwards)
    xboxCont.setupControlCallback(xboxCont.XboxControls.LB, rollBeltBackwards)
    xboxCont.setupControlCallback(xboxCont.XboxControls.RTHUMBY, tilt)
    xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, zMove)
    xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, xMove)
    xboxCont.start()

if __name__ == "__main__":
    xboxCont = XboxController.XboxController(
        controllerCallBack=None,
        joystickNo=0,
        deadzone=0.1,
        scale=1,
        invertYAxis=False)

    try:
        #start the controller
        xboxCont.start()
        print "xbox controller running"
        universalMode()
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

