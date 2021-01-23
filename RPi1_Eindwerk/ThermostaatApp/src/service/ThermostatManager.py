import RPi.GPIO as GPIO
import time

from business.Thermostat import Thermostat
from service.InputManager import InputManager
from service.OutputManager import OutputManager

class ThermostatManager:

    def __init__(self, thermostat, inputManager, outputManager):
        self.thermostat = thermostat
        self.inputMgr = inputManager
        self.outputMgr = outputManager

        self.init()

    def init(self):
       # local variables
        self.startTime10sLoop = 0

       # set Callbacks
        self.setCallbacks()

    def setCallbacks(self):
        self.inputMgr.setStatusCallback(self.toggleStatus)

    def toggleStatus(self, channel=0):
        self.thermostat.status = not self.thermostat.status

        if not self.thermostat.status:
            self.outputMgr.resetStrip()

    def loop(self):
        if self.thermostat.status:
           # 5 s loop
            if self.updateLoop(self.startTime10sLoop, 5):
                self.startTime10sLoop = time.time()
                self.setCurrentTemp()
                self.setOutput()
        
    def updateLoop(self, startTime, loopTime):
        currentTime = time.time()

        if currentTime >= (startTime + loopTime):
            return True

        return False

    def setCurrentTemp(self):
        self.thermostat.currentTemp = self.inputMgr.getTemp()

    def setOutput(self):
        if self.thermostat.settings.inputTemp < self.thermostat.currentTemp:
            self.outputMgr.cool()
        else:
            self.outputMgr.heat()

    
