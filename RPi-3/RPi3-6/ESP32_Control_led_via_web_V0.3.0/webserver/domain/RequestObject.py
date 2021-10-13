class RequestObject:

    def __init__(self) -> None:
        self.__request_type = "" #GET / POST / PUT / DELETE ...
        self.__relative_path = ""
        self.__filename = ""
        self.__file_extension = ""

    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, value):
        self.__request_type = value
    
    @property
    def relative_path(self):
        return self.__relative_path

    @relative_path.setter
    def relative_path(self, value):
        self.__relative_path = value

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    @property
    def file_extension(self):
        return self.__file_extension

    @file_extension.setter
    def file_extension(self, value):
        self.__file_extension = value
