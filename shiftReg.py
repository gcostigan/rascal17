import RPi.GPIO as IO         # calling for header file which helps us use GPIO’s of PI
import time

class shiftReg:
    def __init__(self, DATA, CLOCK, SHIFT, NUM):
        self.d.append(DATA)
        self.c.append(CLOCK)
        self.s.append(SHIFT)
        self.n.append(NUM)
        IO.setup(self.d[NUM-1], IO.OUT)  # initialize GPIO Pins as an output.
        IO.setup(self.c[NUM-1], IO.OUT)
        IO.setup(self.s[NUM-1], IO.OUT)

    def high(self):
        IO.output(self.d, 1)            # pull up the data pin for every bit.
        time.sleep(0.01)               # wait for 100ms
        IO.output(self.c, 1)            # pull CLOCK pin high
        time.sleep(0.01)
        IO.output(self.c, 0)            # pull CLOCK pin down, to send a rising edge
        IO.output(self.d, 0)            # clear the DATA pin
        IO.output(self.s, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.01)
        IO.output(self.s, 0)            # pull down the SHIFT pin

    def low(self):
        IO.output(self.d, 0)  # clear the DATA pin, to send 0
        time.sleep(0.1)  # wait for 100ms
        IO.output(self.c, 1)  # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(self.c, 0)  # pull CLOCK pin down, to send a rising edge
        IO.output(self.d, 0)  # keep the DATA bit low to keep the countdown
        IO.output(self.s, 1)  # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(self.s, 0)

    def data(self, NUM, shiftPins):
        for y in range(8):
            if shiftPins[y] == 1:
                self.high()
            else:
                self.low()


