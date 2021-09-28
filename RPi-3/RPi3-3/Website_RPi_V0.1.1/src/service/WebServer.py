import socket

from domain.RequestObject import RequestObject
from domain.ResponseObject import ResponseObject
from service.RequestHandler import RequestHandler
from service.ResponseHandler import ResponseHandler
from service.IPAddressHelper import IPAddressHelper


class WebServer:

    PORT = 8080

    def __init__(self) -> None:
        self._socket = None
        self._conn = None

        self._request_handler = RequestHandler()
        self._response_handler = ResponseHandler()
        self._ip_helper = IPAddressHelper()

        self._request = RequestObject()
        self._response = ResponseObject()  

    def run(self) -> None:
        self._init_socket()
        self._start_server()

    def _init_socket(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('0.0.0.0', self.PORT))
        self._socket.listen(1)

    def _start_server(self) -> None:
        try:
            while True:
                print(f"Server is waiting for a connection at {self._ip_helper.get_ip_address()}, port : {self.PORT}")
                print()
                
                self._conn = self._socket.accept()[0]
                request = self._conn.recv(2048)
                
                if len(request) > 0:                  
                    self._handle_request(request)
                    self._handle_response()
                                                
                else:
                    print("client disconnected")
                    break

        except Exception as ex:
            print("Exception in _start_server()!!", ex)

    def _handle_request(self, request) -> None:
        self._request = self._request_handler.get_request(request)

    def _handle_response(self) -> None:
        try:
            self._response = self._response_handler.get_response(self._request)

            self._conn.send(self._response.header_1)
            self._conn.send(self._response.header_2)
            self._conn.send(self._response.content_length)
            self._conn.sendall(self._response.content)

            self._conn.close()
        
        except Exception as ex:
            print("Exception in _handle_response()!!", ex)
            self._conn.close()   
