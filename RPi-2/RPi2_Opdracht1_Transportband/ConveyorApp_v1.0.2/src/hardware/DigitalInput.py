import RPi.GPIO as GPIO


class DigitalInput:

    def __init__(self, pin, isPcf=False):
        self.pin = pin
        self.pcf = isPcf
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def getRawValue(self):
        return GPIO.input(self.pin)

    def clearEvent(self):
        GPIO.remove_event_detect(self.pin)

    def setEvent(self, edge, callback, bouncetime):
        GPIO.add_event_detect(self.pin, edge, callback=callback, bouncetime=bouncetime)
