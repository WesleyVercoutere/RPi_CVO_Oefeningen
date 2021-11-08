

class ToDo:

    def __init__(self) -> None:
        self.__id = 0
        self.__title = ""
        self.__carried_out_by = ""
        self.__start = ""
        self.__end = ""

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def carried_out_by(self):
        return self.__carried_out_by

    @carried_out_by.setter
    def carried_out_by(self, value):
        self.__carried_out_by = value

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        self.__start = value

    @property
    def end(self):
        return self.__end

    @end.setter
    def id(self, value):
        self.__end = value
