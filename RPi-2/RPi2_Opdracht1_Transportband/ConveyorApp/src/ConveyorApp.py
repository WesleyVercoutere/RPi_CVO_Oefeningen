#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 1: Transportband applicatie                 #
#########################################################

'''
-	Drukknop 1 : GPIO 18
-	Drukknop 2 : GPIO 23
-	Drukknop 3 : GPIO 25
-	Drukknop 4 : GPIO 12
-	Drukknop 5 : GPIO 16
-	Drukknop 6 : GPIO 26
-	Rotary A : GPIO 20
-	Rotary B : GPIO 21
-	Potentiometer : MCP 3008 channel 1
-	MCP3008 :
    o	CLK : GPIO 11 / SPIO SCLK
    o	Dout : GPIO 9 / SPIO MISO
    o	Din : GPIO 10 / SPIO MOSI
    o	CS/Sh : GPIO 8 / SPIO CS1
-	Led green : GPIO 5
-	Led yellow : GPIO 6
-	Led blue : GPIO 13
-	Led red : GPIO 19
-	Bluetooth module
    o	RX : UARTO TX
    o	TX : UARTO RX
-	Stepper motor
    o	In 1 : GPIO 17
    o	In 2 : GPIO 27
    o	In 3 : GPIO 22
    o	In 4 : GPIO 23
'''

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
