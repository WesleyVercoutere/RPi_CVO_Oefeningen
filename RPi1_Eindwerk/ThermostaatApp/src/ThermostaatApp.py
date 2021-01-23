#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Eindopdracht: Thermostaat applicatie                   ##
#############################################################

# TODO  

import RPi.GPIO as GPIO
import time

from business.Thermostat import Thermostat
from service.InputManager import InputManager
from service.OutputManager import OutputManager
from service.ThermostatManager import ThermostatManager
from frontend.GUI import GUI


class ThermostatApp:

    def __init__(self):
        thermostat = Thermostat()
        inputMgr = InputManager()
        outputMgr = OutputManager()
        self.thermoMgr = ThermostatManager(thermostat, inputMgr, outputMgr)
        self.gui = GUI(self.thermoMgr)

    def run(self):
        while True:
            self.thermoMgr.loop()
            self.gui.loop()

           # time.sleep nodig voor de correcte werking van de rotary encoder! 
            time.sleep(0.001)


if __name__ == '__main__':
    ta = ThermostatApp()
    ta.run()
