import socket

from webserver.service.RequestHandler import RequestHandler


class WebServer:

    PORT = 8080

    def __init__(self) -> None:
        self._socket = None
        self._conn = None

        self._request_handler = RequestHandler()

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
