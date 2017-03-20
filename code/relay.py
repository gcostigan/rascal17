import RPi.GPIO as GPIO


class Relay:

    def __init__(self, pin):
        self.pin = pin
        self.status = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    def toggle(self):
        self.status = not self.status
        if self.status:
            GPIO.output(self.pin, 1)
        else:
            GPIO.output(self.pin, 0)
        return self.status
