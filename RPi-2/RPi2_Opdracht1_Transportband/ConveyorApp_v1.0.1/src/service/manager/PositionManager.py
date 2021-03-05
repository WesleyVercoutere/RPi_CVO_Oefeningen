

class PositionManager:

    def __init__(self, positionRepository):
        self.repo = positionRepository

    def getAllPositions(self):
        return self.repo.getAll()

    def getPositionById(self, id):
        return self.repo.getById(id)
