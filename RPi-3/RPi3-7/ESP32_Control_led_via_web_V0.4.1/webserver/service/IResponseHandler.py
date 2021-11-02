from webserver.domain.RequestObject import RequestObject
from webserver.domain.ResponseObject import ResponseObject
from webserver.service.ResourceContext import ResourceContext

class IResponseHandler:

    def __init__(self, request: RequestObject) -> None:
        self._request = request

        self._context = ResourceContext()
        self._state = None

    def get_response(self) -> ResponseObject:
        raise NotImplementedError

    def _create_response(self) -> ResponseObject:
        response = ResponseObject()

        try:
            response.content = self._state.get_content()
            response.content_length = (f"Content-Length:{str(len(response.content))}\r\n\r\n").encode("UTF-8")
            response.header_1 = b"HTTP/1.1 200 OK\r\n"
            response.header_2 = self._state.get_header()
            response.cache = self._state.get_cache()

        except Exception as ex:
            print(ex)
            response.header_1 = b"HTTP/1.1 404 NOT FOUND\r\n"

        return response
        