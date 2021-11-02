from webserver.domain.RequestObject import RequestObject
from webserver.domain.ResponseObject import ResponseObject
from webserver.domain.Route import Route
from webserver.domain.StateObject import StateObject
from webserver.service.IResponseHandler import IResponseHandler


class RouteResponseHandler(IResponseHandler):

    def __init__(self, request: RequestObject) -> None:
        super().__init__(request)

    def get_response(self) -> ResponseObject: 
        route: Route = self._request.route      
        req = self._execute_handler(route)

        self._context.set_state(type = route.type)
        self._state = self._context.get_state()
        self._state.set_state(req=req)

        return self._create_response()

    def _execute_handler(self, route: Route):
        
        if route.parameters is not None: #and len(route.parameters) != 0:
            par1 = route.parameters[0]
            route.handler()

        return route.handler()

    def _open_html_page(self, html):
        file = open(html, "r")
        return file.read()
