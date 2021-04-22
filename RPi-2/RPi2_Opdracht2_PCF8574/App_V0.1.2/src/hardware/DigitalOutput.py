import RPi.GPIO as GPIO


class DigitalOutput:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def getValue(self):
        return GPIO.input(self.pin)

    def setOutput(self, state):
        GPIO.output(self.pin, state)

    def toggle(self):
        print("toggle ", self.pin)
        GPIO.output(self.pin, not GPIO.input(self.pin))
