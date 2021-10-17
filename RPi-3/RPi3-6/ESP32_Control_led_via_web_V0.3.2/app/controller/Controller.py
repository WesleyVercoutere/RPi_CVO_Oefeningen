from app.service.LedService import LedService
from webserver.WebServer import WebServer


class Controller:

    def __init__(self, web_server: WebServer, led_service: LedService) -> None:
        self._web = web_server
        self._led_service = led_service

    def register_routes(self):

        @self._web.register_route_html("/", "/home", "/index")
        def get_home_page():
            self._led_service.led_off()

            return "resources/html/index.html"

        @self._web.register_route_api("/led_on")
        def set_led_on():
            self._led_service.led_on()

        @self._web.register_route_api("/led_off")
        def set_led_off():
            self._led_service.led_off()

        @self._web.register_route_api("/toggle")
        def toggle_led():
            self._led_service.led_toggle()
