from domain.RequestObject import RequestObject

class IResourceState:

    def get_content(self, request_obj: RequestObject):
        raise NotImplementedError

    def get_header(self):
        raise NotImplementedError
