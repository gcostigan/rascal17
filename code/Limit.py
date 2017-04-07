import RPi.GPIO as GPIO
import time

 '''two switches in x-dir and two in y-dir, maybe two for the trencher?'''
 '''do we want limit switches to stop motors or return them to reset position?'''

class limit:
    def _int_(self, limitswitch1,limitswitch2,limitswitch3,limitswitch4):
        while True:
            if limitswitch1 == 0:
                '''stop motor 1'''
                return
            if limitswitch2 == 0:
                return
            if limitswitch3 == 0:
                return
            if limitswitch4 == 0:
                return
        return