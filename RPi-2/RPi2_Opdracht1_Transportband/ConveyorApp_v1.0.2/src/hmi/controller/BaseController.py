import abc

from domain import ConveyorState


class BaseController(metaclass=abc.ABCMeta):

    def __init__(self, conveyorManager):
        self.conveyorMgr = conveyorManager

    def btnHomePositionReached_clicked(self):
        if self.conveyorMgr.conveyor.isHomed:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor already homed!")
        
        self.conveyorMgr.setHomed()

    def btnMoveOneStep_clicked(self, direction):
        if self.conveyorMgr.conveyor.state == ConveyorState.MOVING_TO_POSITION_1 or self.conveyorMgr.conveyor.state == ConveyorState.MOVING_TO_POSITION_2:
            self.conveyorMgr.stopConveyor()
            return

        if self.conveyorMgr.conveyor.state != ConveyorState.IDLE and self.conveyorMgr.conveyor.state != ConveyorState.SET_POSITION_1 and self.conveyorMgr.conveyor.state != ConveyorState.SET_POSITION_2:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor not ready!")
            return

        self.conveyorMgr.moveOneStep(direction)

    def btnMoveToPosition_clicked(self, position):
        conveyor = self.conveyorMgr.conveyor

        if conveyor.state == ConveyorState.SET_POSITION_GENERAL:
            self.conveyorMgr.setNewPosition(position)

        elif conveyor.state == ConveyorState.SET_POSITION_1 or conveyor.state == ConveyorState.SET_POSITION_2:
            self.conveyorMgr.saveNewPosition(position)
        
        elif conveyor.position.id == position:
            self.conveyorMgr.broadcastMessage(f"Action not allowed - Conveyor is on position {position}!")

        elif conveyor.state == ConveyorState.IDLE:
            self.conveyorMgr.moveToPosition(position)

        else:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor not ready!")

    def btnProgramPosition_clicked(self):
        if self.conveyorMgr.conveyor.state == ConveyorState.IDLE:
            self.conveyorMgr.setProgramMode(True)

        elif self.conveyorMgr.conveyor.state == ConveyorState.SET_POSITION_GENERAL:
            self.conveyorMgr.setProgramMode(False)

        else:
            self.conveyorMgr.broadcastMessage("Action not allowed - Conveyor not ready!")
