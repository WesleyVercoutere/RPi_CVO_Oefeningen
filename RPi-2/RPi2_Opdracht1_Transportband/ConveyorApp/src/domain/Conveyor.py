import domain.ConveyorState as State
import domain.Position as Position


class Conveyor:

    def __init__(self):
        self.isHomed = False
        
        self.position = Position.NONE
        self.state = State.IDLE

        self.nbrOfStepsPos1 = 20
        self.nbrOfStepsPos2 = 40
