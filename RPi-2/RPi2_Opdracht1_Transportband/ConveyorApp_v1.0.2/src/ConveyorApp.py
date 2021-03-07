#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 1: Transportband applicatie                 #
#                                                       #
#  v1.0.0 : Update architecture                         #
#  v1.0.1 : Update architecture                         #
#   - remove hardware repos                             #
#   - led and display -> observers                      #
#  v1.0.2 : Update repository                           #
#########################################################

# TODO - check saved position is not equal to other position

"""
-	Drukknop 1 : GPIO 18
-	Drukknop 2 : GPIO 23
-	Drukknop 3 : GPIO 25
-	Drukknop 4 : GPIO 12
-	Drukknop 5 : GPIO 16
-	Drukknop 6 : GPIO 26
-	Rotary A : GPIO 20
-	Rotary B : GPIO 21

-	Led green : GPIO 5
-	Led yellow : GPIO 6
-	Led blue : GPIO 13
-	Led red : GPIO 19

-	Stepper motor
    o	In 1 : GPIO 17
    o	In 2 : GPIO 27
    o	In 3 : GPIO 24
    o	In 4 : GPIO 22

-   Oled
    o	scl : scl1
    o	sca : sca1
"""

import threading
import time

import RPi.GPIO as GPIO

from domain.Conveyor import Conveyor
from domain.Led import Led
from hardware.DigitalInput import DigitalInput
from hardware.RotaryEncoder import RotaryEncoder
from hardware.StepperMotor import StepperMotor
from hmi.BluetoothInterface import BluetoothInterface
from hmi.DesktopGUI import DesktopGUI
from hmi.LedSignal import LedSignal
from hmi.OLedDisplay import OLedDisplay
from hmi.controller.BluetoothController import BluetoothController
from hmi.controller.DesktopController import DesktopController
from hmi.controller.HardwareController import HardwareController
from repository.PositionRepository import PositionRepository
from service.manager.ConveyorManager import ConveyorManager
from service.manager.MotorManager import MotorManager
from service.manager.OLedDisplayManager import OLedDisplayManager
from service.manager.PositionManager import PositionManager
from service.manager.SimpleLogger import SimpleLogger


class ConveyorApp:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        conveyor = Conveyor()

        self.motorMgr = self.setupMotor()
        positionMgr = self.setupPosition()

        self.conveyorMgr = ConveyorManager(conveyor, self.motorMgr, positionMgr)
        self.hardwareCtrl = self.setupInputs(self.conveyorMgr)
        self.bluetooth = self.setupBluetoothCommunication(self.conveyorMgr)
        self.ledMgr = self.setupLeds(self.conveyorMgr)
        self.setupDisplay(self.conveyorMgr)

        self.gui = self.setupGUI(self.conveyorMgr)

        logger = SimpleLogger(self.conveyorMgr)

    def setupInputs(self, conveyorManager):
        buttons = [DigitalInput(18),
                   DigitalInput(23),
                   DigitalInput(25),
                   DigitalInput(12),
                   DigitalInput(16),
                   DigitalInput(26)]

        rotary = RotaryEncoder(20, 21)

        hardwareCtrl = HardwareController(conveyorManager, buttons, rotary)
        return hardwareCtrl

    def setupMotor(self):
        motor = StepperMotor(17, 27, 24, 22)

        motorMgr = MotorManager(motor)
        return motorMgr

    def setupLeds(self, mgr):
        leds = [Led("green", 5),
                Led("yellow", 6),
                Led("blue", 13),
                Led("red", 19)]

        ledMgr = LedSignal(leds, mgr)
        return ledMgr

    def setupDisplay(self, conveyorManager):
        oLedDisplayManager = OLedDisplayManager()
        displayMgr = OLedDisplay(oLedDisplayManager, conveyorManager)
        return displayMgr

    def setupPosition(self):
        positionRepo = PositionRepository()
        positionMgr = PositionManager(positionRepo)
        return positionMgr

    def setupBluetoothCommunication(self, conveyorManager):
        controller = BluetoothController(conveyorManager)
        interface = BluetoothInterface(conveyorManager, controller)
        return interface

    def setupGUI(self, conveyorManager):
        controller = DesktopController(conveyorManager)
        gui = DesktopGUI(conveyorManager, controller)
        return gui

    def loop(self):
        while True:
            self.bluetooth.loop()
            self.motorMgr.loop()
            self.ledMgr.loop()

            # Needed to get the correct output from the rotary encoder
            time.sleep(0.01)

    def main(self):
        self.conveyorMgr.startHoming()

        threading.Thread(target=self.loop).start()
        self.gui.loop()


if __name__ == '__main__':
    ca = ConveyorApp()
    ca.main()
