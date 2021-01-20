import RPI.GPIO as GPIO


class DigitalInput:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def getRawValue(self):
        return GPIO.input(self.pin)

    def clearEvent(self):
        GPIO.remove_event_detect(self.pin)

    def setEvent(self, edge, callback, bouncetime):
        GPIO.add_event_detect(self.pin, edge, callback=callback, bouncetime=bouncetime)
