import domain.ConveyorState as State
import domain.PositionState as PositionState
from domain.Position import Position


class Conveyor:

    def __init__(self):
        self.isHomed = False
        self.state = State.IDLE
        self.position = Position(PositionState.NONE)
