from webserver.domain.RequestObject import RequestObject
from webserver.domain.ResponseObject import ResponseObject
from webserver.domain.StateObject import StateObject
from webserver.service.IResponseHandler import IResponseHandler
from webserver.service.ResourceContext import ResourceContext


class ResourceResponseHandler(IResponseHandler):

    def __init__(self, request: RequestObject) -> None:
        super().__init__(request)

        self._context = ResourceContext()
        self._state = None

    def get_response(self) -> ResponseObject:        
        file_name = self._get_file_name()
        file_extension = self._get_file_extension()
        state = StateObject(file_name=file_name, file_extension=file_extension)

        self._context.set_state(state_obj=state)
        self._state = self._context.get_state()
        self._state.set_state(state=state)

        return self._create_response()

    def _get_file_name(self):
        return self._request.request_url

    def _get_file_extension(self):
        return self._request.request_url.split(".")[-1]

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
