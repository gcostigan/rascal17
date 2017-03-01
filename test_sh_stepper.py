# Stepper Driver Module
# Copyright (c) 2012 Kevin Cazabon
# kevin@cazabon.com

import time
import math
import wiringpi

# if using RPi.GPIO instead of wiringpi, modify the imports and GPIO_OUT and GPIO_IN classes accordingly - the rest should be fine as-is.
wiringpi.wiringPiSetup()

FORWARD = 1
REVERSE = -1


class GPIO_OUT:
    def __init__(self, channel, postSleep=None):
        # postSleep can be used if the OS is writing faster than your driver board can take data... probably not needed though.
        self.channel = channel
        self.postSleep = postSleep

        wiringpi.pinMode(self.channel, 1)

    def output(self, value):
        wiringpi.digitalWrite(self.channel, 1 if value else 0)
        if self.postSleep:
            time.sleep(self.postSleep)


class GPIO_IN:
    def __init__(self, channel):
        self.channel = channel

        wiringpi.pinMode(self.channel, 2)

    def input(self):
        if wiringpi.digitalRead(self.channel) == 1:
            return False
        else:
            return True


class stepper:
    def __init__(self, dataPin, clockPin, latchPin, limitPin, startLocked=False, callback=None, callbackArg=None,
                 callbackFreqSteps=20):
        # callback(callbackArg) is called every callbackFreqSteps number of steps - allowing you to time other processes if needed.
        #   however, be careful on how long that function takes to return - it can cause hiccups in your stepping.

        self.d = GPIO_OUT(dataPin)
        self.c = GPIO_OUT(clockPin)
        self.l = GPIO_OUT(latchPin)
        self.limit = GPIO_IN(limitPin)
        self.callback = callback
        self.callbackArg = callbackArg
        self.callbackFreqSteps = callbackFreqSteps

        self.stepPattern = [True, True, False, False]
        self.halfStepPattern = [[True, False, False, False], [True, False, False, True], [False, False, False, True],
                                [False, False, True, True], [False, False, True, False], [False, True, True, False],
                                [False, True, False, False], [True, True, False, False]]

        self.stepCount = 0
        self.lastStepTime = time.time()

        # to get accurate step speeds, the timing circuit needs a fudge-factor to account for overhead in the sleep call itself as well as the GPIO latch call
        # 0.00018 seconds is good as a starting point, tested with a stock Raspberry pi, Debian Wheezy - confirmed on Raspbian too
        # test it with the .calibrate() method to ensure it's accurate on your system
        self.stepCalibration = 0.00018

        if startLocked:
            self.lock()

    def lock(self):
        self.step(FORWARD, 1)

    def deEnergize(self, motor1=True, motor2=True):
        self.d.output(False)
        self.c.output(False)
        self.l.output(False)

        # shift 8 blank bits onto the shift register, then latch it. wiringpi.shiftOut() would be better
        for i in range(8):
            self.c.output(True)
            self.c.output(False)

        self.l.output(True)
        self.l.output(False)

    def step(self, steps=1, stepsPerSecond=None, direction=FORWARD, overrideLimit=False):
        # forward can be done by simply shifting one bit at a time through the register - much faster!

        if (direction != FORWARD and steps > 0) or (direction == FORWARD and steps < 0):
            return self.stepReverse(steps, stepsPerSecond, overrideLimit)

        self.c.output(False)
        self.l.output(False)

        if stepsPerSecond:
            stepTime = 1.0 / float(stepsPerSecond)
        else:
            stepTime = 0.0

        for i in range(int(self.stepCount + 1), int(self.stepCount + 1) + steps, 1):
            if overrideLimit:
                print "*** Limit Switch Over-Ridden! Careful! ***"
            else:
                if self.limit.input():
                    print "*** Limit Sensed - cannot move further ***"
                    self.stepCount = i
                    return -1

            self.c.output(False)
            self.d.output(self.stepPattern[i % len(self.stepPattern)])
            self.c.output(True)

            # ensure we're going the right-ish speed
            if stepTime:
                time.sleep(max(0.0, self.lastStepTime + stepTime - self.stepCalibration - time.time()))

            # data should be loaded... latch it to the output!
            self.l.output(True)
            self.lastStepTime = time.time()
            self.l.output(False)

            if self.callback != None and i % self.callbackFreqSteps == 0:
                self.callback(self.callbackArg)

        # we must have completed all steps without hitting the limit switch
        self.stepCount = i
        return 0

    def complexStep(self, pattern, stepCounter, stepsPerSecond, overrideLimit):
        # load all pattern bits into the shift register before latching
        # this only does one step - you'll have to call it multiple times
        if overrideLimit:
            print "*** Limit Switch Over-Ridden! Careful! ***"
        else:
            if self.limit.input():
                print "*** Limit Sensed - cannot move further ***"
                return -1

        self.c.output(False)
        self.l.output(False)

        if stepsPerSecond:
            stepTime = 1.0 / float(stepsPerSecond)
        else:
            stepTime = 0.0

        for i in range(len(pattern)):
            # this should probably be converted to wiringpi.shiftOut()
            self.d.output(pattern[i])
            self.c.output(True)
            self.c.output(False)

        # ensure we're going the right-ish speed
        if stepTime:
            time.sleep(max(0.0, self.lastStepTime + stepTime - self.stepCalibration - time.time()))

        self.l.output(True)
        self.lastStepTime = time.time()
        self.l.output(False)

        if self.callback != None and self.stepCount % self.callbackFreqSteps == 0:
            self.callback(self.callbackArg)

        self.stepCount = self.stepCount + stepCounter

        return 0

    def stepReverse(self, steps=1, stepsPerSecond=None, overrideLimit=False):
        for i in range(steps):
            # load the four data points into motor1
            stepNumber = int(self.stepCount - 1) % len(self.stepPattern)

            # stepNumber will be counting down.  Shift the step pattern left accordingly
            pattern = self.stepPattern[stepNumber:] + self.stepPattern[:stepNumber]

            if self.complexStep(pattern, -1, stepsPerSecond, overrideLimit) != 0:
                # Limit sensed during movement, bail.
                return -1
        return 0

    def halfStep(self, steps=1, stepsPerSecond=None, direction=FORWARD, overrideLimit=False):
        if (direction != FORWARD and steps > 0) or (direction == FORWARD and steps < 0):
            return self.halfStepReverse(steps)

        for i in range(steps):
            stepNumber = int(((float(self.stepCount) + 0.5) * 2.0) % len(self.halfStepPattern))
            pattern = self.halfStepPattern[stepNumber]
            if self.complexStep(pattern, 0.5, stepsPerSecond, overrideLimit) != 0:
                # Limit sensed during movement, bail.
                return -1
        return 0

    def halfStepReverse(self, steps=1, stepsPerSecond=None, overrideLimit=False):
        for i in range(steps):
            stepNumber = int(((float(self.stepCount) - 0.5) * 2.0) % len(self.halfStepPattern))
            pattern = self.halfStepPattern[stepNumber]
            if self.complexStep(pattern, -0.5, stepsPerSecond, overrideLimit) != 0:
                # Limit sensed during movement, bail.
                return -1
        return 0

    def stepTime(self, startTime, normalTime, rampSteps, thisStepNumber):
        # this needs some work for constant acceleration - but it's a start.
        x = float(thisStepNumber) / float(rampSteps)
        x2 = 1 - math.sin(x * math.pi / 2.0)

        timeThisStep = normalTime + (x2 * (startTime - normalTime))

        return timeThisStep

    def ramp(self, function, startSpeed, finalSpeed, rampSteps, callbackDuringRamp=True, overrideLimit=False):
        # DEPRECIATED - timeRamp is better, unless you need to take a specific number of steps during the ramp phase
        # ramps from startSpeed to finalSpeed in rampStep number of steps, following a Sine curve for timing
        if startSpeed == 0:
            startSpeed = min(50, finalSpeed)
        if finalSpeed == 0:
            finalSpeed = min(50, startSpeed)

        for i in range(rampSteps):
            if startSpeed > finalSpeed:
                stepTime = self.stepTime(1.0 / float(startSpeed), 1.0 / float(finalSpeed), rampSteps, i)
            else:
                stepTime = self.stepTime(1.0 / float(finalSpeed), 1.0 / float(startSpeed), rampSteps, rampSteps - i)

            if function(1, 1.0 / stepTime, overrideLimit=overrideLimit) != 0:
                # Limit sensed during movement, bail.
                return -1

            if self.callback != None and callbackDuringRamp and self.stepCount % self.callbackFreqSteps == 0:
                self.callback(self.callbackArg)

    def timeRamp(self, function, startSpeed, finalSpeed, rampTime, callbackDuringRamp=True, overrideLimit=False):
        # this is a true linear ramp, but you have to specify the TIME over which you want to ramp, not the number of steps
        if startSpeed == 0:
            startSpeed = min(50, finalSpeed)
        if finalSpeed == 0:
            finalSpeed = min(50, startSpeed)

        rampTime = float(rampTime)
        startTime = time.time()

        # take the first step
        function(1, startSpeed, overrideLimit=overrideLimit)

        while 1:
            nowSpeed = startSpeed + (((time.time() - startTime) / rampTime) * (finalSpeed - startSpeed))

            if startSpeed <= finalSpeed and nowSpeed >= finalSpeed:
                return 0
            elif startSpeed >= finalSpeed and nowSpeed <= finalSpeed:
                return 0

            if function(1, nowSpeed, overrideLimit=overrideLimit) != 0:
                # Limit sensed during movement, bail.
                return -1

            if self.callback != None and callbackDuringRamp and self.stepCount % self.callbackFreqSteps == 0:
                self.callback(self.callbackArg)

    def calibrate(self):
        # CAREFUL - we're going to dis-engage the motor to do this... don't let anything crash by de-energizing your motor!
        # we probably could shorten the calibration quite a bit and get the same result...

        stepPattern = self.stepPattern
        halfStepPattern = self.halfStepPattern

        self.stepPattern = [False, False, False, False]
        self.halfStepPattern = [[False, False, False, False], [False, False, False, False],
                                [False, False, False, False], [False, False, False, False],
                                [False, False, False, False], [False, False, False, False],
                                [False, False, False, False], [False, False, False, False]]

        errors = []

        # run through a series of speeds and calculate the error
        for i in range(50, 750, 50):
            start = time.time()
            s.step(i * 10, i)
            duration = time.time() - start
            actual = float(i * 10) / duration
            errorPerStep = (duration - 10.0) / float(i * 10)
            errorPct = errorPerStep / actual
            print "%s steps/sec requested = \t%s steps/sec real = error of \t%s sec per step or \t%s %%" % (
            i, actual, errorPerStep, errorPct)
            errors.append(errorPerStep)
        print

        for i in range(50, 750, 50):
            start = time.time()
            s.stepReverse(i * 10, i)
            duration = time.time() - start
            actual = float(i * 10) / duration
            errorPerStep = (duration - 10.0) / float(i * 10)
            errorPct = errorPerStep / actual
            print "%s steps/sec requested = \t%s steps/sec real = error of \t%s sec per step or \t%s %%" % (
            i, actual, errorPerStep, errorPct)
            errors.append(errorPerStep)
        print

        for i in range(50, 750, 50):
            start = time.time()
            s.halfStep(i * 10, i)
            duration = time.time() - start
            actual = float(i * 10) / duration
            errorPerStep = (duration - 10.0) / float(i * 10)
            errorPct = errorPerStep / actual
            print "%s steps/sec requested = \t%s steps/sec real = error of \t%s sec per step or \t%s %%" % (
            i, actual, errorPerStep, errorPct)
            errors.append(errorPerStep)

        s.deEnergize()

        # Average the errors and apply the correction
        total = 0.0
        for e in errors:
            total = total + e
        errorValue = total / flloat(len(e))

        self.stepCalibration = self.stepCalibration - errorValue

        print "Error corrected by: %s (self.stepCalibration = %s)" % (errorValue, self.stepCalibration)

        self.stepPattern = stepPattern
        self.halfStepPattern = halfStepPattern


if __name__ == "__main__":
    # make a stepper class
    s = stepper(1, 7, 0, 3)

    # test calibration - so that the stepping rate is accurate, despite system overhead (likely dependent on OS, SD card speed, etc.)
    s.calibrate()

    # testing
    s.timeRamp(s.step, 0, 400, 2.0)
    s.step(1200, 400)
    s.timeRamp(s.step, 400, 800, 2.0)
    s.step(2400, 800)
    s.timeRamp(s.step, 800, 1200, 2.0)
    s.step(2400, 1200)
    s.timeRamp(s.step, 1200, 600, 2.0)

    # switch to halfsteps
    s.halfStep(2400, 1200)
    s.timeRamp(s.halfStep, 1200, 200, 4.0)
    s.halfStep(200, 200)
    s.timeRamp(s.halfStep, 200, -200, 2.0)
    s.halfStepReverse(200, 200)
    s.timeRamp(s.halfStepReverse, 200, 600, 3.0)
    s.halfStepReverse(600, 600)
    s.timeRamp(s.halfStepReverse, 600, 0, 2.0)

    print "Finished!"
