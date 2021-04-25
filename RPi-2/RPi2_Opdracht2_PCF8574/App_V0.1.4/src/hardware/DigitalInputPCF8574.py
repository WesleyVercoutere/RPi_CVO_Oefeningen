

class DigitalInputPCF8574:

    def __init__(self, pin):
        self._pin = pin
        self._callback = None

    def getPin(self):
        return self._pin

    def callEvent(self):
        if self._callback is not None:
            self._callback()

    def setEvent(self, callback):
        self._callback = callback
