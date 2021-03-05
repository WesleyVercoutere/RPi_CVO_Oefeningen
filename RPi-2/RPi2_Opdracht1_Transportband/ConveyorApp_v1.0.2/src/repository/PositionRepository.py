import json

from repository.Repository import Repository


class PositionRepository(Repository):

    def __init__(self):
        self.positions = []

    def create(self, obj):
        self.positions.append(obj)

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
        raise NotImplementedError

    def delete(self, obj):
        raise NotImplementedError

"""

positionRepo.create(Position(id=PositionState.NONE, nbrOfSteps=-1))
positionRepo.create(Position(id=PositionState.HOME, nbrOfSteps=0))
positionRepo.create(Position(id=PositionState.POSITION_1, nbrOfSteps=50))
positionRepo.create(Position(id=PositionState.POSITION_2, nbrOfSteps=100))

   def initSettings(self):
        default_settings = '{"5":"001", "6":"010", "13":"100"}'
        
        try:
            f = open("settings.txt","rt")
            print("File settings.txt exists!")
            self.settings = json.loads(f.read())
            print("Settings are", self.settings)
            f.close()

        except FileNotFoundError:
            print("File settings.txt not exists, now we create it and save default settings!")
            f = open("settings.txt","wt")
            f.write(default_settings)
            f.close()
            print("File settings.txt made!")
            print("Settings are",default_settings)
            self.settings = json.loads(f.read())

   def saveSettings(self):
        self.settings[self.pinBtn1] = self.string_var_setting_1.get()
        self.settings[self.pinBtn2] = self.string_var_setting_2.get()
        self.settings[self.pinBtn3] = self.string_var_setting_3.get()
        
        current_settings = json.dumps(self.settings)
        print(type(current_settings))
        print("Saving current settings as>",current_settings)
        
        try:
            f = open("settings.txt","wt")
            f.write(current_settings)
            f.close
            print("Saved current settings as>",current_settings)
        except FileNotFoundError:
            print("Error during saving")


    def loadSettings(self):
        # loads json from txt file and shows 3 values in the entry fields
        try:
            f = open("settings.txt","rt")
            self.settings = json.loads(f.read())
            f.close()
            print("Settings are",self.settings)
            
            self.string_var_setting_1.set(self.settings["5"])
            self.string_var_setting_2.set(self.settings["6"])
            self.string_var_setting_3.set(self.settings["13"])
                                    
        except FileNotFoundError:    
            print("Error loading settings!") 
"""