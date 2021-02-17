#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 1: Transportband applicatie                 #
#########################################################


import RPi.GPIO as GPIO
import time
import threading

from service.HardwareManager import HardwareManager
from service.ConveyorManager import ConveyorManager
from service.CommunicationManager import CommunicationManager
from frontend.GUI import GUI


class ThermostatApp:

    def __init__(self):
        self.hardwareMgr = HardwareManager()
        self.conveyorMgr = ConveyorManager(self.hardwareMgr)
        self.CommunicationMgr = CommunicationManager(self.conveyorMgr)

        self.gui = GUI(self.conveyorMgr)

    def run(self):
        threading.Thread(target=self.hardwareMgr.loop).start()
        self.gui.loop()


if __name__ == '__main__':
    ta = ThermostatApp()
    ta.run()
