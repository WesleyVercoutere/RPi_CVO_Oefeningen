#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Eindopdracht: Thermostaat applicatie                   ##
#############################################################

from service.InputManager import InputManager
from service.OutputManager import OutputManager
from service.ThermostatManager import ThermostatManager
from frontend.GUI import GUI

import time


class ThermostatApp:

    def __init__(self):
        self.inputMgr = InputManager()
        self.outputMgr = OutputManager()
        self.thermoMgr = ThermostatManager(self.inputMgr, self.outputMgr)
       # self.gui = GUI(self.thermoMgr)

    def run(self):
        while True:
            print(self.inputMgr.tempSensor.readTemp())
            time.sleep(1)


if __name__ == '__main__':
    ta = ThermostatApp()
    ta.run()
