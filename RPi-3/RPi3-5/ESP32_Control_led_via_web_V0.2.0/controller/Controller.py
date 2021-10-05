from webserver.WebServer import WebServer

class Controller:

    def __init__(self, web_server: WebServer) -> None:
        self._web = web_server

    def register_routes(self):

        @self._web.route("/", "/home", "/index", "/led_off")
        def get_led_off(self):
            return "resources/html/led_off.html"

        @self._web.route("/led_on")
        def get_led_on(self):
            return "resources/html/led_on.html"
