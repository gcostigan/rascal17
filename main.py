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
