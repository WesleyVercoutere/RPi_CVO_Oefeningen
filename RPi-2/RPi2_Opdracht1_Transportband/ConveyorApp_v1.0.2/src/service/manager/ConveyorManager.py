from util import ConveyorState as ConveyorState
from util import PositionState as PositionState
from domain.Position import Position
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
        self.motorMgr.rotateToPosition(direction, nbrOfStepsToTake, self.updatePosition, self.stopConveyor)
        self.notifyObservers(conveyor=self.conveyor, message=f"Move to position {position}...")

    def setProgramMode(self, active):
        conveyorState = ConveyorState.IDLE

        if active:
            conveyorState = ConveyorState.SET_POSITION_GENERAL
    
        self.setConveyorProperties(conveyorState, self.conveyor.position.id)
        self.updateConveyor()
        self.notifyObservers(conveyor=self.conveyor, message=f"Toggle program position mode")

    def setNewPosition(self, posId):
        conveyorState = ConveyorState.SET_POSITION_1

        if posId == PositionState.POSITION_2:
            conveyorState = ConveyorState.SET_POSITION_2

        self.updateConveyor()
        self.setConveyorProperties(conveyorState, self.conveyor.position.id)
        self.notifyObservers(conveyor=self.conveyor, message=f"Set new position for {posId}")

    def saveNewPosition(self, posId):
        if self.conveyor.state == ConveyorState.SET_POSITION_1 and posId == PositionState.POSITION_2:
            self.broadcastMessage(f"Can't save this position for {posId}")
            return

        if self.conveyor.state == ConveyorState.SET_POSITION_2 and posId == PositionState.POSITION_1:
            self.broadcastMessage(f"Can't save this position for {posId}")
            return

        newPos = Position(id=posId, nbrOfSteps=self.conveyor.position.nbrOfStepsFromHomePosition)

        self.positionMgr.update(newPos)
        self.setConveyorProperties(ConveyorState.SET_POSITION_GENERAL, self.conveyor.position.id)
        self.notifyObservers(conveyor=self.conveyor, message=f"New position for {posId} saved")

    def stopConveyor(self):
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
        pos = self.positionMgr.getPositionById(position)
        totalSteps = pos.nbrOfStepsFromHomePosition
        currentSteps = self.conveyor.position.nbrOfStepsFromHomePosition

        return totalSteps - currentSteps

    def setDirection(self, nbrOfSteps):
        rotation = None

        if nbrOfSteps < 0:
            rotation = Rotation.COUNTERCLOCKWISE
        else:
            rotation = Rotation.CLOCKWISE

        return rotation

    def broadcastMessage(self, message):
        self.notifyObservers(conveyor=self.conveyor, message=message)

