

class PositionManager:

    def __init__(self, positionRepository):
        self.repo = positionRepository

    def getAllPositions(self):
        return self.repo.getAll()

    def getPositionById(self, id):
        return self.repo.getById(id)

    def update(self, position):
        
        print(f"Update position {position.id} with {position.nbrOfSteps} nbr of steps from home")
