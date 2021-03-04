

class MotorManager:

    def __init__(self, motor):
        self.motor = motor
        self.keepMoving = False
        self.direction = None
        self.movingToPosition = False
        self.nbrOfStepsTaken = 0
        self.nbrOfStepsToTake = 0

        self.update = None
        self.callback = None

    def rotateLoop(self, direction):
        self.keepMoving = True
        self.direction = direction

    def rotateOneStep(self, direction, updatePosition):
        self.motor.rotate(direction)

        if updatePosition is not None:
            updatePosition(direction)

    def rotateToPosition(self, direction, nbrOfSteps, update, stop):
        self.movingToPosition = True
        self.nbrOfStepsToTake = nbrOfSteps
        self.direction = direction
        self.update = update
        self.callback = stop

    def stop(self):
        self.keepMoving = False
        self.movingToPosition = False
        self.nbrOfStepsTaken = 0
        self.nbrOfStepsToTake = 0
        self.motor.stop()

    def positionReached(self):
        self.stop()
        self.callback()
        
    def loop(self):
        if self.keepMoving or self.movingToPosition:
            self.rotateOneStep(self.direction, self.update)

        if self.movingToPosition:
            self.nbrOfStepsTaken += 1

        if self.movingToPosition and (self.nbrOfStepsTaken == self.nbrOfStepsToTake):
            self.positionReached()
