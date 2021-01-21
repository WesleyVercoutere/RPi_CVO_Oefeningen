from InputManager import InputManager
from OutputManager import OutputManager

class ThermostatManager:

    def __init__(self, inputManager, outputManager):
        self.inputMgr = inputManager
        self.outputMgr = outputManager

        self.init()

    def init(self):
        self.ledStatus = False
        self.inputMgr.btn1.setEvent(edge=GPIO.RISING, callback=self.toggleLed, bouncetime=200)

    def toggleLed(self, channel):
        self.ledStatus = not self.ledStatus
        self.outputMgr.toggleLed(self.ledStatus)



