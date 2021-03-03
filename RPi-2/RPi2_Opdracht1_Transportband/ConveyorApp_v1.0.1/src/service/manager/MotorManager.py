

class MotorManager:

    def __init__(self, motor):
        self.motor = motor
        self.keepMoving = False
        self.direction = None
        self.movingToPosition = False
        self.nbrOfStepsTaken = 0
        self.nbrOfStepsToTake = 0

        self.callback = None

    def rotateLoop(self, direction):
        self.keepMoving = True
        self.direction = direction

    def rotateOneStep(self, direction):
        self.motor.rotate(direction)

    def rotateToPosition(self, direction, nbrOfSteps, callback):
        self.movingToPosition = True
        self.nbrOfStepsToTake = nbrOfSteps
        self.direction = direction
        self.callback = callback

    def stop(self):
        self.keepMoving = False
        self.movingToPosition = False
        self.nbrOfStepsTaken = 0
        self.nbrOfStepsToTake = 0
        self.motor.stop()

    def positionReached(self):
        self.callback(self.nbrOfStepsTaken)
        self.stop()
        
    def loop(self):
        if self.keepMoving or self.movingToPosition:
            self.motor.rotate(self.direction)

        if self.movingToPosition:
            self.nbrOfStepsTaken += 1

        if self.nbrOfStepsTaken == self.nbrOfStepsToTake:
            self.positionReached()
