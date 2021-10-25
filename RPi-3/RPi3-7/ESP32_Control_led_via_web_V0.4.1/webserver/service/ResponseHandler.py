from webserver.domain.ResponseObject import ResponseObject
from webserver.domain.RequestObject import RequestObject
from webserver.service.ResourceContext import ResourceContext


class ResponseHandler:

    def __init__(self, resource_context: ResourceContext) -> None:
        self._context = resource_context

    def get_response(self, request_obj: RequestObject) -> ResponseObject:
        self._context.set_state(request_obj)
        state = self._context.get_state()
        state.request_obj = request_obj
        
        response = ResponseObject()

        try:
            if state.get_content() is not None:
                response.content = state.get_content()
                response.content_length = (f"Content-Length:{str(len(response.content))}\r\n\r\n").encode("UTF-8")
                response.header_1 = b"HTTP/1.1 200 OK\r\n"
                response.header_2 = state.get_header()
                response.cache = state.get_cache()
            else:
                response.header_1 = b"HTTP/1.1 204 No Content\r\n" 

        except Exception as ex:
            print(f"Exception in ResponseHandler request {request_obj.request_route}")
            print(ex)

            response.header_1 = b"HTTP/1.1 404 Not Found\r\n"

        return response
