from controller.Controller import Controller
from webserver.WebServer import WebServer


class App:

    def __init__(self) -> None:
        self._web_server = WebServer()
        self._controller = Controller(self._web_server)

    def run(self) -> None:
        self._controller.register_routes()
        self._web_server.run()
