import os

from webserver.domain.RequestObject import RequestObject
from webserver.service.RouteManager import RouteManager


class RequestHandler:

    def __init__(self, htmlMgr: RouteManager = None, apiMgr: RouteManager = None) -> None:
        self._htmlMgr = htmlMgr
        self._apiMgr = apiMgr
        self._req_obj = None

    def handle_request(self, request) -> RequestObject:
        # print(request.decode("utf-8"))
        # print()

        self._req_obj = RequestObject()

        self._filter_request(request)
        html = self._htmlMgr.get_route(self._req_obj.request_route)
        api = self._apiMgr.get_route(self._req_obj.request_route)
        
        if html is not None:
            self._handle_html_request(html)
            
        elif api is not None:
            self._handle_api_request(api)
            
        else:
            self._handle_resource_request()

        return self._req_obj

    def _filter_request(self, request) -> RequestObject:
        req = request.decode("utf-8")
        req = req.split('\r\n')[0]
        req = req.split(" ")

        self._req_obj.request_type = req[0]
        self._req_obj.request_route = req[1]

    def _handle_html_request(self, html):
        self._req_obj.response_type = "html"
        self._req_obj.filename = html.handler()
        self._req_obj.file_extension = self._get_file_type(self._req_obj.filename)

    def _handle_api_request(self, api):
        self._req_obj.response_type = "api"
        self._req_obj.handler = api.handler
        self._req_obj.file_extension = "api"

    def _handle_resource_request(self):
        self._req_obj.response_type = "resource"
        self._req_obj.filename = self._req_obj.request_route
        self._req_obj.file_extension = self._get_file_type(self._req_obj.filename)

    def _get_file_type(self, file) -> str:
        return file.split(".")[-1]
  