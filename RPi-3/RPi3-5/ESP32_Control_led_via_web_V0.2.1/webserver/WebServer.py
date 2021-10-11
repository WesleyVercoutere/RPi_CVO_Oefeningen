import socket
from webserver.domain.RequestObject import RequestObject

from webserver.service.IPAddressHelper import IPAddressHelper
from webserver.service.ResourceContext import ResourceContext
from webserver.service.ResponseHandler import ResponseHandler
from webserver.service.RequestHandler import RequestHandler
from webserver.service.RouteManager import RouteManager


class WebServer:

    PORT = 8080

    def __init__(self) -> None:
        self._socket = None
        self._conn = None
        
        self._ip_helper = IPAddressHelper()
        self._routeMgr = RouteManager()
        self._request_handler = RequestHandler(self._routeMgr)
        self._resource_context = ResourceContext()
        self._response_handler = ResponseHandler(self._resource_context)

    def run(self) -> None:
        self._init_socket()
        self._start_server()

    def route(self, *routes):
        def wrapper(f):
            for route in routes:
                self._routeMgr.register_route(route, f)
        
        return wrapper

    def _init_socket(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('0.0.0.0', self.PORT))
        self._socket.listen(1)

        print(f"Server is waiting for a connection at {self._ip_helper.get_ip_address()}, port : {self.PORT}")
        print()

    def _start_server(self) -> None:
        try:
            while True:
                self._conn = self._socket.accept()[0]
                request = self._conn.recv(2048)
                
                if len(request) > 0:                  
                    request = self._request_handler.handle_request(request)
                    self._handle_response(request)
                       
                else:
                    print("client disconnected")
                    break

        except Exception as ex:
            print("Exception in _start_server()!!")
            print(ex)
            print()

    def _handle_response(self, request: RequestObject) -> None:
        try:
            response = self._response_handler.get_response(request)

            self._conn.send(response.header_1)
            self._conn.send(response.header_2)
            self._conn.send(response.content_length)
            self._conn.sendall(response.content)

            self._conn.close()
        
        except Exception as ex:
            print("Exception in _handle_response()!!")
            print(ex)
            print()
            self._conn.close()

