class Led():
    
    Id = 0

    def __init__(self, pin_nr, color) -> None:
        Led.Id += 1

        self.__id = Led.Id
        self.__pin_nr = pin_nr
        self.__color = color
        self.__state = False

    @property
    def id(self):
        return self.__id

    @property
    def pin_nr(self):
        return self.__pin_nr

    @property
    def color(self):
        return self.__color
    
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value
