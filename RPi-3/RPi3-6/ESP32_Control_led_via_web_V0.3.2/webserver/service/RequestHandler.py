import os

from webserver.domain.RequestObject import RequestObject
from webserver.service.RouteManager import RouteManager


class RequestHandler:

    def __init__(self, routeManager: RouteManager) -> None:
        self._routeMgr = routeManager
        self._req_obj = None

    def handle_request(self, request) -> RequestObject:
        print(request.decode("utf-8"))
        print()

        self._req_obj = RequestObject

        self._filter_request(request)
        route = self._routeMgr.get_route(self._req_obj.request_route)
        
        if route is not None:
            self._req_obj.filename = route.handler()
        else:
            self._req_obj.filename = self._req_obj.request_route
        
        if self._req_obj.filename is not None:
            self._req_obj.file_extension = self._get_file_type(self._req_obj.filename)
        else:
            self._req_obj.filename = "api"

        return self._req_obj

    def _filter_request(self, request) -> RequestObject:
        req = request.decode("utf-8")
        req = req.split('\r\n')[0]
        req = req.split(" ")

        self._req_obj.request_type = req[0]
        self._req_obj.request_route = req[1]

    def _get_file_type(self, file) -> str:
        return file.split(".")[-1]
  