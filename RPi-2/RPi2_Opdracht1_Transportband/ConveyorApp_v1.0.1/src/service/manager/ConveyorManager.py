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
        self.setConveyorProperties(ConveyorState.MOVING_TO_HOME_POSITION, PositionState.NONE, isHomed=False)
        self.motorMgr.rotateLoop(Rotation.COUNTERCLOCKWISE)
        self.notifyObservers(conveyor=self.conveyor, message="Homing...")

    def moveOneStep(self, direction):
        self.motorMgr.rotateOneStep(direction, self.updatePosition)
        self.updateConveyor()
        self.notifyObservers(conveyor=self.conveyor, message=f"Move one step {direction}")

    def moveToPosition(self, position):
        conveyorState = self.setConveyorState(position)
        nbrOfStepsToTake = self.calculateNbrOfSteps(position)
        direction = self.setDirection(nbrOfStepsToTake)

        self.setConveyorProperties(conveyorState, PositionState.NONE)
        self.motorMgr.rotateToPosition(direction, nbrOfStepsToTake, self.updatePosition, self.stopConceyor)
        # Update conveyor position and state
        self.notifyObservers(conveyor=self.conveyor, message=f"Move to position {position}")

    def stopConceyor(self):
        self.motorMgr.stop()
        self.updateConveyor()
        self.setConveyorProperties(ConveyorState.IDLE, self.conveyor.position.id)
        self.notifyObservers(conveyor=self.conveyor, message="Conveyor is stopped")

    def setHomed(self):
        self.motorMgr.stop()
        self.setConveyorProperties(ConveyorState.IDLE, PositionState.HOME)
        self.conveyor.position.nbrOfStepsFromHomePosition = 0
        self.notifyObservers(conveyor=self.conveyor, message="Conveyor is homed")

    def updatePosition(self, direction):
        self.conveyor.position.nbrOfStepsFromHomePosition += direction

    # def setPositionReached(self):
    #     self.setConveyorProperties()
    #     # self.motorMgr.rotateToPosition(direction, nbrOfSteps, callback):
    #     # Update conveyor position and state
    #     self.notifyObservers(conveyor=self.conveyor, message=f"Move to position {position}")

    def setConveyorProperties(self, conveyorState, positionState, isHomed=True):
        self.conveyor.isHomed = isHomed
        self.conveyor.state = conveyorState
        self.conveyor.position.id = positionState

    def updateConveyor(self):
        positions = self.positionMgr.getAllPositions()

        for pos in positions:
            if self.conveyor.position.nbrOfStepsFromHomePosition == pos.nbrOfStepsFromHomePosition:
                self.conveyor.position.id = pos.id
                break
            else:
                self.conveyor.position.id = PositionState.NONE

    def setConveyorState(self, position):
        conveyorState = None

        if position == ConveyorState.MOVING_TO_POSITION_1:
            conveyorState = ConveyorState.MOVING_TO_POSITION_1

        if position == ConveyorState.MOVING_TO_POSITION_2:
            conveyorState = ConveyorState.MOVING_TO_POSITION_2

        return conveyorState

    def calculateNbrOfSteps(self, position):
        totalSteps = position
        currentSteps = self.conveyor.position.nbrOfStepsFromHomePosition

        return (totalSteps - currentSteps)

    def setDirection(self, nbrOfSteps):
        rotation = None

        if nbrOfSteps < 0:
            rotation = Rotation.COUNTERCLOCKWISE
        else:
            rotation = Rotation.CLOCKWISE

        return rotation

    def broadcastMessage(self, message):
        self.notifyObservers(conveyor=self.conveyor, message=message)

