import json
from app.service.manager.ToDoManager import ToDoManager

from webserver.WebServer import WebServer
from webserver.util.HTTPRequestMethod import HTTPRequestMethod
from webserver.util.RequestType import RequestType


class Controller:

    def __init__(self, web_server: WebServer, todo_mgr: ToDoManager) -> None:
        self._web = web_server
        self._todo_mgr = todo_mgr

    def register_routes(self):

        @self._web.register_route("/", "/home", "/index")
        def get_home_page():
            return "resources/html/index.html"
