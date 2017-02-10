from parts import *
import XboxController
# http://www.stuffaboutcode.com/2014/10/raspberry-pi-xbox-360-controller-python.html

t = trencher()
i = ice_extracter()
r = railing()
xbox = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)

def abort():
    return

def manual_control():
    goto_auto = 0
    while goto_auto == 0:
        # Do manual control until toggled out

if __name__ == "__main__":
    manual_control()

    """
    Example usage:

    import xbox
    joy = xbox.Joystick()         #Initialize joystick

    if joy.A():                   #Test state of the A button (1=pressed, 0=not pressed)
        print 'A button pressed'
    x_axis   = joy.leftX()        #X-axis of the left stick (values -1.0 to 1.0)
    (x,y)    = joy.leftStick()    #Returns tuple containing left X and Y axes (values -1.0 to 1.0)
    trigger  = joy.rightTrigger() #Right trigger position (values 0 to 1.0)

    joy.close()                   #Cleanup before exit
    """
    # Look at these:
    # https://github.com/FRC4564/Xbox
    # https://raw.githubusercontent.com/FRC4564/Xbox/master/xbox.py
    # https://raw.githubusercontent.com/FRC4564/Xbox/master/sample.py

#edit
