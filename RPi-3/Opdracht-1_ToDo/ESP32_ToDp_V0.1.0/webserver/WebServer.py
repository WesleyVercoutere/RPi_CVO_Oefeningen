import socket
from webserver.domain.RequestObject import RequestObject

from webserver.service.IPAddressHelper import IPAddressHelper
from webserver.service.ResponseFactory import ResponseFactory
from webserver.service.RequestHandler import RequestHandler
from webserver.service.RouteManager import RouteManager
from webserver.util.HTTPRequestMethod import HTTPRequestMethod
from webserver.util.RequestType import RequestType


class WebServer:

    PORT = 8080

    def __init__(self) -> None:
        self._socket = None
        self._conn = None
        
        self._ip_helper = IPAddressHelper()
        self._routeMgr = RouteManager()
        self._request_handler = RequestHandler(routeMgr=self._routeMgr)
        self._response_factory = ResponseFactory()

    def run(self) -> None:
        self._init_socket()
        self._start_server()

    def register_route(self, *routes, type: RequestType = RequestType.NORMAL, method: HTTPRequestMethod = HTTPRequestMethod.GET):
        def wrapper(f):
            [self._routeMgr.register_route(type=type, method=method, route=route, f=f) for route in routes]
        
        return wrapper

    def _init_socket(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('0.0.0.0', self.PORT))
        self._socket.listen(1)

        print(f"Server is waiting for a connection at {self._ip_helper.get_ip_address()}, port : {self.PORT}")
        print()

    def _start_server(self) -> None:
        # try:
        while True:
            self._conn = self._socket.accept()[0]
            request = self._conn.recv(2048)
            
            if len(request) > 0:                  
                request = self._request_handler.handle_request(request)
                self._handle_response(request)
                    
            else:
                print("client disconnected")

        # except Exception as ex:
        #     print("Exception in _start_server()!!")
        #     print(ex)
        #     print()

    def _handle_response(self, request: RequestObject) -> None:
        try:
            response = self._response_factory.get_response(request)

            if response.content is not None and not response.error:
                self._conn.send(response.header_1)
                self._conn.send(response.cache)
                self._conn.send(response.header_2)
                self._conn.send(response.content_length)
                self._conn.sendall(response.content)

            else:
                self._conn.send(response.header_1)
                
            self._conn.close()
        
        except Exception as ex:
            print("Exception in _handle_response()!!")
            print(ex)
            print()
            self._conn.close()