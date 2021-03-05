from service.dto.OLedDisplayDTO import OLedDisplayDTO


class OLedDisplayManager:

    def __init__(self):
        pass

    def getDisplayDTO(self, conveyor):
        dto = OLedDisplayDTO()

        dto.state = self.setState(conveyor.state)
        dto.position = self.setPosition(conveyor.position.id)
        dto.nbrOfSteps = str(conveyor.position.nbrOfStepsFromHomePosition)

        return dto

    def setState(self, state):
        if state == 0:
            return "Idle"

        if state == 1:
            return "Homing"

        if state == 2:
            return "GoTo 1"

        if state == 3:
            return "GoTo 2"

        if state == 4:
            return "SET"

        if state == 5:
            return "SET 1"

        if state == 6:
            return "SET 2"

    def setPosition(self, id):
        if id == 0:
            return "None"

        if id == 1:
            return "Home"

        if id == 2:
            return "Pos 1"

        if id == 3:
            return "Pos 2"
