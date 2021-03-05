from hardware.DigitalOutput import DigitalOutput


class Led(DigitalOutput):

    def __init__(self, idOfLed, pin):
        super(Led, self).__init__(pin)
        self.id = idOfLed
        self.blink = False
