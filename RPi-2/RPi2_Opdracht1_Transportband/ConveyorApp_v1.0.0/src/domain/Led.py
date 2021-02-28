from hardware.DigitalOutput import DigitalOutput


class Led(DigitalOutput):

    def __init__(self, idOfLed, pin):
        super.__init__(pin)
        self.id = idOfLed
