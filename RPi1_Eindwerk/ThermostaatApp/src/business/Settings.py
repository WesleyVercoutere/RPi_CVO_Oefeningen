class Settings:

    def __init__(self):
        self.MAX_TEMP = 30
        self.MIN_TEMP = 5

        self.inputTemp = 20

    def setInputTemp(self, temp):
        if temp > self.MAX_TEMP:
            temp = self.MIN_TEMP

        if temp < self.MIN_TEMP:
            temp = self.MAX_TEMP

        self.inputTemp = temp