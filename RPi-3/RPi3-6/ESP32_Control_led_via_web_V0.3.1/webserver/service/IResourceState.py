from webserver.domain.RequestObject import RequestObject


class IResourceState:

    def __init__(self) -> None:
        self.__request_obj = None

    @property
    def request_obj(self) -> RequestObject:
        return self.__request_obj

    @request_obj.setter
    def request_obj(self, value) -> None:
        self.__request_obj = value
    
    def get_content(self):
        raise NotImplementedError

    def get_header(self):
        raise NotImplementedError

    def get_cache(self):
        raise NotImplementedError
