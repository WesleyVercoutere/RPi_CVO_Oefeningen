class RequestObject:

    def __init__(self) -> None:
        self.__request_type = "" #GET / POST / PUT / DELETE ...
        self.__request_route = ""
        self.__filename = ""
        self.__file_extension = ""
        self.__response_type = ""
        self.__handler = None

    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, value):
        self.__request_type = value
    
    @property
    def request_route(self):
        return self.__request_route

    @request_route.setter
    def request_route(self, value):
        self.__request_route = value

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

    @property
    def response_type(self):
        return self.__response_type

    @response_type.setter
    def response_type(self, value):
        self.__response_type = value

    @property
    def handler(self):
        return self.__handler

    @handler.setter
    def handler(self, value):
        self.__handler = value
