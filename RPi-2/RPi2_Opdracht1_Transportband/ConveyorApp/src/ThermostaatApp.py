###########################################################
#  Wesley Vercoutere                                      #
#  CVO Focus                                              #
#  Deel 1: Basis programmeren in Python met RaspberryPi   #
#  Eindopdracht: Thermostaat applicatie                   #
###########################################################

# TODO  

import RPi.GPIO as GPIO
import time
import threading

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
        threading.Thread(target=self.thermoMgr.loop).start()
        self.gui.root.mainloop()


if __name__ == '__main__':
    ta = ThermostatApp()
    ta.run()
