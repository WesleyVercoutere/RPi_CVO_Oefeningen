from app.controller.Controller import Controller
from app.service.LedService import LedService
from webserver.WebServer import WebServer


class App:

    def __init__(self) -> None:
        self._web_server = WebServer()
        self._led_service = LedService()
        self._controller = Controller(self._web_server, self._led_service)

    def run(self) -> None:
        self._controller.register_routes()
        self._web_server.run()
