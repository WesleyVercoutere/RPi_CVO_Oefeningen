

class DigitalOutputPCF8574:

    def __init__(self, pin):
        self._pin = pin
        self._state = False
        self._pcf8574 = None
    
    def setPCF8574(self, pcf8574):
        self._pcf8574 = pcf8574

    def setstate(self, state):
        self._state = state

    def getState(self):
        return self._state

    def getPin(self):
        return self._pin

    def toggle(self):
        self._state = not self._state
        self._pcf8574.updateOutput(self)
