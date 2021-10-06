import socket

from webserver.service.IPAddressHelper import IPAddressHelper
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
                    request = self._handle_request(request)
                                                
                else:
                    print("client disconnected")
                    break

        except Exception as ex:
            print("Exception in _start_server()!!")
            print(ex)
            print()

    def _handle_request(self, request) -> None:
        self._request_handler.handle_request(request)
