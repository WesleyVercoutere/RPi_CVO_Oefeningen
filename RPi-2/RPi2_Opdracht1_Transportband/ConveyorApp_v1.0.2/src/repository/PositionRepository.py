import json

from domain.DefaultPositions import DefaultPositions
from domain.Position import Position
from repository.Repository import Repository
from util.FileHandler import FileHandler


class PositionRepository(Repository):

    def __init__(self):
        self.file = FileHandler("positions")
        self.default = DefaultPositions().positions
        self.positions = []

        self.initPositions()

    def initPositions(self):
        json = self.file.read(self.getDefaultJson())

        for k, v in json.items():
            pos = Position(id=int(k), nbrOfSteps=v)
            self.positions.append(pos)
        
    def create(self, obj):
        raise NotImplementedError

    def readById(self, idOfObj):
        position = None

        for item in self.positions:
            if item.id == idOfObj:
                position = item

        return position

    def readByIndex(self, indexOfObj):
        return self.positions[indexOfObj]

    def readAll(self):
        return self.positions

    def update(self, obj):
        position = self.readById(obj.id)
        position.nbrOfStepsFromHomePosition = obj.nbrOfStepsFromHomePosition

        json = self.setJson()
        self.file.write(json)

    def delete(self, obj):
        raise NotImplementedError

    def getDefaultJson(self):
        settings = {}

        for pos in self.default:
            settings[pos.id] = pos.nbrOfStepsFromHomePosition
        
        return json.dumps(settings)

    def setJson(self):
        settings = {}

        for pos in self.positions:
            settings[pos.id] = pos.nbrOfStepsFromHomePosition
        
        return json.dumps(settings)
