import socket

from domain.RequestObject import RequestObject
from domain.ResponseObject import ResponseObject
from service.RequestHandler import RequestHandler
from service.ResponseHandler import ResponseHandler
from service.IPAddressHelper import IPAddressHelper


class WebServer:

    PORT = 8080

    def __init__(self, request_handler: RequestHandler, response_handler: ResponseHandler, ip_helper: IPAddressHelper) -> None:
        self._socket = None
        self._conn = None

        self._request_handler = request_handler
        self._response_handler = response_handler
        self._ip_helper = ip_helper

    def run(self) -> None:
        self._init_socket()
        self._start_server()

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
                    self._handle_response(request)
                                                
                else:
                    print("client disconnected")
                    break

        except Exception as ex:
            print("Exception in _start_server()!!")
            print(ex)
            print()

    def _handle_request(self, request) -> RequestObject:
        return self._request_handler.get_request(request)

    def _handle_response(self, request: RequestHandler) -> None:
        try:
            response: ResponseHandler = self._response_handler.get_response(request)

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
