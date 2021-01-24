import RPi.GPIO as GPIO
import time

from business.Thermostat import Thermostat
from service.InputManager import InputManager
from service.OutputManager import OutputManager
from service.observer.Observable import Observable

class ThermostatManager(Observable):

    def __init__(self, thermostat, inputManager, outputManager):
        super().__init__()
        self.thermostat = thermostat
        self.inputMgr = inputManager
        self.outputMgr = outputManager

        self.observers = []

        self.init()

    def init(self):
       # local variables
        self.startTime10sLoop = 0

       # set Callbacks
        self.setCallbacks()
        
    def setCallbacks(self):
        self.inputMgr.setCallback(self.inputMgr.btn2, self.toggleStatus)
        self.inputMgr.setCallback(self.inputMgr.btnRot, self.toggleRoomTemp)
        self.inputMgr.setCallback(self.inputMgr.rotary, self.updateRoomTemp)

    def clearCallback(self):
        self.inputMgr.clearCallback(self.inputMgr.btnRot)
        self.inputMgr.clearCallback(self.inputMgr.rotary)
    
    def toggleStatus(self, channel=0):
        self.thermostat.status = not self.thermostat.status

        if not self.thermostat.status:
            self.outputMgr.resetStrip()
            self.thermostat.setRoomTemp = False
            
        self.notifyObservers("Toggle state")

    def toggleRoomTemp(self, channel=0):
        if self.thermostat.status:
            self.thermostat.setRoomTemp = not self.thermostat.setRoomTemp
            self.setOutput()
            self.notifyObservers("Toggle room temp")

    def updateRoomTemp(self, arg):
        if self.thermostat.setRoomTemp:
            if arg == "CW":
                self.updateTemp(0.5)

            if arg == "CCW":
                self.updateTemp(-0.5)

    def updateTemp(self, step):
        temp = self.thermostat.settings.inputTemp
        temp += step
        self.thermostat.settings.setInputTemp(temp)
        self.notifyObservers("Update room temp")

    def minRoomTemp(self):
        temp = self.thermostat.settings.inputTemp
        temp -= 0.5
        self.thermostat.settings.setInputTemp(temp)
        self.notifyObservers("Update room temp")

    def loop(self):
        while True:
            if self.thermostat.status:
            # 5 s loop
                if self.updateLoop(self.startTime10sLoop, 5):
                    self.startTime10sLoop = time.time()
                    self.setCurrentTemp()
                    self.setOutput()
        
            time.sleep(0.01)

    def updateLoop(self, startTime, loopTime):
        currentTime = time.time()

        if currentTime >= (startTime + loopTime):
            return True

    def setCurrentTemp(self):
        self.thermostat.currentTemp = self.inputMgr.getTemp()

        if not self.thermostat.setRoomTemp:
            self.notifyObservers("Update temp")

    def setOutput(self):
        dif = self.thermostat.settings.inputTemp - self.thermostat.currentTemp

        if dif < 0.5:
            self.outputMgr.cool(abs(int(dif)), 120)
        elif dif > -0.5:
            self.outputMgr.heat(abs(int(dif)), 120)
        else:
            self.outputMgr.idle()
