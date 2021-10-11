import os

from webserver.domain.RequestObject import RequestObject
from webserver.service.RouteManager import RouteManager


class RequestHandler:

    def __init__(self, routeManager: RouteManager) -> None:
        self._routeMgr = routeManager

    def handle_request(self, request) -> RequestObject:
        # print(request.decode("utf-8"))
        # print()

        req = self._filter_request(request)
        route = self._routeMgr.get_route(req.path)
        
        if route is not None:
            file = route.handler()
        
        else:
            file = req.path

        req.file = file
        req.file_type = self._get_file_type(file)

        return req

    def _filter_request(self, request) -> RequestObject:
        req = request.decode("utf-8")
        req = req.split('\r\n')[0]
        req = req.split(" ")

        req_obj = RequestObject()
        req_obj.request_type = req[0]
        req_obj.path = req[1]

        return req_obj

    def _get_file_type(self, file) -> str:
        return file.split(".")[-1]
  