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
        self.setConveyorProperties(False, ConveyorState.MOVING_TO_HOME_POSITION, PositionState.NONE)
        self.motorMgr.rotateLoop(Rotation.COUNTERCLOCKWISE)
        self.notifyObservers(self.conveyor)

    def moveOneStep(self, direction):
        print(f"Rotate one step {direction}")
        # Move motor one step
        # Update conveyor position and state
        pass

    def moveToPosition(self, position):
        # Move motor to position
        # Update conveyor position and state
        pass

    def setConveyorProperties(self, isHomed, conveyorState, positionState):
        self.conveyor.isHomed = isHomed
        self.conveyor.state = conveyorState
        self.conveyor.position = positionState

    def loop(self):
        self.motorMgr.loop()
