import domain.ConveyorState as State
import domain.Position as Position
import hardware.Rotation as Rotation
from service.observer.Observable import Observable


class ConveyorManager(Observable):

    def __init__(self, hardwareManager):
        self.isHomed = False
        self.position = Position.NONE
        self.state = State.IDLE

        self.nbrOfStepsPos1 = 20
        self.nbrOfStepsPos2 = 40

        self.hardwareMgr = hardwareManager
        self.hardwareMgr.setConveyor(self)
        self.hardwareMgr.setCallbacks()

        self.moveToHomePosition()

    # region Main methods conveyor

    def moveToHomePosition(self):
        print("Moving to home position")
        self.state = State.MOVING_HOME_POSITION
        self.hardwareMgr.motorRotate(Rotation.COUNTERCLOCKWISE)
        self.updateLights()

    def moveToPosition(self, position):
        if self.state == State.MOVING_HOME_POSITION:
            print("Action not allowed - Homing")
            return

        if self.state != State.IDLE:
            print("Conveyor not ready")
            return

        if self.position == position:
            print(f"Conveyor already on position {position}")
            return

        print(f"Moving to {position}")
        direction = self.calculateDirection(position)
        self.state = position
        self.hardwareMgr.motorRotate(direction)
        self.updateLights()

    def move(self, direction):
        if self.state == State.MOVING_HOME_POSITION:
            print("Action not allowed - Homing")
            return

        if self.state != State.IDLE:
            print("Conveyor not ready")
            return

        if self.state == State.IDLE:
            print(f"Moving one step {direction}")
            self.hardwareMgr.motorRotateOneStep(direction)
        else:
            print("Stop motor")
            self.hardwareMgr.motorStop()

        self.state = State.IDLE
        self.updatePosition()
        self.updateLights()

    def setPosition(self):
        print("Set position")
        if self.state == State.MOVING_HOME_POSITION:
            print("Action not allowed - Homing")
            return

        if self.state == State.MOVING_POSITION_1 or self.state == State.MOVING_POSITION_2:
            print("Conveyor not ready")
            return

        if self.state == State.IDLE:
            print(f"Setup position")
            self.state = State.SET_POSITION
            self.updateLights()
            return

        if self.state == State.SET_POSITION:
            print("Save new position")
            self.state = State.IDLE
            self.updateLights()
            return

    # endregion

    # region Callbacks

    def homePositionReached(self):
        if self.isHomed:
            print("Conveyor is already homed.")
            return

        if self.position == Position.HOME and not self.state == State.MOVING_HOME_POSITION:
            print("Is already on home position")
            return

        print("Home position reached")
        self.hardwareMgr.motorStop()
        self.hardwareMgr.setHomePosition()
        self.state = State.IDLE
        self.isHomed = True
        self.updatePosition()
        self.updateLights()

    def positionReached(self):
        newPosition = 0
        nbrOfSteps = self.hardwareMgr.nbrOfStepsFromHomePosition

        if self.state == State.MOVING_POSITION_1:
            newPosition = self.nbrOfStepsPos1
        else:
            newPosition = self.nbrOfStepsPos2

        if nbrOfSteps == newPosition:
            print("Position reached")
            self.hardwareMgr.motorStop()
            self.state = State.IDLE
            self.updatePosition()
            self.updateLights()

    # endregion

    def updatePosition(self):
        nbrOfSteps = self.hardwareMgr.nbrOfStepsFromHomePosition

        if nbrOfSteps == 0:
            self.position = Position.HOME
        elif nbrOfSteps == self.nbrOfStepsPos1:
            self.position = Position.POSITION_1
        elif nbrOfSteps == self.nbrOfStepsPos2:
            self.position = Position.POSITION_2
        else:
            self.position = Position.NONE

    def updateLights(self):
        self.hardwareMgr.resetLeds()

        if self.state == State.IDLE:
            if self.position == Position.HOME:
                self.hardwareMgr.ledHigh(0)

            if self.position == Position.POSITION_1:
                self.hardwareMgr.ledHigh(1)

            if self.position == Position.POSITION_2:
                self.hardwareMgr.ledHigh(2)

        if self.state == State.MOVING_HOME_POSITION:
            self.hardwareMgr.toggleBlinkLed(0)

        if self.state == State.MOVING_POSITION_1:
            self.hardwareMgr.toggleBlinkLed(1)

        if self.state == State.MOVING_POSITION_2:
            self.hardwareMgr.toggleBlinkLed(2)

        if self.state == State.SET_POSITION:
            self.hardwareMgr.toggleBlinkLed(3)

    def calculateDirection(self, newPosition):
        currentPosition = self.hardwareMgr.nbrOfStepsFromHomePosition
        toPosition = 0

        if newPosition == Position.POSITION_1:
            toPosition = self.nbrOfStepsPos1
        else:
            toPosition = self.nbrOfStepsPos2

        if currentPosition < toPosition:
            return Rotation.CLOCKWISE
        else:
            return Rotation.COUNTERCLOCKWISE
