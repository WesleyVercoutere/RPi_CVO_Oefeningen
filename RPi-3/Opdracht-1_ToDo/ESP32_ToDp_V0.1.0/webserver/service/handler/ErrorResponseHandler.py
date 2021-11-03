from webserver.domain.RequestObject import RequestObject
from webserver.domain.ResponseObject import ResponseObject
from webserver.service.IResponseHandler import IResponseHandler


class ErrorResponseHandler(IResponseHandler):

    def __init__(self, request: RequestObject) -> None:
        super().__init__(request)

    def get_response(self) -> ResponseObject:
        response = ResponseObject()
        response.header_1 = b"HTTP/1.1 404 Not Found\r\n"

        return response
