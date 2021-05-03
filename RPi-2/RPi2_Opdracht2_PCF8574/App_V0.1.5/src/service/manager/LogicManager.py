"""
Deze class voert de logica van de applicatie uit.
"""


class LogicManager:

    def __init__(self):
        self.leds = []
        self.initLeds()

    def initLeds(self):
        for i in range(8):
            self.leds.append(False)

    def toggleLed(self, *args, **kwargs):
        pass
