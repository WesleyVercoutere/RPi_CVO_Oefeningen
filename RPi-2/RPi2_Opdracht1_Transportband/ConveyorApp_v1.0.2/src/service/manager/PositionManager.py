class PositionManager:

    def __init__(self, positionRepository):
        self.repo = positionRepository

    def getAllPositions(self):
        return self.repo.readAll()

    def getPositionById(self, id):
        return self.repo.readById(id)

    def update(self, position):
        self.repo.update(position)
