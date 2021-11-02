from webserver.domain.RequestObject import RequestObject
from webserver.domain.ResponseObject import ResponseObject

class IResponseHandler:

    def __init__(self, request: RequestObject) -> None:
        self._request = request

    def get_response(self) -> ResponseObject:
        raise NotImplementedError
