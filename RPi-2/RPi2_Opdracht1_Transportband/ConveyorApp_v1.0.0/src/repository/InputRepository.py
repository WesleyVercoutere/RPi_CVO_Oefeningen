from repository.Repository import Repository


class InputRepository(Repository):

    def __init__(self):
        self.inputs = []

    def append(self, obj):
        self.inputs.append(obj)

    def getById(self, idOfObj):
        pass

    def getByIndex(self, indexOfObj):
        return self.inputs[indexOfObj]

    def getAll(self):
        return self.inputs
