#########################################################
#  Wesley Vercoutere                                    #
#  CVO Focus                                            #
#  Deel 2: INTEGRATIE EN COMMUNICATIE MET RASPBERRY PI  #
#  Opdracht 1: Transportband applicatie                 #
#                                                       #
#  v1.0.0 : Update architecture                         #
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
import RPi.GPIO as GPIO

from domain import PositionState
from domain.Conveyor import Conveyor
from domain.Led import Led
from domain.Position import Position
from frontend.GUI import GUI
from hardware.DigitalInput import DigitalInput
from hardware.OLedDisplay import OLedDisplay
from hardware.RotaryEncoder import RotaryEncoder
from hardware.StepperMotor import StepperMotor
from repository.InputRepository import InputRepository
from repository.LedRepository import LedRepository
from repository.PositionRepository import PositionRepository
from service.manager.ConveyorManager import ConveyorManager
from service.manager.DisplayManager import DisplayManager
from service.manager.InputManager import InputManager
from service.manager.LedManager import LedManager
from service.manager.MotorManager import MotorManager
from service.manager.PositionManager import PositionManager
from service.manager.SettingsManager import SettingsManager


class ConveyorApp:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        conveyor = Conveyor()
        inputMgr = self.setupInputs()
        ledMgr = self.setupLeds()
        motorMgr = self.setupMotor()
        displayMgr = self.setupDisplay()
        positionMgr = self.setupPosition()
        settingsMgr = SettingsManager()

        self.conveyorMgr = ConveyorManager(conveyor, inputMgr, ledMgr, motorMgr, displayMgr, positionMgr, settingsMgr)
        self.gui = GUI(self.conveyorMgr)

    def setupInputs(self):
        inputRepo = InputRepository()
        inputRepo.append(DigitalInput(18))
        inputRepo.append(DigitalInput(23))
        inputRepo.append(DigitalInput(25))
        inputRepo.append(DigitalInput(12))
        inputRepo.append(DigitalInput(16))
        inputRepo.append(DigitalInput(26))
        inputRepo.append(RotaryEncoder(20, 21))

        inputMgr = InputManager(inputRepo)
        return inputMgr

    def setupLeds(self):
        ledRepo = LedRepository()
        ledRepo.append(Led("green", 5))
        ledRepo.append(Led("yellow", 6))
        ledRepo.append(Led("blue", 13))
        ledRepo.append(Led("red", 19))

        ledMgr = LedManager(ledRepo)
        return ledMgr

    def setupMotor(self):
        motor = StepperMotor(17, 27, 24, 22)

        motorMgr = MotorManager(motor)
        return motorMgr

    def setupDisplay(self):
        display = OLedDisplay()

        displayMgr = DisplayManager(display)
        return displayMgr

    def setupPosition(self):
        positionRepo = PositionRepository()
        positionRepo.append(Position(id=PositionState.NONE))
        positionRepo.append(Position(id=PositionState.HOME, nbrOfSteps=0))
        positionRepo.append(Position(id=PositionState.POSITION_1, nbrOfSteps=50))
        positionRepo.append(Position(id=PositionState.POSITION_2, nbrOfSteps=100))

        positionMgr = PositionManager(positionRepo)
        return positionMgr

    def run(self):
        threading.Thread(target=self.conveyorMgr.loop).start()
        self.gui.loop()


if __name__ == '__main__':
    ca = ConveyorApp()
    ca.run()
