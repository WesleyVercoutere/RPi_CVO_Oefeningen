from webserver.domain.RequestObject import RequestObject
from webserver.service.RouteManager import RouteManager
from webserver.util.ResponseType import ResponseType


class RequestHandler:

    def __init__(self, routeMgr: RouteManager = None) -> None:
        self._htmlMgr = routeMgr
        self._req_obj = None

    def handle_request(self, request) -> RequestObject:
        # print(request.decode("utf-8"))
        # print()

        self._req_obj = RequestObject()

        self._filter_request(request)
        route = self._htmlMgr.find_route(self._req_obj.request_url)
        
        if route is not None:
            self._handle_route_request(route)
            
        else:
            self._handle_resource_request()

        return self._req_obj

    def _filter_request(self, request) -> RequestObject:
        req = request.decode("utf-8")
        req = req.split('\r\n')[0]
        req = req.split(" ")

        self._req_obj.request_type = req[0]
        self._req_obj.request_url = req[1]

    def _handle_route_request(self, route):
        self._req_obj.response_type = ResponseType.ROUTE
        self._req_obj.route = route

    def _handle_resource_request(self):
        self._req_obj.response_type = ResponseType.RESOURCE
  