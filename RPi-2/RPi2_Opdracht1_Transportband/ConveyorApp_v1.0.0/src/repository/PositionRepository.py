from repository.Repository import Repository


class PositionRepository(Repository):

    def __init__(self):
        super.__init__()
        self.positions = []

    def append(self, obj):
        self.positions.append(obj)

    def getById(self, idOfObj):
        position = None

        for item in self.positions:
            if item.id == idOfObj:
                position = item

        return position

    def getByIndex(self, indexOfObj):
        return self.positions[indexOfObj]

    def getAll(self):
        return self.positions
