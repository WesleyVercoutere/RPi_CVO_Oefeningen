import domain.ConveyorState as State
import domain.PositionState as Position


class Conveyor:

    def __init__(self):
        self.isHomed = False
        
        self.position = Position.NONE
        self.state = State.IDLE
