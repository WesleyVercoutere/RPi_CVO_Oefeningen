import domain.ConveyorState as State
import domain.PositionState as PositionState
from domain.Position import Position


class Conveyor:

    def __init__(self):
        self.isHomed = False
        self.position = PositionState.NONE
        self.state = State.IDLE

        self.currentPosition = Position(PositionState.CURRENT_POSITION)
