from service.WebServer import WebServer
from service.IPAddressHelper import IPAddressHelper
from service.RequestHandler import RequestHandler
from service.ResponseHandler import ResponseHandler
from service.ResourceContext import ResourceContext

class IOCContainer:

    def __init__(self) -> None:
        resource_context = ResourceContext()

        request_handler = RequestHandler()
        response_handler = ResponseHandler(resource_context)
        ip_helper = IPAddressHelper()
        
        self._webserver = WebServer(request_handler, response_handler, ip_helper)

    def get_webserver(self):
        return self._webserver
