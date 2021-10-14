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
        route = self._routeMgr.get_route(req.relative_path)
        
        if route is not None:
            file = route.handler()
        
        else:
            file = req.relative_path

        req.relative_path = file
        req.filename = self._get_filename(file)
        req.file_extension = self._get_file_type(file)

        return req

    def _filter_request(self, request) -> RequestObject:
        req = request.decode("utf-8")
        req = req.split('\r\n')[0]
        req = req.split(" ")

        req_obj = RequestObject()
        req_obj.request_type = req[0]
        req_obj.relative_path = req[1]

        return req_obj

    def _get_filename(self, file) -> str:
        return file.split("/")[-1]

    def _get_file_type(self, file) -> str:
        return file.split(".")[-1]
  