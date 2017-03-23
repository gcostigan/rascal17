import RPi.GPIO as IO
import time


class ShiftRegister:
    def __init__(self, data, clock, shift, size):
        self.data = data
        self.clock = clock
        self.shift = shift
        self.size = size
        self.bits = size*8
        for y in range(self.size):
            IO.setup(self.data, IO.OUT)  # initialize GPIO Pins as an output.
            IO.setup(self.clock, IO.OUT)
            IO.setup(self.shift, IO.OUT)

    def high(self):
        IO.output(self.data, 1)            # pull up the data pin for every bit.
        time.sleep(0.01)               # wait for 100ms
        IO.output(self.clock, 1)            # pull CLOCK pin high
        time.sleep(0.01)
        IO.output(self.clock, 0)            # pull CLOCK pin down, to send a rising edge
        IO.output(self.data, 0)            # clear the DATA pin
        IO.output(self.shift, 1)            # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.01)
        IO.output(self.shift, 0)            # pull down the SHIFT pin
        return

    def low(self):
        IO.output(self.data, 0)  # clear the DATA pin, to send 0
        time.sleep(0.1)  # wait for 100ms
        IO.output(self.clock, 1)  # pull CLOCK pin high
        time.sleep(0.1)
        IO.output(self.clock, 0)  # pull CLOCK pin down, to send a rising edge
        IO.output(self.data, 0)  # keep the DATA bit low to keep the countdown
        IO.output(self.shift, 1)  # pull the SHIFT pin high to put the 8 bit data out parallel
        time.sleep(0.1)
        IO.output(self.shift, 0)
        return

    def string_data(self, position):
        data_string = []
        y = 0
        for x in range(self.bits):
            if position[y] == x:
                data_string.append(1)
                y += 1
            else:
                data_string.append(0)
        return data_string

    def send_data(self, data):
        for y in range(self.bits):
            if data[y]:
                self.high()
            else:
                self.low()
        return


