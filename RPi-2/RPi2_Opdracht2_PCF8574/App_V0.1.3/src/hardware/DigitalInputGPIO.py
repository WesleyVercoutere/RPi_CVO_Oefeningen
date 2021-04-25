import RPi.GPIO as GPIO


class DigitalInputGPIO:

    def __init__(self, pin, pull_up_down):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=pull_up_down)

    def getRawValue(self):
        return GPIO.input(self.pin)

    def clearEvent(self):
        GPIO.remove_event_detect(self.pin)

    def setEvent(self, edge, callback, bouncetime=None):
        if bouncetime is None:
            GPIO.add_event_detect(self.pin, edge, callback=callback)
        else:
            GPIO.add_event_detect(self.pin, edge, callback=callback, bouncetime=bouncetime)
