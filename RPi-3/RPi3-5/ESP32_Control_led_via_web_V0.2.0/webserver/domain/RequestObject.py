class RequestObject:

    def __init__(self) -> None:
        self.__request_type = "" #GET / POST / PUT / DELETE ...
        self.__path = ""
        self.__file = ""
        self.__file_type = ""

    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, value):
        self.__request_type = value
    
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        self.__file = value

    @property
    def file_type(self):
        return self.__file_type

    @file_type.setter
    def file_type(self, value):
        self.__file_type = value
