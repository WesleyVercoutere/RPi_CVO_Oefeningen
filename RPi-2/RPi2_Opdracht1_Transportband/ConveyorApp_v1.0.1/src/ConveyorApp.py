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
#########################################################

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

from domain import PositionState
from domain.Conveyor import Conveyor
from domain.Led import Led
from domain.Position import Position
from hardware.DigitalInput import DigitalInput
from hardware.OLedDisplay_I2C import OLedDisplay_I2C
from hardware.RotaryEncoder import RotaryEncoder
from hardware.StepperMotor import StepperMotor
from hmi.DesktopGUI import DesktopGUI
from hmi.LedSignal import LedSignal
from hmi.OLedDisplay import OLedDisplay
from hmi.controller.HardwareController import HardwareController
from repository.PositionRepository import PositionRepository
from service.manager.ConveyorManager import ConveyorManager
from service.manager.MotorManager import MotorManager
from service.manager.PositionManager import PositionManager


class ConveyorApp:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        conveyor = Conveyor()

        self.motorMgr = self.setupMotor()
        positionMgr = self.setupPosition()

        self.conveyorMgr = ConveyorManager(conveyor, self.motorMgr, positionMgr)
        self.hardwareCtrl = self.setupInputs(self.conveyorMgr)
        self.ledMgr = self.setupLeds(self.conveyorMgr)
        self.setupDisplay(self.conveyorMgr)

        self.gui = DesktopGUI(self.conveyorMgr)

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

    def setupDisplay(self, mgr):
        display = OLedDisplay_I2C()

        displayMgr = OLedDisplay(display, mgr)
        return displayMgr

    def setupPosition(self):
        positionRepo = PositionRepository()
        positionRepo.append(Position(id=PositionState.NONE, nbrOfSteps=-1))
        positionRepo.append(Position(id=PositionState.HOME, nbrOfSteps=0))
        positionRepo.append(Position(id=PositionState.POSITION_1, nbrOfSteps=50))
        positionRepo.append(Position(id=PositionState.POSITION_2, nbrOfSteps=100))

        positionMgr = PositionManager(positionRepo)
        return positionMgr

    def loop(self):
        while True:
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
