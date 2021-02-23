import domain.Position as Position
import domain.ConveyorState as State

class Conveyor:

    def __init__(self):
        self.isHomed = False
        
        self.position = Position.NONE
        self.state = State.IDLE

        self.nbrOfStepsPos1 = 20
        self.nbrOfStepsPos2 = 40
