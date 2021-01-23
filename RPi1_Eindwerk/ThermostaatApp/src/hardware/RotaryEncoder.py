import RPi.GPIO as GPIO

from hardware.DigitalInput import DigitalInput


class RotaryEncoder:

    def __init__(self, pinA, pinB):
       # Werkt niet met het gebruik van een standaard DigitalInput 
        self.rotA = DigitalInput(pinA)
        self.rotB = DigitalInput(pinB)

        self.setCallback()

    def setCallback(self):
        self.rotA.setEvent(edge=GPIO.RISING, callback=self.direction, bouncetime=10)

    def direction(self, channel):
        statusB = self.rotB.getRawValue()
        
        direction = "CW"

        if not statusB:
            direction = "CCW"

        print(direction)
        return direction
