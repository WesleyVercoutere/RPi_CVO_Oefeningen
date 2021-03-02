import RPi.GPIO as GPIO

from domain import PositionState
from hardware import Rotation


class InputController:

    def __init__(self, buttons, rotary, conveyorManager, motorManager):
        self.buttons = buttons
        self.rotary = rotary
        self.conveyorMgr = conveyorManager
        self.motorMgr = motorManager

        self.setCallbacks()

    def setCallbacks(self):
        self.buttons[0].setEvent(GPIO.RISING, lambda _: self.btnHomePositionReached_clicked(), 200)
        self.buttons[1].setEvent(GPIO.RISING, lambda _: self.btnMoveOneStep_clicked(Rotation.COUNTERCLOCKWISE), 200)
        self.buttons[2].setEvent(GPIO.RISING, lambda _: self.btnMoveOneStep_clicked(Rotation.CLOCKWISE), 200)
        self.buttons[3].setEvent(GPIO.RISING, lambda _: self.btnMoveToPosition_clicked(PositionState.POSITION_1), 200)
        self.buttons[4].setEvent(GPIO.RISING, lambda _: self.btnMoveToPosition_clicked(PositionState.POSITION_2), 200)
        self.buttons[5].setEvent(GPIO.RISING, lambda _: self.btnProgramPosition_clicked(), 200)
        self.rotary.setEvent(self.conveyorMgr.btnMoveOneStep_clicked)

    def btnHomePositionReached_clicked(self):
        # Homing position reached
        pass

    def btnMoveOneStep_clicked(self, direction):
        # TODO check state and throw message
        self.conveyorMgr.moveOneStep(direction)

    def btnMoveToPosition_clicked(self, position):
        # Move to position 1 or program position 1
        pass

    def btnProgramPosition_clicked(self):
        # Program positions
        pass
