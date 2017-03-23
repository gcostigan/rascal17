import time


class Actuator:
    def __init__(self, dir1, dir2):
        self.dir1 = dir1
        self.dir2 = dir2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dir1, GPIO.OUT)
        GPIO.setup(dir2, GPIO.OUT)
        GPIO.output(dir1, 1)
        GPIO.output(dir2, 1)
        return

    def move(self, dir):
        if dir:
            GPIO.output(self.dir1, 1)
            time.sleep(0.05)
            GPIO.output(self.dir1, 0)
        else:
            GPIO.output(self.dir2, 1)
            time.sleep(0.05)
            GPIO.output(self.dir2, 0)
        return
