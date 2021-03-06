import RPi.GPIO as GPIO

from hardware import Rotation
from hmi.controller.BaseController import BaseController
from util import PositionState


class HardwareController(BaseController):

    def __init__(self, conveyorManager, buttons, rotary):
        super(HardwareController, self).__init__(conveyorManager)
        self.buttons = buttons
        self.rotary = rotary

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
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor already homed!")
        
        self.conveyorMgr.setHomed()
