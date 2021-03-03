

class PositionManager:

    def __init__(self, positionRepository):
        self.repo = positionRepository

    def getAllPositions(self):
        return self.repo.getAll()

