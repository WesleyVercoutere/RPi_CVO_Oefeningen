import RPi.GPIO as GPIO

import hardware.Rotation as Rotation
from hardware.DigitalInput import DigitalInput


class RotaryEncoder:

    def __init__(self, pinA, pinB):
        self.rotA = DigitalInput(pinA)
        self.rotB = DigitalInput(pinB)

    def clearEvent(self):
        self.rotA.clearEvent()

    def setEvent(self, callback, bouncetime=10):
        self.rotA.setEvent(edge=GPIO.RISING, callback=lambda x: self.direction(self.rotB.getRawValue(), callback), bouncetime=bouncetime)

    def getSignalA(self):
        return self.rotA.getRawValue()

    def getSignalB(self):
        return self.rotB.getRawValue()

    def direction(self, statusB, callback):
        direction = Rotation.CLOCKWISE

        if not statusB:
            direction = Rotation.COUNTERCLOCKWISE

        callback(direction)
