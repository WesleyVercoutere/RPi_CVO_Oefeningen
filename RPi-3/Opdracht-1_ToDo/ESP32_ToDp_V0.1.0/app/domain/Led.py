from machine import Pin

class Led:
    
    Id = 0

    def __init__(self, pin_nr, color) -> None:
        Led.Id += 1

        self.__id = Led.Id
        self.__pin_nr = pin_nr
        self.__color = color
        self.__state = False
        self._pin = None

        self._init_pin()

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def pin_nr(self):
        return self.__pin_nr

    @pin_nr.setter
    def pin_nr(self, value):
        self.__pin_nr = value

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    def get_pin(self):
        return self._pin

    def _init_pin(self) -> None:
        self._pin = Pin(self.pin_nr, Pin.OUT)
