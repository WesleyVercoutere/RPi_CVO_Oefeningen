from service.LedService import LedService
from webserver.WebServer import WebServer


class Controller:

    def __init__(self, web_server: WebServer, led_service: LedService) -> None:
        self._web = web_server
        self._led_service = led_service

    def register_routes(self):

        @self._web.route("/", "/home", "/index", "/led_off")
        def get_led_off():
            self._led_service.led_off()

            return "resources/html/led_off.html"

        @self._web.route("/led_on")
        def get_led_on():
            self._led_service.led_on()
            
            return "resources/html/led_on.html"
