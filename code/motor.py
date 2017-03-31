'''
import shift

DATA1, CLOCK1, SHIFT1 = 4, 5, 6
number_of_shift = 3
s = shift.ShiftRegister(DATA1, CLOCK1, SHIFT1, number_of_shift)
'''


import RPi.GPIO as GPIO
import time


class Motor:
    def __init__(self, dire, pul):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.dir = dire
        self.pul = pul
        self.speed = 3  # rev/s
        self.freq = 100 # Hz

        GPIO.setup(pul, GPIO.OUT)
        GPIO.setup(dire, GPIO.OUT)

        GPIO.output(dire, 0)
        GPIO.output(pul, 0)
        GPIO.output(self.pul, 0)
        '''
        self.enb = enb[0]*8 + enb[1]
        self.dir = dir[0]*8 + dire[1]
        self.pul = pul[0]*8 + pul[1]
        '''
        return

    def on(self, direction, t):
        if direction:
            GPIO.output(self.dir, 1)
        else:
            GPIO.output(self.dir, 0)
        GPIO.output(self.pul, 1)
        time.sleep(t)
        GPIO.output(self.pul, 0)
        return

    def off(self):
        GPIO.output(self.enb, 0)
        return

    def move(self, rev, direction):
        if direction:
            GPIO.output(self.dir, 1)
        else:
            GPIO.output(self.dir, 0)
        # t_stop = rev/self.speed
        # t = 0
        # while t < t_stop:
        for i in range(5):
            GPIO.output(self.pul, 1)
            time.sleep(1.0/self.freq)
            GPIO.output(self.pul, 0)
            time.sleep(1.0/self.freq)
        return

    def pulse_on(self, direction):
        if direction:
            GPIO.output(self.dir, 1)
        else:
            GPIO.output(self.dir, 0)
        GPIO.output(self.pul, 1)
        return

'''
    def enable(self):
        data = s.string_data(self.enb)
        s.send_data(data)
        return

    def direction(self):
        data = s.string_data(self.dir)
        s.send_data(data)
        return

    def pulse(self):
        data = s.string_data(self.pul)
        s.send_data(data)
        return
'''
