#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 1: Transportband applicatie                 #
#########################################################


import threading

from frontend.GUI import GUI
from service.manager.CommunicationManager import CommunicationManager
from service.manager.ConveyorManager import ConveyorManager
from service.manager.HardwareManager import HardwareManager


class ConveyorApp:

    def __init__(self):
        self.hardwareMgr = HardwareManager()
        self.conveyorMgr = ConveyorManager(self.hardwareMgr)
        self.CommunicationMgr = CommunicationManager(self.conveyorMgr)

        self.gui = GUI(self.conveyorMgr)

    def run(self):
        threading.Thread(target=self.hardwareMgr.loop).start()
        self.gui.loop()


if __name__ == '__main__':
    ca = ConveyorApp()
    ca.run()
