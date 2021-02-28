from repository.Repository import Repository


class LedRepository(Repository):

    def __init__(self):
        super.__init__()
        self.leds = []

    def append(self, obj):
        self.leds.append(obj)

    def getById(self, idOfObj):
        led = None

        for item in self.leds:
            if item.id == idOfObj:
                led = item

        return led

    def getByIndex(self, indexOfObj):
        return self.leds[indexOfObj]

    def getAll(self):
        return self.leds
