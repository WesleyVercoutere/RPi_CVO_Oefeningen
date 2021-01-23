import RPi.GPIO as GPIO
import time

from service.InputManager import InputManager
from service.OutputManager import OutputManager

class ThermostatManager:

    def __init__(self, inputManager, outputManager):
        self.inputMgr = inputManager
        self.outputMgr = outputManager

        self.init()

    def init(self):
       # local variables
        self.startTime10sLoop = 0

       # set Callbacks
        self.setCallbacks()

    def loop(self):
       # 10 s loop
        if self.updateLoop(self.startTime10sLoop, 10):
            self.startTime10sLoop = time.time()
           # print temperature
            print(f"Temperature : {self.inputMgr.getTemp()} °C")
        
    def updateLoop(self, startTime, loopTime):
        currentTime = time.time()

        if currentTime >= (startTime + loopTime):
            return True

        return False

    def setCallbacks(self):
        self.inputMgr.setCallbacks(self.test)

    def test(self, channel):
        print(f"Button {channel} pressed")
