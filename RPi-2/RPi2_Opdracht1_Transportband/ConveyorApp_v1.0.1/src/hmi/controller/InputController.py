import RPi.GPIO as GPIO

from domain import ConveyorState
from domain import PositionState
from hardware import Rotation


class InputController:

    def __init__(self, buttons, rotary, conveyorManager):
        self.buttons = buttons
        self.rotary = rotary
        self.conveyorMgr = conveyorManager

        self.setCallbacks()

    def setCallbacks(self):
        self.buttons[0].setEvent(GPIO.RISING, lambda _: self.btnHomePositionReached_clicked(), 200)
        self.buttons[1].setEvent(GPIO.RISING, lambda _: self.btnMoveOneStep_clicked(Rotation.COUNTERCLOCKWISE), 200)
        self.buttons[2].setEvent(GPIO.RISING, lambda _: self.btnMoveOneStep_clicked(Rotation.CLOCKWISE), 200)
        self.buttons[3].setEvent(GPIO.RISING, lambda _: self.btnMoveToPosition_clicked(PositionState.POSITION_1), 200)
        self.buttons[4].setEvent(GPIO.RISING, lambda _: self.btnMoveToPosition_clicked(PositionState.POSITION_2), 200)
        self.buttons[5].setEvent(GPIO.RISING, lambda _: self.btnProgramPosition_clicked(), 200)
        self.rotary.setEvent(self.btnMoveOneStep_clicked)

    def btnHomePositionReached_clicked(self):
        if self.conveyorMgr.conveyor.isHomed:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor allready homed!")
        
        self.conveyorMgr.setHomed()

    def btnMoveOneStep_clicked(self, direction):
        if self.conveyorMgr.conveyor.state != ConveyorState.IDLE:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor not ready!")
            return

        self.conveyorMgr.moveOneStep(direction)

    def btnMoveToPosition_clicked(self, position):
        conveyor = self.conveyorMgr.conveyor

        if conveyor.state != ConveyorState.IDLE or conveyor.state != ConveyorState.SET_POSITION_GENERAL:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor not ready!")
            return

        self.conveyorMgr.moveToPosition(position)

    def btnProgramPosition_clicked(self):
        if self.conveyorMgr.conveyor.state != ConveyorState.IDLE:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor not ready!")
            return
