from domain import ConveyorState, PositionState
from hardware import Rotation
from service.observer.Observable import Observable


class ConveyorManager(Observable):

    def __init__(self, conveyor,
                 inputManager,
                 motorManager,
                 positionManager):
        super(ConveyorManager, self).__init__()

        self.conveyor = conveyor
        self.inputMgr = inputManager
        self.motorMgr = motorManager
        self.positionMgr = positionManager

        self.inputMgr.setManagers(self, self.motorMgr)
        self.inputMgr.setCallbacks()
        self.startHoming()

    def startHoming(self):
        self.setConveyorProperties(False, ConveyorState.MOVING_TO_HOME_POSITION, PositionState.NONE)
        self.motorMgr.rotate(Rotation.COUNTERCLOCKWISE)
        self.notifyObservers(self.conveyor)

    def moveOneStep(self, direction):
        # Move motor one step
        # Update conveyor position and state
        pass

    def moveToPosition(self, position):
        pass

    def setConveyorProperties(self, isHomed, conveyorState, positionState):
        self.conveyor.isHomed = isHomed
        self.conveyor.state = conveyorState
        self.conveyor.position = positionState

    def loop(self):
        self.inputMgr.loop()
        self.motorMgr.loop()
