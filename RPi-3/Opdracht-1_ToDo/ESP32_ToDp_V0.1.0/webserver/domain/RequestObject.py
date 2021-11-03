class RequestObject:

    def __init__(self) -> None:
        self.__request_type = "" #GET / POST / PUT / DELETE ...
        self.__request_url = ""
        self.__response_type = ""
        self.__route = None
        
    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, value):
        self.__request_type = value
    
    @property
    def request_url(self):
        return self.__request_url

    @request_url.setter
    def request_url(self, value):
        self.__request_url = value

    @property
    def response_type(self):
        return self.__response_type

    @response_type.setter
    def response_type(self, value):
        self.__response_type = value

    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, value):
        self.__route = value
