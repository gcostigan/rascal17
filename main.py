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

if __name__ == "__main__":
    # def controlCallBack(controlId, value):
    #     print "Control id = {}, Value = {}".format(controlId, value)
    #     # return controlId, value

    xbox = modes()

    try:
        #start the controller
        modes.start()
        print "Xbox controller running"
        modes.universalMode(1)
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
        modes.stop()

