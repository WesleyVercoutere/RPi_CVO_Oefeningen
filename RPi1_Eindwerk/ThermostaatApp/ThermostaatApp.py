#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Eindopdracht: Thermostaat applicatie                   ##
#############################################################

from service.InputManager import *
from service.OutputManager import *
from service.ThermostatManager import *

from frontend.GUI import *
import time


class ThermostaatApp:

    def __init__(self):
        self.inputMgr = InputManager()
        self.outputMgr = OutputManager()
        self.thermoMgr = ThermostatManager(self.inputMgr, self.outputMgr)
       # self.gui = GUI(thermoMgr)

    def run(self):
        while True:
            print(self.inputMgr.tempSensor.readTemp())
            time.sleep(1)


if __name__ == '__main__':
    ta = ThermostaatApp()
    ta.run()
