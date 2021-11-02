from webserver.domain.RequestObject import RequestObject
from webserver.domain.ResponseObject import ResponseObject
from webserver.domain.Route import Route
from webserver.service.IResponseHandler import IResponseHandler


class RouteResponseHandler(IResponseHandler):

    def __init__(self, request: RequestObject) -> None:
        super().__init__(request)

    def get_response(self) -> ResponseObject:
        response = ResponseObject()
        req = self._execute_handler()
        
        if ".html" in req.lower():
            html = self._open_html_page(req)

            response.content = html.encode("UTF-8")
            response.content_length = (f"Content-Length:{str(len(response.content))}\r\n\r\n").encode("UTF-8")
            response.header_1 = response.header_1 = b"HTTP/1.1 200 OK\r\n"
            response.header_2 = b"Content-Type: text/html\r\n"
            response.cache = b"Cache-Control: no-cache, no-store\r\n"

        return response

    def _execute_handler(self):
        route: Route = self._request.route

        if route.parameters is not None and len(route.parameters) != 0:
            pass

        return route.handler()

    def _open_html_page(self, html):
        file = open(html, "r")
        return file.read()
