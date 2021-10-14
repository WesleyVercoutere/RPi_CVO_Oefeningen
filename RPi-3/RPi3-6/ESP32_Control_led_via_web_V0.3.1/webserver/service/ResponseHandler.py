from webserver.domain.ResponseObject import ResponseObject
from webserver.domain.RequestObject import RequestObject
from webserver.service.ResourceContext import ResourceContext


class ResponseHandler:

    def __init__(self, resource_context: ResourceContext) -> None:
        self._context = resource_context

    def get_response(self, request_obj: RequestObject) -> ResponseObject:
        self._context.set_state(request_obj.file_extension)
        state = self._context.get_state()
        state.request_obj = request_obj
        
        response = ResponseObject()

        try:
            response.content = state.get_content()
            response.content_length = (f"Content-Length:{str(len(response.content))}\r\n\r\n").encode("UTF-8")
            response.header_2 = state.get_header()
            response.header_1 = b"HTTP/1.1 200 OK\r\n"
            response.cache = state.get_cache()

        except Exception as ex:
            print(f"In ResponseHandler file {request_obj.relative_path} {ex}")

            response.header_1 = b"HTTP/1.1 404 Not Found\r\n"

        return response
