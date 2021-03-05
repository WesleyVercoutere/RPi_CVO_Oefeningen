class Position:

    def __init__(self, id=None, nbrOfSteps=None):
        self.id = id if id is not None else ""
        self.nbrOfStepsFromHomePosition = nbrOfSteps if nbrOfSteps is not None else 0
