from domain.Position import Position
from util import PositionState


class DefaultPositions:

    def __init__(self):
        self.positions = []

        self.positions.append(Position(id=PositionState.NONE, nbrOfSteps=-1))
        self.positions.append(Position(id=PositionState.HOME, nbrOfSteps=0))
        self.positions.append(Position(id=PositionState.POSITION_1, nbrOfSteps=50))
        self.positions.append(Position(id=PositionState.POSITION_2, nbrOfSteps=100))
