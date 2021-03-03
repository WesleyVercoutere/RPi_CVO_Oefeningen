from domain import ConveyorState as ConveyorState
from domain import PositionState as PositionState
from hardware import Rotation
from service.observer.Observable import Observable


class ConveyorManager(Observable):

    def __init__(self, conveyor,
                 motorManager,
                 positionManager):
        super(ConveyorManager, self).__init__()

        self.conveyor = conveyor
        self.motorMgr = motorManager
        self.positionMgr = positionManager

    def startHoming(self):
        self.setConveyorProperties(ConveyorState.MOVING_TO_HOME_POSITION, PositionState.NONE, 0, False)
        self.motorMgr.rotateLoop(Rotation.COUNTERCLOCKWISE)
        self.notifyObservers(conveyor=self.conveyor, message="Homing...")

    def moveOneStep(self, direction):
        self.motorMgr.rotateOneStep(direction)
        self.conveyor.position.nbrOfStepsFromHomePosition += direction
        self.updateConveyor()
        self.notifyObservers(conveyor=self.conveyor, message=f"Move one step {direction}")
        pass

    def moveToPosition(self, position):
        self.setConveyorProperties()
        self.motorMgr.rotateToPosition(direction, nbrOfSteps, callback):
        # Update conveyor position and state
        self.notifyObservers(conveyor=self.conveyor, message=f"Move to position {position}")

    def setHomed(self):
        self.motorMgr.stop()
        self.setConveyorProperties(ConveyorState.IDLE, PositionState.HOME, 0)
        self.notifyObservers(conveyor=self.conveyor, message="Conveyor is homed")

    def broadcastMessage(self, message):
        self.notifyObservers(conveyor=self.conveyor, message=message)

    def setConveyorProperties(self, conveyorState, positionState, nbrOfStepsFromHomePosition, isHomed=True, ):
        self.conveyor.isHomed = isHomed
        self.conveyor.state = conveyorState
        self.conveyor.position.id = positionState
        self.conveyor.position.nbrOfStepsFromHomePosition = nbrOfStepsFromHomePosition

    def updateConveyor(self):
        positions = self.positionMgr.getAllPositions()

        for pos in positions:
            if self.conveyor.position.nbrOfStepsFromHomePosition == pos.nbrOfStepsFromHomePosition:
                self.conveyor.position.id = pos.id
