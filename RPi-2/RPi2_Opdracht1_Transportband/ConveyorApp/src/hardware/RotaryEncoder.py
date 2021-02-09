import RPi.GPIO as GPIO

from hardware.DigitalInput import DigitalInput


class RotaryEncoder:

    def __init__(self, pinA, pinB):
       # Werkt niet met het gebruik van een standaard DigitalInput 
        self.rotA = DigitalInput(pinA)
        self.rotB = DigitalInput(pinB)

    def clearEvent(self):
        self.rotA.clearEvent()

    def setEvent(self, edge, callback, bouncetime=50):
        self.rotA.setEvent(edge=GPIO.RISING, callback=lambda x: self.direction(callback), bouncetime=bouncetime)

    def direction(self, callback):
        statusB = self.rotB.getRawValue()
        
        direction = "CW"

        if not statusB:
            direction = "CCW"

        callback(direction)
