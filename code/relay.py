import RPi.GPIO as GPIO


class Relay:

    def __init__(self, pin):
        self.pin = pin
        self.status = False
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    def toggle(self):
        self.status = not self.status
        if self.status:
            GPIO.output(pin, 1)
        else:
            GPIO.output(pin, 0)
        return self.status
