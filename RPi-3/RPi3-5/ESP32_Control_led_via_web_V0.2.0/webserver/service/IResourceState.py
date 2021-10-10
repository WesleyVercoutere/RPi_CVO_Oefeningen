from webserver.domain.RequestObject import RequestObject


class IResourceState:

    def __init__(self,) -> None:
        pass
    
    def get_content(self, request_obj: RequestObject):
        raise NotImplementedError

    def get_header(self):
        raise NotImplementedError
