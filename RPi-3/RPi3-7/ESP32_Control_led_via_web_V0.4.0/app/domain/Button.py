from machine import Pin

class Button:
    
    Id = 0

    def __init__(self, pin_nr) -> None:
        Button.Id += 1

        self.__id = Button.Id
        self.__pin_nr = pin_nr
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
    def state(self):
        return self._pin.value()

    def get_pin(self):
        return self._pin

    def _init_pin(self) -> None:
        self._pin = Pin(self.pin_nr, Pin.IN, Pin.PULL_UP)
